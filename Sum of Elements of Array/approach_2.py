def FindSumInSubarray(arr,num):
    d={}
    # x+y=10
    # y=10-x
    for x in arr:

        d[x]=num-x
    for i in d.values():
        if i in arr:
            return i,d[i]
    return None

"""Note:
This program takes into account that there is only one such subarray
which can sum to the given number num.
In some cases, the question can be modified as to return all such values,
which sum up to the given number.
In such a case, we need to store the values instead of returning single value here
"""


if __name__=="__main__":
    print(FindSumInSubarray([4,3,-1,17,5,11,18,13],10))
    print()
    print(FindSumInSubarray([-4,-1,1,3,5,6,8,11],10))
    print()
    print(FindSumInSubarray([1,2,3,4,5,6,71,8],20))
