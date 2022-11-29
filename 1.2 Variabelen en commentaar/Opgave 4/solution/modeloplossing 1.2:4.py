# dit programma berekent de straal (r) van een cirkel als de oppervlakte (A) gegeven is
from math import sqrt, pi
A = 500
r = round(sqrt(A / pi), 1)
print(r)
