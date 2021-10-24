# lees het bedrag in dat je wilt afhalen
bedrag = int(input('Geef een bedrag in euro: '))

# bereken de kosten
kosten_A = 2 + 0.02 * bedrag
kosten_B = 0.05 * bedrag
kosten_C = 5

# controleer welke van de kosten de laagste is
if kosten_A == min(kosten_A, kosten_B, kosten_C):
    print('A')
    print(bedrag + kosten_A)
elif kosten_B == min(kosten_A, kosten_B, kosten_C):
    print('B')
    print(bedrag + kosten_B)
else:
    print('C')
    print(bedrag + kosten_C)
