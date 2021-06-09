n = eval(input("Geef een natuurlijk getal: "))

som = 0
for i in range(n):
    if(i% 3 == 0 or i%5 == 0): 
        # print(i)
        som = som + i
print(som)



from random import randint

def deelbaarsom(n):
  som = 0
  for i in range(n):
    if(i% 3 == 0 or i%5 == 0): 
      # print(i)
      som = som + i
  return(som)

#print(deelbaarsom(10))
#print("")

for i in range(10):
  n = randint(1000, 1000000)
  print(n)
  print(deelbaarsom(n))
