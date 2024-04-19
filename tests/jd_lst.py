import unittest
import sys , os
from datetime import datetime
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))

# Import the functions you want to test
from orbital_gui.tasks.jd_lst import calculate_jd, calculate_lst

class TestCalculateJDAndLST(unittest.TestCase):
    def test_calculate_jd(self):
        # Test calculate_jd function with known inputs and expected output
        year = 2024
        month = 4
        day = 19
        hour = 12
        minute = 30
        second = 15
        ut = hour + minute / 60 + second / 3600
        expected_jd = 2460420.0210069446  # This is the expected Julian Date and Time for the given inputs
        jd = calculate_jd(year, month, day, hour, minute, second, ut)
        print(jd) 
        self.assertAlmostEqual(jd, expected_jd, places=5)  # Assert that the calculated JD is close to the expected value

    def test_calculate_lst(self):
        # Test calculate_lst function with known inputs and expected output
        jd = 2459426.0219791666  # Example Julian Date and Time
        longitude = 86.441662  # Example longitude
        ut = 12.508333333333333  # Example Universal Time
        expected_lst = 3.3565558518166654  # This is the expected Local Sidereal Time for the given inputs
        lst = calculate_lst(jd, longitude, ut)
        print(lst)
        self.assertAlmostEqual(lst, expected_lst, places=5)  # Assert that the calculated LST is close to the expected value

if __name__ == '__main__':
    unittest.main()
