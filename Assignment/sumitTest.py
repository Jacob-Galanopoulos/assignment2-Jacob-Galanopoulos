import unittest
import Assignment.sumit as sumit

class SumitTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test100_010_ShouldCollapseOneGoodDigit(self):
        value = '5'
        expectedResult = '5'
        actualResult = sumit.sumit(value)
        self.assertEqual(expectedResult, actualResult)
