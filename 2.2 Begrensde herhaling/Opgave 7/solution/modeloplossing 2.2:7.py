# lees een natuurlijk getal n in
getal = int(input('Geef een natuurlijk getal: '))

# initialiseer een numerieke variabele som:
som = 0

# herhaal n keer
for i in range(getal+1):
    # verhoog de waarde van som met i
    som = som + i

# toon het resultaat    
print(som)



# alternatieve oplossing, via de som van de termen van een rekenkundige rij

# lees een natuurlijk getal in
getal = int(input('Geef een natuurlijk getal: '))

# gebruik de formule voor de som van de termen van een rekenkundige rij:
som = getal * (getal + 1) / 2

# toon het resultaat 
print(som)
