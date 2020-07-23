# use try and except. for finding of error.

x = input('Enter Any integer Value : ')
while type(x) != float:
    try:
        x=float(x)
    except:
        print('Your are Enter some wrong try again')
        x = input('Enter Any integer Value : ')


print(x/2)
