# why doesn't it work for bigger arrays
# chechk logic

def printAnagrams(words):
    d={}
    for word in words:
        s=0
        for w in word:
            s+=ord(w)
        if s in d.keys():
            d[s].append(word)
        else:
            d[s]=[word]
    return d.values()

# test-case
ans=(printAnagrams(['act','god','cat','dog','tac']))
for i in ans:
    print(i, end=' ')
