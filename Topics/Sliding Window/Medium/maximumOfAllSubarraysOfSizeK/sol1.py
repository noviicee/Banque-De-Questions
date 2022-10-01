def max_of_subarrays(arr,n,k):
    ans=[]
    for i in range(n-k+1):
        ans.append(max(arr[i:i+k]))
    return ans

if __name__=="__main__":
    print(max_of_subarrays([1, 2, 3, 1, 4, 5, 2, 3, 6],9,3))

# basic sliding window
# won't work for large values of n
