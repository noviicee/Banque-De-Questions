# Problem Description

## Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:

```txt
Input: nums = [2,3,-2,4]
Output: 6
```

*Explanation: [2,3] has the largest product 6.*

Example 2:

```txt
Input: nums = [-2,0,-1]
Output: 0
```

*Explanation: The result cannot be 2, because [-2,-1] is not a subarray.*
 
*Constraints:*

* 1 <= nums.length <= 2 * 104
* -10 <= nums[i] <= 10
* The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

<hr>

## Approach

### Approach-1

Loop inside Loop.
<br>
Basically we are keeping two loops (i and j). For each element at a place i, we are traversing the array from the next element of i and keeping a record of the maximum product found so far.

[Solution](sol.py)

**Complexity-Analysis**
* Time Complexity= O(N^2)
* Space-Complexity= O(1)

*This approach might exceed the time-limit if the length of the array is too big.*

### Approach-2

This is the optimized version of the above approach. Instead of repeteadly traversing the array for each element in it, we traverse the array just once, and keep a track of the maximum product found so far.

[Solution](sol-1.py)

**Complexity-Analysis**
* Time Complexity= O(N)
* Space-Complexity= O(1)

>[Refer](https://leetcode.com/problems/maximum-product-subarray/)
