import unittest


class Script(unittest.TestCase):

    def test_A(self):
        data = '''工程档案-非基建	KJ
工程档案-基建	KJ
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
        for line in data.split("\n"):
            print("INSERT INTO ea_category(code, name, tenant_id) VALUES ('{}', '{}', '-1');".format(line.split()[0], line.split()[1]))
