# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from sasa.tasks.result import Result


class TestResult(unittest.TestCase):

    def test(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
