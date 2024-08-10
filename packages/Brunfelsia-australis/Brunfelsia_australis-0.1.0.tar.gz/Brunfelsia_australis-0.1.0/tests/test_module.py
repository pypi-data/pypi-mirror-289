# tests/test_module.py

import unittest
from Brunfelsia_australis.module import find_closest_day

class TestFindClosestDay(unittest.TestCase):
    def test_find_closest_day(self):
        self.assertEqual(find_closest_day(114, 68, 190), '1日目')
        self.assertEqual(find_closest_day(240, 235, 250), '8日目')
        self.assertEqual(find_closest_day(158, 163, 236), '4日目')

if __name__ == "__main__":
    unittest.main()
