# Closing Bracket Index
# https://practice.geeksforgeeks.org/problems/closing-bracket-index5900/1/?category[]=Strings&category[]=Strings&problemStatus=unsolved&page=1&query=category[]StringsproblemStatusunsolvedpage1category[]Strings

class Solution:
    def closing (self,s, pos):
        # your code here
        c=0
        for i in range(pos,len(s)):
            if s[i]=='[':
                c+=1
            elif s[i]==']':
                c-=1
            if c==0:
                return i

if __name__=="__main__":
    obj=Solution()
    print(obj.closing(s = "[ABC[23]][89]", pos = 0)) # 8
    print(obj.closing(s = "ABC[58]", pos = 3)) # 6
