# simple intersection of list

from random import randint

x=[]
y=[]
z=[]
num = 10

for i in range(num):
    x.append(randint(1,15))
    y.append(randint(1,15))

z= list(set(x) & set(y))

print(z)
#print(x)
#print(y)
