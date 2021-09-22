# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3982/

def maxConsecutiveOnes(arr):
    count=0
    res=0
    for i in arr:
        if i==1:
            count+=1
        else:
            res=max(res,count)
            count=0
    return max(res,count)

if __name__=="__main__":
    print(maxConsecutiveOnes([1,1,1,0,0,1,1,0,1]))
    print(maxConsecutiveOnes([1,1,0,1,1,1]))
