from unittest import TestCase
from mypack.mysubmodule import greeting


class GreetingTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGreeting(self):
        self.assertEqual('Hello World', greeting())
