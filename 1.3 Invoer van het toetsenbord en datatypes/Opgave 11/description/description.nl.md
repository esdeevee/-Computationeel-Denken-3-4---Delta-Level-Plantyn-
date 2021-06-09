### Opgave

Schrijf een programma dat een willekeurig getal genereert tussen 0 en 10. Laat de gebruiker vervolgens dat getal raden. Wanneer het antwoord juist is, wordt ook het aantal pogingen getoond om het getal te raden.

Om een random getal te genereren, kan je gebruik maken van volgende code:
```python
from random import randint
getal = randint(0,10)
# randint = random integer
```

`randint(a,b)` genereert een (pseudo-)willekeurig getal n zodat a <= n <= b.

### Voorbeeld

    Doe een gok: 5
    Fout. Doe opnieuw een gok: 3
    Fout. Doe opnieuw een gok: 8
    Juist! Je had 3 pogingen nodig om het getal te raden!
