# calculatethe orbital speed

from math import pi

dis = float(input('Enter Your KM in (millions) : '))
vel = float(input('Enter Orbital Speed in (km/sec) : '))

dis = dis*1000000  #convert into km.

yr_1=2*pi*dis/vel

yr_2 = yr_1/(60*60*24)

print(round(yr_2))
