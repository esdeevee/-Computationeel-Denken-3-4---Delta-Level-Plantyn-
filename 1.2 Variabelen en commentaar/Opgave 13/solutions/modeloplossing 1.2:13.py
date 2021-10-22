# dit programma berekent de hoogte (in cm) van een kegel als de straal van het grondvlak r (in cm) en het volume (in cm3) gegeven zijn
from math import pi
r = 8
V = 400
h = 3 * V / (pi * r**2)
print(round(h, 1))
