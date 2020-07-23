# generate a three digit number and sum its integer
from random import randint

num = randint(100,1000)
print(f'Generated Number = {num}')
sum1 = 0
while num > 0:
    x = num%10
    sum1 +=x
    num = num//10
    x = 0

print(f'Sum = {sum1}')