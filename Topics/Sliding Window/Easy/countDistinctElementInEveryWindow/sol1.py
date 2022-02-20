def countDistinct(A,N,K):
    window=A[:K]
    ans=[len(set(window))]

    for i in range(1,N-K+1):
        tmp=len(set(A[i:i+K]))
        ans.append(tmp)
    return ans

if __name__=="__main__":
    print(countDistinct([1,2,1,3,4,2,3],7,4)) # [3,4,4,3]

# won't work for large values of N :(
