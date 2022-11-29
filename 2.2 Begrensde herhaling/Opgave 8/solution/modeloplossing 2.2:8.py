# lees een woord in
woord = input('Geef een woord (allemaal kleine letters): ')
# initialiseer twee numerieke variabelen:
aantal_klinkers = 0
aantal_medeklinkers = 0
# maak een string met alle mogelijke klinkers:
klinkers = 'aeiou'
# herhaal voor elke letter in het woord
for letter in woord:
    # controleer of letter een klinker is
    if letter in klinkers:
    # zo ja, verhoog dan de waarde van aantal_klinkers met 1
        aantal_klinkers = aantal_klinkers + 1
    # letter is geen klinker, dus het is een medeklinker
    else:
        # verhoog de waarde van aantal_medeklinkers met 1
        aantal_medeklinkers = aantal_medeklinkers + 1
# print de uitvoer
print(woord, 'heeft', aantal_klinkers, 'klinkers en', aantal_medeklinkers, 'medeklinkers')
