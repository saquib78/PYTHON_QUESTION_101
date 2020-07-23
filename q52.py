# print longest order in tha list..

from random import randint
x = []
num = 15

for i in range(num):
    x.append(randint(1,25))

print(x)

my_l =0
length = 1
maxi = 1

for i in range(num):
    if x[i] > x[i-1]:
        length +=1
    else:
        if length > maxi:
            maxi = length
            my_l = i
        length = 1


print('Maximum length = ',maxi)
print('Order is = ',x[my_l-maxi : my_l])
