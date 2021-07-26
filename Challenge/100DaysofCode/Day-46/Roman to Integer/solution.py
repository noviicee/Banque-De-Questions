class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        if s in d.keys():
            return d[s]
        sum=0
        i=0
        while i<len(s)-1:
            if d[s[i]]<d[s[i+1]]:
                sum+=d.get((s[i]+s[i+1]))
                i+=2
            else:
                sum+=d[s[i]]
                i+=1
        if i==len(s)-1:
            sum+=d[s[i]]
        return sum
        
if __name__=="__main__":
    obj=Solution()
    s=input("Enter a string: ")
    ans=obj.romanToInt(s)
    print(ans)
    