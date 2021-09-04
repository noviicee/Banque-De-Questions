"""Recursive factorial function
"""
class Solution:

    def fact(self,n):
        if n==0:
            return 1
        return n*self.fact(n-1)


    def trailingZeroes(self, N):
        #code here 
        
        res=self.fact(N)
        #print(res)
        count=0
        while res%10==0:
            count+=1
            res=res//10
        return count

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        N=int(input())
        obj=Solution()
        ans=obj.trailingZeroes(N)
        print(ans)
