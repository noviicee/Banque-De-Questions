"""An anagram of a string is another string that contains the same characters,
only the order of characters can be different."""

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        d1,d2={},{}
        for i in a:
            d1[i]=d1.get(i,0)+1
        for x in b:
            if x not in a:
                return False
            d2[x]=d2.get(x,0)+1
        for k,v in d1.items():
            if k not in d2.keys():
                return False
            if d2[k]!=v:
                return False
        return True


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
