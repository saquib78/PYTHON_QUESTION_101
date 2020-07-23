# how to get percentage of lower case and upper case in a string

str = input('Enter Your String : ')

leng =len(str)
small =0
big = 0
other = 0
for i in str:
    if 'a' <= i <= 'z':
        small +=1
    elif 'A' <= 'Z':
        big +=1

    else:
        other +=1


sum = small+big+other

print(f'percentage of upper case alphabet is {(big/sum)*100} and '
      f'percentage of lower'
      f' case alphabet is {(small/sum)*100}.')