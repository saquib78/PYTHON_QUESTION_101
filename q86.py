# find the existing file is available or not . if available open it.

file = input('Enter Your File Name with Extension : ')
try:
    fb = open(file)
except:
    print('Error . This File is not available')

else:
    print(fb.read())