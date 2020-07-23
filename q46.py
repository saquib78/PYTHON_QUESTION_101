# use random function . and get number greater then average of array

from random import randint

num = 25
arr = []
maxi = []
sumi = 0

for i in range(num):
    arr.append(randint(1,1000))

for i in arr:
    sumi +=i

result = sumi//num

maxim = result

for i in arr:
    if maxim < i:
        maxi.append(i)

print(f'Array are : {arr}')
print('-'*40)
print(f'Average of array : {result}')
print('-'*40)
print(f'Number greater then average : {maxi}')





