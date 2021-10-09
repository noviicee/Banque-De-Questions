# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings

def isValid(s):
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
    # print(d)

    #temp=min(d.values())
    #temp=d[s[0]]
    temp=max(d.values(), key=list(d.values()).count) 
    # print(temp)

    flag=0

    for v in d.values():
        if (v-temp==1 and flag==0) or (v-temp==0 and flag==0):
            flag+=1
        elif v-temp==0:
            continue
        else:
            return "NO"
    return "YES"

if __name__=="__main__":
    s=input()
    print(isValid(s))
