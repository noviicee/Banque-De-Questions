# Problem Description

Given an array arr of size `n` and an integer `X`. Find if there's a triplet in the array which sums up to the given integer X.

Example 1:

```txt
Input:
n = 6, X = 13
arr[] = [1 4 45 6 10 8]

Output:
1

Explanation:
The triplet {1, 4, 8} in 
the array sums up to 13.
```

Example 2:

```txt
Input:
n = 5, X = 10
arr[] = [1 2 4 3 6]

Output:
1

Explanation:
The triplet {1, 3, 6} in 
the array sums up to 10.
```

**Complexity Analysis:**

Expected Time Complexity: O(n2) <br>
Expected Auxiliary Space: O(1)

_Constraints:_ <br>
1 ≤ n ≤ 103 <br>
1 ≤ A[i] ≤ 105 <br>

<br>

>Reference: <br>
[GfG](https://practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1#)

<hr>

## Approaches:

1. [Best-Approach](.triplet_sum_array_1.py):

    - Time-Complexity: O(n^2)
    - Space-Complexity: O(1)

2. [Approach-2](./triplet_sum_array_2.py)

    - Time-Complexity: O(n^2)
    - Space-Complexity: O(n)

3. Naive Approach | Worst Approach

    - Time-Complexity: O(n^3)
    - Space-Complexity: O(1)
