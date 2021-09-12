from lorem_text import lorem
from random import randint

def aantal_klinkers(tekst):
    # we beginnen het aantal klinkers te tellen vanaf nul
    aantal_klinkers = 0

    # controleer of de letter a (kleine letter of hoofdletter) voorkomt
    if 'a' in tekst or 'A' in tekst:
        # verhoog de waarde van aantal_klinkers met 1
        aantal_klinkers = aantal_klinkers + 1
    # doe nu hetzelfde voor de andere klinkers
    if 'e' in tekst or 'E' in tekst:
        aantal_klinkers = aantal_klinkers + 1
    if 'i' in tekst or 'I' in tekst:
        aantal_klinkers = aantal_klinkers + 1
    if 'o' in tekst or 'O' in tekst:
        aantal_klinkers = aantal_klinkers + 1
    if 'u' in tekst or 'U' in tekst:
        aantal_klinkers = aantal_klinkers + 1 

    # schrijf het aantal klinkers uit
    return(aantal_klinkers)

# wis alle gegevens in in.csv
f = open("0.in", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("0.out", "w")
f.truncate()
f.close()

for i in range(20):
  aantal_woorden = randint(1,3)
  tekst = lorem.words(aantal_woorden)
  with open('0.in', 'a') as f:
    f.write(tekst)
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(str(aantal_klinkers(tekst)))
    g.write("\n")

for i in range(20):
  aantal_woorden = randint(3,5)
  tekst = lorem.words(aantal_woorden)
  with open('0.in', 'a') as f:
    f.write(tekst)
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(str(aantal_klinkers(tekst)))
    g.write("\n")

for i in range(20):
  aantal_woorden = randint(5,8)
  tekst = lorem.words(aantal_woorden)
  with open('0.in', 'a') as f:
    f.write(tekst)
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(str(aantal_klinkers(tekst)))
    g.write("\n")

for i in range(20):
  aantal_woorden = randint(1,10)
  tekst = lorem.words(aantal_woorden)
  with open('0.in', 'a') as f:
    f.write(tekst)
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(str(aantal_klinkers(tekst)))
    g.write("\n")

for i in range(20):
  tekst = lorem.sentence()
  with open('0.in', 'a') as f:
    f.write(tekst)
    f.write("\n")
  with open('0.out', 'a') as g:
    g.write(str(aantal_klinkers(tekst)))
    g.write("\n")
