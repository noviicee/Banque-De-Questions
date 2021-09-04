def run_ar_sum(arr):
    l=len(arr)
    out_arr=[arr[0]]

    for i in range(l-1):
        out_arr.append(out_arr[i]+arr[i+1])

    return out_arr

if __name__=="__main__":
    print(run_ar_sum([1,2,3,4]))
    print(run_ar_sum([1,1,1,1,1]))
    print(run_ar_sum([3,1,2,10,1]))