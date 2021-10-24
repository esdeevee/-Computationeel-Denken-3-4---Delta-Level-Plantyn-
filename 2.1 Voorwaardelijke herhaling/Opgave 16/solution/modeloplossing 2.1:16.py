# lees een jaartal in
jaar = int(input('Geef een jaartal: '))

# als een jaartal deelbaar is door 400, is het altijd een schrikkeljaar (bv. 1600, 2000)
if jaar % 400 == 0:
    print(jaar, 'is een schrikkeljaar.')
    
# als een jaartal niet deelbaar is door 400, maar wel door 100, is het nooit een schrikkeljaar (bv. 1900, 2300)
elif jaar % 100 == 0:
    print(jaar, 'is geen schrikkeljaar.')
    
# als een jaartal niet deelbaar is door 100, maar wel door 4, is het altijd een schrikkeljaar (bv. 1988, 2020)
elif jaar % 4 == 0:
    print(jaar, 'is een schrikkeljaar.')
    
# als een jaartal niet deelbaar is door 4, is het nooit een schrikkeljaar (bv. 1987, 2021)
else:
    print(jaar, 'is geen schrikkeljaar.')
