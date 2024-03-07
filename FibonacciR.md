# Supplemental File: Fibonacci Robust (FibonacciR.md)

This document serves as a supplement to the main [Fibonacci document](Fibonacci.md). It provides additional information and an alternative solution for calculating Fibonacci numbers efficiently.

## Introduction

Building upon the fast dynamic programming approach presented in the main Fibonacci document, 
this supplemental file introduces an additional method for calculating Fibonacci numbers: utilizing matrix exponentiation. 

The two solutions offer different trade-offs in terms of space complexity and potential performance, providing a comprehensive overview of different techniques for Fibonacci number computation.

## Pseudocode - Matrix Exponentiation

```python
Function fibonacci(n, init1 = 0, init2 = 1) -> T:
    Create a square matrix M of size 2 * 2
    Set M[0][0] = M[0][1] = M[1][0] = 1
    Set M[1][1] = 0
    
    Create a vertical matrix V of size 2 * 1
    Set V[0][0] = init2
    Set V[1][0] = init1

    Compute M raised to the power of n using matrix exponentiation
    result_matrix = M.pow(n) * V

    Return the element at position (1, 0) of result_matrix, representing the nth Fibonacci number
```

## C++ Realization

```cpp
// using a lib which i will upload later
template <typename T>
T fibonacci(size_t n, T init1 = 0, T init2 = 1) {
    // Define the matrix M for Fibonacci calculation
    square_matrix<T> M(2);
    M(0, 0) = M(0, 1) = M(1, 0) = 1;

    vertical_matrix<T> V(2);
    V(0, 0) = init2;
    V(1, 0) = init1;
    // Compute M^n
    auto result_matrix = M.pow(n) * V;

    // Return the element at (0, 1) which represents the nth Fibonacci number
    return result_matrix(1, 0);
}
```

## Complexity Analysis

- **Time Complexity:** Both methods have a time complexity of $O(\log n)$ due to the divide-and-conquer strategy used. However, the exact constants involved may differ.
- **Space Complexity:**
  - **Matrix Exponentiation Method:** The space complexity is $O(1)$, requiring only constant space for matrices M and V and intermediate computations.
  - **Fast Dynamic Programming Method:** The space complexity is $O(n)$ due to the array used for memoization. This may not be favorable for extremely large values of n due to memory constraints.

## Comparison and Conclusion

Although both methods operate within the $O(\log n)$ time complexity, the fast dynamic programming method might exhibit better performance due to its interaction with primitive types, 
while the matrix exponentiation method involves interacting with containers. However, the matrix exponentiation method offers a space-efficient solution with a constant space complexity of $O(1)$, 
making it suitable for large values of n where memory overhead is a concern. Therefore, the choice between the two methods depends on the specific requirements and constraints of the application.
