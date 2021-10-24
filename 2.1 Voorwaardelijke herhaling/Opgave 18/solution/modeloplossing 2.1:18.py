# lees jaar, maand en dag in
jaar = int(input('Geef een jaartal (2000 - 2099): '))
maand = int(input('Geef het nummer van de maand: '))
dag = int(input('Geef de dag van de maand: '))

# om problemen met schrikkeldagen te vermijden, beschouw je januari en februari als de 13de en 14de maand van het vorige jaar
if maand == 1 or maand == 2:
    maand = maand + 12
    jaar = jaar - 1

# bereken d, het getal dat overeenkomt met de referentieweekdag
j = jaar % 100
if j % 2 == 1:
    j = j + 11
j = j/2
if j % 2 == 1:
    j = j + 11
d = (72 - j) % 7

# als de maand januari of februari was, zet deze dan terug om naar de normale situatie
if maand == 13 or maand == 14:
    maand = maand - 12
    jaar = jaar + 1

# gebruik de referentieweekdag en de referentiedatum om de weekdag van de ingevoerde datum te bepalen
# deze weekdag is een getal tussen 0 en 6
# 0 komt overeen met zondag, ..., 6 komt overeen met zaterdag
if maand == 3:
    weekdag = (d + (dag - 7)) % 7
elif maand == 4:
    weekdag = (d + (dag - 4)) % 7
elif maand == 5:
    weekdag = (d + (dag - 2)) % 7
elif maand == 6:
    weekdag = (d + (dag - 6)) % 7
elif maand == 7:
    weekdag = (d + (dag - 4)) % 7
elif maand == 8:
    weekdag = (d + (dag - 1)) % 7
elif maand == 9:
    weekdag = (d + (dag - 5)) % 7
elif maand == 10:
    weekdag = (d + (dag - 3)) % 7
elif maand == 11:
    weekdag = (d + (dag - 7)) % 7
elif maand == 12:
    weekdag = (d + (dag - 5)) % 7
elif maand == 1:
    weekdag = (d + (dag - 2)) % 7
elif maand == 2:
    weekdag = (d + (dag - 6)) % 7

# print de uitvoer
if weekdag == 0:
    print('zondag', dag, maand, jaar)
elif weekdag == 1:
    print('maandag', dag, maand, jaar)
elif weekdag == 2:
    print('dinsdag', dag, maand, jaar)
elif weekdag == 3:
    print('woensdag', dag, maand, jaar)
elif weekdag == 4:
    print('donderdag', dag, maand, jaar)
elif weekdag == 5:
    print('vrijdag', dag, maand, jaar)
elif weekdag == 6:
    print('zaterdag', dag, maand, jaar)
