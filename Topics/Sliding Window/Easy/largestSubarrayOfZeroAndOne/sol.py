"""This problem is similar to-
finding two indexes i & j in array[]
such that
array[i] = array[j] and (j-i) is maximum."""

def maxLen(arr, N):
    if arr.count(1)==arr.count(0):
        return N
    
    d={}
    max_len=0
    curr_sum=0

    for i in range(N):
        if arr[i]==1:
            arr[i]=-1
        else:
            arr[i]=1

    for i in range(N):
        curr_sum+=arr[i]

        if curr_sum==0:
            max_len=i+1
        if curr_sum in d:
            max_len=max(max_len,i-d[curr_sum])
        else:
            d[curr_sum]=i

    return max_len

if __name__=="__main__":
    print(maxLen([0,0,1,0,0],5)) # 2
    print(maxLen([1,1,0,1,1],5)) # 1

# TC= O(N) | SC=O(1)
