### Opgave

Schrijf een programma dat vraagt om twee strings. Druk alle letters af die de strings gemeen hebben. Je mag hoofdletters beschouwen als verschillend van kleine letters, maar iedere letter mag niet meer dan één keer gerapporteerd worden. Zo hebben de strings peer en een bijvoorbeeld slechts één letter gemeen, namelijk de letter e.


### Voorbeeld

**Invoer:**

    Geef een eerste woord: seminarie
    Geef een tweede woord: De Vusser

**Uitvoer:**

    De strings "seminarie" en "De Vusser" hebben volgende letters gemeenschappelijk: s, e, r

**Invoer:**

    Geef een eerste woord: Python
    Geef een tweede woord: is de max!

**Uitvoer:**

    De strings "Python" en "is de max" hebben geen enkele letter gemeenschappelijk.

### Nieuwe commando's in deze opgave

Je zal voor deze opgave waarschijnlijk een nieuw commando nodig hebben. Probeer volgende code en de bijhorende uitvoer te begrijpen voor je aan deze opgave begint.

```
string = "seminarie"
print("i" in string)
print("t" in string)
print("I" in string)
```
geeft als uitvoer
```
True
False
False
```

Om een aanhalingsteken (") te printen, kan je `\"` gebruiken. Het commando

`print("\"First, solve the problem. Then, write the code.\" – John Johnson")`

geeft dus als uitvoer

`"First, solve the problem. Then, write the code." – John Johnson`
