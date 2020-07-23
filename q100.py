# get total surface area of cylinder
from math import pi

height = float(input('Enter Height of cylinder : '))
radius = float(input('Enter Radius of Cylinder : '))

circle = 2*(pi*radius**2) # area of bottom circle
side = 2*pi*radius*height # area of curved surface


area = circle+side

print(f'Area of Total Surface = {round(area,2)}')