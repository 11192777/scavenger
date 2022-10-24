import unittest


class CategoryScripts(unittest.TestCase):

    def setUp(self):
        data = '''工程档案	KJ
                文书档案	WS
                合同档案	HT
                产品档案	CP
                招投标档案	ZT
                科研档案	KY
                审计档案	SJ
                实物档案	SW
                会计档案	KJ
                标准化档案	QYBZ
                教学档案	JX
                权证档案	QZ
                特殊载体档案	TS
                专题档案	ZT
                专利档案	QYZL
                声像档案	SX'''
        items = []
        lines = data.split("\n")
        for line in lines:
            items.append({"name": line.split()[0], "code": line.split()[1]})
        self.items = items
        print("\n")

    def test_生成SQL(self):
        index = 1001
        print("\nDELETE FROM ea_category WHERE 1 = 1;")
        for item in self.items:
            print(
                "INSERT INTO ea_category(id, code, original_code, name, tenant_id) VALUES ('{}', '{}', '{}', '{}', '-1');".format(
                    index,
                    item["code"],
                    item["code"],
                    item["name"]))
            index = index + 1

    def test_生成枚举(self):
        for item in self.items:
            name = item["name"]
            code = item["code"]
            print('''
               /**
               * {}
               */
               {}("{}", "{}"),'''.format(name, code, code, name))

    def test_生成分表(self):
        tables = ["ea_document", "ea_document_attachment", "ea_document_field_value", "ea_archive",
                  "ea_archive_document", "ea_archive_field_value", "ea_attachment", "ea_operation_audit_log"]
        for table in tables:
            for item in self.items:
                print("CREATE TABLE IF NOT EXISTS {}_{} LIKE {};".format(table, item["code"], table))
            print("\n")
