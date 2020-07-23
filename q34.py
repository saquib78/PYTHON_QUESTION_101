# extend the alphabet ==> give two input and it is print all
# alphabetic letter b/w them



str1 = input('Enter Start Letter : ')
str2 = input('Enter Last Letter : ')

while str1 <= str2:
    print(str1,end=' ')
    str1 = chr(ord(str1)+1)

print()
