#Function to find triplets with zero sum.    

# not correct, have to remove duplicates
def findTriplets(arr, n):
    #code here
    
    # one element and two sum
    for i in arr:
        target=0-i
        # two sum of this target
        d={}
        for j in arr:
            d[j]=target-j
        for k,v in d.items():
            # we have to take care of duplicates here
            if v in arr:
                return 1
    return 0

# test-case
if __name__=="__main__":
    print(findTriplets([0, -1, 2, -3, 1], 5)) #1