class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def isMaxHeap(self,arr,n):
        # Your code goes here  

        """
        To verify if a given array is a max-heap,
        we need to check whether each node satisfies
        the max-heap property, that is,
        that key[Parent(i)]≥key[i] for all nodes i
        except for the root.
        """

        for i in range(1, n):
            parent_node=(i+1)//2
            if arr[parent_node-1]<arr[i]:
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
