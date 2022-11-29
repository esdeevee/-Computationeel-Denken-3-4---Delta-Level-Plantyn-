# dit programma berekent de lengte l (in cm) van een persoon als de massa m (in kg) en de BMI (in kg/m2) gegeven zijn
from math import sqrt
m = 55
BMI = 22
l = 100 * sqrt(m / BMI)
print(round(l))
