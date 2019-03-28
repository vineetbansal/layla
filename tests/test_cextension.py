from unittest import TestCase
from layla.mycmodule import hello, Double


class CExtTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHello(self):
        hello('world')

    def testDouble(self):
        self.assertEqual(84, Double(42))
