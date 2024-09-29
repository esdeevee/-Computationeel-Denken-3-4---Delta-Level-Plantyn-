from math import ceil
aantal_bakken = int(input('Geef het aantal bestelde bakken water: '))
aantal_palletten = ceil(aantal_bakken / 48)
aantal_vrachtwagens = aantal_palletten // 20
aantal_palletten_niet_in_vrachtwagen = aantal_palletten % 20
aantal_bestelwagens = ceil(aantal_palletten_niet_in_vrachtwagen / 8)
aantal_palletten_bestelwagen = aantal_palletten_niet_in_vrachtwagen % 8
aantal_bakken_op_halfvolle_pallet = aantal_bakken % 48

print(aantal_palletten)
print(aantal_vrachtwagens)
print(aantal_palletten_niet_in_vrachtwagen)
print(aantal_bestelwagens)
print(aantal_palletten_bestelwagen)
print(aantal_bakken_op_halfvolle_pallet)
