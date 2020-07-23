# how to get most occurrence value

from random import randint
x=[]
num = 25
for i in range(num):
    x.append(randint(1,10))
    x.sort()

print(x)

my_set = set(x)

times = None
maxi_time = 0


for j in my_set:
    freq = x.count(j)

    if freq > maxi_time:
        maxi_time = freq
        times = j

print(f'In The above set {times} is comes {maxi_time} times.'
      f' so it is comes more times')
