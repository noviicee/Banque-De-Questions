def solution(arr,k):
    res=[]
    for i in arr:
        eq=""
        s=str(i)
        for y in s:
            if int(y)-k>0:
                eq+=str(int(y)-k)
        res.append(int(eq))
    return(res)

if __name__=="__main__":
    arr=[2345, 8786, 2478, 8664, 3568, 28]
    k=4
    print(solution(arr,k))
