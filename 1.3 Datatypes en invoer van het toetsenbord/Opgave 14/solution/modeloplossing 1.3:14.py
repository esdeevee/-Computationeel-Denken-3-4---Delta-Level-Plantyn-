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
