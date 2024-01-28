# Fibonacci: Efficient Calculation with Dynamic Programming

This file presents an overview of the Fibonacci sequence and introduces an algorithm for calculating Fibonacci numbers using dynamic programming, significantly improving performance, especially for large values of $n$.

## What is Fibonacci?

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with $0$ and $1$.

The sequence begins:

$$f(0) = 0$$

$$f(1) = 1$$

For $n > 1$, each subsequent number $f(n)$ is calculated as the sum of the previous two numbers:

$$f(n) = f(n-1) + f(n-2)$$

## Fast Fibonacci Algorithm

### Pseudocode:

```pseudocode
FUNCTION Fibonacci(n):
    IF n < 0:
        RETURN INVALID_INPUT
    IF n == 0:
        RETURN 0
    IF n == 1:
        RETURN 1

    ARRAY Fibonacci_Arr[n + 1]
    FOR i FROM 0 TO n:
        Fibonacci_Arr[i] = UNDEFINED
    END FOR

    Fibonacci_Arr[0] = 0
    Fibonacci_Arr[1] = 1
    Fibonacci_Arr[2] = 1

    RETURN FibonacciHelper(n, Fibonacci_Arr)

FUNCTION FibonacciHelper(n, memo):
    IF memo[n] is not UNDEFINED:
        RETURN memo[n]

    more = FibonacciHelper(n / 2 + 1, memo)
    less = FibonacciHelper(n / 2, memo)

    IF n % 2 == 1:
        memo[n] = more * more + less * less
    ELSE:
        memo[n] = less * (2 * more - less)
    END IF

    RETURN memo[n]
```

### C++ Implementation:

```cpp
#include <iostream>
#include <vector>

#define UNDEFINED -1

int FibonacciHelper(int n, std::vector<int>& memo) {
    if (memo[n] != UNDEFINED)
        return memo[n];

    int more = FibonacciHelper(n / 2 + 1, memo);
    int less = FibonacciHelper(n / 2, memo);

    if (n % 2 == 1)
        memo[n] = more * more + less * less;
    else
        memo[n] = less * (2 * more - less);

    return memo[n];
}

int Fibonacci(int n) {
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

    return FibonacciHelper(n, memo);
}

```

## Complexity Analysis

- **Traditional Recursive Approach -> $O(2^n)$ :** The traditional recursive approach to compute Fibonacci numbers has a time complexity of $O(2^n)$, leading to exponential growth in computation time for larger values of $n$.

- **Dynamic Programming Approach -> $O(n)$ :** By using dynamic programming, the time complexity of computing Fibonacci numbers can be reduced to $O(n)$. This approach efficiently stores previously computed values and reuses them to compute subsequent Fibonacci numbers, significantly improving performance.

- **Improved Algorithm with Dynamic Programming -> $O(log(n))$ :** The provided algorithm, combined with dynamic programming, achieves a time complexity of $O(log(n))$. By utilizing memoization and a divide-and-conquer strategy, the algorithm efficiently computes Fibonacci numbers, offering a considerable speedup, especially for large values of $n$.
