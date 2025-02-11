n = int(input('Geef n: '))

aantal_links = n-1
aantal_midden = -1

print(aantal_links * '.' + 'X' + aantal_links * '.')
for i in range(n-1):
    aantal_links -= 1
    aantal_midden += 2
    uitvoer = aantal_links * '.' + 'X' + aantal_midden * '.' + 'X' + aantal_links * '.'
    print(uitvoer)
for i in range(n-2):
    aantal_links += 1
    aantal_midden -= 2
    uitvoer = aantal_links * '.' + 'X' + aantal_midden * '.' + 'X' + aantal_links * '.'
    print(uitvoer)


aantal_links += 1
print(aantal_links * '.' + 'X' + aantal_links * '.')
