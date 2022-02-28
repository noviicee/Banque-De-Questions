def search(matrix, n, m, x): 
    # code here 
    
    # binary search algo
    # only if the matrix is sorted
    row,col=0,m-1
    while row<n and col>=0:
        if matrix[row][col]>x:
            col-=1
        elif matrix[row][col]<x:
            row+=1
        else:
            return 1
    return 0
