# Problem Description

## House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

```txt
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

Example 2:

```txt
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
``` 

*Constraints:*

1 <= nums.length <= 100 <br>
0 <= nums[i] <= 400 <br>

<hr>

## Approach

***Base Case***
<br>
If the length of `nums` is 1 or 2, then answer will straight-forward be maximum of *nums[1]* and *nums[2]* .

### Approach-1

***Dynamic Programming***
<br>
Let us initialize an array dp of length of `nums`.
dp[i] will indicate the maximum money that can be earned till the *i-th day*.
<br>
Therefore, dp[0]= 0 and dp[1] will be maximum of nums[1] and nums[2].
<br>
Now, for rest of the elements, *(nums[2] to nums[-1])*, on each day, we must find out the maximum amount of money that can be robbed till that day.
<br>
According to the question, we cannot rob houses on adjacent days.


>Therefore for each day, *dp[i]*, we have two choices- **either to rob on that day, or to not rob on that day**.

*If we already robbed on the previous day, we cannot rob today and so the maximum money robbed will be dp[i-1].
<br>
If we did not rob the previous day, then we must rob today and in this case the maximum money robbed wll be dp[i-2]+nums[i].*

>Our job is to find the maximum amount that can be robbed from these two choices and proceed with that.

If we try to put this statement into a formula,
for each day dp[i], the maximum money robbed will be maximum of dp[i-1] and dp[i-2]+nums[i].

If we do this for all the remaining elements in the array, the resultant *dp[i]* will be the maximum money that can be robbed

### [Solution](Challenges/Monthly_Challenge/December/Day-1/sol.py)

*Complexity-Analysis*
<br>
* Time-Complexity= O(N)
* Space-Complexity= O(N)

### Approach-2

**Dynamic-Programming Space-Optimized**
<br>
The approach is similar to the abpve approach. Only difference is that instead of keeping the whole array *dp*. we only keep the maximum money earned till the previous day and the day before the previous day.
<br>
Ultimately, we require only these value so we can optimize space complexity by using a varible instead of the whole array.

### [Solution-1](Challenges/Monthly_Challenge/December/Day-1/sol-1.py)

*Complexity-Analysis*
<br>
* Time-Complexity= O(N)
* Space-Complexity= O(1)

<hr>

*Note: Approach-1 was found to be a little faster than Approach-2 in practical implementation*.

>[Refer](https://leetcode.com/problems/house-robber/)
