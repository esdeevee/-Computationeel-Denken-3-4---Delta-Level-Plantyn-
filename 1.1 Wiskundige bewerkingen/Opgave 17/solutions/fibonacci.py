n = eval(input("Geef een natuurlijk getal: "))

som = 0
a = 1
b = 1
#print(a)
#print(b)

while True:
  c = a+b
  if c < n:
    a = b
    b = c
    # print(c)
    if(c%2 == 0):
      som = som + c
  else:
    break

print(som)





from random import randint

def fibonacci(n):
  som = 0
  a = 1
  b = 1
  #print(a)
  #print(b)

  while True:
    c = a+b
    if c < n:
      a = b
      b = c
      # print(c)
      if(c%2 == 0):
        som = som + c
    else:
      break

  return(som)

# print(fibonacci(80))

for i in range(10):
  n = randint(1000,1000000)
  print(n, fibonacci(n))


