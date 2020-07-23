# read text from file and print it as dictionary

goods = {}

for i in open('project_82.txt'):
    thing = i.split()
    thing[1] =int(thing[1])
    thing[2] = float(thing[2])
    goods[thing[0]] = thing[1:]

print(goods)