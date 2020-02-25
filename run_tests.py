import sys
import unittest

from tests.MainTest import MainTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MainTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
