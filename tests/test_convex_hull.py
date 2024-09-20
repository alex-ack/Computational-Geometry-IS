import unittest
from basics.point import Point
from algorithms.convex_hull import graham_scan

class TestConvexHull(unittest.TestCase):
    def test_convex_hull(self):
        points = [Point(0, 0), Point(1, 1), Point(2, 2), Point(0, 2), Point(2, 0)]
        hull = graham_scan(points)
        expected_hull = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
        self.assertEqual(hull, expected_hull)

if __name__ == '__main__':
    unittest.main()