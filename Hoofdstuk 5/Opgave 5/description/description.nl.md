### Blokje om (VPW 2016)

Een dronken man vertrekt ‘s avonds vanuit zijn favoriete kroeg. Hij weet echter niet meer waar hij heen moet en loopt doelloos rond in de stad. Na een paar uur komt hij eindelijk iemand tegen die hem hulp biedt. Op welke plaats in stad is de redding nabij?

De kroeg waar de man start, ligt op locatie (0, 0). Je krijgt telkens een reeks stappen die de dronken man zet, aangegeven met de windrichtingen:
* N: de dronkeman zet een stap omhoog, volgens de positieve oriëntatie van de y-as;
* O: de dronkeman zet een stap naar rechts, volgens de positieve oriëntatie van de x-as;
* Z: de dronkeman zet een stap omlaag, volgens de negatieve oriëntatie van de y-as;
* W: de dronkeman zet een stap naar links, volgens de negatieve oriëntatie van de x-as.

Gevraagd wordt om de eindpositie van de man na zijn wandeling te bepalen. Stel dat de man volgende stappen zet:

O O N N N W W W W Z Z Z Z Z O O O W W W W W Z Z Z W W W,

dan eindigt hij in (−7, −5). Verifieer dit!

De eerste regel van de invoer bevat steeds een geheel getal 1 ≤ n ≤ 1000 dat het aantal testgevallen aangeeft. Per geval volgt dan één regel met:
* het aantal stappen s die de man zet;
* per stap een letter die de richting aangeeft.
Alle getallen en letters in de invoer die op dezelfde regel voorkomen, worden gescheiden door één enkele spatie.

De uitvoer bestaat uit n regels, voor elk testgeval één. Elke regel bestaat uit drie getallen, gescheiden door één enkele spatie:
* het eerste getal geeft het testgeval aan;
* het tweede getal stelt de x-coördinaat van de eindpositie voor;
* het derde getal stelt de y-coördinaat van de eindpositie voor.

### Voorbeeld

**Invoer:**

    2
    3 N O Z
    28 O O N N N W W W W Z Z Z Z Z O O O W W W W W Z Z Z W W W

**Uitvoer:**

    1 1 0
    2 -7 -5
