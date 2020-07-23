# check for non-existing number

x = 20
y = 30
z = 40

ab = input('Enter x , y , z only : ')

try:
    exec ("print("+ab+")")

except:
    print('You are enter some wrong keyword')

