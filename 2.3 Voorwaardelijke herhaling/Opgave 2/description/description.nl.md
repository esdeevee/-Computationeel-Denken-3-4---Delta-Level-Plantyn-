### Opgave

Kopieer en plak onderstaand programma in je IDE. Voer het programma uit.

```python
# definieer twee numerieke variabelen
som = 0
aantal = 0
# herhaal voor altijd
while True:
    # lees de invoer in, die ofwel een getal kan zijn, ofwel de string STOP
    invoer = input('Geef een getal of typ STOP: ')
    if invoer == 'STOP':
         # als de gebruiker STOP heeft getypt, onderbreek je onmiddellijk de while-lus
         # het programma gaat verder op lijn 18
        break
    else:
        # de gebruiker heeft een getal getypt
        # verhoog de waarde van de variabele som met het ingevoerde getal
        som = som + float(invoer)
        # verhoog de waarde van de variabele som met 1
        aantal = aantal + 1
# bereken en toon het gemiddelde van de ingevoerde getallen
gemiddelde = som / aantal
print('Het gemiddelde van deze getallen is', gemiddelde)
```
