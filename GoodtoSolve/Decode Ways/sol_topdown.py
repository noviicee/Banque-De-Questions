def decodeWays(s):
    n=len(s)

    def dp(i):
        ans=0
        if i==-1:
            return 1
        if s[i]>"0":
            ans+=dp(i-1)
        if  i>=1 and "10"<=s[i-1:i+1]<="26":
            ans+=dp(i-2)
        return ans

    return dp(n-1)
    
if __name__=="__main__":
    print(decodeWays('12')) #2
    print(decodeWays('226')) #3
    print(decodeWays('0')) #0
    print(decodeWays('06')) #0