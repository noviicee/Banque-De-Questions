def MaximumSumSubarray(nums):
    
    # base case
    if len(nums)<=1:
        return nums[0]

    max_ending=nums[0]
    max_so_far=nums[0]

    i=1

    while i<len(nums):

            max_ending = max(nums[i], max_ending+nums[i])
            
            if max_ending>max_so_far:
                max_so_far=max_ending
            
            i+=1
    return max_so_far