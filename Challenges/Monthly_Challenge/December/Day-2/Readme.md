# Problem Description

## Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

**You must solve the problem in O(1) extra space complexity and O(n) time complexity.**

Example 1:

```txt
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
```

Example 2:

```txt
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
```

*Constraints:*
<br>
n == number of nodes in the linked list <br>
0 <= n <= 104 <br>
-106 <= Node.val <= 106

<hr>

## Approach

**Intuitive Approach**
<br>
The basic approach of this problem can be to store the odd nodes in one Linked List, and even ones in another. At last, concatenate both the Linked Lists.
This might seem to be simple, but not only it violates the Space-Complexity as asked in the question, but also writing a concise and error-free code while using this approach may seem to be tough.
<br>
We are going to follow a different approach in order to solve this problem.

**Space-Complexity O(1)**
<br>

>A well-formed LinkedList need two pointers head and tail to support operations at both ends. 

Here, we are forming two Linked Lists, oddList (for storing the odd values) and evenList (for storing the even values).
<br>
We are taking *head* and *odd* as the head and tail for oddList, and *evenhead* and *even* as the head and tail for the evenList.
<br>
Note that here *odd* and *even* act as both tail nodes for new Linked Lists as well as iterators for the given Linked List.
