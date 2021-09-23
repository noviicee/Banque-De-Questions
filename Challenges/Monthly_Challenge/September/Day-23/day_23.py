# https://leetcode.com/problems/break-a-palindrome/

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        
        res=""

        for i in range(len(palindrome)):
            if palindrome[i]!='a':
                res=palindrome[:i]+'a'+palindrome[i+1:]
                # changing first non 'a' charcter to 'a'
                # but we need to check whether that is still a palindrome or not
                if res!=res[::-1]:
                    return res
        # code has reached here mmeans that now there are only a's in the string
        res=palindrome[:len(palindrome)-1]+'b'
        return res

obj=Solution()
print(obj.breakPalindrome('aba')) # abb
print(obj.breakPalindrome('a')) # ""
print(obj.breakPalindrome('aa')) # ab
