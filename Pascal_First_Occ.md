# Finding the First Occurrence of a Positive Integer in Pascal's Triangle (양휘의 삼각형)

## Introduction

Pascal's Triangle, known as "양휘의 삼각형" in  Chinese Korean (Yang Hui's Triangle), is a triangular array of binomial coefficients, named after the French mathematician Blaise Pascal. 

Each row $i$ of Pascal's Triangle contains $i+ 1$ elements, with the first row indexed as 0. 

The triangle holds historical significance in Chinese mathematics as well, known as "楊輝三角" (Yang Hui's Triangle), named after the Chinese mathematician Yang Hui. 

The value at position $(i, j)$ in Pascal's Triangle represents the binomial coefficient $C(i, j)$, which calculates the number of ways to choose $j$ elements from a set of $i$ elements. 
In other words, 
$$Pascal[i][j] = C(i, j)$$

In this documentation, we explore an algorithm to find the first occurrence of a given positive integer $n$ in Pascal's Triangle.

## Algorithm Overview

The provided algorithm iterates through Pascal's Triangle to locate the first occurrence of a specified positive integer `n`. It starts from the top of the triangle and moves diagonally down, examining each element until it finds `n`. 
The algorithm employs a combination-based approach to efficiently traverse the triangle.

### Pseudocode

```python
Function find_in_pascal(n) -> Tuple[int, int]:
    If n = 1 Then
        Return (0, 0)  # Special case: 1 at the top of the triangle
    End If
    
    row: int = 2  # Start at row 2
    col: int = 1  # Start at column 1
    comb: long long int = 2  # Initial combination value
    
    While True:
        If comb < n Then
            If row / 2 = col Then
                # At the middle, already the greatest value of this row, move to the next row
                row = row + 1
                comb = comb * row / (row - col)
            Else
                greater_comb: long long int = comb * (row - col) / (col + 1)
                If greater_comb > n Then
                    # The value to the right is greater than n, move to the next row
                    row = row + 1
                    comb = comb * row / (row - col)
                Else
                    col = col + 1
                    comb = greater_comb
                End If
            End If
        Else If comb > n Then
            # Too large, move left
            col = col - 1
            comb = comb * (col + 1) / (row - col)
        Else
            Return (row, col)  # Found the first occurrence of n
        End If
        
        If row * (row - 1) / 2 > n Then
            Return (n, 1)  # No possibility to find n in column greater than 1
        End If
    End While
```

## Realization in C++

### Implementation

```cpp
#include <iostream>
#include <tuple>

std::tuple<int, int> find_in_pascal(int n) {
    if (n == 1) {
        return std::make_tuple(0, 0);
        // Special case: 1 at the top of the triangle
    }

    int row = 2;            // Start at row 2
    int col = 1;            // Start at column 1
    long long int comb = 2; // Initial combination value

    while (true) {
        if (comb < n) {
            if (row / 2 == col) {
                /* At the middle, already the greatest value of this row, move
                 * to the next row
                 */
                row = row + 1;
                comb = comb * row / (row - col);
            } else {
                long long int greater_comb = comb * (row - col) / (col + 1);
                if (greater_comb > n) {
                    /* The value to the right is greater than n, move to the
                     * next row
                     */
                    row = row + 1;
                    comb = comb * row / (row - col);
                } else {
                    col = col + 1;
                    comb = greater_comb;
                }
            }
        } else if (comb > n) {
            // Too large, move left
            col = col - 1;
            comb = comb * (col + 1) / (row - col);
        } else {
            return std::make_tuple(row, col);
            // Found the first occurrence of n
        }

        if (row * (row - 1) / 2 > n) {
            return std::make_tuple(n, 1);
            // No possibility to find n in column greater than 1
        }
    }
}
```

## Complexity Analysis

### Time Complexity

The time complexity of the algorithm varies based on the location of the target integer within Pascal's Triangle.

- **Best Case**: $O(log(n))$ 
  In the best case scenario, the target integer is found relatively quickly, typically closer to the top of Pascal's Triangle. This behavior resembles binary search, where the search space is halved at each step.

- **Worst Case**: $O(sqrt(n))$ 
  In the worst case scenario, the target integer is located near the bottom of Pascal's Triangle. As the algorithm traverses diagonally, approaching the target, the number of iterations grows approximately proportionally to the square root of the target integer.

### Space Complexity

The space complexity of the algorithm is $O(1)$, as it utilizes only a constant amount of additional memory regardless of the input size.

## Conclusion

This algorithm efficiently locates the first occurrence of a positive integer in Pascal's Triangle, providing a clear and concise solution for this problem.

## Comparison with Traditional DP Algorithm

Here's the comparison between the provided algorithm and a traditional brute force dynamic programming (DP) algorithm for finding the first occurrence of a positive integer in Pascal's Triangle:

### Provided Algorithm

- **Time Complexity**: 
  - Best Case: $O(log(n))$
  - Worst Case: $O(sqrt(n))$

- **Space Complexity**: $O(1)$

### Traditional DP Algorithm

- **Time Complexity**: $O(n)$
  - Generating Pascal's Triangle up to $sqrt(2 * n) + 1$ requires iterating through each element, leading to linear time complexity.

- **Space Complexity**: $O(n)$
  - Pascal's Triangle up to $sqrt(n)$ elements requires storing $sqrt(n)$ rows with $O(sqrt(n))$ elements each, leading to linear space complexity.

The traditional DP algorithm iterates through rows from 0 to $sqrt(2 * n) + 1$. If $n$ is not found within these rows, it is guaranteed to be located at position $(n, 1)$ 
since each row $i$ has $i + 1$ elements and only about half of the elements $i + 1 /2$ need to be considered. Therefore, the time complexity is $O(n)$ and the space complexity is also $O(n)$, proportional to the input size $n$.

### Comparison

- **Time Complexity**: 
  - The provided algorithm has a superior time complexity, especially for large values of $n$, due to its more efficient traversal method.
  - Traditional DP algorithm has a linear time complexity, which is also efficient for finding the first occurrence of a positive integer in Pascal's Triangle.

- **Space Complexity**: 
  - The provided algorithm has a space complexity of $O(1)$, indicating that it uses a constant amount of additional memory irrespective of the input size.
  - The traditional DP algorithm has a space complexity of $O(n)$, where $n$ represents the target integer, indicating that it uses a linear amount of additional memory proportional to the input size.
    
## Conclusion

This algorithm efficiently locates the first occurrence of a positive integer in Pascal's Triangle, providing a clear and concise solution for this problem.


For more examples and implementations in C++ and Python, visit the [Pascal folder](/Pascal).
