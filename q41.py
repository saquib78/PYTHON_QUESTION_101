# generate 20 random number using array b/w 1 to 1000

from random import randint

num = 20
arr = []

for i in range(num):
    arr.append(randint(1,1000))

arr.sort()
print(arr)