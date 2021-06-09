woord_1 = input("Geef een eerste woord: ")
woord_2 = input("Geef een tweede woord: ")

uitvoer = ""

for letter in woord_1:
    if letter in woord_2 and uitvoer == "":
        uitvoer = uitvoer + letter
    elif letter in woord_2 and not(letter in uitvoer):
        uitvoer = uitvoer + ", " + letter
    
if(uitvoer == ""):
    print("De woorden \"" + woord_1 + "\" en \"" + woord_2 + "\" hebben geen enkele letter gemeenschappelijk.")
else:
    print("De woorden \"" + woord_1 + "\" en \"" + woord_2 + "\" hebben de volgende letters gemeenschappelijk:", uitvoer)




def gemeenschappelijke_letters(woord_1, woord_2):
  uitvoer = ""
  for letter in woord_1:
    if letter in woord_2 and uitvoer == "":
      uitvoer = uitvoer + letter
    elif letter in woord_2 and not(letter in uitvoer):
      uitvoer = uitvoer + ", " + letter
  return(uitvoer)

woordenlijst = ["opgebouwd", "grammaticale", "verfijnd", "fractievoorzitter",
"voel", "ingevulde", "chirurg", "afbeeldingen", "datum", "lichtjes",
"verleidingen", "koninklijke", "omver", "antwoordde", "dragen",
"waarmee", "aanhangers", "gepubliceerde", "bondgenoten", "campus"]

for i in range(int(len(woordenlijst)/2)):
  if(gemeenschappelijke_letters(woordenlijst[2*i], woordenlijst[2*i+1]) == ""):
    print("De woorden \"" + woordenlijst[2*i] + " \"en \"", woordenlijst[2*i+1] + "\" hebben geen enkele letter gemeenschappelijk.")  
  else:
    print("De woorden \"" + woordenlijst[2*i] + "\" en \"", woordenlijst[2*i+1] + "\" hebben de volgende letters gemeenschappelijk:", gemeenschappelijke_letters(woordenlijst[2*i], woordenlijst[2*i+1]))
