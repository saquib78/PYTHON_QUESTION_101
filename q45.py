# chose positive and negative number b/w (-100,100)

from random import randint

num = 25
arr = []
posi = []
negi = []

for i in range(num):
    arr.append(randint(-100,100))

for i in arr:
    if i >= 0:
        posi.append(i)
    else:
        negi.append(i)

print(f'Array is : {arr}')
print('+'*40)
print(f'Positive number is : {posi}')
print('+'*40)
print(f'Negative number is : {negi}')