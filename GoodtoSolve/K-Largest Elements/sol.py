class Solution: 
    def quickSort(self, array):
        if len(array)<=1:
            return array
        #base-case
        pivot=array.pop()
        left=[]
        right=[]
        for item in array:
            if item<pivot:
                left.append(item)
            else:
                right.append(item)
        return(self.quickSort(left)+[pivot]+self.quickSort(right))
        #the above process is repeated until there is just one element,
        #or no element left in the original array

    def kLargest(self,arr, n, k):
        # code here
        
        #using a sorting algo of tc =NlogN
        # quick sort
        # with O(N) space
        
        ans=self.quickSort(arr)
        ans=ans[::-1]
        return ans[:k]

if __name__=="__main__":
    obj=Solution()
    print("Enter the elements of array")
    arr=[int(ele) for ele in input().split()]
    k=int(input("Enter the values of k: "))
    res=obj.kLargest(arr, len(arr), k)
    print(res)
        