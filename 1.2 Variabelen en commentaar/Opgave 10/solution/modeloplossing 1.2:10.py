# gebruik een variabele voor elke gegeven numerieke waarde
muuroppervlakte = 52
aantal_m2_per_l = 12
aantal_lagen = 2
prijs_1 = 35
prijs_4 = 110
# bereken de totale te verven oppervlakte
aantal_m2 = muuroppervlakte * aantal_lagen
# bereken het aantal potten verf van 4 liter
aantal_4 = aantal_m2 // (4 * aantal_m2_per_l)
# bereken het aantal potten verf van 1 liter
aantal_1 = 1 + (aantal_m2 % (4 * aantal_m2_per_l)) // aantal_m2_per_l
# bereken de prijs
prijs = aantal_4 * prijs_4 + aantal_1 * prijs_1
# toon de uitvoer
print(aantal_4, aantal_1)
print(prijs)
