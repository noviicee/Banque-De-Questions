N=int(input()) # number of elements in A
A=[int(i) for i in input().split()]

ans=[]

l=len(A)
i=0
while i<(l-1):
    cond=( A[i] & A[i+1] ) * 2 < ( A[i] | A[i+1] )
    if cond:
        ans.append([A[i],A[i+1]])
        i+=1
    i+=1


print(ans)