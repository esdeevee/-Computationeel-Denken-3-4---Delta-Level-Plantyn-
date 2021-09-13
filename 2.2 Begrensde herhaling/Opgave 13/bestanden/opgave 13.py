import dutch_words
words = dutch_words.get_ranked()
from random import randint

def gemeenschappelijke_letters(woord_1,woord_2):
    # maak een variabele waarin we de gemeenschappelijke letters bewaren
    # als datatype kiezen we een string
    # bij het begin van het programma moet deze string leeg zijn 
    uitvoer = ''
    # itereer over elke letter in het eerste ingelezen woord
    for letter in woord_1:
        # controleer of de letter ook in het tweede woord zit en we de letter nog niet bewaard hebben  
        if letter in woord_2 and not letter in uitvoer:
            uitvoer = uitvoer + letter
    if(uitvoer == ''):
        # als er geen enkele letter gemeenschappelijk is, tonen we dat
        output = 'De woorden ' + woord_1 + ' en ' + woord_2 + ' hebben geen enkele letter gemeenschappelijk.'
    else:
        # als er minstens 1 gemeenschappelijke letter is, tonen we dat 
        output = 'De woorden ' + woord_1 + ' en ' + woord_2 + ' hebben volgende letter(s) gemeenschappelijk: ' + uitvoer
    return(output)

# wis alle gegevens in in.csv
f = open("0.in", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("0.out", "w")
f.truncate()
f.close()



for i in range(100):
  n = randint(1,len(words))
  woord1 = words[n]
  n = randint(1,len(words))
  woord2 = words[n]
  with open('0.in', 'a') as f:
    f.write(woord1)
    f.write("\n")
    f.write(woord2)
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(gemeenschappelijke_letters(woord1,woord2))
    g.write("\n")
