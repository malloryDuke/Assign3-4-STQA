import unittest
import src.bmiFunctions as bmiFunctions
import src.retFunctions as retFunctions

class test_calculations(unittest.TestCase):
    def test_calcBMI(self):
        #self.assertAlmostEqual(bmiFunctions.calcBMI(5, 5, 140), 23.8580)
        self.assertAlmostEqual(bmiFunctions.calcBMI(5,5,140), 23.8580, None, None, 0.0001)
        self.assertAlmostEqual(bmiFunctions.calcBMI(10, 10, 280), 11.9290, None, None, 0.0001)
        self.assertAlmostEqual(bmiFunctions.calcBMI(.1, .2, 1.1), 404.0816, None, None, 0.0001)
        self.assertAlmostEqual(bmiFunctions.calcBMI(100, 100, 2800), 1.1929, None, None, 0.0001)
        self.assertAlmostEqual(bmiFunctions.calcBMI(10000, 10000, 280000), 0.011929, None, None, 0.0001)

    def test_BMICat(self):
        self.assertEqual(bmiFunctions.getBMICategory(18.0), "underweight")
        self.assertEqual(bmiFunctions.getBMICategory(1.0), "underweight")
        self.assertEqual(bmiFunctions.getBMICategory(10.0), "underweight")
        self.assertEqual(bmiFunctions.getBMICategory(18.4), "underweight")
        self.assertEqual(bmiFunctions.getBMICategory(18.5), "normal")
        self.assertEqual(bmiFunctions.getBMICategory(18.6), "normal")
        self.assertEqual(bmiFunctions.getBMICategory(20.0), "normal")
        self.assertEqual(bmiFunctions.getBMICategory(24.9), "normal")
        self.assertEqual(bmiFunctions.getBMICategory(25.0), "overweight")
        self.assertEqual(bmiFunctions.getBMICategory(25.1), "overweight")
        self.assertEqual(bmiFunctions.getBMICategory(27.0), "overweight")
        self.assertEqual(bmiFunctions.getBMICategory(29.9), "overweight")
        self.assertEqual(bmiFunctions.getBMICategory(30.0), "obese")
        self.assertEqual(bmiFunctions.getBMICategory(30.1), "obese")
        self.assertEqual(bmiFunctions.getBMICategory(50.0), "obese")
        self.assertEqual(bmiFunctions.getBMICategory(1000.0), "obese")
        self.assertEqual(bmiFunctions.getBMICategory(0.1), "underweight")

    def test_retAge(self):
        self.assertEqual(retFunctions.getRetirementAge(45, 3444, 0.10, 16000), 80)
        self.assertEqual(retFunctions.getRetirementAge(5, 34, 0.5, 8000), 354)
        self.assertEqual(retFunctions.getRetirementAge(0.5, 0.34, 0.0010, 16), 34859.5)
        self.assertEqual(retFunctions.getRetirementAge(100, 100, 100, 100), 101)
        self.assertEqual(retFunctions.getRetirementAge(0.1, 0.1, 0.1, 0.1), 8.1)
        self.assertEqual(retFunctions.getRetirementAge(450, 34440, 0.20, 160000), 468)
        self.assertEqual(retFunctions.getRetirementAge(100, 100, 100, 100), 101)


    def test_retCat(self):
        self.assertEqual(retFunctions.getRetirementCategory(101), "Goal will NOT be met")
        self.assertEqual(retFunctions.getRetirementCategory(99), "Goal will be met")
        self.assertEqual(retFunctions.getRetirementCategory(100), "Goal will NOT be met")
        self.assertEqual(retFunctions.getRetirementCategory(1000), "Goal will NOT be met")
        self.assertEqual(retFunctions.getRetirementCategory(1), "Goal will be met")
        self.assertEqual(retFunctions.getRetirementCategory(0.11111), "Goal will be met")



if __name__ == '__main__':
    unittest.main()