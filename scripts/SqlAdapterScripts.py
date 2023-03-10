import base64
import json
import os
import re
import unittest

import jsonpath
from sqlalchemy.dialects import mysql

from utils.MySqlHelper import MysqlDb

ignoreList = ["20220823115878", "20220826113000", "2022091509270001"]


def listChangeLogsByFilePath(path, ignoreFiles=None):
    fileNames = [fileName for fileName in os.listdir(path) if fileName.endswith(".xml") and (ignoreFiles is None or fileName not in ignoreFiles)]
    filePaths = ["{}/{}".format(path, fileName) for fileName in fileNames]
    result = []
    for filePath in filePaths:
        with open(filePath, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                changeSetIds = re.findall(r'id="(.+?)"', line)
                for changeSetId in changeSetIds:
                    result.append(str(changeSetId).replace("oracle", ""))
    return result


def getOracleInsertByMysqlRowData(data, tableName=None, types=None):
    kvs = []
    for key in list(dict(data).keys()):
        value = str(data[key])
        for type in types:
            if type["Field"] == key:
                if str(type["Type"]).startswith("varchar"):
                    value = "'{}'".format(value)
        if key == "last_modified_date" or key == "created_date":
            value = "sysdate"
        kvs.append({"name": key, "value": value})
    columns = ", ".join(jsonpath.jsonpath(kvs, "$..name"))
    values = ", ".join(jsonpath.jsonpath(kvs, "$..value"))
    return "INSERT INTO {} ({}) VALUES ({});".format(tableName, columns, values)


def printOracleSqlByTableName(db, tableName):
    datas = db.select("select * from {};".format(tableName))
    types = db.select("show COLUMNS from {};".format(tableName))
    for data in datas:
        print(getOracleInsertByMysqlRowData(data, tableName, types))


class SalAdapterScripts(unittest.TestCase):

    def test_生成ChangeSet差异(self):
        oracleOldPath = "/Users/vicoko/workspace/idea/e-archives/archive/src/main/resources/db/changelog/oracle/oldFile"
        oraclePath = "/Users/vicoko/workspace/idea/e-archives/archive/src/main/resources/db/changelog/oracle"
        mysqlPath = "/Users/vicoko/workspace/idea/e-archives/archive/src/main/resources/db/sub-table/sub-table.xml"

        oracleChangeSets = listChangeLogsByFilePath(oraclePath) + listChangeLogsByFilePath(oracleOldPath) + ignoreList
        mysqlChangeSets = listChangeLogsByFilePath(mysqlPath, ["release.1.0.xml", "release.1.1.xml", "release.1.2.xml", "release.1.3.xml", "release.1.4.xml", "release.1.5.xml", "release.20220617.xml", "release.20220715.xml", "release.20220812.xml", "sub-table.xml"])

        diffs = set(mysqlChangeSets).difference(set(oracleChangeSets))
        for changeSetId in mysqlChangeSets:
            if changeSetId in diffs:
                print("===> 待适配: {}".format(changeSetId))

    def test_证据链模板Oracle(self):
        db = MysqlDb(host="hly-uatmask-polardb.mysql.polardb.rds.aliyuncs.com", port=3306, user="artemis", passwd=str(base64.b64decode("USF3MmUzcjR0NVle"), "utf-8"), db="e_archives_private")
        print("\nDELETE FROM ea_evidence_chain_template WHERE 1=1;")
        printOracleSqlByTableName(db, "ea_evidence_chain_template")
        print("\n\nDELETE FROM ea_evidence_chain_template_relation WHERE 1=1;")
        printOracleSqlByTableName(db, "ea_evidence_chain_template_relation")

    def test_ChangeSet创建表转换(self):
        data = '''
   <changeSet id="20221010152238" author="haoxuan.tang">
    <preConditions onFail="MARK_RAN">
      <not>
        <tableExists tableName="ea_query_condition_history"/>
      </not>
    </preConditions>
    <createTable tableName="ea_query_condition_history" remarks="查询条件记录表">
      <column name="id" type="bigint" autoIncrement="${autoIncrement}" remarks="主键id">
        <constraints nullable="false" primaryKey="true"/>
      </column>
      <column name="code" type="varchar(100)" remarks="编码">
        <constraints nullable="false"/>
      </column>
      <column name="operator" type="varchar(20)" remarks="操作符">
        <constraints nullable="true"/>
      </column>
      <column name="count" type="int(11)" defaultValueNumeric="1" remarks="数量">
        <constraints nullable="true"/>
      </column>
      <column name="is_fixed" type="bit(1)" defaultValueBoolean="1" remarks="是否固定字段,默认为true" >
        <constraints nullable="false"/>
      </column>
      <column name="tenant_id" type="bigint" remarks="租户id">
        <constraints nullable="false"/>
      </column>
    </createTable>
    <createIndex tableName="ea_query_condition_history" indexName="idx_query_tenant_id">
      <column name="tenant_id"/>
    </createIndex>
  </changeSet>'''
        data = data.replace("bigint(20)", "bigint")
        data = data.replace("bigint", "number(20)")
        data = data.replace("int", "number(11)")
        data = data.replace("varchar", "nvarchar2")
        data = data.replace("timestamp", "date")
        data = data.replace('type="text"', 'type="varchar2(4000)"')
        data = data.replace('autoIncrement="${autoIncrement}" ', "")
        temp = ""
        for line in data.split("\n"):
            if "<createTable tableName" in line and "remarks=" in line:
                line = line.split("remarks=")[0] + ">"
            temp = temp + line + "\n"
        data = temp
        print(data)
