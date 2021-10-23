# dit programma vraagt een tijdstip en een aantal uur
# het berekent de hoek tussen de grote en de kleine wijzer van een klok nadat deze op tijdstip beginuur aantal_uur wordt doorgedraaid
begintijdstip = int(input('Geef het tijdstip waarop de klok wordt verder gedraaid: '))
aantal_uur = int(input('Geef het aantal uur waarop de klok wordt verder gedraaid: '))
eindtijdstip = (begintijdstip + aantal_uur) % 12
hoek = min(eindtijdstip * 30, 360 - eindtijdstip * 30)
print(hoek)
