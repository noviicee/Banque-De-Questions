class Solution:
    def sol1(self, s):
        # O(n**2)
        l=[]
        # reason for taking  dictionary here is that
        # we can even get the substring
        res={'':0}
        # 0 is initialised for empty string
        i=0
        j=0
        lgt=len(s)
        while i<lgt and j<lgt:
            if s[j] not in l:
                l.append(s[j])
                j+=1
            elif s[j] in l:
                res[''.join(l)]=(len(l))
                l.clear()
                i+=1
                j=i

        res[''.join(l)]=len(l)
        print(res)
        m=max(res.values())
        return m







if __name__=="__main__":
    obj=Solution()
    s=input("Enter a string ")
    print(obj.sol1(s))
