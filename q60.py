# interchange the principle diagonal element

from random import randint

row = 4
col = 4
matrix = []

for i in range(row):
    y=[]
    for j in range(col):
        y.append(randint(1,6))
    matrix.append(y)

for my in matrix:
    print(my)

dig_1 =[]
dig_2 = []

for i in range(row):
    for j in range(col):
        if i == j:
            dig_1.append(matrix[i][j])
        elif row - i -1 == j:
            dig_2.append(matrix[i][j])

print('*'*50)
print(f'Diagonal element are : {dig_1}')
print(' '*50)
print(f'Diagonal element are : {dig_2}')
print('*'*50)
for i in range(row):
    x = matrix[i][i]
    matrix[i][i] = matrix[i][row-1-i]
    matrix[i][row - 1 - i] = x

for i in matrix:
    for j in i:
        print("%4d" %j, end=' ')
    print()