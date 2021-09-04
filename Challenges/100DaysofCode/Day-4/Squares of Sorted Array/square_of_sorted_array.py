def dq_sorted_arr(nums):
    l=len(nums)
    i=0 # constant pointer
    j=l-1 # moving pointer

    while j>0:
        if abs(nums[i])>abs(nums[j]):
            nums[i],nums[j]=nums[j],nums[i]
        j-=1

    for n in range(l):
        nums[n]=nums[n]**2

    return nums

if __name__=="__main__":
    print(dq_sorted_arr([-4,-1,0,3,10]))
    print(dq_sorted_arr([-7,-3,2,3,11]))