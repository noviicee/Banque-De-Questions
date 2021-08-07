n=int(input()) # number of monsters
e=int(input()) # initial experience
poweri=[int(i) for i in input().split()]
bonusi=[int(i) for i in input().split()]

c=0
killed=[]

d={}
for i in range(len(poweri)):
    d[poweri[i]]=bonusi[i]
print(d)

i=0
while i<len(d):
    for k in d.keys():
        if k<e and k not in killed:
            e+=d[k]
            killed.append(k)
            c+=1
    i+=1
print(c)