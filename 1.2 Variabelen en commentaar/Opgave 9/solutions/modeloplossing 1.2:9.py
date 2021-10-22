en kleine diagonaal (in cm) gegeven zijn
# stel de grote en de kleine diagonaal voor door de variabelen GD en KD
# A is de oppervlakte en P is de omtrek
from math import sqrt
GD = 12
KD = 7
A = GD * KD/2
P = 4 * sqrt((GD/2)**2 + (KD/2)**2)
print(A)
print(round(P, 1))
