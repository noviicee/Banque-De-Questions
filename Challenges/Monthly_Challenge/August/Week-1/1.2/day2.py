# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3836/

def twoSum(nums, target):
    hash_set={}
    for i,j in enumerate(nums):
        if target-j in hash_set:
            return [hash_set[target-j],i]
        hash_set[j]=i

if __name__=="__main__":
    print(twoSum([2,2,3,1,4,5],6))
