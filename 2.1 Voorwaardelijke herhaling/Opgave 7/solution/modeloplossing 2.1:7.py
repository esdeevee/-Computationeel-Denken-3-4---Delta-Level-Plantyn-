# lees de lengte in
l = float(input("Geef je lengte (in m): "))
# lees de massa in
m = float(input("Geef je massa (in kg): "))
# bereken de BMI, maar toon deze nog niet
BMI = m / l**2
if(BMI < 18.5):
    print(round(BMI, 1), 'ondergewicht')
elif(18.5 <= BMI < 25):
    print(round(BMI, 1), 'gezond gewicht')
elif(25 <= BMI < 30):
    print(round(BMI, 1), 'overgewicht')
else:
    print(round(BMI, 1), 'obesitas')
