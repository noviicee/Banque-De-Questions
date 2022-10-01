def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
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

if __name__=="__main__":
    print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
