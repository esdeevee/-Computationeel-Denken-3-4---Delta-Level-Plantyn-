# dit programma vraagt een bedrag
# berekent het aantal biljetten van 50, 20, 10 en 5 euro en het aantal munten van 2 en 1 euro om dit bedrag te betalen met zo weinig mogelijk biljetten en munten
# de aantallen worden op een lijn uitgevoerd in de volgorde 50, 20, 10, 5, 2, 1 euro
bedrag = int(input('Geef een bedrag (in euro): '))
aantal_50 = bedrag // 50
bedrag = bedrag % 50        # de nieuwe waarde van bedrag is gelijk aan het bedrag dat je niet met biljetten van 50 kan betalen
aantal_20 = bedrag // 20
bedrag = bedrag % 20        # de nieuwe waarde van bedrag is gelijk aan het bedrag dat je niet met biljetten van 50 en 20 kan betalen
aantal_10 = bedrag // 10
bedrag = bedrag % 10        # de nieuwe waarde van bedrag is gelijk aan het bedrag dat je niet met biljetten van 50, 20 en 10 kan betalen
aantal_5 = bedrag // 5
bedrag = bedrag % 5         # de nieuwe waarde van bedrag is gelijk aan het bedrag dat je niet met biljetten van 50, 20, 10 en 5 kan betalen
aantal_2 = bedrag // 2
bedrag = bedrag % 2         # de nieuwe waarde van bedrag is gelijk aan het bedrag dat je niet met biljetten van 50, 20, 10, 5 en munten van 2 kan betalen
aantal_1 = bedrag           # het bedrag dat nu overblijft, moet met munten van 1 euro betaald worden
print(aantal_50, aantal_20, aantal_10, aantal_5, aantal_2, aantal_1)
