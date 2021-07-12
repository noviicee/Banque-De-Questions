def run_length_encoding(S): 
    """Time Complexity: O(N)
    Space Complexity: O(1)
    """   
    i=0
    l=len(arr)
    #c=1
    s=""
    
    while i<=l-1:
        c=1
        while i<l-1 and arr[i]==arr[i+1]:
            c+=1
            i+=1
        if i==l-1 and arr[i]==arr[i-1]:
            #c+=1
            i+=1
            s+=arr[i-1]+str(c)            
        else:
            i+=1
            s+=arr[i-1]+str(c)
            
    return s