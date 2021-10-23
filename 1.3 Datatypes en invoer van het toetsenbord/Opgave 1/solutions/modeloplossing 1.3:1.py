# lees de gegevens in
aantal_ballen = int(input('Geef het gewenste aantal ballen: '))
eenheidsprijs = float(input('Geef de eenheidsprijs: '))
kortingspercentage = float(input('Geef het kortingspercentage: '))
administratiekost = float(input('Geef de administratiekost: '))
# bereken
totaalprijs = aantal_ballen * eenheidsprijs
korting = kortingspercentage / 100 * totaalprijs
verzendingskosten = 0.5*min(10, aantal_ballen)
# print het totale bedrag
print(round(totaalprijs - korting + administratiekost + verzendingskosten,2))
