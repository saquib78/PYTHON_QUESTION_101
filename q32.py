# find the quadratic equation solution
import math
x = int(input('Enter coefficient of x square : '))
y = int(input('Enter coefficient of x : '))
z= int(input('Enter constant value : '))

solution = (math.sqrt((y*y)-(4*x*z)))+(-y)
solution1 = (math.sqrt((y*y)-(4*x*z)))-(-y)

print(f'Solution of quadratic equation is : {solution} , {solution1}')