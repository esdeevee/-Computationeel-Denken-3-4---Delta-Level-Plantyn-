from random import randint

def eendjes_vissen(lijst, aantal):
    maximum = 0
    positie = 0
    for i in range(len(lijst)):
        som = 0
        for j in range(aantal):
            som += lijst[(i + j) % len(lijst)]
        if som > maximum:
            maximum = som
            positie = i
    return (positie, maximum)



# wis alle gegevens in in.csv
file = open("0.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("0.out", "w")
file.truncate()
file.close()

for i in range(1, 11):
    for k in range(10):  
        lijst = []
        for j in range(5*i):
            eendje = randint(1,10)
            lijst.append(eendje)
        aantal = randint(2, 5*i - 2)
        with open('0.in', 'a') as file:
            file.write('>>> eendjes_vissen(' + str(lijst) + ', ' + str(aantal) + ')')
            file.write('\n')
            file.write(str(eendjes_vissen(lijst, aantal)))
            file.write('\n')

