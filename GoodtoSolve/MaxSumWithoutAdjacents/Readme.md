# Max Sum without Adjacents

Given an array Arr of size N containing positive integers. Find the maximum sum of a subsequence such that no two numbers in the sequence should be adjacent in the array.

Example 1:

```txt
Input:
N = 6
Arr[] = {5, 5, 10, 100, 10, 5}
Output: 110
```

Explanation: If you take indices 0, 3
and 5, then Arr[0]+Arr[3]+Arr[5] =
5+100+5 = 110.

Example 2:

```txt
Input:
N = 4
Arr[] = {3, 2, 7, 10}
Output: 13
```

Explanation: 3 and 10 forms a non
continuous  subsequence with maximum
sum.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

*Constraints:*
1 ≤ N ≤ 106
1 ≤ Arr[i] ≤ 107

[Refer](https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1)
