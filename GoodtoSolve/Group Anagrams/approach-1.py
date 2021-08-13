def GroupAnagrams(arr):
    if len(arr)==0 or len(arr)==1:
        return [arr]
    # this will save us the space for length of input=0 or 1

    d={}
    for i in arr:
        s=''.join(sorted(i))
        if s in d.keys():
            d[s]+=[i]
        else:
            d[s]=[i]
    return list(d.values())

if __name__=="__main__":
    print(GroupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(GroupAnagrams([""]))
    print(GroupAnagrams(["a"]))
