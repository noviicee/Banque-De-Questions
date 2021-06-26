"""Missing Number from an array
Approach-2:

We get the missing element by first finding the sum of n natural numbers,
and then subtracting the sum of the array.

Formula:
Sum of N natural numbers = n x (n + 1) / 2
"""

def missing_num_2(N,arr):
    sum_of_N=N*(N+1)//2
    sum_of_arr=sum(arr)
    """Alternative:
    count=0
    for i in arr:
        count+=i
    return count
    """
    missing_num=sum_of_N-sum_of_arr
    return missing_num

if __name__=="__main__":
    print(missing_num_2(5,[1,2,3,5]))
    print(missing_num_2(10,[1,2,3,4,5,6,7,8,10]))
    print(missing_num_2(2,[1]))