#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        low, mid, high=0,0, n-1
        while mid<=high:
            if arr[mid]==0:
                arr[low], arr[mid]= arr[mid], arr[low]
                low+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[high], arr[mid]= arr[mid], arr[high]
                high-=1
        return arr

n=int(input("Enter the size of the array "))
arr=list(map(int, input("Enter the elements for the array ").split(' ')))     
obj=Solution()
print(obj.sort012(arr, n))
