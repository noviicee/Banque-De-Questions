def maximumMoneyRobbed(nums):
    
    # base case
    if len(nums)<=2:
        return max(nums)

    max_money_robbed=0
    L=len(nums)
    dp=[0]*L
    dp[0]=nums[0] # max money robbed till day-1
    dp[1]=max(nums[0], nums[1]) # max money robbed till day-2

    for i in range(2,L):
        dp[i]=max(dp[i-1], dp[i-2]+nums[i])
        # two cases
        # robbed on prev day =dp[i-1]
        # did not rob prev day (then must rob today) =dp[i-2]+nums[i]

    max_money_robbed=dp[i]
    return max_money_robbed

if __name__=="__main__":
    print(maximumMoneyRobbed([1,2,3,1])) #4
    print(maximumMoneyRobbed([2,1,1,2])) #4
    print(maximumMoneyRobbed([2,7,9,3,1])) #12
