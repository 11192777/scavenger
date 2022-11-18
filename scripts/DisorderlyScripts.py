import unittest


class DisorderlyScript(unittest.TestCase):


    def test_1(self):
        str = '''   @Test
    public void case{}() {{

    }}\n\n'''

        for i in range(0, 20):
            print(str.format(i))

