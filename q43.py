# find minimum value present in an array

from random import randint

num = 20

arr = []

for i in range(num):
    arr.append(randint(1,1000))

less = arr[1]

for i in arr:
    if less > i:
        less = i

arr.sort()
print(arr)
print('Minimum Value is : ',less)