### Opgave

Kopieer en plak het programma in je IDE. Voer het programma uit. Noteer wat het programma precies doet. Wat gebeurt er wanneer je toch een even getal intypt?

```python
# lees een getal in
getal = int(input('Typ een oneven getal: '))
# voer een blokje code uit zolang het ingevoerde getal even is
while getal % 2 == 0:
    print(getal, 'is geen oneven getal. Probeer opnieuw.')
    getal = int(input('Typ een oneven getal: '))
# het ingevoerde getal is niet even
print(getal, 'is oneven.')
```
