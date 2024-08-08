# src/matmul.py

from joblib import Parallel, delayed
import numpy as np

def matrix_multiply(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("Number of columns in A must be equal to the number of rows in B")

    def compute_element(i, j):
        return sum(A[i, k] * B[k, j] for k in range(A.shape[1]))

    result = Parallel(n_jobs=-1)(delayed(compute_element)(i, j) for i in range(A.shape[0]) for j in range(B.shape[1]))
    return np.array(result).reshape(A.shape[0], B.shape[1])
