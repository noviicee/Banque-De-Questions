def maximumMoneyRobbed(nums):
    
    # base case
    if len(nums)<=2:
        return max(nums)

    max_money_robbed=0
    L=len(nums)
    a,b=nums[0], max(nums[0], nums[1])
    for i in range(2, L):
        a,b=b,max(b, a+nums[i])

    max_money_robbed=b
    return max_money_robbed

if __name__=="__main__":
    print(maximumMoneyRobbed([1,2,3,1])) #4
    print(maximumMoneyRobbed([2,1,1,2])) #4
    print(maximumMoneyRobbed([2,7,9,3,1])) #12