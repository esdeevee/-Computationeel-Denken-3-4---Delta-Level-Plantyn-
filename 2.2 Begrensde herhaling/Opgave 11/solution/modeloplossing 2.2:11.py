# lees het aantal termen in
n = int(input('Geef een natuurlijk getal (minstens 2): '))

# definieer de eerste twee termen van de rij:
a = 1
b = 1

# print deze eerste twee termen van de rij:
print(a)
print(b)

for i in range(2, n):
    # het volgende getal in de rij is de som van a en b:
    c = a + b
    # toon deze nieuw berekende waarde:
    print(c) 
    # de nieuwe waarde van a is gelijk aan b:
    a = b  
    # de waarde van b zit nu opgeslagen in de variabele a   
    # de nieuwe waarde van b is gelijk aan c:
    b = c
    # de waarde van c zit nu opgeslagen in de variabele b
