# sum of odd digits and even digits in an integer

num = int(input('Enter your Integer Value : '))
even =0
odd = 0
while num > 0:
    digit = num%10
    if digit%2==0:
        even +=digit
    else:
        odd +=digit

    num = num//10

print('Sum of Even digits : ',even)
print('Sum of odd digits : ',odd)

