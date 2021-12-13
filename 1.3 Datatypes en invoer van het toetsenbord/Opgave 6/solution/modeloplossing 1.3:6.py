# dit programma leest de oppervlakte (A) van een cirkel (in cm2) in en berekent de straal (r) van de cirkel
from math import sqrt, pi
A = float(input('Geef de oppervlakte van de cirkel (in cm2): '))
r = round(sqrt(A / pi), 1)
print(r)
