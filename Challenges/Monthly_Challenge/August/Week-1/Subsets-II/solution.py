def subsetsWithDup(nums):
    from itertools import combinations
    ans=[]
    l=len(nums)
    for i in range(l+1):
        res=list(combinations(nums,i))
        print(res)
        for i in res:
            if i not in ans:
                ans.append(i)
    return ans

if __name__=="__main__":
    print(subsetsWithDup([1,2,2]))