from unittest import TestCase
from layla.mycmodule import fibonacci_init, fibonacci_next, fibonacci_current


class CExtTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFib1(self):
        fibonacci_init(1, 1)
        fibonacci_next()
        self.assertEqual(1, fibonacci_current())

    def testFib2(self):
        fibonacci_init(1, 1)
        for _ in range(5):
            fibonacci_next()
        self.assertEqual(8, fibonacci_current())  # 1 1 2 3 5 8
