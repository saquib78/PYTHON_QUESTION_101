# sorting of array without using (short function)
from random import randint
x=[]
num = 20

for i in range(num):
    x.append(randint(1,25))
print(f'Original list : {x}')

for i in range(num):
    for j in range(num-i-1):
        if x[j] > x[j+1]:
            z = x[j]
            x[j] = x[j+1]
            x[j+1] = z

print(f'Shorted list : {x}')