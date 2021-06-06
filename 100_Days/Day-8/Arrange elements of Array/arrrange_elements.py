def arrange_ele(arr):
    arr.sort()
    i=0
    l=len(arr)

    while i<l-1:
        arr=right_rotate_arr_by_one(arr,i)
        i+=2
    
    return arr

def right_rotate_arr_by_one(arr,start):

    l=len(arr)
    temp=arr[l-1]
    #print(arr)
    
    if start<l:
        for i in range(l-1,start-1,-1):
            arr[i]=arr[i-1]
            #print(arr)
        arr[start]=temp

    return arr

if __name__=="__main__":
    print(arrange_ele([1,2,3,4,5,6]))
    print(arrange_ele([10,20,30,40,50,60,70]))

