class Solution:
    
    def shiftAndUpdate(self, array, num, ind):
        for i in range(ind+1):
            if i==ind:
                array[i]=num
            else:
                array[i]=array[i+1]
                
    def updateLargest(self, array, num):
        l=len(array)
        i=l-1
        while i>=0:
            if array[i] is None or array[i]<num:
                self.shiftAndUpdate(array, num, i)
            i-=1

    def kLargest(self,arr, n, k):
        # code here
        
        k_largest=[None]*k
        for a in arr:
            self.updateLargest(k_largest, a)
        return k_largest

obj=Solution()
print(obj.kLargest([1, 23, 12, 9, 30, 2, 50], 7, 3))
print(obj.kLargest([1, 2, 9, 12, 23, 30, 50], 7, 3))
