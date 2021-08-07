n=int(input()) # number of rows
col=2
mat=[]
for i in range(n):
    mat.append([int(i) for i in input().split()])
print(mat)
