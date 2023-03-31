import base64
import re

from utils import MySqlHelper


class HermesMenuScripts:
    def __init__(self):
        self.hermes = MySqlHelper.MysqlDb('hly-uatmask-polardb.mysql.polardb.rds.aliyuncs.com', 3306, 'artemis', base64.b64decode('USF3MmUzcjR0NVle'), 'hermes')
        self.resourceIds = []
        self.sqls = []
        self.keys = []

    def listAllMenuByNames(self, names):
        sql = '''
            SELECT parent_id, resource_name, resource_type, resource_id, `key`, resource_layout, 
                   IF(default_enabled, 'TRUE', 'FALSE') AS default_enabled,
                   resource_order,
                   pinyin_resource_name, 
                   IF(default_readable, 'TRUE', 'FALSE') AS default_readable,
                   IF(is_enabled, 'TRUE', 'FALSE') AS is_enabled,
                   IF(is_deleted, 'TRUE', 'FALSE') AS is_deleted
               FROM
                   art_resource_detail
               WHERE
                   resource_name IN ({})
        '''.format(','.join(names))
        return self.hermes.select(sql)

    def getMenuByResourceId(self, resourceId):
        return self.hermes.select_one('''
            SELECT parent_id, resource_name, resource_type, resource_id, `key`, resource_layout, 
                IF(default_enabled, 'TRUE', 'FALSE') AS default_enabled,
                resource_order,
                pinyin_resource_name, 
                IF(default_readable, 'TRUE', 'FALSE') AS default_readable,
                IF(is_enabled, 'TRUE', 'FALSE') AS is_enabled,
                IF(is_deleted, 'TRUE', 'FALSE') AS is_deleted
            FROM
                art_resource_detail
            WHERE
                resource_id = {} AND is_deleted = FALSE LIMIT 1;'''.format(resourceId))

    def loopMenusSql(self, menu):
        fatherId = menu["parent_id"]
        if fatherId and fatherId not in self.resourceIds:
            self.loopMenusSql(self.getMenuByResourceId(fatherId))
        script = '''
INSERT INTO art_resource_detail(parent_id, resource_name, resource_type, resource_id, `key`, resource_layout, default_enabled, resource_order, pinyin_resource_name, default_readable, is_enabled, is_deleted, ) SELECT {}, '{}', '{}', '{}', '{}', '{}', {}, {}, '{}', {} ,{} ,{} FROM DUAL WHERE NOT EXISTS(SELECT 1 FROM art_resource_detail WHERE `key` = '{}');
UPDATE art_resource_detail SET parent_id = {}, resource_name = '{}', resource_type = '{}', resource_id = '{}',`key` = '{}', resource_layout = '{}',default_enabled = {}, resource_order = '{}', pinyin_resource_name = '{}', default_readable = {}, is_enabled = {}, is_deleted = {} WHERE `key` = '{}';'''
        resultSql = script.format(
            menu["parent_id"],
            menu["resource_name"],
            menu["resource_type"],
            menu["resource_id"],
            menu["key"],
            menu["resource_layout"],
            menu["default_enabled"],
            menu["resource_order"],
            menu["pinyin_resource_name"],
            menu["default_readable"],
            menu["is_enabled"],
            menu["is_deleted"],
            menu["key"],

            menu["parent_id"],
            menu["resource_name"],
            menu["resource_type"],
            menu["resource_id"],
            menu["key"],
            menu["resource_layout"],
            menu["default_enabled"],
            menu["resource_order"],
            menu["pinyin_resource_name"],
            menu["default_readable"],
            menu["is_enabled"],
            menu["is_deleted"],
            menu["key"],
        )
        self.sqls.append({"key": menu["resource_id"] * 100000000000 + menu["resource_order"], "sql": resultSql})
        self.keys.append({"key": menu["key"], "name": menu["resource_name"]})
        self.resourceIds.append(menu["resource_id"])

    def build(self, resourceNames):
        names = ["'{}'".format(item) for item in resourceNames]
        for menu in self.listAllMenuByNames(names):
            self.loopMenusSql(menu)
        sorted(self.sqls, key=lambda u: u["key"])

    def printSqlScripts(self):
        for sqlItem in self.sqls:
            print(sqlItem["sql"])

    def printMenuEnums(self):
        for key in self.keys:
            print('{}("{}", "{}"),'.format(str.upper(key["key"]).replace("-", "_"), key["key"], key["name"]))


if __name__ == '__main__':
    resourceVar = '''
E档案保留的功能范围：

公共菜单：管理员首页、快捷设置中心

1、档案管理所有功能，包括：资料归集、立卷成册、卷册管理、装盒入库

2、库房管理所有功能，包括：入库查询、库内调整、库位设置

3、档案借阅部分功能，包括：电子借阅、实物借阅、归还登记、借阅查询

4、综合查询部分功能，包括：资料查询、卷册查询、目录检索、档案调阅、四性检测

5、在线审计不保留功能

6、处置鉴定所有功能，包括：档案鉴定、档案处置、销毁查询

7、基础配置部分功能，包括：资料类型、完整性规则、调阅模板、档案名称配置、审批流设置

8、权限管理部分功能，包括：公司管理、用户管理、部门管理、角色管理

9、操作日志所有功能，包括：任务设置、任务日志、安全审计、系统监测、资料回收站、档案更新

10、租户管理部分功能，包括：其他设置、租户详情

11、智能验签所有功能，包括：验签配置、验签结果、档案生态

12、流程审批部分功能，包括：鉴定审批
        '''
    resourceNames = []
    for item in re.findall(r'[(包括)(公共菜单)]：(.+?)[\s+]', resourceVar):
        resourceNames = resourceNames + item.split('、')
    hermes = HermesMenuScripts()
    hermes.build(resourceNames)
    hermes.printMenuEnums()
