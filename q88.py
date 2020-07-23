# user enter index value . print it if that index have any value.

list_1 = [1,2,3,4,5,6,7,8,9]


print('t = for stop')


while True:
    x = input('Enter Index Value : ')
    if x == 't':
        break
    try:
        x = int(x)
        print(list_1[x])

    except ValueError:
        print('only Integer is allowed!')

    except IndexError:
        print(f'Error ! , Number is out of index :{x}')
