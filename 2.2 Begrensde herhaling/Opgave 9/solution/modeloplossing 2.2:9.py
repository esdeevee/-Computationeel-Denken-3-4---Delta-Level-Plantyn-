# lees een getal in
n = int(input('Geef een natuurlijk getal: '))

# neem aan dat n een priemgetal is tot je een deler vindt van n
# de booleaanse variabele priem is bij het begin van het programma dus True
priem = True

# itereer over alle getallen 2, 3, ..., n-1
for i in range(2, n):
    # als i een deler is van n
    if n % i == 0:
        # dan is n zeker geen priemgetal
        priem = False
        
# controleer de boolean priem en toon de gewenste uitvoer
if priem:
    print(n, 'is een priemgetal.')
else:
    print(n, 'is geen priemgetal.')
