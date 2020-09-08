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

    def test100_020_ShouldCollapseOneGoodDigit(self):
        value = '0'
        expectedResult = '0'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_030_ShouldCollapseTwoGoodDigits(self):
        value = '10'
        expectedResult = '1'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_040_ShouldCollapseThreeGoodDigits(self):
        value = '123'
        expectedResult = '6'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_050_ShouldCollapseTwoGoodDigits(self):
        value = '99'
        expectedResult = '9'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_060_ShouldCollapseFiveGoodDigits(self):
        value = '98769'
        expectedResult = '3'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test100_070_ShouldCollapseFiftyGoodDigits(self):
        value = '11111111111111111111111111111111111111111111111111'
        expectedResult = '5'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test200_010_ShouldNotCollapseFiftyOneGoodDigits(self):
        value = '111111111111111111111111111111111111111111111111111'
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test200_020_ShouldNotCollapseZeroGoodDigits(self):
        value = ''
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test200_030_ShouldNotCollapseThreeBadDigits(self):
        value = 'abc'
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test200_040_ShouldNotCollapseOneBadDigits(self):
        value = '-1'
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    def test200_050_ShouldNotCollapseTwoBadDigits(self):
        value = '1.1'
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)