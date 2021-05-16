## Problem Description

You are provided with an array(arr) and a number(num). The task is to find two values in the subarray whose sum is equal to the number num.<br>
If there do not exist nay such value in the subarray, the function should return `None` .

### Examples:

```
Input 1:
arr=[4,3,-1,17,5,11,18,13]
num=10
Output 1: (11,-1)
```

```
Input 2:
arr=[-4,-1,1,3,5,6,8,11]
num=10
Output 2: None
```

<hr>

## Approach:


* ### [Approach-1](#)

Linear Traverse<br><br>
Time-Complexity: O(n^2)<br>
Space-Complexity: O(1)

* ### [Approach-2](./approach_2.py)

Using Hashing Technique `[Hashmaps][Dictionaries]`<br><br>
Time Complexity: O(n)<br>
Space Complexity: O(n)

* ### [Approach-3](#)

Sort the array and Find sum<br><br>
Time-Compelxity: O(nlogn)<br>
Space-Complexity: O(1)<br>

>Note: Approach-3 is based on the algorithm [**Divide and Conquer**](#) <br>
Time-Compelxity is O(nlogn) due to sorting the array.<br>
[Tweet](https://twitter.com/reachtoana/status/1393061275681259521)
