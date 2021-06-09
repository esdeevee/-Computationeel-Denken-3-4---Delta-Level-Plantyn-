from math import sqrt

n = eval(input("Geef een natuurlijk getal: "))
grootste = 1

#for i in range(2, int(sqrt(n))+1):
for i in range(2, n):
    while(n%i == 0):
        n = n/i
        #print(i)
        grootste = i

print("De grootste priemfactor van dit getal is", grootste)
if(grootste == 1):
    print(n, "is dus een priemgetal!")
else:
    print(n, "is dus geen priemgetal.")
