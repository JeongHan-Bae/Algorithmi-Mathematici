# cython: language_level=3

import numpy as np
cimport numpy as np
from numpy.linalg import matrix_power

cdef np.ndarray[object, ndim=2] compute_result_matrix(int n, int init1: int, int init2: int):
    cdef np.ndarray[object, ndim=2] M = np.array([[1, 1], [1, 0]], dtype=object)
    cdef np.ndarray[object, ndim=2] V = np.array([[init2], [init1]], dtype=object)
    return np.dot(matrix_power(M, n), V)

def fibonacci(int n, *args) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    init1: int = 0
    init2: int = 1

    if len(args) == 1 and isinstance(args[0], tuple):
        init1, init2 = args[0]
    elif len(args) == 2:
        init1, init2 = args

    cdef np.ndarray[object, ndim=2] result_matrix = compute_result_matrix(n, init1, init2)

    return result_matrix[1, 0]

def fibonacci_list(int length, int n=0, init_vals: tuple[int, int]=(0, 1)) -> list:
    if length < 1:
        raise ValueError("length must be greater than or equal to 1")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    init1: int = init_vals[0]
    init2: int = init_vals[1]

    cdef np.ndarray[object, ndim=2] result_matrix = compute_result_matrix(n, init1, init2)

    fib_n = result_matrix[1, 0]
    fib_n1 = result_matrix[0, 0]

    cdef np.ndarray[object, ndim=1] fib_list = np.zeros(length, dtype=object)
    fib_list[0] = fib_n
    if length > 1:
        fib_list[1] = fib_n1

    for i in range(2, length):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]

    return fib_list.tolist()
