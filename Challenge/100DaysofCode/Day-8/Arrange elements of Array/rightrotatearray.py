def right_rotate_arr_by_one(arr,start):

    l=len(arr)
    temp=arr[l-1]
    #print(arr)
    try:
        if start<l:
            for i in range(l-1,start-1,-1):
                arr[i]=arr[i-1]
                #print(arr)
            arr[start]=temp
    except:
        pass
    return arr

if __name__=="__main__":
    print(right_rotate_arr_by_one([1,2,3,4,5,6],0))
    print(right_rotate_arr_by_one([6, 1, 2, 3, 4, 5],2))
    print(right_rotate_arr_by_one([6, 1, 5, 2, 3, 4],4))
    print(right_rotate_arr_by_one([6, 1, 5, 2, 4, 3],6))