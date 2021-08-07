from itertools import *
n=int(input()) # max possible value in the arrays
k=int(input()) # length of the array

if k==1:
	print(n)

ans=[]
l=[i for i in range(1,n+1)]
new=list(permutations(l,k))
print(new)

for i in new:
    if i[k-1]%i[k-2]==0:
        ans.append(i)

count=len(ans)+n
print(count%10000)
