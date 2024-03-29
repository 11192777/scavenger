import unittest


from server import LoginServer
from server.CategoryServer import CategoryServer
from utils import RandomUtils, ResponseUtil

ENV = LoginServer.local_private_dev_11192777()


class CategoryTests(unittest.TestCase):

    def setUp(self):
        self.server = CategoryServer(ENV)

    def test_获取一级门类列表(self):
        ResponseUtil.format_json(self.server.listSubCategory().data())

    def test_新增二级门类(self):
        parentId = self.server.listSubCategory().data(0)["id"]
        data = {"name": RandomUtils.random_str(20), "code": RandomUtils.random_str(20), "parentId": parentId}
        ResponseUtil.format_json(self.server.saveOrUpdate(data).data())

    def test_获取一级门类并附带子类(self):
        ResponseUtil.format_json(self.server.listSubCategory(isWithSubCategory=True).data())
