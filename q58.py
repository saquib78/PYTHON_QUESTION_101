# sum of each row and column in the matrix

from random import randint

col = 4
row = 4

matrix = []

sum_col = [0]*col
sum_row = [0]*row

for i in range(row):
    my_row = []
    for j in range(col):
        my_row.append(randint(1,6))
    matrix.append(my_row)

for i in range(row):
    for j in range(col):
        sum_col[j] +=matrix[i][j]
        sum_row[i] +=matrix[i][j]

for i in range(row):
    print(matrix[i] ,"|",sum_row[i])

print('-'*5*col)
print(sum_col)

