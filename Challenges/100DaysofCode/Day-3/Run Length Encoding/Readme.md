# Problem Description

Given a string, Your task is to  complete the function encode that returns the run length encoded string for the given string. <br>
Eg.: if the input string is "wwwwaaadexxxxxx", then the function should return "w4a3d1e1x6". <br>

```
Example 1:

Input:
str = aaaabbbccc
Output: a4b3c3
Explanation: a repeated 4 times
consecutively b 3 times, c also 3
times.
```

```
Example 2:

Input:
str = abbbcdddd
Output: a1b3c1d4
```

* Expected Time Complexity: O(N), N = length of given string.
* Expected Auxiliary Space: O(1)
<br><br>

_Constraints:_ <br>
1<=length of str<=100
