def maximumProductSubarray(nums):
    result=nums[0]
    for i in range(len(nums)):
        mul=nums[i]
        for j in range(i+1, len(nums)):
            result=max(mul,result)
            mul*=nums[j]
    return result

if __name__=="__main__":
    print("Enter the elements of the array:")
    nums=[int(ele) for ele in input().split()]
    print(maximumProductSubarray(nums))
