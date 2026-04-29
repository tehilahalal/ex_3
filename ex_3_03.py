import sys
import numpy as np

def matrix_multiply_naive(A, B):
    # check A.shape and B.shape and make sure that the matrices
    # are compatible for multiplication
    if A.shape[1]!=B.shape[0]: # Replace with a condition that checks compatibility
        raise ValueError("Matrix dimensions are not compatible for multiplication")

    result_dtype = np.result_type(A.dtype, B.dtype)
    result_shape = (A.shape[0], B.shape[1])
    result = np.zeros(result_shape, dtype=result_dtype)

    number_of_multiplications = 0
    for i in range (
        for j in range(
            for k in range(
                
    return result, number_of_multiplications
