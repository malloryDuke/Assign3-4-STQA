import unittest
import src.bmi_functions as bmi_functions
import src.ret_functions as ret_functions


class test_calculations(unittest.TestCase):
    def test_calc_bmi(self):
        # self.assertAlmostEqual(bmi_functions.calc_bmi(5, 5, 140), 23.8580)
        self.assertAlmostEqual(bmi_functions.calc_bmi(5, 5, 140), 23.8580, None, None, 0.0001)
        self.assertAlmostEqual(bmi_functions.calc_bmi(10, 10, 280), 11.9290, None, None, 0.0001)
        self.assertAlmostEqual(bmi_functions.calc_bmi(.1, .2, 1.1), 404.0816, None, None, 0.0001)
        self.assertAlmostEqual(bmi_functions.calc_bmi(100, 100, 2800), 1.1929, None, None, 0.0001)
        self.assertAlmostEqual(bmi_functions.calc_bmi(10000, 10000, 280000), 0.011929, None, None, 0.0001)

    def test_bmi_cat(self):
        self.assertEqual(bmi_functions.get_bmi_category(18.0), "underweight")
        self.assertEqual(bmi_functions.get_bmi_category(1.0), "underweight")
        self.assertEqual(bmi_functions.get_bmi_category(10.0), "underweight")
        self.assertEqual(bmi_functions.get_bmi_category(18.4), "underweight")
        self.assertEqual(bmi_functions.get_bmi_category(18.5), "normal")
        self.assertEqual(bmi_functions.get_bmi_category(18.6), "normal")
        self.assertEqual(bmi_functions.get_bmi_category(20.0), "normal")
        self.assertEqual(bmi_functions.get_bmi_category(24.9), "normal")
        self.assertEqual(bmi_functions.get_bmi_category(25.0), "overweight")
        self.assertEqual(bmi_functions.get_bmi_category(25.1), "overweight")
        self.assertEqual(bmi_functions.get_bmi_category(27.0), "overweight")
        self.assertEqual(bmi_functions.get_bmi_category(29.9), "overweight")
        self.assertEqual(bmi_functions.get_bmi_category(30.0), "obese")
        self.assertEqual(bmi_functions.get_bmi_category(30.1), "obese")
        self.assertEqual(bmi_functions.get_bmi_category(50.0), "obese")
        self.assertEqual(bmi_functions.get_bmi_category(1000.0), "obese")
        self.assertEqual(bmi_functions.get_bmi_category(0.1), "underweight")

    def test_ret_age(self):
        self.assertEqual(ret_functions.get_retirement_age(45, 3444, 0.10, 16000), 80)
        self.assertEqual(ret_functions.get_retirement_age(5, 34, 0.5, 8000), 354)
        self.assertEqual(ret_functions.get_retirement_age(0.5, 0.34, 0.0010, 16), 34859.5)
        self.assertEqual(ret_functions.get_retirement_age(100, 100, 100, 100), 101)
        self.assertEqual(ret_functions.get_retirement_age(0.1, 0.1, 0.1, 0.1), 8.1)
        self.assertEqual(ret_functions.get_retirement_age(450, 34440, 0.20, 160000), 468)
        self.assertEqual(ret_functions.get_retirement_age(100, 100, 100, 100), 101)

    def test_retCat(self):
        self.assertEqual(ret_functions.get_retirement_category(101), "Goal will NOT be met")
        self.assertEqual(ret_functions.get_retirement_category(99), "Goal will be met")
        self.assertEqual(ret_functions.get_retirement_category(100), "Goal will NOT be met")
        self.assertEqual(ret_functions.get_retirement_category(1000), "Goal will NOT be met")
        self.assertEqual(ret_functions.get_retirement_category(1), "Goal will be met")
        self.assertEqual(ret_functions.get_retirement_category(0.11111), "Goal will be met")


if __name__ == '__main__':
    unittest.main()
