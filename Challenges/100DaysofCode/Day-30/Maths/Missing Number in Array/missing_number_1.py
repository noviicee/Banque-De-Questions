"""Missing Number from an array
Approach-1
"""

def missing_num_1(N, arr):
    arr.sort() #nlogn
    for i in range(1,N+1):
        if arr[i-1]!=i:
            return i

if __name__=="__main__":
    print(missing_num_1(5,[1,2,3,5]))
    print(missing_num_1(10, [1,2,3,4,5,6,7,8,10]))
    print(missing_num_1(2,[1])) # won't work