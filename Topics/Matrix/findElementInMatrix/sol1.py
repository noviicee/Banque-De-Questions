def search(matrix, n, m, x): 
        # code here 
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==x:
                    return 1
        return 0
