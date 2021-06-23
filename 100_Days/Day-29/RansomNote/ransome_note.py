def checkMagazine(magazine, note):
    m={}
    for i in magazine:
        m[i]=m.get(i,0)+1
    n={}
    for i in note:
        n[i]=n.get(i,0)+1

    #print(m)
    #print(n)
        
    res = all(m.get(key, -1) >= val for key, val
                                 in n.items())
    if res==True:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    checkMagazine(["apgo", "clm", "w", "lxkvg", "mwz", "elo", "bg", "elo", "lxkvg", "elo", "apgo", "apgo", "w", "elo", "bg"], ["elo", "lxkvg", "bg", "mwz", "clm", "w"])
