def sol(arr):
    curr=0
    next=curr
    res=[]
    while curr<len(arr) and next<len(arr):
        if next!=curr:
            res.append([arr[curr],arr[next]])
            next+=1
        elif next==curr:
            next+=1
        if next==len(arr):
            curr+=1
            next=curr
    return res

if __name__=="__main__":
    print(sol([1,2,3,4]))
