# https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=sliding-window&sortBy=submissions

def maxSumSubarrayOfSizeK(Arr,K):

    N=len(Arr)

    # for first window
    window_sum=sum(Arr[:K])

    ans=window_sum

    # for rest of the windows
    for i in range(N-K):
        window_sum-=Arr[i]
        window_sum+=Arr[i+K]
        ans=max(window_sum, ans)

    return ans

if __name__=="__main__":
    print(maxSumSubarrayOfSizeK([100, 200, 300, 400],2)) # 700