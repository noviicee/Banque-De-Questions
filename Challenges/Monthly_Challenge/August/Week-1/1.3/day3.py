# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3837/

"""Subsets-2
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order."""

from itertools import combinations
import itertools
def subSets2(nums):
    """Python has itertools.combinations(iterable, n) which Return n length subsequences of elements from the input iterable.
    This can be used to Print all subsets of a given size of a set.
    Now, we have various alternatives to use this function."""

    ans=set()
    l=len(nums)
    for i in range(l+1):
        poss_anss=(list(combinations(nums, i)))
        for anss in poss_anss:
            ans.add(anss)
    return sorted(list(ans))

if __name__=="__main__":
    print(subSets2([1,2,2]))
