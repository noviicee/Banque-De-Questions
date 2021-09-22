# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution:
    def maxLength(self, arr):
        if len(arr)==1:
            if len(arr[0])==len(set(arr[0])):
                return len(arr[0])
            return -1

        # else
        ml=0 # maximum_length
        res=[""]

        l=sorted(arr, key=len, reverse=True) # to make the process more easier
        
        for x in l:
            for j in range(len(res)):
                new_res=x+res[j]
                if len(new_res)!=len(set(new_res)):
                    continue # breaks loops based on conditions and moves the cursor at the beginning of the loop

                res.append(new_res)
                ml=max(ml, len(new_res)) 
        return ml
                

if __name__=="__main__":
    obj=Solution()
    print(obj.maxLength(["arr", "ay"]))
    print(obj.maxLength(["ana", "mik", "a", "si", "ngh"]))
    print(obj.maxLength(["un", "iq", "ue"]))
        