# area and perimeter of right angle triangle..

import math

x = float(input('Enter Length of Base : '))
y = float(input('Enter Length of Height : '))

z = math.sqrt((pow(x,2)+pow(y,2)))

Area = (x*y)/2
pre = x+y+z

print(f'Area of triangle : {round(Area,2)}')
print(' ')
print(f'Perimeter of Triangle : {round(pre,2)}')