# Problem Description

Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.

<br>

Example-1

![Example-1](https://assets.leetcode.com/uploads/2020/05/14/leetcode_max_area_2.png)

```py
Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]

Output: 4

Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
```

<br>

**Example-2**

![Example-2](https://assets.leetcode.com/uploads/2020/05/14/leetcode_max_area_3.png)

```py
Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
```

* _Constraints:_ <br>
2 <= h, w <= 10^9 <br>
1 <= horizontalCuts.length < min(h, 10^5) <br>
1 <= verticalCuts.length < min(w, 10^5) <br>
1 <= horizontalCuts[i] < h <br>
1 <= verticalCuts[i] < w <br>
It is guaranteed that all elements in horizontalCuts are distinct. <br>
It is guaranteed that all elements in verticalCuts are distinct. <br>

<br>

>Reference: <br>
[Leetcode](https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3766/)
