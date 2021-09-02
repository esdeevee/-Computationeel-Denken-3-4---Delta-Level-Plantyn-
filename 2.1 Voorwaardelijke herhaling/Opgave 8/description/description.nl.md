### Opgave

Op het einde van de opleiding aan een universiteit of hogeschool wordt aan elke
student een graad toegekend. Die graad wordt bepaald in functie van het gemiddelde
van alle resultaten die de student behaald heeft tijdens de opleiding. De tabel geeft aan
hoe het gemiddelde omgezet wordt naar een graad.

gemiddelde     | graad                   | afkorting
:-------------:|:-----------------------:|:---------:
minder dan 68% | voldoening              | V
minstens 68%   | onderscheiding          | O
minstens 77%   | grote onderscheiding    | GO
minstens 85%   | grootste onderscheiding | GGO
minstens 90%   | felicitaties            | F

Onderstaande code bevat een redeneringsfout. Zoek de fout en verbeter het programma.

```python
# lees de gemiddelde score in
gemiddelde = float(input(’Geef de gemiddelde score: ’))

# bepaal de graad
if gemiddelde < 68:
    graad = ’V’
elif gemiddelde >= 68:
    graad = ’O’
elif gemiddelde >= 77:
    graad = ’GO’
elif gemiddelde >= 85:
    graad = ’GGO’
elif gemiddelde >= 90:
    graad = ’F’

# schrijf de graad uit
print(graad)
```

### Voorbeeld

**Invoer:**

    Geef de gemiddelde score: 54

**Uitvoer:**

    V

**Invoer:**

    Geef de gemiddelde score: 82.7

**Uitvoer:**

    GO
