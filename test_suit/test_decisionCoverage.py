import unittest
from isTriangle import Triangle

class TestTriangleClassification(unittest.TestCase):

    def test_classify(self):

        # Scalene triangles
        #1
        actual = Triangle.classify(3, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

        #2
        actual = Triangle.classify(15, 32, 34)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

        # Invalid triangles

        #1 - all sides 0 is an invalid triangle
        actual = Triangle.classify(0, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        #2 - having a negative side is an invalid triangle
        actual = Triangle.classify(-5, 2, 6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        #3 - having a negative side is an invalid triangle
        actual = Triangle.classify(2, -5, 6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        #4 - having a negative side is an invalid triangle
        actual = Triangle.classify(2, 6, -5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        #5 - Does not follow [(a+b > c), (b+c > a), (c+a > b)] and one side is 0
        actual = Triangle.classify(0, 4, 6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        #6 - Does not follow [(a+b > c), (b+c > a), (c+a > b)] and one side is 0
        actual = Triangle.classify(6, 0, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        #7 - Does not follow [(a+b > c), (b+c > a), (c+a > b)] and one side is 0
        actual = Triangle.classify(12, 8, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        #8 - Does not follow [(a+b > c), (b+c > a), (c+a > b)]
        actual = Triangle.classify(1, 4, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        #9 - Does not follow [(a+b > c), (b+c > a), (c+a > b)]
        actual = Triangle.classify(5, 5, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        #10 - a side can not be negative
        actual = Triangle.classify(12, 8, -2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        #11 - a side can not be negative
        actual = Triangle.classify(1, -4, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        #12 - a side can not be negative
        actual = Triangle.classify(-5, 5, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        
        # Equilateral triangles

        #1
        actual = Triangle.classify(5, 5, 5)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
        


        # Isosceles triangles

        #1
        actual = Triangle.classify(5, 5, 8)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

        #2
        actual = Triangle.classify(3, 2, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

        #3
        actual = Triangle.classify(2, 3, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
