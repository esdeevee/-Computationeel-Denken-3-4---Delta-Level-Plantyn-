# dit programma zet een Belgisch bankrekeningnummer om naar het IBAN-formaat
rekeningnummer = 1357924680
# bereken de rest bij deling door 97 (stel dit getal voor als xy: x is het cijfer van de tientallen, y is het cijfer van de eenheden)
controlegetal_2 = rekeningnummer % 97
# stel een nieuw getal samen van de vorm xyxy111400
# het getal xy00000000 kun je maken door xy te vermenigvuldigen met 10**8
# het getal xy000000 kun je maken door xy te vermenigvuldigen met 10**6
# als je xy*10**8 optelt bij xy*10**6, bekom je xyxy000000
# tel hier nog eens 111400 bij op
getal = controlegetal_2 * 10**8 + controlegetal_2 * 10**6 + 111400
# bereken het tweede controlegetal
controlegetal_1 = 98 - getal % 97
# genereer de uitvoer
print('BE', controlegetal_1, rekeningnummer, controlegetal_2)
