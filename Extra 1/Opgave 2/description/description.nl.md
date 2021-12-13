### Opgave

Elk boek dat wordt uitgegeven, krijgt een zogenaamd ISBN-nummer. Deze afkorting staat voor International Standard Book Number. Er bestaan verschillende codes, maar in deze opgave beschouwen we uitsluitend ISBN-nummers met 13 cijfers.

Het laatste cijfer van een ISBN-nummer is een controlecijfer dat als volgt berekend wordt.
* Bereken de som van het eerste cijfer, drie maal het tweede cijfer, het derde cijfer, drie maal het vierde cijfer, ..., het elfde cijfer en drie maal het twaalfde cijfer.
* Bereken van deze som de rest bij deling door 10.
* Bereken het verschil van 10 en deze rest.
* Bereken van dit getal nogmaals de rest bij deling door 10. Dit resultaat geeft je het controlecijfer.

Schrijf een programma dat een getal van 12 cijfers vraagt. Het programma berekent het controlecijfer en toont het volledige ISBN-nummer, inclusief liggende streepjes.


### Voorbeeld

**Invoer:**

    Geef het getal van 12 cijfers: 978616557262

**Uitvoer:**

    978-6-165-57262-0
    
