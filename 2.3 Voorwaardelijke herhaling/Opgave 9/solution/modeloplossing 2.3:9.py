# lees een getal in
getal = int(input("Geef een natuurlijk getal: "))

# noem n het aantal cijfers van dit getal
n = len(str(getal))

# i neemt achtereenvolgens de waarden 1, 2, 3, ... aan
# stop pas als het kwadraat van i eindigt op getal
i = 1

# blijf herhalen
while True:
    # bereken het kwadraat van i
    kwadraat = i**2
    # controleer of het kwadraat van i eindigt op getal
    if kwadraat % 10 ** n == getal:
        # je hebt het gezochte getal gevonden
        # toon de uitvoer
        print(i, "*", i, "=", kwadraat)
        # onderbreek de while-lus
        break
    else:
        # het gezochte getal werd nog niet gevonden: onderzoek het volgende natuurlijk getal
        i = i + 1
