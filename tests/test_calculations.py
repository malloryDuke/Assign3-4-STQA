import unittest
import src.bmiFunctions as bmiFunctions
import src.retFunctions as retFunctions

class test_calculations(unittest.TestCase):
    def test_calcBMI(self):
        #self.assertAlmostEqual(bmiFunctions.calcBMI(5, 5, 140), 23.8580)
        self.assertAlmostEquals(bmiFunctions.calcBMI(5,5,140), 23.8580, None, None, 0.0001)

    def test_BMICat(self):
        self.assertEquals(bmiFunctions.getBMICategory(18.0), "underweight")

    def test_retAge(self):
        self.assertEquals(retFunctions.getRetirementAge(45, 3444, 0.10, 16000), 80)

    def test_retCat(self):
        self.assertEquals(retFunctions.getRetirementCategory(101), "Goal will NOT be met")

if __name__ == '__main__':
    unittest.main()
