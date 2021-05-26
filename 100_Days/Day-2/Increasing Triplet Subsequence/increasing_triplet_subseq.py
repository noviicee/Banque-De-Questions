def increasing_triplet(nums):

    l=len(nums)

    i=nums[0]
    j=2**31
    
    for index in range(1,l):
        if nums[index]>j:
            return True
        if nums[index]<=i:
            i=nums[index]
        else:
            j=nums[index]
    return False

if __name__=="__main__":
    print(increasing_triplet([1,2,3,4,5])) # true
    print(increasing_triplet([5,4,3,2,1])) # false
    print(increasing_triplet([5,6,1])) # false
    print(increasing_triplet([1,5,0,4,1,3])) # true
    print(increasing_triplet([20,100,10,12,5,13])) # true


"""Complexity-Analysis
Time-Complexity: O(n)
Space-Complexity: O(1)
"""