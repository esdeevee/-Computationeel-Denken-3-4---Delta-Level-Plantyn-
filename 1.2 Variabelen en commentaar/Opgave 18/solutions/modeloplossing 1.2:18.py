# dit programma berekent de hoek tussen de grote en de kleine wijzer van een klok nadat deze op tijdstip beginuur aantal_uur wordt doorgedraaid
beginuur = 13
aantal_uur = 2467
einduur = (beginuur + aantal_uur) % 12
hoek = min(einduur * 30, 360 - einduur * 30)
print(hoek)
