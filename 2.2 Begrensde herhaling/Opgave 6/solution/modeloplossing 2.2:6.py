# lees een natuurlijk getal in
n = int(input('Geef het aantal oneven getallen: '))

# begin te tellen bij 1, neem stapjes van 2 en stop vlak voor 2*n
# het laatste getal dat getoond wordt, is 2n - 1, en dat is precies het n-de oneven getal
for i in range(1, 2*n, 2):
    print(i)



# alternatieve oplossing

# lees een natuurlijk getal in
n = int(input('Geef het aantal oneven getallen: '))

# herhaal n keer
for i in range(n):
    # bereken en toon het i-de oneven getal met de formule die je gevonden hebt:
    x = 2*i + 1
    print(x)
