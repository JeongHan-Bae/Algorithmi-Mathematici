# The Josephus Problem: Finding the Last Survivor

## Introduction

The Josephus Problem is a classic mathematical puzzle with applications in various fields such as computer science and number theory. It involves determining the position of the last survivor in a circle of people subjected to a deadly elimination process.

## Problem Statement

Given a circle of $n$ people numbered from 1 to $n$, where each person kills the next person in a clockwise direction until only one person remains, the task is to find the position of the last survivor.

## Traditional Approach

The traditional approach works by simulating the elimination process in a circle. If it's person $i$'s turn and there exists a person $j$ alive, with all people between $i$ and $j$ being dead, then person $j$ is eliminated. The search for the next alive person continues after $j$.

## Recursive Solution

### Pseudocode

```python
Function josephus_recursive(n) -> Integer:
    # Base case
    If n == 1:
        Return 1
    End If
    # Divide the problem size by 2
    If n is Even:
        Return 2 * josephus_recursive(n / 2) - 1
    Else:
        If josephus_recursive((n + 1)/ 2) == 1:
            Return n
        Else:
            Return 2 * josephus_recursive((n + 1)/ 2) - 3
```

### Explanation
For the recursive approach, once the persons are eliminated from beginning to end:

If $n$ is even, all even positions are eliminated, leaving only the odd positions. 
Thus, we need to process the remaining queue of $n/2$ persons, and the new position $k = \text{josephus}(n/2)$ can be projected to $2 \times k - 1$ in the original queue.

If $n$ is odd, we eliminate $n/2$ persons, leaving $n/2 + 1$ persons. 
The last person becomes the first. For the new position $k = \text{josephus}((n+1)/2)$, if $k$ is 1, it refers to the last position in the original queue, which is $n$. 
Otherwise, it refers to $2 \times k - 3$ in the original queue.

### Iterative C++ Implementation:
```cpp
#include <stack>

int josephus(int n) {
    std::stack<int> num_stk;
    std::stack<bool> parity_stk;
    num_stk.emplace(n);
    while(num_stk.top() != 1){
        if (n % 2 == 1){
            parity_stk.emplace(true);
        } else {
            parity_stk.emplace(false);
        }
        num_stk.emplace(n = (n + 1) / 2);
    }
    int result = 1;
    while(!parity_stk.empty()){
        bool odd = parity_stk.top();
        parity_stk.pop();
        num_stk.pop();
        if (odd){
            if (result == 1){
                result = num_stk.top();
            } else {
                result = 2 * result - 3;
            }
        } else {
            result = 2 * result - 1;
        }
    }
    return result;
}
```

## Improved Solution

### Pseudocode

```python
Function josephus_rapid(n) -> Integer:
    Let k = floor(log2(n))
    # Find the largest k such that 2 ^ k - 1 < n
    Let j = n - pow(2, k) + 1
    Return 2 * j - 1
```

### Explanation

The improved solution utilizes a pattern observed in the Josephus sequence to directly compute the position of the last survivor without iterating through the entire circle.

We observe that if $n$ persons remain, the person at position $\text{josephus}(n)$ will be the last survivor. 
When we increment $n$, one more person needs to be eliminated, so the person at position $\text{josephus}(n) + 1$ will be eliminated, and the survivor will be the person at position $\text{josephus}(n) + 2$.

If $\text{josephus}(n) + 2 > (n + 1)$, this will bypass to the front, leading to position $\text{josephus}(n) + 1 - n$.

**This observation forms a pattern:**

For each row $k$, the elements $j$ are $2 \times j - 1$.

The number of elements in rows from 1 to $k$ is given by $2 ^ k - 1$.

We can find the maximum $k$ such that $2 ^ k - 1 < n$, and let $j = n - 2 ^ k + 1$. Then, the result should be $2 \times j - 1$.

```python
1 # 1 + 2 = 3 > 2
1 3 # 3 + 2 = 5 > 4
1 3 5 7 # 7 + 2 = 9 > 8
1 3 5 7 9 11 13 15 # 15 + 2 = 17 > 16
"""
1st row has 2 ^ 1 - 1 element
1st & 2nd rows have 2 ^ 2 - 1 elements
1st to 3rd rows have 2 ^ 3 - 1 elements, etc.
"""
...
```

By utilizing this formula, the improved solution achieves constant time complexity $O(1)$ and constant space complexity $O(1)$, making it highly efficient for calculating the position of the last survivor.

### C++ Implementation:

```cpp
#include <cmath>

int josephus(int n) {
    int k = std::floor(std::log2(n));
    int j = n - static_cast<int>(std::pow(2, k)) + 1;
    // int j = n - (1 << k) + 1;
    return 2 * j - 1;
}
```

## Complexity Analysis

### Traditional Approach

The time complexity of the traditional approach is **$O(n)$**. In each iteration, one person is eliminated, resulting in exactly $n$ iterations in the worst, average, and best cases. 
Thus, the time complexity remains linear with respect to the input size $n$. 
Additionally, the space complexity is $O(n)$ as we need to maintain a list of the remaining people in the circle.

### Recursive/Iterative Solution

The time complexity of the recursive solution is **$O(\log n)$**. This is because the problem size is halved in each recursive call, leading to a logarithmic number of function calls. 
The space complexity is also $O(\log n)$ due to the recursion stack depth.

### Improved Solution

The time complexity of the improved solution is **$O(1)$**. This is because the calculation involves simple arithmetic operations and does not depend on the size of the input $n$. 
Similarly, the space complexity is $O(1)$ as there is no additional space required beyond a few variables used in the calculation.
