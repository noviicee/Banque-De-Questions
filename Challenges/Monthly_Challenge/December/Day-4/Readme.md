# Problem Description

## Stream of Characters

Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings words.

For example, if words = ["abc", "xyz"] and the stream added the four characters (one by one) 'a', 'x', 'y', and 'z', your algorithm should detect that the suffix "xyz" of the characters "axyz" matches "xyz" from words.

Implement the StreamChecker class:

StreamChecker(String[] words) Initializes the object with the strings array words. <br>
boolean query(char letter) Accepts a new character from the stream and returns true if any non-empty suffix from the stream forms a word that is in words.
 

Example 1:

```txt
Input
["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
Output
[null, false, false, false, true, false, true, false, false, false, false, false, true]
```

Explanation

StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]); <br>
streamChecker.query("a"); // return False <br>
streamChecker.query("b"); // return False <br>
streamChecker.query("c"); // return False <br>
streamChecker.query("d"); // return True, because 'cd' is in the wordlist <br>
streamChecker.query("e"); // return False <br>
streamChecker.query("f"); // return True, because 'f' is in the wordlist <br>
streamChecker.query("g"); // return False <br>
streamChecker.query("h"); // return False <br>
streamChecker.query("i"); // return False <br>
streamChecker.query("j"); // return False <br>
streamChecker.query("k"); // return False <br>
streamChecker.query("l"); // return True, because 'kl' is in the wordlist <br>

*Constraints:*

* 1 <= words.length <= 2000
* 1 <= words[i].length <= 2000
words[i] consists of lowercase English letters.
letter is a lowercase English letter.
* At most 4 * 104 calls will be made to query.

<hr>

## Approach

We are keeping a dictionary for the last character of all the word in `words`. For each key (char), their values are stored as a list of words, which are present in `words`, and end with that particular character.
<br>
Alongside, we are also adding up on the stream of letters.
<br>
If we see a letter in the dictionary (key by default)
and the length of string is greater than the word (this is required in order to be a suffix), we reverse query the string and see if it matches the words.

[Solution](sol.py)

<!--**Time-Complexity:**

* Time-Complexity= O()
* Space-Complexity=O()-->

>[Refer](https://leetcode.com/problems/stream-of-characters/)
