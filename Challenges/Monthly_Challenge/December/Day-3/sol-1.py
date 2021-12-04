def maxProductSubarray(nums):
    currMax, currMin=1,1
    res=nums[0]
    for n in nums:
        vals=(n, currMax*n, currMin*n) # tuples can enhance time-complexity
        currMax, currMin=max(vals), min(vals)
        res=max(res, currMax)
    return res

if __name__=="__main__":
    print("Enter the elements of the array:")
    nums=[int(ele) for ele in input().split()]
    print(maxProductSubarray(nums))
