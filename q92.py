# fill the list when you take input from user as min , max and number of trwams
# from user.........
from random import randint

mini = int(input('Enter Your Minimum Value : '))
maxi = int(input('Enter Your Maximum Value : '))
term = int(input('Number of Terms : '))

list_2 = []

for i in range(term):
    list_2.append(randint(mini,maxi))

print(list_2)