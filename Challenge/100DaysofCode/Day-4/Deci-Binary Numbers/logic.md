# Partitioning Into Minimum Number Of Deci-Binary Numbers

**If each deci-binary number has no higher than a 1 in each position, then it will take at least x numbers to achieve an x in any given position of n.**

**This means that the largest character in any position in n will determine how many deci-binary numbers must be added together to obtain n.**

<br>

1. Visualize n as a graph of its digits:

    ![Visual 1](https://res.cloudinary.com/practicaldev/image/fetch/s--4GHzuyBM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/rn13iSv.png)

2. Think of a graph as a stack of numbers to be added:

    ![Visual 2](https://res.cloudinary.com/practicaldev/image/fetch/s--om3zivbv--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/0CqWfzM.png)

This stack must necessarily then be as tall as the largest single digit in **n**.

Complexity Analysis:

* Time Complexity: O(N) where N is the length of the input string n
* Space Complexity: O(1) <br>
or O(N) depending on whether or not we split n to an array first
<br>(for languages other than python)
