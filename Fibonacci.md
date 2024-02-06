# fibonacci: Efficient Calculation with Dynamic Programming

This file presents an overview of the fibonacci sequence and introduces an algorithm for calculating fibonacci numbers using dynamic programming, significantly improving performance, especially for large values of $n$.

## What is fibonacci?

The fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with $0$ and $1$.

The sequence begins:

$$f(0) = 0$$

$$f(1) = 1$$

For $n > 1$, each subsequent number $f(n)$ is calculated as the sum of the previous two numbers:

$$f(n) = f(n-1) + f(n-2)$$

## Fast fibonacci Algorithm

### Pseudocode:

```python
Function fibonacci(n) -> Integer:
    If n < 0:
        Return INVALID_INPUT
    If n == 0:
        Return 0
    If n == 1:
        Return 1
    End If

    Array fibonacci_arr[n + 1]
    For i from 0 to n:
        fibonacci_arr[i] = UNDEFINED
    End For

    fibonacci_arr[0] = 0
    fibonacci_arr[1] = 1
    fibonacci_arr[2] = 1

    Return fibonacci_helper(n, fibonacci_arr)

Function fibonacci_helper(n, memo) -> Integer:
    If memo[n] is not UNDEFINED:
        Return memo[n]
    End If

    more = fibonacci_helper(n / 2 + 1, memo)
    less = fibonacci_helper(n / 2, memo)

    If n % 2 == 1:
        memo[n] = more * more + less * less
    Else:
        memo[n] = less * (2 * more - less)
    End If

    Return memo[n]
```

### C++ Implementation:

```cpp
#include <iostream>
#include <vector>

#define UNDEFINED -1

int fibonacci_helper(int n, std::vector<int>& memo) {
    if (memo[n] != UNDEFINED)
        return memo[n];

    int more = fibonacci_helper(n / 2 + 1, memo);
    int less = fibonacci_helper(n / 2, memo);

    if (n % 2 == 1)
        memo[n] = more * more + less * less;
    else
        memo[n] = less * (2 * more - less);

    return memo[n];
}

int fibonacci(int n) {
    if (n < 0)
        return -1; // INVALID_INPUT
    if (n == 0)
        return 0;
    if (n == 1)
        return 1;

    std::vector<int> memo(n + 1, UNDEFINED);
    memo[0] = 0;
    memo[1] = 1;
    memo[2] = 1;

    return fibonacci_helper(n, memo);
}

```

## Complexity Analysis

- **Traditional Recursive Approach -> $O(2^n)$ :** The traditional recursive approach to compute fibonacci numbers has a time complexity of $O(2^n)$, leading to exponential growth in computation time for larger values of $n$.

- **Dynamic Programming Approach -> $O(n)$ :** By using dynamic programming, the time complexity of computing fibonacci numbers can be reduced to $O(n)$. This approach efficiently stores previously computed values and reuses them to compute subsequent fibonacci numbers, significantly improving performance.

- **Improved Algorithm with Dynamic Programming -> $O(log(n))$ :** The provided algorithm, combined with dynamic programming, achieves a time complexity of $O(log(n))$. By utilizing memoization and a divide-and-conquer strategy, the algorithm efficiently computes fibonacci numbers, offering a considerable speedup, especially for large values of $n$.
