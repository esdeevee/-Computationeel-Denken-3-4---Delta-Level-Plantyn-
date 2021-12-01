### Opgave

Sinds 2014 maken alle Europese banken gebruik van het International Bank Account Number (IBAN). Een voorbeeld van een geldig Belgisch IBAN-bankrekeningnummer is BE69 7331 2345 6778. Een Belgisch IBAN-nummer wordt als volgt opgebouwd:
* BE is een internationaal afgesproken code voor Belgische banken.
* 69 is een eerste controlegetal.
* De eerste drie cijfers (733) vormen de bankcode. Dit getal verwijst naar de bank die de rekening beheert.
* De volgende zeven cijfers (1234567) vormen het rekeningnummer van de klant bij deze bank.
* De twee laatste cijfers (78) vormen een tweede controlegetal.

Het eigenlijke rekeningnummer heeft dus maar 10 cijfers, zoals 733-1234567. De controlegetallen worden als volgt berekend:
* Laat het liggend streepje weg. Bereken de rest bij deling van het eigenlijke rekeningnummer door 97. Het getal dat je zo bekomt, is het tweede controlegetal.
* Schrijf twee keer het tweede controlegetal en vul aan met 111400. Bereken van dit getal opnieuw de rest bij deling door 97. Trek deze rest af van 98. Het getal dat je zo bekomt, is het eerste controlegetal.
* Beide controlegetallen hebben altijd twee cijfers. Als een controlegetal een getal tussen 0 en 9 is, dan moet je er een nul voor zetten.

Met de twee controlegetallen kan snel gecontroleerd worden of een ingevoerd rekeningnummer wel geldig is. Als je een cijfer verkeerd ingeeft, zal dat dankzij deze controlegetallen altijd gedetecteerd worden. Zo verkleint de kans dat je per ongeluk geld overschrijft naar een verkeerd rekeningnummer.

Schrijf een programma dat als invoer een getal van 10 cijfers inleest (bv. 7331234567) dat overeenkomt met een Belgisch rekeningnummer. Er wordt geen liggend streepje ingevoerd tussen de bankcode en het eigenlijke rekeningnummer. Het programma berekent de twee controlegetallen. Als uitvoer geeft het programma het volledige IBAN-nummer in de vorm BE 69 7331234567 78.

### Voorbeeld

**Invoer:**

    Geef een Belgisch rekeningnummer: 1234567890

**Uitvoer:**

    BE 32 1234567890 02
