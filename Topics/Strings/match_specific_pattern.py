"""
Given a dictionary of words and a pattern.
Every character in the pattern is uniquely mapped to a character in the dictionary.
Find all such words in the dictionary that match the given pattern. 

Example 1:

Input:
N = 4
dict[] = {abb,abc,xyz,xyy}
pattern  = foo
Output: abb xyy
Explanation: xyy and abb have the same
character at index 1 and 2 like the
pattern.

"""
def encode(string):
    code=''
    map={}
    i=0

    for s in string:
        if s not in map:
            map[s]=i
            i+=1
        code+=str(map[s])
    
    return code
    
def findSpecificPattern(Dict, pattern):
    #Code here
    res=[]

    hash=encode(pattern)

    l=len(pattern)
    for d in Dict:
        if len(d)==l and encode(d)==hash:
            res.append(d)
    return res

if __name__=="__main__":
    Dict= ['abb','abc','xyz','xyy']
    pattern= 'foo'
    ans=(findSpecificPattern(Dict, pattern))
    for i in ans:
        print(i, end=' ')