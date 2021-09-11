# https://practice.geeksforgeeks.org/problems/remove-duplicates-in-small-prime-array/1/?category[]=Prime%20Number&category[]=Prime%20Number&page=1&query=category[]Prime%20Numberpage1category[]Prime%20Number#

"""Given an array consisting of only prime numbers, remove all duplicate numbers from it. 

Example 1:

Input:
N = 6
A[] = {2,2,3,3,7,5}
Output: 2 3 7 5
Explanation: After removing the duplicate
2 and 3 we get 2 3 7 5.

Constraints:
1<=N=106
2<=A[i]<100
"""

"""Challenge
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
"""

def removeDuplicates(arr):
    d={}
    ans=[]
    for i in arr:
        if i not in d:
            d[i]=1
            # searching in dictionary=O(n)
            ans.append(i)
    return ans

if __name__=="__main__":
    print(removeDuplicates([1,2,1,2,1,2,1,2,1,2,3,4,4,5,4,5,6,7]))
