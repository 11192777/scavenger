import base64
import unittest

from utils.MySqlHelper import MysqlDb


class CategoryScripts(unittest.TestCase):

    def setUp(self):
        data = '''工程档案	KJ
文书档案	WS
合同档案	HT
产品档案	CP
招投标档案	ZTB
科研档案	KY
审计档案	SJ
实物档案	SW
会计档案	CMJX-KJ
标准化档案	QYBZ
教学档案	JX
权证档案	QZ
专题档案	ZT
专利档案	QYZL
声像档案	SX
信访档案	XF'''
        items = []
        lines = data.split("\n")
        for line in lines:
            items.append({"name": line.split()[0], "code": line.split()[1]})
        self.items = items
        print("\n")
        self.db = MysqlDb(host="106.15.26.10", port=21906, user="artemis",
                          passwd=str(base64.b64decode("MTIzNDU2TXMz"), "utf-8"), db="e_archives_jxmobile")
        self.categories = self.db.select("SELECT * FROM ea_category;")

    def test_生成SQL(self):
        index = 1001
        print("\nDELETE FROM ea_category WHERE 1 = 1;")
        for item in self.items:
            print(
                "INSERT INTO ea_category(id, code, name, tenant_id) VALUES ('{}', '{}', '{}', '-1');".format(
                    index,
                    item["code"],
                    item["name"]))
            index = index + 1

    def test_生成枚举(self):
        for item in self.categories:
            name = item["name"]
            code = item["code"]
            print('''
               /**
               * {}
               */
               {}("{}", "{}"),'''.format(name, str(code).replace("—", "_"), code, name))

    def test_生成分表(self):
        tables = ["ea_document", "ea_document_attachment", "ea_document_field_value", "ea_archive",
                  "ea_archive_document", "ea_archive_field_value", "ea_attachment", "ea_operation_audit_log"]
        for table in tables:
            for category in self.categories:
                # print("CREATE TABLE IF NOT EXISTS {}_{} LIKE {};".format(table, str(category["code"]).lower().replace("-", "_"), table))
                print("DROP TABLE IF EXISTS {}_{}01;".format(table, str(category["code"]).lower().replace("-", "_")))
            print("\n")

    def test_生成接口描述(self):
        for item in self.categories:
            print("编码:{}  名称:{}".format(str(item["code"]).replace("-", "_"), item["name"]))


    def test_生成脚本SQL(self):
        for item in self.categories:
            code = str(item["code"]).replace("-", "_").lower()
            print("ALTER TABLE ea_archive_{} ADD COLUMN project_id bigint NOT NULL DEFAULT '-1' COMMENT '项目id';".format(code))
            print("ALTER TABLE ea_archive_{} ADD COLUMN year int NOT NULL DEFAULT '1970' COMMENT '年份';".format(code))
            print("CREATE INDEX idx_projectId ON ea_archive_{} (project_id);".format(code))
            print("\n")

    def test_资料表增加排序号(self):
        for item in self.categories:
            code = str(item["code"]).replace("-", "_").lower()
            print("ALTER TABLE ea_document_{} ADD COLUMN sort_number int NOT NULL DEFAULT '2147483647' COMMENT '顺序号';".format(code))
