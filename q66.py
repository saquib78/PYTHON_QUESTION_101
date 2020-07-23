# delete the dictionary items

from random import choice
from random import randint
import string
import random
num = 6
x=[]
y=[]
for i in range(num):
    x.append(randint(1,9))
    y.append(choice(string.ascii_letters.upper()))

dic_1 ={}
for i in range(len(x)):
    dic_1 = dict(zip(x,y))

print(f'Before Delete : {dic_1}')

keys =list(dic_1.keys())
del_key =random.choice(keys)
del dic_1[del_key]
print(' '*20)
print('*'*50)
print(' '*20)
print(f'After Delete : {dic_1}')
