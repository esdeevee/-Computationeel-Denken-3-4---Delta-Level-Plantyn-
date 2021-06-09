def aantaldagen(jaar, maand):
  lijst_31 = ["januari", "maart", "mei", "juli", "augustus", "oktober", "december"]
  lijst_30 = ["april", "juni", "september", "november"]
  if(maand in lijst_31):
    aantal_dagen = 31
  elif(maand in lijst_30):
    aantal_dagen = 30
  elif(maand == "februari"):
    if jaar % 400 == 0:
      aantal_dagen = 29
    elif jaar % 100 == 0:
      aantal_dagen = 28
    elif jaar % 4 == 0:
      aantal_dagen = 29
    else:
      aantal_dagen = 28
  return(aantal_dagen)

jaar = eval(input("Geef een jaartal: "))
maand = input("Geef een maand: ")
print(maand, jaar, "heeft", aantaldagen(jaar, maand), "dagen")






from random import randint
import csv
#import StringIO

def aantaldagen(jaar, maand):
  lijst_31 = ["januari", "maart", "mei", "juli", "augustus", "oktober", "december"]
  lijst_30 = ["april", "juni", "september", "november"]
  if(maand in lijst_31):
    aantal_dagen = 31
  elif(maand in lijst_30):
    aantal_dagen = 30
  elif(maand == "februari"):
    if jaar % 400 == 0:
      aantal_dagen = 29
    elif jaar % 100 == 0:
      aantal_dagen = 28
    elif jaar % 4 == 0:
      aantal_dagen = 29
    else:
      aantal_dagen = 28
  return(aantal_dagen)

#jaar = eval(input("Geef een jaartal: "))
#maand = input("Geef een maand: ")
#print(maand, jaar, "heeft", aantaldagen(jaar, maand), "dagen")

maandlijst = []
jaarlijst = []

with open('in.csv', 'w') as f:
  for i in range(1000):
    jaar = randint(0, 10000)
    maand_getal = randint(1,12)
    if maand_getal == 1: maand = "januari"
    elif maand_getal == 2: maand = "februari"
    elif maand_getal == 3: maand = "maart"
    elif maand_getal == 4: maand = "april"  
    elif maand_getal == 5: maand = "mei"
    elif maand_getal == 6: maand = "juni"
    elif maand_getal == 7: maand = "juli" 
    elif maand_getal == 8: maand = "augustus"
    elif maand_getal == 9: maand = "september"
    elif maand_getal == 10: maand = "oktober"
    elif maand_getal == 11: maand = "november"
    elif maand_getal == 12: maand = "december"
    maandlijst.append(maand)
    f.write(maand)
    f.write("\n")
    jaarlijst.append(jaar)
    f.write(str(jaar))
    f.write("\n")

with open('out.csv', 'w') as f:
  for i in range(1000):
  #print(jaarlijst[i])
  #print(maandlijst[i])
    #uitvoer = ""
    uitvoer = maandlijst[i] + " " + str(jaarlijst[i]) + " " + "heeft" + " " + str(aantaldagen(jaarlijst[i], maandlijst[i])) + " " + "dagen"
    f.write(uitvoer)
    f.write("\n")
    #print(maandlijst[i], jaarlijst[i], "heeft", aantaldagen(jaarlijst[i], maandlijst[i]), "dagen")
    #f.write(maandlijst[i], jaarlijst[i], "heeft", aantaldagen(jaarlijst[i], maandlijst[i]), "dagen")
