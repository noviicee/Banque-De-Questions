from calendar import c


def lenOfLongSubarr (A, N, K):
    # base-case
    d={}
    curr_sum=0
    max_len=0
    for i in range(N):
        curr_sum+=A[i]
        if curr_sum==K:
            max_len=i+1
        if curr_sum-K in d:
            max_len=max(max_len,i-d[curr_sum-K])
        if curr_sum not in d:
            d[curr_sum]=i
    return max_len

if __name__=="__main__":
    print(lenOfLongSubarr([10,5,2,7,1,9],6,15))
    # 4 [5,2,7,1]
