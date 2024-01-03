class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        d={}
        for a in arr:
            d[a]=d.get(a,0)+1
        #print(d)
        
        m=-1
        for v in d.values():
            if v>=m:
                m=v
        # max number of votes are m now
        #print(m)
        
        l=[]
        for k in d.keys():
            if d[k]==m:
                l.append(k)
        #print(l)
        return [min(l),m]

# {    
# Driver Code Starts
if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        n=int(input())
        arr=input.strip().split()

        result=Solution.winner(arr, n)
        print(result[0], result[1])
# } Driver Code Ends
