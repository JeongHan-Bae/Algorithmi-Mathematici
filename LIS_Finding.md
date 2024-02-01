# Longest Increasing Subsequence Finding

## What is Longest Increasing Subsequence?

In the context of an array, a Longest Increasing Subsequence (LIS) refers to a subsequence of the array elements where the elements are sorted in increasing order. 

Mathematically, if we have an array $arr$ of length $n$, and there exists a subsequence $S$ of $arr$ such that 
$$S = [arr[i_1], arr[i_2], ..., arr[i_k]]$$
where $$0 ≤ i_1 < i_2 < ... < i_k ≤ n$$
and $$arr[i_1] < arr[i_2] < ... < arr[i_k]$$
then $S$ is an Increasing Subsequence of $arr$.

The longest possible $S$ is called a LIS.

## How to Find the length Longest Increasing Subsequence?

There are multiple algorithms to find the length of the Longest Increasing Subsequence (LIS) in an array. Two common approaches are Dynamic Programming (DP) and Greedy.

## Algorithm in Pseudocode

### Dynamic Programming Approach

```python
Function lengthOfLIS_DP(nums: List[int]) -> int:

    Array[nums.length] dp initialized to 1
    max_length = 1

    For i from 1 to nums.length - 1:
        For j from 0 to i - 1:
            If nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                max_length = max(max_length, dp[i])
            End If
        End For
    End For

    Return max_length
```

### Greedy Approach

```python
Function lengthOfLIS_Greedy(nums: List[int]) -> int:
    Array helper initialized to an empty array

    For Each num in nums:
        Perform Binary Search to find the minimal insertion point Where:
            {helper[insertion point] > num}
        If insertion point is found:
            helper[insertion point] = num
        Else:
            Append num to the end of the helper array
        End If
    End For Each

    Return helper.length
```

## Realization in C++

### Dynamic Programming Implementation

```cpp
#include <algorithm>
#include <vector>

int lengthOfLIS_DP(std::vector<int>& nums) {
    std::vector<int> dp(nums.size(), 1);
    int max_length = 1;

    for (int i = 1; i < nums.size(); ++i) {
        for (int j = 0; j < i; ++j) {
            if (nums[i] > nums[j]) {
                dp[i] = std::max(dp[i], dp[j] + 1);
                max_length = std::max(max_length, dp[i]);
            }
        }
    }

    return max_length;
}

```

### Greedy Implementation

```cpp
#include <algorithm>
#include <vector>

int lengthOfLIS_Greedy(std::vector<int>& nums) {
    std::vector<int> helper;

    for (int num : nums) {
        auto it = std::lower_bound(helper.begin(), helper.end(), num);
        if (it != helper.end()) {
            *it = num;
        } else {
            helper.push_back(num);
        }
    }

    return helper.size();
}

```

## Complexity Analysis

### Time Complexity Analysis

Both Dynamic Programming and Greedy approaches have different time complexities.

#### Dynamic Programming:
- Time complexity: $O(n^2)$
  - We have two nested loops iterating through the array elements. 

#### Greedy:
- Time complexity: $O(n \log n)$
  - This is due to the binary search-like operation inside the loop.

### Space Complexity Analysis

Both algorithms have different space complexities as well.

#### Dynamic Programming:
- Space complexity: $O(n)$
  - We use an additional array of length $n$ to store DP values.

#### Greedy:
- Space complexity: $O(n)$
  - We use an additional array to store potential candidates, which can grow up to the size of the input array.

### Conclusion

Both Dynamic Programming and Greedy approaches offer solutions to finding the length of the Longest Increasing Subsequence (LIS) in an array. 
While Dynamic Programming provides a more straightforward solution, it can have higher time complexity compared to the Greedy approach, which guarantees a time complexity of $O(n \log n)$. 
The choice of algorithm depends on the constraints and characteristics of the problem.
