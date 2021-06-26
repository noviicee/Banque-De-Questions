class Solution:
    def trailingZeroes(self, N):
    	#code here 
    	if not N:
    	    return 0
        return N//5 +self.trailingZeroes(N//5)

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        N=int(input())
        obj=Solution()
        ans=obj.trailingZeroes(N)
        print(ans)
        