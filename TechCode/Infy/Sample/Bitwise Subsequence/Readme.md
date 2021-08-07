# Bitwise subsequence

You have an array A of N integers A1 A2 .. An. <br>
Find the longest increasing subsequence Ai1 Ai2 .. Ak
(1 <= k <= N) that satisfies the following condition:

For every adjacent pair of numbers of the chosen subsequence Ai[x] and Ai[x+1] (1 < x < k) <br>
The expression *( Ai[x] & Ai[x+1] ) \* 2 < ( Ai[x] | Ai[x+1] ) is true.*

Note: *'&' is the bitwise AND operation, ' | ' is the bit-wise OR operation*

## Input:

The first line contains an integer, N, denoting the number of elements in A. <br>
Each line i of the N subsequent lines (where 0 ≤ i < N) contains an integer describing Ai.

## Sample cases:

![Sample-case](./Fwd-Infosys-2.png)
