import unittest
import bmiFunctions
import retFunctions

class test_calculations(unittest.TestCase):
    def test_calcBMI(self):
        #self.assertAlmostEqual(bmiFunctions.calcBMI(5, 5, 140), 23.8580)
        self.assertAlmostEquals(bmiFunctions.calcBMI(5,5,140), 23.8580, None, None, 0.0001)

if __name__ == '__main__':
    unittest.main()
