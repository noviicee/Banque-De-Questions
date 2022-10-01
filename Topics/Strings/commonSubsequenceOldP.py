""""Given two strings S1 and S2,
print whether they contain any common subsequence (non empty) or not."""

def commonSubsequenceOldP(S1, S2):
    for i in S1:
        if i not in S2:
            return 0
    return 1
    # do we need to check for the lengths of the strings here??
    # maybe npt because we need not follow the order/sequence here
    # the characters can be in any order

# test-case
print(commonSubsequenceOldP('anamika', 'singh')) # 0
print(commonSubsequenceOldP('geeksforgeeks', 'forgeeskgeeks')) # 1