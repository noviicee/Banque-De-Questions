def triplet_sum_array_1(arr,n,X):

    arr.sort() #nlogn

    for i in range(n-2):
        j=i+1 # for the second element
        l=n-1 # for the last element

        while j<l:
            temp=arr[i] #starting from first element
            sum=temp+arr[j]+arr[l]
            if sum==X:
                print(temp,arr[j],arr[l])
                return True
            if sum<X:
                j+=1
            else:
                l-=1
        
    return False

if __name__=="__main__":
    print(triplet_sum_array_1([12, 3, 4, 1, 6, 9],6,24))
