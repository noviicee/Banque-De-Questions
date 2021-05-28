def reverseWords(s: str) -> str:
        
        s=s.strip()
        
        s=s.split(' ')
        
        if '' in s:
            while '' in s:
                s.remove('')
            
        #print(s)
        
        l=len(s)
        
        for i in range((l//2)):
            s[i],s[l-i-1]=s[l-i-1],s[i]
            
        
        return(' '.join(s))
        