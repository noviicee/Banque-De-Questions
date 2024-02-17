class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def isMaxHeap(self,arr,n):
        # Your code goes here  
        parent = arr[0]
        
        # j can be written as (2*i+1, and 2*i+2)
        for i in range(n//2):
            j=(2*i)+1
            # comparing last loop in case j became equal to n-1 during the last loop:
            if (arr[i]<arr[j]) or (j+1<n and arr[i]<arr[j]):
                return False
        return True

# {    
# Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input.split()]
        ob=Solution()
        print(ob.isMaxHeap(arr, n))
# } Driver Code Ends
