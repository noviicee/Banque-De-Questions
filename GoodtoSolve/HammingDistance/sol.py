def hammingDistance(n1, n2):
    b1=f'{n1:031b}'
    b2=f'{n2:031b}'

    c=0
    m=min(len(b1), len(b2))

    for i in range(m):
        if b1[i]!=b2[i]:
            c+=1
    
    return c

if __name__=="__main__":
    print(hammingDistance(5,3))
    print(hammingDistance(123,33))

"""Complexity Analysis:
Time-Complexity: O(N)
Space-Compelxity: O(N)
where N is the length of bin(n1)+bin(n2)
"""