# lees de tekst in
tekst = input('Geef een stuk tekst: ')

# begin het aantal klinkers te tellen vanaf nul
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
print(aantal_klinkers)
