# dit programma vraagt de straal van een bol (in cm) en berekent het volume van de bol (in cm3)
from math import pi
r = float(input('Geef de straal van de bol (in cm): '))
V = 4/3 * pi * r**3
# het volume moet afgerond worden naar een natuurlijk getal
print(round(V))
