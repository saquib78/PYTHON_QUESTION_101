# check a element that is present in a row and column

from random import randint
row = 5
col = 5
matrix = []

for i in range(row):
    y=[]
    for j in range(col):
        y.append(randint(10,40))
    matrix.append(y)

for i in matrix:
    print(i)
print()

num = int(input('Enter Your Number b/w (10,40) : '))

for i in range(row):
    for j in range(col):
        if num == matrix[i][j]:
            print(f'Row is {i+1} , and column is {j+1}')





