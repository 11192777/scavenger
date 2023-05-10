from datetime import time

import autotest.tests.FormTests
import server.LoginServer
from server.FormFieldServer import FormFieldServer
from server.FormServer import FormServer

import unittest

from utils import ResponseUtil, RandomUtils

ENV = server.LoginServer.private_sit_16660000000()


class ArchiveTypeTests(unittest.TestCase):

    def setUp(self):
        self.server = FormServer(ENV)

    def tearDown(self):
        pass

    def test_档案编码长度限制(self):
        form = {"code": "1234567890123456789012345678901234567890", "name": "auto_test_archive_type", "retentionPeriod": "100", "businessType": "ACCOUNTANT", "isEnabled": True, "isParentType": True, "formFieldList": [], "sortNumber": 0}
        ResponseUtil.assert_status(self.server.save_form(form), "103021")

    def test_档案编码字符校验(self):
        form = {"code": "9*&(*jshdjfk", "name": "auto_test_archive_type", "retentionPeriod": "100", "businessType": "ACCOUNTANT", "isEnabled": True, "isParentType": True, "formFieldList": [], "sortNumber": 0}
        ResponseUtil.assert_status(self.server.save_form(form), "103023")

    def test_档案编码唯一(self):
        form1 = {"code": "auto_test_archive_type", "name": "auto_test_archive_type", "retentionPeriod": "100", "businessType": "ACCOUNTANT", "isEnabled": True, "isParentType": True, "formFieldList": [], "sortNumber": 0}
        form1_result = ResponseUtil.assert_status(self.server.save_form(form1), "0000")
        form2 = {"code": "auto_test_archive_type", "name": "auto_test_archive_type_2", "retentionPeriod": "100", "businessType": "ACCOUNTANT", "isEnabled": True, "isParentType": True, "formFieldList": [], "sortNumber": 0}
        ResponseUtil.assert_status(self.server.save_form(form2), "103031")
        ResponseUtil.assert_status(self.server.delete_form(form1_result.data(key="id")), "0000")

    def test_档案名称长度校验(self):
        form = {"code": "auto_test_archive_type", "name": "auto_test_archive_type_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "retentionPeriod": "100", "businessType": "ACCOUNTANT", "isEnabled": True, "isParentType": True, "formFieldList": [], "sortNumber": 0}
        ResponseUtil.assert_status(self.server.save_form(form), "103027")

    def test_档案名称字符校验(self):
        form = {"code": "auto_test_archive_type", "name": "auto_te@#@#@xxxxx", "retentionPeriod": "100", "businessType": "ACCOUNTANT", "isEnabled": True, "isParentType": True, "formFieldList": [], "sortNumber": 0}
        ResponseUtil.assert_status(self.server.save_form(form), "103029")

    def test_档案名称唯一(self):
        form1 = {"code": "auto_test_archive_type_1", "name": "auto_test_archive_type", "retentionPeriod": "100", "businessType": "ACCOUNTANT", "isEnabled": True, "isParentType": True, "formFieldList": [], "sortNumber": 0}
        form1_result = ResponseUtil.assert_status(self.server.save_form(form1), "0000")
        form2 = {"code": "auto_test_archive_type_2", "name": "auto_test_archive_type", "retentionPeriod": "100", "businessType": "ACCOUNTANT", "isEnabled": True, "isParentType": True, "formFieldList": [], "sortNumber": 0}
        ResponseUtil.assert_status(self.server.save_form(form2), "103082")
        ResponseUtil.assert_status(self.server.delete_form(form1_result.data(key="id")), "0000")


class DocumentTypeTests(unittest.TestCase):

    def setUp(self):
        env = ENV
        self.server = FormServer(env)
        self.parent_type_id = ResponseUtil.assert_status(self.server.random_archive_form(), "0000").data("id")

    def tearDown(self):
        ResponseUtil.assert_status(self.server.delete_form(self.parent_type_id), "0000")

    def test_资料编码长度限制(self):
        form = {"isEnabled": True, "code": "012345678901234567890123456789_31", "name": "auto_test_document_type", "fieldTemplateId": "10", "baseIsPaper": "true", "attachCustomEnums": [], "parentId": self.parent_type_id, "isParentType": False, "formFieldList": [], "businessType": "LOAN_BILL", "sortNumber": 3}
        ResponseUtil.assert_status(self.server.save_form(form), "103022")

    def test_资料编码字符校验(self):
        form = {"isEnabled": True, "code": "auto_test_d(&(&(*&(_type", "name": "auto_test_document_type", "fieldTemplateId": "10", "baseIsPaper": "true", "attachCustomEnums": [], "parentId": self.parent_type_id, "isParentType": False, "formFieldList": [], "businessType": "LOAN_BILL", "sortNumber": 3}
        ResponseUtil.assert_status(self.server.save_form(form), "103024")

    def test_资料编码唯一(self):
        form = {"isEnabled": True, "code": "auto_test_document_type", "name": "auto_test_document_type", "fieldTemplateId": "10", "baseIsPaper": "true", "attachCustomEnums": [], "parentId": self.parent_type_id, "isParentType": False, "formFieldList": [], "businessType": "LOAN_BILL", "sortNumber": 3}
        result = ResponseUtil.assert_status(self.server.save_form(form), "0000")
        form["name"] = "auto_test_document_type_2"
        ResponseUtil.assert_status(self.server.save_form(form), "103026")
        ResponseUtil.assert_status(self.server.delete_form(result.data("id")), "0000")

    def test_资料名称长度校验(self):
        form = {"isEnabled": True, "code": "auto_test_document_type", "name": "012345678901234567890123456789_31", "fieldTemplateId": "10", "baseIsPaper": "true", "attachCustomEnums": [], "parentId": self.parent_type_id, "isParentType": False, "formFieldList": [], "businessType": "LOAN_BILL", "sortNumber": 3}
        ResponseUtil.assert_status(self.server.save_form(form), "103028")

    def test_资料名称字符校验(self):
        form = {"isEnabled": True, "code": "auto_test_document_type", "name": "*(&(*&(__SDf", "fieldTemplateId": "10", "baseIsPaper": "true", "attachCustomEnums": [], "parentId": self.parent_type_id, "isParentType": False, "formFieldList": [], "businessType": "LOAN_BILL", "sortNumber": 3}
        ResponseUtil.assert_status(self.server.save_form(form), "103030")

    def test_资料名称唯一(self):
        form = {"isEnabled": True, "code": "auto_test_document_type", "name": "auto_test_document_type", "fieldTemplateId": "10", "baseIsPaper": "true", "attachCustomEnums": [], "parentId": self.parent_type_id, "isParentType": False, "formFieldList": [], "businessType": "LOAN_BILL", "sortNumber": 3}
        result = ResponseUtil.assert_status(self.server.save_form(form), "0000")
        form["code"] = "auto_test_document_type_2"
        ResponseUtil.assert_status(self.server.save_form(form), "103032")
        self.server.delete_form(result.data("id"))

    def test_资料备注长度校验(self):
        form = {"remark": str(RandomUtils.random_str(101)), "isEnabled": True, "code": "auto_test_document_type", "name": "auto_test_document_type", "fieldTemplateId": "10", "baseIsPaper": "true", "attachCustomEnums": [], "parentId": self.parent_type_id, "isParentType": False, "formFieldList": [], "businessType": "LOAN_BILL", "sortNumber": 3}
        ResponseUtil.assert_status(self.server.save_form(form), "103038")

    def test_人事基础信息资料类型限制创建一次(self):
        archive_type = self.server.random_archive_form("PERSONNEL")
        form = {"isEnabled": True, "code": RandomUtils.random_time(), "name": RandomUtils.random_time(), "fieldTemplateId": "38", "baseIsPaper": "true", "attachCustomEnums": [], "parentId": archive_type.data("id"), "isParentType": False, "formFieldList": [], "businessType": "BASIC_PERSONNEL_INFORMATION", "sortNumber": 1}
        ResponseUtil.assert_status(self.server.save_form(form), "103016")
        self.server.delete_form(archive_type.data("id"))


class FormFieldTests(unittest.TestCase):

    def setUp(self):
        env = ENV
        self.server = FormServer(env)
        self.field_server = FormFieldServer(env)
        self.parent_type = ResponseUtil.assert_status(self.server.random_archive_form(), "0000").data()
        self.parent_type_id = self.parent_type["id"]
        self.document_type = ResponseUtil.assert_status(self.server.random_document_type(parent_id=self.parent_type_id), "0000").data()
        self.document_type_id = self.document_type["id"]

    def tearDown(self):
        ResponseUtil.assert_status(self.server.delete_form(self.parent_type_id), "0000")

    def test_编码重复校验(self):
        field1 = {"name": RandomUtils.random_time(), "code": "test_field", "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        field2 = {"name": RandomUtils.random_time(), "code": "test_field", "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.document_type["formFieldList"] = [field1, field2]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "103061")

    def test_会计凭证下的部分字段不可禁用且必填(self):
        expense_voucher = ResponseUtil.assert_status(self.server.random_document_type(parent_id=self.parent_type_id, business_type="EXPENSE_VOUCHER"), "0000").data()
        field1 = {"name": RandomUtils.random_time(), "code": "GL_CODE", "formId": expense_voucher["id"], "widgetType": "TEXT", "inputManually": False, "required": False, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        expense_voucher["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(expense_voucher), "103311")

    def test_编码长度限制(self):
        field1 = {"name": RandomUtils.random_time(), "code": RandomUtils.random_str(31), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100054")

    def test_编码字符校验(self):
        field1 = {"name": RandomUtils.random_time(), "code": "RandomUtils.random_str(20)", "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100055")

    def test_超链接字段不能作为成册主键(self):
        field1 = {"name": RandomUtils.random_time(), "code": RandomUtils.random_str(20), "formId": self.document_type_id, "widgetType": "HYPERLINK", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": True, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100141")

    def test_相同编码字段控件类型需要一致校验(self):
        code = RandomUtils.random_str(30)
        field1 = {"name": RandomUtils.random_time(), "code": code, "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "0000")
        self.document_type = ResponseUtil.assert_status(self.server.random_document_type(parent_id=self.parent_type_id), "0000").data()
        field2 = {"name": RandomUtils.random_time(), "code": code, "formId": self.document_type["id"], "widgetType": "HYPERLINK", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.document_type["formFieldList"] = [field2]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100058")

    def test_相同编码字段控件类型需要一致校验(self):
        code = RandomUtils.random_str(30)
        field1 = {"name": RandomUtils.random_time(), "code": code, "formId": self.document_type_id, "widgetType": "DATE", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"DATE_FORMAT": "yyyy-MM-dd", "DATE_FORMAT_WEB": "YYYY-MM-DD"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "0000")
        self.document_type = ResponseUtil.assert_status(self.server.random_document_type(parent_id=self.parent_type_id), "0000").data()
        field2 = {"name": RandomUtils.random_time(), "code": code, "formId": self.document_type["id"], "widgetType": "DATE", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"DATE_FORMAT": "yyyy-MM-dd HH:mm:ss", "DATE_FORMAT_WEB": "YYYY-MM-DD HH:mm:ss"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.document_type["formFieldList"] = [field2]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100059")

    def test_文本日期类型支持资料防重复配置(self):
        field1 = {"name": RandomUtils.random_time(), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": True, "isSpecialText": False}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "0000")
        field2 = {"name": RandomUtils.random_time(), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "HYPERLINK", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": True, "isSpecialText": False}
        self.document_type["formFieldList"] = [field2]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "103009")

    def test_名称长度限制(self):
        field1 = {"name": RandomUtils.random_str(31), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100344")

    def test_字段默认值长度限制(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "value": RandomUtils.random_str(251), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "103070")

    def test_字段备注长度限制(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "value": RandomUtils.random_str(250), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": RandomUtils.random_str(51), "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100057")

    def test_编码字段不可非必填(self):
        field = self.field_server.list_form_fields(self.document_type_id).data(0)
        self.document_type["encodingFieldId"] = field["id"]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "0000")

        field["required"] = False
        self.document_type["formFieldList"] = [field]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "105053")

    def test_档案类型不支持长文本超链接(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "value": RandomUtils.random_str(250), "formId": self.parent_type_id, "widgetType": "LONG_TEXT", "inputManually": True, "required": True, "remark": RandomUtils.random_str(50), "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.parent_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.parent_type), "103102")

    def test_资料类型动态字段编码不允许使用档案类型固定字段编码(self):
        field1 = {"name": RandomUtils.random_str(30), "code": "BASE_ARCHIVE_NAME", "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100367")

    def test_资料类型长文本字段数量限制(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "LONG_TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        field2 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "LONG_TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        field3 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "LONG_TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": False}
        self.document_type["formFieldList"] = [field1, field2, field3]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "103053")

    def test_控制资料防重复校验字段个数限制(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": True, "isSpecialText": False}
        field2 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": True, "isSpecialText": False}
        field3 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": True, "isSpecialText": False}
        field4 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "200"}, "volumePrimaryKey": False, "isDocumentUniqueControl": True, "isSpecialText": False}
        self.document_type["formFieldList"] = [field1, field2, field3, field4]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "103054")

    def test_控制特殊文本中拆分类型字段(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"SPECIAL_TYPE": "SPLIT", "SYMBOL": 0, "WORDS_LIMIT": 200, "EXTEND_RULE": "LENGTH_RIGHT", "WITH_FIELDS": ["1551400775756177410"]}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": True}
        field2 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"SPECIAL_TYPE": "SPLIT", "SYMBOL": 0, "WORDS_LIMIT": 200, "EXTEND_RULE": "LENGTH_RIGHT", "WITH_FIELDS": ["1551400775756177410"]}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": True}
        self.document_type["formFieldList"] = [field1, field2]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "103052")

    def test_控制特殊文本中合并类型字段(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"SPECIAL_TYPE": "COMBINE", "WORDS_LIMIT": 200, "EXTEND_RULE": "LENGTH_LEFT", "WITH_FIELDS": ["1551400775756177410", "1551400775764566018", "1551400775764566019", "1551825394562473985"]}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": True}
        field2 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"SPECIAL_TYPE": "COMBINE", "WORDS_LIMIT": 200, "EXTEND_RULE": "LENGTH_LEFT", "WITH_FIELDS": ["1551400775756177410", "1551400775764566018", "1551400775764566019", "1551825394562473985"]}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": True}
        self.document_type["formFieldList"] = [field1, field2]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "103051")

    def test_未能解析的日期精度(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "DATE", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"DATE_FORMAT": "87162873"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": True}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100046")

    def test_未能解析的浮点数范围(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "DOUBLE", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"MAX_VALUE": "abx", "MIN_VALUE": "2222.22"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": True}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100047")

    def test_DOUBLE最大值需要大於最小值(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "DOUBLE", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"MAX_VALUE": "123.99", "MIN_VALUE": "22222.22"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": True}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100048")

    def test_未能解析的浮点数范围(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "INTEGER", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"MAX_VALUE": "abx", "MIN_VALUE": "2222.22"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": True}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100049")

    def test_INTEGER最大值需要大於最小值(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "INTEGER", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"MAX_VALUE": "444444", "MIN_VALUE": "555555555"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": True}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100048")

    def test_未能解析的字段长度限制(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "TEXT", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"WORDS_LIMIT": "abs"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": True}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "100051")

    def test_未能解析的字段长度限制(self):
        field1 = {"name": RandomUtils.random_str(30), "code": RandomUtils.random_str(30), "formId": self.document_type_id, "widgetType": "TEXT_ARRAY", "inputManually": True, "required": True, "remark": "", "isEnabled": True, "sortNumber": 0, "widgetTypeProperty": {"ITEM_WORDS_LIMIT": "abs", "ITEMS_LIMIT": "12"}, "volumePrimaryKey": False, "isDocumentUniqueControl": False, "isSpecialText": True}
        self.document_type["formFieldList"] = [field1]
        ResponseUtil.assert_status(self.server.save_form(self.document_type), "103086")
