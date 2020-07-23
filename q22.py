# binary search of number in an array

from random import random

n=20

array = []

for x in range(n):
    array.append(int(random()*100))

array.sort()
print(array)

num = int(input('Enter Your Number : '))

mini = 0
maxi = n-1

while mini <= maxi:
    mid = (mini+maxi)//2

    if num <array[mid]:
        maxi = mid-1

    elif num > array[mid]:
        mini = mid+1

    else:
        print('The location of index is : ',mid)
        break
else:
    print('Number is not present')