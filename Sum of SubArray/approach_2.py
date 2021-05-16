def FindSumOfSubarray(arr,num):
    d={}
    # x+y=10
    # y=10-x
    for x in arr:

        d[x]=num-x
    for i in d.values():
        if i in arr:
            return i,d[i]
    return None



if __name__=="__main__":
    print(FindSumOfSubarray([4,3,-1,17,5,11,18,13],10))
    print()
    print(FindSumOfSubarray([-4,-1,1,3,5,6,8,11],10))
    print()
    print(FindSumOfSubarray([1,2,3,4,5,6,71,8],20))
