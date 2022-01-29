# Special Numbers
"""A number is a special number if it's digits only consist 0, 1, 2, 3, 4 or 5.
Given a number N and we have to find N-th Special Number. 
"""

from traceback import print_tb


def specialNumber(n):
    if n==0:
        return n
    ans=''
    n-=1
    while n:
        ans+=str(n%6)
        n//=6
    return int(ans[::-1])

# test-case
if __name__=="__main__":
    print(specialNumber(7)) #10
    print(specialNumber(6)) #5

"""Analysis:
This is a PURE MATHS QUESTION
who's answer is
It's DECIMAL TO BASE 6.

Time-Complexity= O(logN)
Space-Complecity= O(1)"""