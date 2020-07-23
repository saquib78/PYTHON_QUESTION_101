# find number of lines , words and letter..
lines = 0
words = 0
letters = 0


fb = "project_83.txt"
for line in open(fb):
    lines +=1
    letters +=len(line)

    posi = 'out'

    for letter in line:
        if letter != ' ' and posi == 'out':
            words +=1
            posi = 'in'

        elif letter == ' ':
            posi = 'out'


print("Lines : ",lines)
print("Words : ",words)
print("Letters : ",letters)
