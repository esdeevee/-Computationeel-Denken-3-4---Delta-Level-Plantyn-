# coding=utf-8

"""
# dit programma vraagt naar de lengte van de rechthoekszijden AB en BC in een rechthoekige driehoek (B=90°)
# het berekent sin A, cos A en tan A in deze driehoek
from math import sqrt
AB = float(input('Geef de lengte (in cm) van rechthoekszijde AB: '))
BC = float(input('Geef de lengte (in cm) van rechthoekszijde BC: '))
AC = sqrt(AB**2 + BC**2)
sin_A = BC / AC
cos_A = AB / AC
tan_A = BC / AB
print(round(sin_A, 2))
print(round(cos_A, 2))
print(round(tan_A, 2))
"""

from random import randint
from math import sqrt

def goniometrie(AB,BC):
    AC = sqrt(AB**2 + BC**2)
    sin_A = BC / AC
    cos_A = AB / AC
    tan_A = BC / AB
    return([round(sin_A, 2), round(cos_A, 2), round(tan_A, 2)])


# wis alle gegevens in in.csv
f = open("0.in", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("0.out", "w")
f.truncate()
f.close()

for i in range(20):
    AB = randint(1,10)
    BC = randint(1,10)
    with open('0.in', 'a') as f:
      f.write(str(AB))
      f.write("\n")
      f.write(str(BC))
      f.write("\n")
    with open('0.out', 'a') as g:
      g.write(str(goniometrie(AB,BC)[0]))
      g.write("\n")
      g.write(str(goniometrie(AB,BC)[1]))
      g.write("\n")
      g.write(str(goniometrie(AB,BC)[2]))
      g.write("\n")

for i in range(20):
    AB = randint(10,100)
    BC = randint(10,100)
    with open('0.in', 'a') as f:
      f.write(str(AB))
      f.write("\n")
      f.write(str(BC))
      f.write("\n")
    with open('0.out', 'a') as g:
      g.write(str(goniometrie(AB,BC)[0]))
      g.write("\n")
      g.write(str(goniometrie(AB,BC)[1]))
      g.write("\n")
      g.write(str(goniometrie(AB,BC)[2]))
      g.write("\n")

for i in range(30):
    AB = 0.1*randint(2,100)
    print(AB)
    BC = 0.1*randint(1,100)
    print(BC)
    with open('0.in', 'a') as f:
      f.write(str(AB))
      f.write("\n")
      f.write(str(BC))
      f.write("\n")
    with open('0.out', 'a') as g:
      g.write(str(goniometrie(AB,BC)[0]))
      g.write("\n")
      g.write(str(goniometrie(AB,BC)[1]))
      g.write("\n")
      g.write(str(goniometrie(AB,BC)[2]))
      g.write("\n")

for i in range(30):
    AB = randint(2,10000)*0.01
    BC = randint(1,10000)*0.01
    with open('0.in', 'a') as f:
      f.write(str(AB))
      f.write("\n")
      f.write(str(BC))
      f.write("\n")
    with open('0.out', 'a') as g:
      g.write(str(goniometrie(AB,BC)[0]))
      g.write("\n")
      g.write(str(goniometrie(AB,BC)[1]))
      g.write("\n")
      g.write(str(goniometrie(AB,BC)[2]))
      g.write("\n")
