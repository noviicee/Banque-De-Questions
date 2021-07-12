def triplet_sum_arr_2(arr, n, X):
    for i in range(n):
        s=set()
        for j in range(i+1,n):
            ele=X-arr[i]-arr[j]
            if ele in s:
                print(arr[i],arr[j],X-arr[i]-arr[j])
                return True
            s.add(arr[j])
    return False

if __name__=="__main__":
    print(triplet_sum_arr_2([12, 3, 4, 1, 6, 9], 6, 24))
