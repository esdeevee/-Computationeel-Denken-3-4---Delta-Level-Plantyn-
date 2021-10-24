# lees een natuurlijk getal in
n = int(input('Geef een natuurlijk getal: '))

# vermenigvuldig dit getal met alle getallen van 1 tot en met 10
# dat kan je doen met de functie range(1, 11)

for i in range(1, 11):
    print(i, '*', n, '=', i*n)
