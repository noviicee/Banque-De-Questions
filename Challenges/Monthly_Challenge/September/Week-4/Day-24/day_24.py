# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        
        # creating an array of size 38 because a contarint of size 38 is given in the question
        arr=[0]*38

        arr[0],arr[1],arr[2]=0,1,1
        for i in range(len(arr)-3):
            arr[i+3]=arr[i]+arr[i+1]+arr[i+2]

        return arr[n]

obj=Solution()
print(obj.tribonacci(2))
print(obj.tribonacci(4))
print(obj.tribonacci(7))
print(obj.tribonacci(11))
print(obj.tribonacci(15))
print(obj.tribonacci(20))
print(obj.tribonacci(24))
print(obj.tribonacci(29))
print(obj.tribonacci(34))
print(obj.tribonacci(37))

# observe the pattern, i.e, the increase in the result
