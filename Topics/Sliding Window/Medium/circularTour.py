def circularTour(lis,N):
    '''
    lis[][0]:Petrol
    lis[][1]:Distance
    '''
    start=0
    p=0 # petrol
    d=0 # distance

    for i in range(N-1):
        d+=lis[i][0]-lis[i][1]
        if d<0:
            start=i+1
            p+=d
            d=0
    if p+d>0:
        return start
    return -1

if __name__=="__main__":
    print(circularTour([[4,6],[6,5],[7,3],[4,5]],4)) # 1

"""
Time Complexity: O(N)
Auxiliary Space : O(1)"""
