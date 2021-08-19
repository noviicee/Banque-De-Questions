# Problem Description

A message containing letters from A-Z can be encoded into numbers using the following mapping:

```txt
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6) <br>
"KJF" with the grouping (11 10 6) <br>
*Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".*

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

```txt
Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

```txt
Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

```txt
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0.
The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
Hence, there are no valid ways to decode this since all digits need to be mapped.
```

```txt
Example 4:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
```

*Constraints:*

1 <= s.length <= 100 <br>
s contains only digits and may contain leading zero(s). <br>

<hr>

## Approach

`Dynamic-Programming` `Top-Down` `Bottom-Up` `Memoization`

Let `n` be the length of the string given.

* **Top-Down**

Here, if n=-1, we return 1, because there is 1 possible way to decode an empty string. <br>
If last digit is not equal to 0, we need to add dp(i-1) to our answer. <br>
If last two digits form number from 10 to 26, we can use last 2 symbols for decoding, so we add dp(i-2) to our answer.

[Top-Down Approach](./sol_topdown.py)

* **Bottom-Up**

Here if the count reaches to n, that is , the length of the string, we return 1. <br>
If first digit is equal to 0 (assuming we are starting from first), we return 0. <br>
If first two digits (assuming we are starting from first) form number less than 27, we can use them for decoding, so we add dp(i+2) to our answer.

[Bottom-Up Approach](./sol_bottomup.py)
