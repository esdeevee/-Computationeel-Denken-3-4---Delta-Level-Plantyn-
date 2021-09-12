### Opgave

De Britse wiskundige John Conway (1937 – 2020) heeft een methode bedacht om uit het hoofd te berekenen met welke weekdag een willekeurige datum overeenkomt. In deze opgave wordt gewerkt met een vereenvoudigd algoritme dat geldig is van 1 maart 2000 tot en met 28 februari 2100. Het algoritme bestaat uit twee stappen.
* In een eerste stap bereken je een zogenaamde referentieweekdag. Het algoritme hiervoor staat schematisch weergegeven in het beslissingsdiagram in de cursustekst.

Het resultaat van dit algoritme is een getal `d` tussen 0 en 6. `d=0` wil zeggen dat de referentieweekdag in het ingevoerde jaar een zondag is. Bij `d=1` valt de referentieweekdag in dat jaar op een maandag, ... `d=6` wil zeggen dat de referentieweekdag in dat jaar op een zaterdag valt.

* De referentieweekdag die je in het eerste deel hebt berekend, is meestal niet de weekdag van de ingevoerde datum. Voor een willekeurig jaar komt de referentieweekdag wel overeen met de referentiedatums die in de tabel gegeven zijn.

|  maand  | referentiedag |
|:-------:|:-------------:|
maart     | 7             |
april     | 4             |
mei       | 2             |
juni      | 6             |
juli      | 4             |
augustus  | 1             |
september | 5             |
oktober   | 3             |
november  | 7             |
december  | 5             |
|:-------:|:-------------:|
januari   | 2             |
februari  | 6             |


Implementeer het algoritme in Python. Het programma vraagt eerst het jaartal (een natuurlijk getal tussen 2000 en 2099). Daarna vraagt het de maand (een natuurlijk getal tussen 1 en 12). Ten slotte vraagt het de dag (een natuurlijk getal tussen 1 en 31). Het programma berekent de weekdag voor de ingevoerde datum. De uitvoer van het programma is in het formaat `dinsdag 9 1 2007`.


### Voorbeeld

**Invoer:**

    Geef een jaartal (2000 - 2099): 2011
    Geef het nummer van de maand: 7
    Geef de dag van de maand: 28



**Uitvoer:**

    donderdag 28 7 2011
