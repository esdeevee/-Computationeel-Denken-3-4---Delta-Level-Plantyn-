# lees een maand en een jaartal in
maand = input('Geef een maand: ')
jaar = int(input('Geef een jaartal: '))

# de maanden januari, maart, mei, juli, augustus, oktober en december hebben altijd 31 dagen
if maand == 'januari' or maand == 'maart' or maand == 'mei' or maand == 'juli' or maand == 'augustus' or maand == 'oktober' or maand =='december':
    print(maand, jaar, 'heeft 31 dagen.')

# de maanden april, juni, september en november hebben altijd 30 dagen
elif maand == 'april' or maand == 'juni' or maand == 'september' or maand == 'november':
    print(maand, jaar, 'heeft 30 dagen.')

# februari kan 28 of 29 dagen hebben: hier moet je dus weten of jaar een schrikkeljaar is
elif maand == 'februari':
    # als een jaartal deelbaar is door 400, is het altijd een schrikkeljaar (bv. 1600, 2000)
    if jaar % 400 == 0:
        # definieer de Booleaanse variabele schrikkeljaar, die True is wanneer jaar een schrikkeljaar is, en False wanneer dat niet het geval is
        schrikkeljaar = True
        
    # als een jaartal niet deelbaar is door 400, maar wel door 100, is het nooit een schrikkeljaar (bv. 1900, 2300)
    elif jaar % 100 == 0:
        schrikkeljaar = False
        
    # als een jaartal niet deelbaar is door 100, maar wel door 4, is het altijd een schrikkeljaar (bv. 1988, 2020)
    elif jaar % 4 == 0:
        schrikkeljaar = True
        
    # als een jaartal niet deelbaar is door 4, is het nooit een schrikkeljaar (bv. 1987, 2021)
    else:
        schrikkeljaar = False
        
    # controleer of jaar een schrikkeljaar is
    if schrikkeljaar:
        print(maand, jaar, 'heeft 29 dagen.')
    else:
        print(maand, jaar, 'heeft 28 dagen.')
