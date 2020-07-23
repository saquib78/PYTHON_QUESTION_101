# sum of diagonal element

from random import randint

row = 4
col = 4

matrix =[]
for i in range(row):
    y =[]
    for j in range(col):
        y.append(randint(1,6))
    matrix.append(y)

for my in  matrix:
    print(my)

digonal_1 = 0
digonal_2 = 0

for i in range(row):
    for j in range(col):
        if i == j:
            digonal_1 +=matrix[i][j]
        elif row - i -1 == j:
            digonal_2 +=matrix[i][j]

print(digonal_1)
print(digonal_2)

