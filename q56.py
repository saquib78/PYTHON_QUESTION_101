# generate a random matrix

from random import randint
row = int(input('Enter Number of Row : '))
col = int(input('Enter Number of Column : '))


x = []

for i in range(row):
    y = []
    for j in range(col):
        y.append(randint(1,20))
    x.append(y)

for i in x:
    for j in i:
        print("%3d" % j , end= ' ')
    print()


