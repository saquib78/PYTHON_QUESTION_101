# intersection of list using loop

from random import randint

x =[]
y =[]
num =10

for i in range(num):
    x.append(randint(1,20))
    y.append(randint(1,20))

#print(x)
#print(y)

z = []

for i in x:
    for j in y:
        if i==j:
            z.append(i)
            break

print(z)