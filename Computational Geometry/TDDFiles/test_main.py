import unittest
from closest_pair_points import closestPairs
from convex_hull import convexHull
from largest_empty_circle import largestEmptyCircle
from line_segment_intersection import lineSegmentIntersection

class TestCalls(unittest.TestCase):

    # not entirely sure if these tests are
    # set up correct

    def testClosestPairs(self):
        points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
        expected_output = [(2, 3), (3,4)]

        result = closestPairs(points)
        self.assertEqual(result, expected_output)

    def testLineSegmentIntersection(self):
        # Test case 1: Intersecting line segments
        line1 = [(0, 0), (2, 2)]
        line2 = [(0, 2), (2, 0)]
        expected_output = (1, 1)
        self.assertEqual(lineSegmentIntersection(line1, line2), expected_output)

        # Test case 2: Non-intersecting line segments
        line1 = [(0, 0), (2, 2)]
        line2 = [(3, 3), (4, 4)]
        expected_output = None
        self.assertEqual(lineSegmentIntersection(line1, line2), expected_output)

    def testLargestEmptyCircle(self):
        # Test case 1: Points are collinear
        points = [(0, 0), (1, 1), (2, 2)]
        expected_output = (1, 1, 1)
        self.assertEqual(largestEmptyCircle(points), expected_output)

        # Test case 2: Points are not collinear
        points = [(0, 0), (1, 1), (2, 0)]
        expected_output = (0.5, 0.5, 0.5)
        self.assertEqual(largestEmptyCircle(points), expected_output)

    def testConvexHull(self):
        # Test case 1: Points are collinear
        points = [(0, 0), (1, 1), (2, 2)]
        expected_output = [(0, 0), (2, 2)]
        self.assertEqual(convexHull(points), expected_output)

        # Test case 2: Points are not collinear
        points = [(0, 0), (1, 1), (2, 0), (1, 0)]
        expected_output = [(0, 0), (2, 0), (1, 1)]
        self.assertEqual(convexHull(points), expected_output)

if __name__ == '__main__':
    unittest.main()
