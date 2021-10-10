# https://leetcode.com/problems/bitwise-and-of-numbers-range/

def rangeBitwiseAnd(left: int, right: int) -> int:
    # if there's a range of power of 2
    # then the answer will be 0
    # beacause
    # 2**(n) & (2**(n)-1) = 0

    if left*2<right:
        return 0

    ans=left
    for i in range(left+1, right+1):
        ans=ans&i
    return ans

if __name__=="__main__":
    print(rangeBitwiseAnd(5, 7)) # 4
    print(rangeBitwiseAnd(0, 0)) # 0
    print(rangeBitwiseAnd(1, 2147483647)) # 0
    print(rangeBitwiseAnd(1, 7)) # 0
    print(rangeBitwiseAnd(1, 1)) # 1
