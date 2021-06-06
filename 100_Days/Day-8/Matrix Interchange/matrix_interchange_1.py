def matrix_interchange_1(matrix):
    for rows in matrix:
        rows[0],rows[-1]=rows[-1],rows[0]
        
    for rows in matrix:
        for elements in rows:
            print(elements,end=" ")
        print()


if __name__=="__main__":
    (matrix_interchange_1([[1, 2, 3, 4],
           [4, 3, 2, 1],
           [6, 7, 8, 9]]))