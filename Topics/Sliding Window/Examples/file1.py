# Brute-Force

def findSum(arr,N):

    # base-case
    if len(arr)<N:
        return None
        # invalid
    s=0
    for i in range(len(arr)-N+1):
        tmp=arr[i]
        for j in range(i+1,i+N):
            tmp+=arr[j]
        s=max(s,tmp)
        
    return s

if __name__=="__main__":
    arr= [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4 
    ans=findSum(arr,k)
    print(ans) #39

print("Enter the elements of the array:")
arr=[int(ele) for ele in input().split()]
k=int(input("Enter the value of k: "))
print("Result= ", findSum(arr,k))

"""Complexity-Analysis:
Time: O(n*k)
Space: O(1)
"""
