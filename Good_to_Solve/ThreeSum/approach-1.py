def threeSum(nums):
    nums.sort()
    i=0
    res=[]
    while i<len(nums):
        a=nums[i]
        start=i+1
        end=len(nums)-1
        while start<end:
            b=nums[start]
            c=nums[end]
            if a+b+c==0:
                if [a,b,c] not in res:
                    res.append([a,b,c])
                start+=1
                end-=1
            elif a+b+c<0:
                start+=1
            elif a+b+c>0:
                end-=1
        i+=1
    return res

if __name__=="__main__":
    print(threeSum([-1,0,1,2,-1,-4]))
    print(threeSum([]))
    print(threeSum([0]))
