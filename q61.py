# sorting of first row

from random  import randint

row = 4
col = 4
matrix =[]

for i in range(row):
    y=[]
    for j in range(col):
        y.append(randint(1,16))
    matrix.append(y)

for i in range(row):
    for j in range(col):
        print('%3d'%matrix[i][j],end=' ')
    print()

#matrix[0].sort()
k = col-1
while k!=0:
    z=0
    for j in range(1,k+1):
        if matrix[0][j] > matrix[0][z]:
            z = j


    for i in range(row):
        x = matrix[i][z]
        matrix[i][z] = matrix[i][k]
        matrix[i][k] = x
    k -=1
print(' '*50)
print('*'*50)
print(' '*50)


for i in matrix:
    print(i)






