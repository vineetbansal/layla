from unittest import TestCase
from layla.mycmodule import square


class CExtTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSquare(self):
        self.assertEqual(9, square(3))
