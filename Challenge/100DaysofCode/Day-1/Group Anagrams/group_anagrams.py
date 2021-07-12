def group_anagrams(strs):
    d={}
    for word in strs:
        s=''.join(sorted(word))
    

        if s not in d.keys():
            d[s]=[word]
        else:
            d[s]+=[word]

    return list(d.values())

if __name__=="__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

"""Complexity Analysis:
Time-Complexity: O(N)
Space-Complexity: O(N)
"""