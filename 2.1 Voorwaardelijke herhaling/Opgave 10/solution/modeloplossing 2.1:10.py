# lees de afstand in
afstand = float(input('Geef een afstand in km: '))

# bereken de prijzen voor beide tickets
standaardprijs = 1.5 + 0.15 * afstand
jongerenprijs = 7

# controleer of de standaardprijs de laagste prijs is
if standaardprijs == min(standaardprijs, jongerenprijs):
    print('standaard ticket')
    print(standaardprijs)
else:
    print('jongerenticket')
    print(jongerenprijs)
