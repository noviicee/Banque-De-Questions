def FindSumInSubarray(arr, num):
    l=len(arr)
    left=0
    right=l-1

    arr.sort() # nlogn
    while(right>0):
        if(arr[left]+arr[right]==num):
            return (arr[left],arr[right])
        else:
            # left+=1
            right-=1
    return None

if __name__=="__main__":
    print(FindSumInSubarray([4, 3, -1, 17, 5, 11, 18, 13], 10))
