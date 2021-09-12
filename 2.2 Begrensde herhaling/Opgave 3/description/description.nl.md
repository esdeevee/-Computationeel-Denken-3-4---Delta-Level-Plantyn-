### Opgave

Kopieer en plak onderstaand programma in een IDE. Analyseer de code. Je mag ze kopiëren en plakken in een IDE en daar uitvoeren.

```python
# laat i toenemen van 1 t.e.m. 10
for i in range(1, 11):   
    # definieer uitvoer als een lege string
    uitvoer = ''
    # laat ook j toenemen van 1 t.e.m. 10
    for j in range(1, 11):  
        # bereken het product van i en j
        product = i*j
        # plak het berekende product en een spatie aan de bestaande uitvoer
        uitvoer = uitvoer + str(product) + ' '
    # toon de variabele uitvoer
    print(uitvoer)
```
