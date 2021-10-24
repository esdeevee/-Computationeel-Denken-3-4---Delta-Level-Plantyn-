# lees een natuurlijk getal in
n = int(input('Geef een natuurlijk getal: '))

# initialiseer een numerieke variabele som
som = 0

# herhaal voor elk getal strikt kleiner dan n:
for i in range(n):
    # controleer of i deelbaar is door 3 of door 5
    if i % 3 == 0 or i % 5 == 0: 
        # verhoog de waarde van som met i
        som = som + i
        
# print de berekende som
print(som)
