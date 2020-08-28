import unittest
import Assignment.collapse as collapse

class CollapseTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test100_010_ShouldCollapseOneGoodDigit(self):
        value = '5'
        expectedResult = '5'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
