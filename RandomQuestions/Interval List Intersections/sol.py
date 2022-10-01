"""user-definition required"""

class Solution:
    def intervalIntersection(self, firstList, secondList):
            res=[]
            i=j=0
            while i<len(firstList) and j<len(secondList):
                lo=max(firstList[i][0], secondList[j][0])
                hi = min(firstList[i][1],secondList[j][1])
                if lo <= hi:
                    res.append([lo, hi])

                # Remove the interval with the smallest endpoint
                if firstList[i][1] < secondList[j][1]:
                    i += 1
                else:
                    j += 1

            return res


"""
firstList=[ele for ele in input().split()]
secondList=list(map(int, input("Enter the elements of the second list ").split(' ')))

...tbc
"""

obj=Solution()
firstList, secondList= [[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]
# [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

ans=obj.intervalIntersection(firstList, secondList)
print(ans)
