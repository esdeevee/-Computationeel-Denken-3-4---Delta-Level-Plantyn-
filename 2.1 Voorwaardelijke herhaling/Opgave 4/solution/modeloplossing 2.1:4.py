# lees twee getallen in
getal_1 = int(input('Geef een eerste geheel getal: '))
getal_2 = int(input('Geef een tweede geheel getal: '))

# controleer of de getallen gelijk zijn aan elkaar
if getal_1 == getal_2:
    print('De getallen zijn gelijk aan elkaar.')

# controleer of het eerste getal groter is dan het tweede    
elif getal_1 > getal_2:
    print('Het eerste getal is groter dan het tweede getal.')

# het eerste getal moet kleiner zijn dan het eerste    
else:
    print('Het eerste getal is kleiner dan het tweede getal.')
