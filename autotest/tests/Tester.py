import json
import unittest


class Tester(unittest.TestCase):

    def test_NonStack(self):
        raise NoStackException


class NoStackException(Exception):

    def __str__(self):
        return "nothing"


    def __testNormal(self):
       pass
