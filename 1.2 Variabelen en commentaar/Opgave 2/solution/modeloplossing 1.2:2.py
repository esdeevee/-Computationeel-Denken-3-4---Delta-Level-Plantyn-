# maak een variabele voor elk van de bedragen
beginbedrag = 213
nieuwjaar = 100
zakgeld = 20
verjaardag = 50
broodje = 3
drankje = 1.5
aantal_maanden = 12
aantal_weken = 52
# bereken en toon het eindbedrag
eindbedrag = beginbedrag + nieuwjaar + verjaardag + aantal_maanden * zakgeld - aantal_weken * broodje - aantal_weken * 0.5 * drankje
print(eindbedrag)
