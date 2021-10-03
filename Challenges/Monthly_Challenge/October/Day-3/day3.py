# https://leetcode.com/problems/jump-game/submissions/

# Greedy Approach

def smmallestJump(nums):
    farthest=0

    for k,v in enumerate(nums):
        if k>farthest:
            return False
        farthest=max(farthest, k+v)
    return True

if __name__=="__main__":
    print("Enter the elements of the array: ")
    nums=[int(ele) for ele in input().split()]
    print(smmallestJump(nums))
