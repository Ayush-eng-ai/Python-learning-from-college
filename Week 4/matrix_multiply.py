r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [1,2,3]
s2 = [4,5,6]
s3 = [7,8,9]

A = []
A.append(r1)
A.append(r2)
A.append(r3)
B = []
B.append(s1)
B.append(s2)
B.append(s3)    

c =[[0,0,0],[0,0,0],[0,0,0]]
dim = 3

#c[i][j] is the dot product of the ith row of A and the jth column of B
for i in range(dim):#for each row of A
    for j in range(dim):#for each column of B
        for k in range(dim):#for each element in dot product
            c[i][j] = c[i][j] + A[i][k] * B[k][j]
    print("The product of A and B is:",c)
    print(c)
#c[i][j] = dot_product of A[i][...] and B[....][j]

    



