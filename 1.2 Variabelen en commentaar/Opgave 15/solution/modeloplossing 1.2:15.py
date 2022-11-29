# dit programma berekent sin A, cos A en tan A in een rechthoekige driehoek (B=90) als de lengte van de rechthoekszijden AB en BC gegeven is
from math import sqrt
AB = 8
BC = 4
AC = sqrt(AB**2 + BC**2)
sin_A = BC / AC
cos_A = AB / AC
tan_A = BC / AB
print(round(sin_A, 3))
print(round(cos_A, 3))
print(round(tan_A, 3))
