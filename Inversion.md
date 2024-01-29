# Inversion Finding

## What is Inversion?

In the context of an array, an Inversion refers to a situation where there exist two indices $i$ and $j$ where

$$0 < i < j < arr.length$$

such that $$arr[i] > arr[j]$$

Mathematically, if $arr[i]$ is greater than $arr[j]$, violating the order of the array, then this pair $(arr[i], arr[j])$ constitutes an Inversion.

## How to Find Inversions?

Inversions can be found using various algorithms. One efficient approach is to use a modified version of the merge sort algorithm. During the merge step, while merging two sorted subarrays, the count of Inversions can be incremented whenever an element from the right subarray is moved before an element from the left subarray.

## Algorithm in Pseudocode

```python
Function Sort_Count(arr) -> Integer:
    count = 0
    MergeSort(arr, 0, arr.length - 1, count)
    Return count

Function MergeSort(arr, l, r, count) -> None:
    If l < r Then
        m = l + (r - l) / 2
        MergeSort(arr, l, m, count)
        MergeSort(arr, m + 1, r, count)
        Merge(arr, l, m, r, count)
    End If

Function Merge(arr, l, m, r, count) -> None:
    n1 = m - l + 1
    n2 = r - m
    Create arrays L of size n1 and R of size n2
    Copy values from arr[l:m] to L and from arr[m+1:r] to R

    i = 0
    j = 0
    k = l
    While i < n1 and j < n2 Do
        If L[i] <= R[j] Then
            arr[k] = L[i]
            i = i + 1
        Else
            arr[k] = R[j]
            j = j + 1
            count = count + (n1 - i)
        End If
        k = k + 1
    End While

    Copy remaining_elements from L and R back to arr if Any
```

## Realization in C++

```cpp
#include <algorithm>
#include <vector>

void merge(std::vector<int>& arr, int l, int m, int r, int& count);

void mergeSort(std::vector<int>& arr, int l, int r, int& count);

// Function to sort and count inversions
int Sort_Count(std::vector<int>& arr) {
    int count = 0; // Initialize Inversion count to 0
    mergeSort(arr, 0, static_cast<int>(arr.size() - 1), count);
    return count;
}

// Main function to perform merge sort
void mergeSort(std::vector<int>& arr, int l, int r, int& count) {
    if (l < r) {
        // Find the middle point
        int m = l + (r - l) / 2;

        // Sort first and second halves
        mergeSort(arr, l, m, count);
        mergeSort(arr, m + 1, r, count);

        // Merge the sorted halves
        merge(arr, l, m, r, count);
    }
}
// Function to merge two sorted subArrays arr[l:m] and arr[m+1:r]
void merge(std::vector<int>& arr, int l, int m, int r, int& count) {
    int n1 = m - l + 1;
    int n2 = r - m;

    // Create temporary arrays
    std::vector<int> L(n1), R(n2);

    // Use swap to fast copy the values to L[] and R[]
    std::swap_ranges(arr.begin() + l, arr.begin() + m + 1, L.begin());
    std::swap_ranges(arr.begin() + m + 1, arr.begin() + r + 1, R.begin());

    // Merge the temporary arrays back into arr[l...r]
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            std::swap(arr[k], L[i]);
            i++;
        } else {
            /* From L[i] to L[n1-1] all > R[j]
             *->  found n1 - i Inversions
             */
            std::swap(arr[k], R[j]);
            j++;
            count += n1 - i;
        }
        k++;
    }

    // Use swap to copy the rest of L[] and R[] if exist
    std::swap_ranges(L.begin() + i, L.end(), arr.begin() + k);
    std::swap_ranges(R.begin() + j, R.end(), arr.begin() + k);
}
```

## Complexity Analysis

Both bubble sort and merge sort can be analyzed using this logic:

### Time Complexity Analysis

- **Bubble Sort:**
  - Time complexity: $O(n^2)$
    - Bubble sort iterates through the array, comparing adjacent elements and swapping them if they are in the wrong order. This process is repeated until the array is sorted. In the worst case scenario, when the array is in reverse order, each element needs to be compared with each other, resulting in $n(n-1) / 2$ comparisons, which simplifies to $O(n^2)$.

- **Merge Sort:**
  - Time complexity: $O(n log (n))$
    - Merge sort divides the array into halves recursively until each subarray has only one element. Then, it merges them back together in sorted order. The division process occurs $log(n)$ times (base $2$), and each merge operation takes linear time. Therefore, the time complexity is $O(n log (n))$.

### Space Complexity Analysis

- **Bubble Sort:**
  - Space complexity: $O(1)$
    - Bubble sort operates in-place, meaning it doesn't require any additional space beyond the array itself. It performs swaps directly within the array.

- **Merge Sort:**
  - Space complexity: $O(n log (n))$
    - Merge sort requires additional memory for the recursive calls and the temporary arrays used during merging. As it divides the array into halves recursively, it creates $log(n)$ levels of recursion, each level requiring memory proportional to the size of the array. Therefore, the space complexity is $O(n log (n))$.

### Conclusion

For better time efficiency, merge sort is preferred over bubble sort. Despite its higher space complexity, merge sort's time complexity of $O(n log (n))$ makes it a more efficient choice for sorting large arrays, compared to the $O(n^2)$ time complexity of bubble sort. Additionally, merge sort provides stable sorting and is not sensitive to the initial order of elements, further enhancing its usefulness in various scenarios.
