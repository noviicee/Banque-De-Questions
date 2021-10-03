# Problem Description

You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

```txt
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

```txt
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

*Constraints:*

1 <= nums.length <= 104 <br>
0 <= nums[i] <= 105

>[Reference](https://leetcode.com/problems/jump-game/)

<hr>

## Solution

<br>
[Approach 1](./October/Day-3/day3.py):

[Greedy Approach]()

These type of problem can be solved using segmented bfs taking maximum element from a range it can go. Here the approach is to go as far as possible and once our index crosses the farthest then we return False as its not possible to reach the end.
