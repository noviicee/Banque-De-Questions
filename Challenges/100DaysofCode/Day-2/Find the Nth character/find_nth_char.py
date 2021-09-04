def solve(s, r, n):
        
        l=len(s)
        while r>0:
            for i in range(l):
                if s[i]=="0":
                    s=s.replace(s[i],"1")
                    r-=1
                elif s[i]=="1":
                    s=s.replace(s[i],"10")
                    r-=1
        print(s)
        #return(s[n-1])

"""ongoing"""