# chose 30 random number and differentiate with odd and even

from random import randint

num = 30
arr = []

for i in range(num):
    arr.append(randint(1,1000))

od = []
odd = 0
eve = []
even = 0

for i in arr:
    if i%2==0:
        even +=1
        eve.append(i)

    else:
        odd +=1
        od.append(i)

print(arr)
print('*'*40)
print(f'Number of even integer is {even} and that is {eve}')
print('*'*40)
print(f'Number of odd integer is {odd} and it is {od}')
