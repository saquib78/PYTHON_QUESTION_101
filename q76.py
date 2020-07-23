# make a right shift or recycle items of list

from random import randint
def right(f,n):
    if n <0:
        n = abs(n)
        for i in range(n):
            f.append(f.pop(0))
    else:
        for i in  range(n):
            f.insert(0,f.pop())


list_1 = []
num =  10
for i in range(num):
    list_1.append(randint(1,10))

print(f'Original : {list_1}')
print(' '*50)

right(list_1,-2)
print(f'List after (-2) shift : {list_1}')
print(' '*50)

right(list_1,3)
print(f'List after (3) shift : {list_1}')
print(' '*50)

right(list_1,5)
print(f'List after (5) shift : {list_1}')
print(' '*50)





