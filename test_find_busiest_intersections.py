import unittest
from find_busiest_intersections import find_busiest_intersections

class TestFindBusiestInterSections(unittest.TestCase):
    def test_single_busiest_intersection(self):
        data = {
            'Intersection1' : 100,
            'Intersection2' : 200,
            'Intersection3' : 150
        }
        result = find_busiest_intersections(data)
        self.assertEqual(result, ['Intersection2'])

    def test_multiple_busiest_intersections(self):
        data = {
            'Intersection1' : 100,
            'Intersection2' : 200,
            'Intersection3' : 200
        }
        result = find_busiest_intersections(data)
        self.assertEqual(result, ['Intersection2','Intersection3'])

    def test_empty_data(self):
        data = {}
        result = find_busiest_intersections(data)
        self.assertEqual(result, [])

    def test_all_same_values(self):
        data = {
            'Intersection1' : 100,
            'Intersection2' : 100,
            'Intersection3' : 100
        }
        result = find_busiest_intersections(data)
        self.assertEqual(result, ['Intersection1','Intersection2','Intersection3'])

if __name__ == '__main__':
    unittest.main()