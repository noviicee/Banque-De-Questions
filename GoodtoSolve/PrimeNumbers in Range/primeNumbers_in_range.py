#  Given two integers M and N, generate all primes between M and N.

"""Excpected-Complexity:
T-C= O(N*sqrt(N))
S-C= O(1)"""

import math

def isPrime(n):
    """A function to check
    whether the number N is
    prime or not."""
    if n==1:
        return False
    for x in range(2,int(math.sqrt(n)+1)):
        # take care for math module
        if n%x==0:
            return False
    return True

def primeNumbersInRange(M,N):
    ans=[]
    for i in range(M,N+1):
        if isPrime(i):
            ans.append(i)
    return ans

# test-cases
if __name__=="__main__":
    l=int(input("Enter lower bound: "))
    u=int(input("Enter upper bound: "))
    ans=(primeNumbersInRange(l,u))
    for i in ans:
        print(i, end=' ')
    