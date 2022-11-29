# lees het wachtwoord in
wachtwoord = input('Geef het wachtwoord: ')

# controleer of het wachtwoord lang genoeg is
voorwaarde_1 = len(wachtwoord) >= 12

# controleer of er een cijfer in het wachtwoord zit
voorwaarde_2 = '0' in wachtwoord or '1' in wachtwoord or '2' in wachtwoord or '3' in wachtwoord or '4' in wachtwoord or '5' in wachtwoord or '6' in wachtwoord or '7' in wachtwoord or '8' in wachtwoord or '9' in wachtwoord

# controleer of er een %, !, ? in het wachtwoord zit
voorwaarde_3 = '%' in wachtwoord or '!' in wachtwoord or '?' in wachtwoord

# controleer of er voldaan is aan alle drie de voorwaarden
voorwaarde = voorwaarde_1 and voorwaarde_2 and voorwaarde_3

if voorwaarde:
    print('veilig')
else:
    print('onveilig')
