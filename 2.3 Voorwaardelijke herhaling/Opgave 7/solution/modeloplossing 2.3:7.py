# importeer de functie randint
from random import randint

# genereer een willekeurig getal tussen 0 en 10
getal = randint(0, 10)
# print(getal)
# definieer een variabele waar je het aantal pogingen bijhoudt
aantal_pogingen = 0

# herhaal
while True:
    # lees de poging in
    poging = int(input('Raad het geheime getal: '))
    aantal_pogingen = aantal_pogingen + 1
    # als de gebruiker juist heeft geraden, moet de while-lus afgebroken worden
    if poging == getal:
        break
    # anders krijgt de gebruiker feedback
    else:
        if getal > poging:
            print('Hoger')
        else:
            print('Lager')

# de gebruiker heeft het getal geraden    
print('Je had', aantal_pogingen, 'pogingen nodig om het getal te raden.')
