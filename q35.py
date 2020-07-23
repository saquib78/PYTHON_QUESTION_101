str = "ABDUL , MALIK , SAQUIB , HAMDAN , TARIQUE , SUBHAM , PARSOON , KHALID"

print(str)

str1 = input('Enter name you wants to replace : ')
str2 = input('Enter new name : ')

lstr1 = len(str1)

while str.find(str1) > 0:
    i= str.find(str1)
    str = str [:1] + str2 + str[i+lstr1:]

print(str)