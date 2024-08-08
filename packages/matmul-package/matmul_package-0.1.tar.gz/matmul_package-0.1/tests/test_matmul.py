# tests/test_matmul.py
import unittest
import numpy as np
from src.matmul import matrix_multiply

class TestMatrixMultiplication(unittest.TestCase):
    def test_multiplication(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        result = matrix_multiply(A, B)
        expected = np.array([[19, 22], [43, 50]])
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
