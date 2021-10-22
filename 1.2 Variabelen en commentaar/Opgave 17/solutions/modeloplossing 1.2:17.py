# dit programma berekent de datum (variabele einddatum) en het tijdstip (einduur) waarop een timer afloopt die start op 1 december om beginuur
# de duur van de timer noem je timer_duur
# het tijdstip waarop de timer start, noem je begintijdstip
begindatum = 1
begintijdstip = 21
timer_duur = 537
einddatum = begindatum + (begintijdstip + timer_duur) // 24
eindtijdstip = (begintijdstip + timer_duur) % 24
print(einddatum, eindtijdstip)
