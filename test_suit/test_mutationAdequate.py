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
        
        #3
        actual = Triangle.classify(7, 10, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

        #4
        actual = Triangle.classify(9, 40, 41)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
        
        #3
        actual = Triangle.classify(7, 10, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

        #4
        actual = Triangle.classify(9, 40, 41)
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
        
        #13 - Does not follow [(a+b > c), (b+c > a), (c+a > b)]
        actual = Triangle.classify(2.5, 5, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        #14 - Does not follow [(a+b > c), (b+c > a), (c+a > b)]
        actual = Triangle.classify(1, 2, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        #15 - Does not follow [(a+b > c), (b+c > a), (c+a > b)]
        actual = Triangle.classify(3, 1, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
         #16 - Does not follow [(a+b > c), (b+c > a), (c+a > b)]
        actual = Triangle.classify(2, 3, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
         #17 - Does not follow [(a+b > c), (b+c > a), (c+a > b)]
        actual = Triangle.classify(1, 1, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        # 18 - Does not follow [(a+b > c), (b+c > a), (c+a > b)]
        actual = Triangle.classify(1, 2, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        #19 - Does not follow [(a+b > c), (b+c > a), (c+a > b)]
        actual = Triangle.classify(2, 1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        # 20 - Does not follow [(a+b > c), (b+c > a), (c+a > b)]
        actual = Triangle.classify(1, 2, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        #21 - inputs can not be negative and zero
        actual = Triangle.classify(-1, -2, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        #22 - inputs can not be negative and zero
        actual = Triangle.classify(0, -1, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        #23 - inputs can not be negative and zero
        actual = Triangle.classify(-1, 0, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        #24 - inputs can not be negative and zero
        actual = Triangle.classify(-1, 2, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        #25 - inputs can not be negative and zero
        actual = Triangle.classify(0, -1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        #26 - inputs can not be negative and zero
        actual = Triangle.classify(1, 0, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        #26 - inputs can not be negative and zero
        actual = Triangle.classify(-1, -5, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        #27 - Does not follow [(a+b > c), (b+c > a), (c+a > b)]
        actual = Triangle.classify(10, 2, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        #28 - Does not follow [(a+b > c), (b+c > a), (c+a > b)]
        actual = Triangle.classify(2, 10, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
        #29 - Does not follow [(a+b > c), (b+c > a), (c+a > b)]
        actual = Triangle.classify(4, 2, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

        
        # Equilateral triangles

        #1
        actual = Triangle.classify(5, 5, 5)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
        
         #2
        actual = Triangle.classify(2.5, 2.5, 2.5)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
        
        #3
        actual = Triangle.classify(1, 1, 1)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)
        
         #4
        actual = Triangle.classify(100, 100, 100)
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
        
        #4
        actual = Triangle.classify(3, 3, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

        #5
        actual = Triangle.classify(3, 5, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

        #6
        actual = Triangle.classify(5, 3, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
        

if __name__ == '__main__':
    unittest.main()
