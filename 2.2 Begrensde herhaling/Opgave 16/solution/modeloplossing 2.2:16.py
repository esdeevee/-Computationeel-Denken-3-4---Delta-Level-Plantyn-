# zet de teller op nul voor de verschillende dagen
aantal_ma = 0
aantal_di = 0
aantal_wo = 0
aantal_do = 0
aantal_vr = 0
aantal_za = 0
aantal_zo = 0

# itereer over alle jaren tussen 2000 en 2099
for jaar in range(2000, 2100):    
    # de datum is 25/12
    maand = 12
    dag = 25

    # bereken d, het getal dat overeenkomt met de referentieweekdag
    j = jaar % 100
    if j % 2 == 1:
        j = j + 11
    j = j/2
    if j % 2 == 1:
        j = j + 11
    d = (72 - j) % 7

    # bereken het getal dat overeenkomt met de weekdag van 25/12/jaar
    weekdag = (d + (dag - 5)) % 7

    # houd de boekhouding bij
    if weekdag == 0:
        aantal_zo = aantal_zo + 1
    elif weekdag == 1:
        aantal_ma = aantal_ma + 1
    elif weekdag == 2:
        aantal_di = aantal_di + 1
    elif weekdag == 3:
        aantal_wo = aantal_wo + 1
    elif weekdag == 4:
        aantal_do = aantal_do + 1
    elif weekdag == 5:
        aantal_vr = aantal_vr + 1
    elif weekdag == 6:
        aantal_za = aantal_za + 1

# print de uitvoer
print('Aantal keer Kerstmis op maandag:', aantal_ma)
print('Aantal keer Kerstmis op dinsdag:', aantal_di)
print('Aantal keer Kerstmis op woensdag:', aantal_wo)
print('Aantal keer Kerstmis op donderdag:', aantal_do)
print('Aantal keer Kerstmis op vrijdag:', aantal_vr)
print('Aantal keer Kerstmis op zaterdag:', aantal_za)
print('Aantal keer Kerstmis op zondag:', aantal_zo)
