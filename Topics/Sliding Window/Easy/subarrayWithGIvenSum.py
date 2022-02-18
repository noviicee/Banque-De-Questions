# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1/?page=1&status[]=unsolved&category[]=sliding-window&sortBy=submissions#

from curses import window


def subArraySum(arr, n, s):
    start=0
    window_sum=arr[start]
    i=1
    while i<=n:
        while window_sum>s and start<i-1:
            window_sum-=arr[start]
            start+=1
        if window_sum==s:
            return (start+1, i)
        if i<n:
            window_sum+=arr[i]
        i+=1
    return (-1,)

if __name__=="__main__":
    print(subArraySum([1,2,3,7,5], 5, 12)) # (2,4)