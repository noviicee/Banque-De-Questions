"""Given a string check if it is Pangram or not.
A pangram is a sentence containing every letter in the English Alphabet."""

import string


def pangramChecking(s):

    s=''.join([i for i in s if i.isalpha()])
    if len(s)<26:
        return 0

    import string
    d=dict.fromkeys(string.ascii_lowercase, 0)

    s=s.lower()
    for i in s:
        d[i]=d.get(i,0)+1
    for v in d.values():
        if v<1:
            return 0
    return 1

# test-case
print(pangramChecking('my name is anamika')) # 0
print(pangramChecking('a quick brown fox jumps over the lazy dog')) # 1