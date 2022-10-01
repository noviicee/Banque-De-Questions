class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        d={}
        for i in a:
            d[i]=d.get(i,0)+1
        for x in b:
            if x not in a:
                return False
            d[x]=d.get(i,0)+1
        for v in d.values():
            if v<2:
                return False
        return True
        # won't work if the string contains repeated characters
        
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
