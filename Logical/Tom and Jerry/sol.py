class Solution:
    def numsGame(self, N):
        # code here
        return int(N%2==0)

N=int(input("Enter the value of N: "))
obj=Solution()
print(obj.numsGame(N))
