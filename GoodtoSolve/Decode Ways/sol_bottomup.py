def decodeWays(s):
    n=len(s)

    def dp(i):
        ans=0
        if i==n:
            return 1
        if s[i]=="0":
            return 0
        ans=dp(i+1)
        if i<n-1 and s[i:i+2]<"27":
            ans+=dp(i+2)
        return ans
    
    return dp(0)

if __name__=="__main__":
    print(decodeWays('12')) #2
    print(decodeWays('226')) #3
    print(decodeWays('0')) #0
    print(decodeWays('06')) #0