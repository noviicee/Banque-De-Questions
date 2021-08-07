# Grid Path

Given a grid. Each cell of the grid contains a single integer value. These values are described by 2D integer array a with N rows and 2 columns, where a[i][j] is the value in the cell located in row i,
column j.

Standing in (i; j), the player can move to any cell of the next row (i+1; j2) under the condition that
a[i+1][j2] > a[i][j]. In other words, the value in the next cell of the player's path should be strictly
greater than the value in the current cell of the player's path.

The player can't make any moves if he's already in the last row.

If the player starts in any cell of the first row (either (1; 1) or (1; 2)), what is the maximum possible total sum of values in all cells he can visit on his path? <br>
Print the answer modulo 10^9+7.

## Input:

The first line contains an integer, n, denoting the number of rows in a. <br>
The next line contains an integer, 2, denoting the number of columns in a. <br>
Each line i of the n subsequent lines (where 0 ≤ i < n) contains 2 space separated integers each
describing the row a[i]. <br>

![Sample-Cases](./Fwd-Infosys-3.png)
