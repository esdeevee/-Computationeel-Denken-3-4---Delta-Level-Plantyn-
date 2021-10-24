# lees het aankoopbedrag in, zonder korting
aankoopbedrag = float(input('Voor hoeveel euro heb je gekocht? '))
if aankoopbedrag >= 200:
    kortingspercentage = 5
elif aankoopbedrag >= 150:
    kortingspercentage = 4
elif aankoopbedrag >= 100:
    kortingspercentage = 3
elif aankoopbedrag >= 50:
    kortingspercentage = 2
else:
    kortingspercentage = 0
    
# bereken de korting en rond af op 0,01 euro
korting = round(aankoopbedrag * kortingspercentage / 100, 2)

# bereken het te betalen bedrag
te_betalen = round(aankoopbedrag - korting, 2)
print(te_betalen, korting)
