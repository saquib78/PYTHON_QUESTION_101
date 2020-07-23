# how to make two list into dictionary.

from random import randint # for integer
from random import choice
import string

list_1 = []
list_2 = []
num = 5
for i in range(num):
    list_1.append(randint(1,6))
    list_2.append(choice(string.ascii_letters))
print('-'*40)
print(list_1)
print(' '*40)
print(list_2)
print('-'*40)
dic = {}

for i in range(len(list_1)):
    dic = dict(zip(list_2,list_1))

print(dic)