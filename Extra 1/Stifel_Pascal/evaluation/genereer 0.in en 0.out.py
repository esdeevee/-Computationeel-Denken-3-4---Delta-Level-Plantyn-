from random import randint

def Pascal(n, k):
    if n == k or k == 0:
        return 1
    else:
        return Pascal(n-1, k-1) + Pascal(n-1, k)

def som_Pascal(n):
    som = 0
    for k in range(n+1):
        som = som + Pascal(n, k)
    return som


# wis alle gegevens in in.csv
file = open("0.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("0.out", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("1.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("1.out", "w")
file.truncate()
file.close()


for i in range(50):
    with open('0.in', 'a') as file:
        n = randint(0, 25)
        k = randint(0, n)
        file.write('>>> Pascal(' + str(n) + ', ' + str(k) + ')')
        file.write('\n')

        file.write(str(Pascal(n, k)))
        file.write('\n')
        #file.write('\n')

for n in range(20):   
    with open('1.in', 'a') as file:
        file.write('>>> som_Pascal(' + str(n) + ')')
        file.write('\n')

        file.write(str(som_Pascal(n)))
        file.write('\n')
        #file.write('\n')
