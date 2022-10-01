# Sliding Window Technique

def findSum(arr, k):
    """
    1. We compute the sum of first k elements out of n
    terms using a linear loop and
    store the sum in variable window_sum.
    2. Then we will graze linearly over the array
    till it reaches the end
    and simultaneously keep track of maximum sum.
    3. To get the current sum of block of k elements,
    just subtract the first element from the previous block
    and add the last element of the current block 
    """

    # base-case
    if len(arr)<k:
        return None
        # invalid

    window_sum=0
    
    # first window
    for i in range(k):
        window_sum+=arr[i]

    ans=window_sum

    # rest windows
    for i in range(len(arr)-k):
        window_sum-=arr[i]
        window_sum+=arr[i+k]
        # removing first old value and adding first new value
        ans=max(ans,window_sum)
    return ans


if __name__=="__main__":
    arr= [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4 
    ans=findSum(arr,k)
    print(ans) #39

print("Enter the elements of the array:")
arr=[int(ele) for ele in input().split()]
k=int(input("Enter the value of k: "))
print("Result= ", findSum(arr,k))

"""Complexity-Analysis:
Time: O(N)
Space: O(1)
"""
