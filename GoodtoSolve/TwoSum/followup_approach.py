class Solution:
    def twoSum(self, nums, target):
        # create a dictionary/hasmap to maintain the elements and index
        d={}
        for i,j in enumerate(nums):
            if (target-j) in d:
                return([d[target-j],i])
            d[j]=i

if __name__=="__main__":
    obj=Solution()
    print(obj.twoSum([2,7,11,15],9)) # [0,1]
    print(obj.twoSum([3,2,4],6)) # [1,2]
    print(obj.twoSum([3,3],6)) # [0,1]
