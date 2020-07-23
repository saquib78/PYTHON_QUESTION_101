# get price of total things

things = {'apple':180, 'mango':64, 'orange':80}


for pro, price in things.items():
    print(pro, ' = ',price)

cost = 0
while True:
    pro = input('Select product : (for stop press n ) : ')
    if pro == 'n':
        break
    qty = int(input('no of product : '))
    cost +=things[pro]*qty

print(cost)

# if i use quit() statement in line 13. then it stop complete
# program and nothing is worked after while loop. but
# if i use break statement then it is only stop while loop .
# and after that it will execute simply.
