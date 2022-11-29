### Opgave

In de vorige opgaves werd een if-statement altijd gevolgd door een test (`if getal_1 > getal_2`, `if getal % 3 == 0`, ...). Dat hoeft niet altijd het geval te zijn. Je kunt ook het resultaat van de test opslaan in een variabele met het datatype boolean. In de `if ...`-constructie kun je dan op een elegante manier verwijzen naar deze variabele.

Analyseer onderstaande code. Noteer de uitvoer die de computer volgens jou zal geven. Controleer door de code te plakken in een IDE en het programma uit te voeren.

```python
# lees een natuurlijk getal in
getal = int(input('Geef een natuurlijk getal: '))
# controleer de deelbaarheid van dit getal door 3 en door 7
getal_deelbaar_door_3 = getal % 3 == 0
getal_deelbaar_door_7 = getal % 7 == 0
# als een getal deelbaar is door 3 en door 7, is het deelbaar door 21
if getal_deelbaar_door_3 and getal_deelbaar_door_7:
    print(getal, 'is deelbaar door 21.')
elif getal_deelbaar_door_3:
    print(getal, 'is deelbaar door 3.')
elif getal_deelbaar_door_7:
    print(getal, 'is deelbaar door 7.')
else:
    print(getal, 'is niet deelbaar door 3 en 7.')
```
