# Problem Description:

Given a binary string `S` . Perform `R` iterations on string `S`, where in each iteration-

 0 becomes 01 and
 1 becomes 10.
 
 Find the Nth character of the string after performing `R `iterations.

<br>

```
Example 1

Input:
S = 101
R = 2 
N = 3
Output:
1
Explanation : 
Expand S 2 times and get 1 at third position
```

```
Example 2

Input:
S = 11
R = 1 
N = 3
Output:
0
Explanation : 
Expand S once and get 0 at third position
```

### Time and Space Complexities:

Expected Time Complexity: O(r*len(s)) <br>
Expected Auxilary Space: O(len(s))
 
_Constraints:_
<br>
1<=|string length|<=1000 <br>
1<=R<=20 <br>
0<=N<|Length of final string|

<br>

>Reference:<br>
[GfG](https://practice.geeksforgeeks.org/problems/find-the-n-th-character5925/1#)
