# find maximum number

from random import randint

x = 20
arr = []

for i in range(x):
    arr.append(randint(1,1000))

maxi = arr[1]

for i in arr:
    if maxi < i:
        maxi = i

arr.sort()
print(arr)
print('Maximum Value is : ',maxi)