import unittest


from server.RdcUtilServer import RdcUtilServer


class RdcUtilScripts(unittest.TestCase):

    def setUp(self):
        token = "bearer bc318b09-d366-4856-ab39-694397c4b454"
        self.server = RdcUtilServer(token=token)

    def test_拉取任务(self):
        forms = '''
e-archive-5069
           '''
        for code in forms.splitlines():
            if code.startswith("e-archive"):
                self.server.saveSubTask(code, taskTypeName="开发任务", associateName="孟庆宇")

    def test_分配任务主要负责人(self):
        # 格式 ## 任务号，前端，后端，测试，没有的用-
        tasks = '''
e-archive-4032	-	孟庆宇	肖淙榕
e-archive-4425	林琛越	孟庆宇	刘亚丽
e-archive-4426	-	唐皓轩	刘亚丽
e-archive-4427	林琛越	黄博	肖淙榕
e-archive-4201	李琦	李军良	肖淙榕
e-archive-4202	林琛越	孟庆宇	肖淙榕
e-archive-4415	李琦	孟庆宇	肖淙榕
e-archive-4415	李琦	孟庆宇	肖淙榕
e-archive-4443	林琛越	孟庆宇	肖淙榕
e-archive-4416	李琦	周昕	刘亚丽
e-archive-4417	李琦	周昕	刘亚丽
e-archive-4475	李琦	唐皓轩	刘亚丽
e-archive-4444	林琛越	唐皓轩	肖淙榕
e-archive-4428	-	唐皓轩	肖淙榕
e-archive-4429	-	唐皓轩	刘亚丽
e-archive-4430	林琛越	唐皓轩	肖淙榕
e-archive-4432	林琛越	唐皓轩	刘亚丽
e-archive-4473	林琛越	黄博	肖淙榕
e-archive-4445	李琦	黄博	刘亚丽
e-archive-4450	李琦	唐皓轩	刘亚丽
e-archive-4451	林琛越	-	刘亚丽
e-archive-4474	林琛越	李军良	刘亚丽
e-archive-4436	林琛越	周昕	肖淙榕
e-archive-4452	林琛越	黄博	刘亚丽
e-archive-4433	林琛越	李军良	刘亚丽
e-archive-4453	-	孟庆宇	刘亚丽
e-archive-4434	-	唐皓轩	刘亚丽
e-archive-4435	-	孟庆宇	肖淙榕
e-archive-4456	林琛越	唐皓轩	刘亚丽
e-archive-4457	李琦	唐皓轩	刘亚丽
e-archive-4458	林琛越	孟庆宇	肖淙榕
e-archive-4460	-	周昕	刘亚丽
e-archive-4472	林琛越	周昕	肖淙榕
e-archive-4476	李琦	周昕	刘亚丽
e-archive-4461	李琦	周昕	刘亚丽
e-archive-4462	李琦	-	肖淙榕
e-archive-4464	林琛越	-	刘亚丽
e-archive-4471	林琛越	孟庆宇	肖淙榕
e-archive-4487	林琛越	李军良	刘亚丽
e-archive-4489	李琦	孟庆宇	肖淙榕
e-archive-4516	李琦	黄博	刘亚丽
e-archive-4519	李琦	周昕	刘亚丽
e-archive-4521	李琦	孟庆宇	刘亚丽
e-archive-4614	林琛越	周海	刘亚丽
'''
        for line in tasks.splitlines():
            if line.startswith("e-archive"):
                self.server.saveTaskAssociateMember(line)

    def 无用_个人测试用的(self):
        # print(self.server.queryTaskByCode("e-archive-4425"))
        # print(self.server.getTaskTypeId("开发任务"))
        # print(self.server.queryUser("刘亚丽"))
        # print(self.server.queryTaskById("416997149407059968"))
        # print(self.server.getNextTaskVersionNumber("416997149407059968"))
        # print(self.server.getUserIdByName("刘亚丽"))
        pass
