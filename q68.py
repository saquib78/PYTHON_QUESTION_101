# fill the list ==> when range and number of element take by user

from random import randint

def list_1(mat,maxi,mini,no):
    for i in range(no):
        mat.append(randint(mini,maxi))


list_2 =[]
x=int(input('Enter min value : '))
y=int(input('Enter max value : '))
z=int(input('Enter number of element : '))

list_1(list_2,y,x,z)

print(list_2)