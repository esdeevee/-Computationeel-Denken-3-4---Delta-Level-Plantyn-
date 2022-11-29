# lees 2 woorden in
woord_1 = input('Geef een eerste woord: ')
woord_2 = input('Geef een tweede woord: ')

# definieer een variabele waarin je de gemeenschappelijke letters bewaart en uiteindelijk ook toont
# als datatype kies je een string
# bij het begin van het programma moet deze string leeg zijn 
uitvoer = ''

# itereer over elke letter in het eerste ingelezen woord
for letter in woord_1:
    # controleer of de letter ook in het tweede woord zit en de letter nog niet bewaard werd  
    if letter in woord_2 and not letter in uitvoer:
        uitvoer = uitvoer + letter
        
if(uitvoer == ''):
    # als er geen enkele letter gemeenschappelijk is, toon je dat
    print('De woorden', woord_1, 'en', woord_2, 'hebben geen enkele letter gemeenschappelijk.')
else:
    # als er minstens 1 gemeenschappelijke letter is, toon je dat
    print('De woorden', woord_1, 'en', woord_2, 'hebben volgende letter(s) gemeenschappelijk:', uitvoer)
