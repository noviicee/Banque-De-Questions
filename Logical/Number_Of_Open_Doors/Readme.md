# Problem Description

Consider a long alley with a N number of doors on one side. All the doors are closed initially. You move to and fro in the alley changing the states of the doors as follows: you open a door that is already closed and you close a door that is already opened. You start at one end go on altering the state of the doors till you reach the other end and then you come back and start altering the states of the doors again.
In the first go, you alter the states of doors numbered 1, 2, 3, … , n.

In the second go, you alter the states of doors numbered 2, 4, 6…

In the third go, you alter the states of doors numbered 3, 6, 9 …

You continue this till the Nth go in which you alter the state of the door numbered N.
You have to find the number of open doors at the end of the procedure.

Example 1:

```txt
Input:
N = 2
Output:
1
```

Explanation:
<br>
Initially all doors are closed.
After 1st go, all doors will be opened.
After 2nd go second door will be closed.
So, Only 1st door will remain Open.

Example 2:

```txt
Input:
N = 4
Output:
2
```

Explanation:
<br>
Following the sequence 4 times, we can
see that only 1st and 4th doors will
remain open.

Expected Time Complexity: O(1) <br>
Expected Auxiliary Space: O(1)

*Constraints:* <br>
1 <= N <= 1012

>[Refer](https://practice.geeksforgeeks.org/problems/number-of-open-doors1552/1/?company[]=TCS&company[]=TCS&problemStatus=unsolved&page=1&query=company[]TCSproblemStatusunsolvedpage1company[]TCS#)

<hr>

## Approach
If we approach via Mathematics, we can clearly see that returning sqrt(N) will give the answer.
<br>
[Solution](Logical\Number_Of_Open_Doors\sol.py)

*Note:*
<br>
This approach does not follown the Time-Complexity expected in the problem.
It is not really a Time-Complexity of O(1). The actual time complexity of the given solution will be O(log(N)).
We should keep in mind the time complexity of square root.
