# Problem Description

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

```
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

```
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
``` 

_Constraints:_

1 <= nums1.length, nums2.length <= 1000 <br>
0 <= nums1[i], nums2[i] <= 1000

<br>

>Reference
[Leetcode](https://leetcode.com/problems/intersection-of-two-arrays/solution/)

<br>

# Idea

This problem can be solved by enumerous methods- either by uding loops, or by using sets.
Needless to say, the time-complexity varies from approach to approach.

### Appproach-1

>Time-Complexity: O(nlogn) <br>
Space-Complexity: O(n)

### Approach-2

>Time-Complexity: O(n*m); <br>
n is the size of the first array, and m is the size of thhe second array <br><br>
Space-Complexity: O(n)