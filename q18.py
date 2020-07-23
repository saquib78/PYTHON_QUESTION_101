# convert from base 2 to 9          ** NOT**

num = int(input('Enter number to convert : '))

num_base = int(input('Chose the base 2-9 : '))

if not (2<=num_base <=9):
    quit()

num1 = ''

while num >0:
    num1 = str(num%num_base)+num1
    num //= num_base
    # '//' this called floor division operator . that is convert simple whole number
print(num1)