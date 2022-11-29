# dit programma berekent de datum (einddatum) en het tijdstip (einduur) waarop een timer met duur timer afloopt die start op 31 december om beginuur
begindatum = int(input('Geef de datum (in december) waarop de timer wordt gestart: '))
beginuur = int(input('Geef het tijdstip waarop de timer wordt gestart: '))
timer = int(input('Geef de duur (in uur) van de timer: '))
einddatum = (begindatum + (beginuur + timer) // 24) % 31
einduur = (beginuur + timer) % 24
print(einddatum, einduur)
