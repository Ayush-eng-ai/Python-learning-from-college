#Matrix addition by first principles (?)
dim = 3
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

print("Matrix A is:")
print(A)
print("Matrix B is:")
print(B)

#I need to add A and B
C = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(dim): #for each row
    for j in range(dim): #for each column
        C[i][j] = A[i][j] *  B[i][j]
print("The sum of A and B is:")
print(C)