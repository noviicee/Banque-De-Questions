"""Given an array of strings,
return all groups of strings that are anagrams.
The groups must be created in order of their appearance in the original array.
"""

def printAnagrams(words):
    d={}
    for word in words:
        s=''.join(sorted(word))
        if s in d.keys():
            d[s].append(word)
        else:
            d[s]=[word]
    return d.values()

# test-case
ans=(printAnagrams(['act','god','cat','dog','tac']))
for i in ans:
    print(i, end=' ')
