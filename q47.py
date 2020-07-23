# replace (-1,0,1) w.r.t negative , zero ,positive

from random import randint
num = 20

arr = []
dupli = []

for i in range(num):
    arr.append(randint(-100,100))

for i in arr:
    if i ==0:
        dupli.append(0)
    elif i > 0:
        dupli.append(1)
    elif i < 0:
        dupli.append(-1)

print(f'Real array is : {arr}')
print(f'Duplicate array is : {dupli}')