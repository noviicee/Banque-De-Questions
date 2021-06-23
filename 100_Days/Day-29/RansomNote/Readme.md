# Problem Description

Given the words in a magazine and the words in a ransom note, print Yes if he can replicate the ransom note exactly using whole words from the magazine; otherwise, print No.

**Example**

*magazine* = "attack at dawn"  
*note* = "Attack at dawn"

The magazine has all the right words, but there is a case mismatch. The answer is ***No***.

* Sample Input 0

```txt
6 4
give me one grand today night
give one grand today
```

* Sample Output 0

```txt
Yes
```

* Sample Input 1

```txt
6 5
two times three is not four
two times two is four
```

* Sample Output 1

```txt
No
```

* Explanation 1

'two' only occurs once in the magazine.

<br>

* Sample Input 2

```txt
7 4
ive got a lovely bunch of coconuts
ive got some coconuts
```

* Sample Output 2

```txt
No
```

* Explanation 2

Harold's magazine is missing the word ***some*** .

<br>

>Reference: <br>
[Hackerrank](https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D=dictionaries-hashmaps&isFullScreen=true)
