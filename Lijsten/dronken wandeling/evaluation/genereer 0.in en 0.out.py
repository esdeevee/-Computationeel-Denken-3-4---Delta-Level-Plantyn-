from random import randint

def dronken_wandeling(lijst):
    x = 0
    y = 0
    for stap in lijst:
        if stap == 'N':
            y += 1
        elif stap == 'Z':
            y -= 1
        elif stap == 'O':
            x += 1
        elif stap == 'W':
            x -= 1
    return ((x,y), len(lijst))




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
        aantal_stappen = randint(5, 10*i)
        lijst = []
        for j in range(aantal_stappen):
            stap = randint(1,4)
            if stap == 1:
                lijst.append('N')
            if stap == 2:
                lijst.append('Z')
            elif stap == 3:
                lijst.append('O')
            elif stap == 4:
                lijst.append('W')
                
        with open('0.in', 'a') as file:
            file.write('>>> dronken_wandeling(' + str(lijst) + ')')
            file.write('\n')
            file.write(str(dronken_wandeling(lijst)))
            file.write('\n')

