class Solution:
    def findMaxSum(self,arr):
		# code here
        
        """
        keep two variables- inclusive and exclusive
        incl= sum including current element
        excl= sum excluding current element
        iterate through the array

        Max sum excluding the current will be max(incl, excl), and
		max sum including the current will be excl + current element

        answer is maximum of incl and excl
        """
        
        incl, excl=0,0
        for i in arr:
            new_excl=max(incl, excl)
            incl=excl+i
            excl=new_excl

        ans= max(incl, excl)
        return ans

obj=Solution()
print(obj.findMaxSum([1, 2, 3, 5, 7, 9]))
print(obj.findMaxSum([5,5,10,100,10,5])) #110
print(obj.findMaxSum([1,2,3])) #4