def FindSumInSubarray(arr,num):
    n=num//2
    l=len(arr)
    for i in range(l-1):
        for j in range(1,l):
            s=arr[i]+arr[j]
            # print(s)
            if s==num:
                return arr[i],arr[j]
    return None

"""Note:
This program takes into account that there is only one such subarray
which can sum to the given number num.
In some cases, the question can be modified as to return all such values,
which sum up to the given number.
In such a case, we need to store the values instead of return one value here
"""

if(__name__=="__main__"):
    print(FindSumInSubarray([4,3,-1,17,5,11,18,13],10))

    print(FindSumInSubarray([1,2,3,4,5,6,7,8,9],20))

    print(FindSumInSubarray([1,2,3,4,5,6,7,8,9],10))