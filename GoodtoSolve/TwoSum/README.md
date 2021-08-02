# Problem Description

You are provided with an array(arr) and a number(num). The task is to find two values in the subarray whose sum is equal to the number num.<br>
If there do not exist any such value in the subarray, the function should return `None` .

Examples:

```txt
Input 1:
arr=[4,3,-1,17,5,11,18,13]
num=10
Output 1: (11,-1)
```

```txt
Input 2:
arr=[-4,-1,1,3,5,6,8,11]
num=10
Output 2: None
```

<hr>

## Approach:

* ### [Approach-1](./approach_1.py)

Linear Traverse<br><br>
Time-Complexity: O(n^2)<br>
Space-Complexity: O(1)

* ### [Approach-2](./approach_2.py)

Using Hashing Technique `[Hashmaps][Dictionaries]`<br><br>
Time Complexity: O(n)<br>
Space Complexity: O(n)

* ### [Approach-3](./approach_3.py)

Sort the array and Find sum<br><br>
Time-Compelxity: O(nlogn)<br>
Space-Complexity: O(1)<br>

*This is basically a two pointer approach where we first sort the array.<br>Then we take a first-node and a last-node, comapre the sum, and then accordingly shift the nodes.<br><br>*

>Note: Approach-3 is based on the algorithm [**Divide and Conquer**](https://github.com/noviicee/DSA_noviicee/tree/main/Algo/Divide%20and%20Conquer) <br>
Time-Compelxity is O(nlogn) due to sorting of the array.<br>
[Tweet](https://twitter.com/reachtoana/status/1393061275681259521)

<hr>

## Follow-Up:

Everything remains the same, the only change is that we have to **return the list of indices of the elements as output**.

### Solution:

There can be numerous solutions, with different time and space-complexities. <br>
The goal is to find the *optimal solution*.

* ### [Approach](./followup_approach.py)

Using Hashing Technique `[Hashmaps][Dictionaries]`
<br><br>
Time Complexity: O(n)<br>
Space Complexity: O(n)
<br><br>
>[Reference](https://leetcode.com/problems/two-sum/)
