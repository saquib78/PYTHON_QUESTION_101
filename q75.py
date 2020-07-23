# search a binary number

from random import randint

def b_search(num,list_2):
    for j in range(x):
        if num == list_2[j]:
            return j+1



list_1 = []
x = 10
for i in range(x):
    list_1.append(randint(1,15))
list_1.sort()
print(list_1)

x = int(input('Enter Your Value . that You Wants to Search : '))
print(b_search(x,list_1))