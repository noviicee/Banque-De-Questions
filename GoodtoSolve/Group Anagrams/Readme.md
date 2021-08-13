# Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

```txt
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

```txt
Example 2:

Input: strs = [""]
Output: [[""]]
```

```txt
Example 3:

Input: strs = ["a"]
Output: [["a"]]
```

_Constraints:_

1 <= strs.length <= 104 <br>
0 <= strs[i].length <= 100 <br>
strs[i] consists of lower-case English letters.

<hr>

## Approach

We can follow a simple approach of using hash, or dictionary in Python. <br>
The idea is that any word formed with a particular set of letters, when sorted will be same for all. <br>
So, we create a dictionary, and for each word in given array add the sorted word as keys. <br>
For the values, we check if an existing value exists with the key. If it does not, we add the value (as list) to the key, and if the value already exists, we append the newer values to the list of values. <br>
Finally we return the list of values as the answer.

* [Approach-1](./approach-1.py)

Space-Complexity= O(n) <br>
Time-Complexity= O(1)
