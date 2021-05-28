from typing import Counter


def height_checker(heights):
    l=len(heights)
    h=sorted(heights) # O(nlogn)

    count=0

    for i in range(l): # O(n)
        if heights[i]!=h[i]:
            count+=1
    
    return count

if __name__=="__main__":
    print(height_checker([1,1,4,2,1,3]))
    print(height_checker([5,1,2,3,4]))
    print(height_checker([1,2,3,4,5]))
