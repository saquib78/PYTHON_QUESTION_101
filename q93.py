# select even number and odd number from list..

from random import randint

mini = int(input('Enter Your Minimum Value : '))
maxi = int(input('Enter Your Maximum Value : '))
term = int(input('Number of Terms : '))

list_1 = []

for i in range(term):
    list_1.append(randint(mini,maxi))

print(' ')
print(f'Original List = {list_1}')

list_2 = []
list_3 = []

for j in list_1:
    if j%2==0:
        list_2.append(j)
    else:
        list_3.append(j)
print(' ')
print(f'Even number List = {list_2}')
print(' ')
print(f'Odd Number List = {list_3}')