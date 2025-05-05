from random import randint

def gespiekt(lijst):
    aantal = 0
    for i in range(len(lijst) - 1):
        if lijst[i] - lijst[i+1] == 0:
            print(i+1, 'en', i+2, 'zijn erg verdacht.')
            aantal +=1
        elif abs(lijst[i] - lijst[i+1]) <= 5:
            print(i+1, 'en', i+2, 'zijn verdacht.')
            aantal +=1
    if aantal == 0:
        print('Er waren geen verdachte situaties.')
        
def gespiekt_write(lijst):
    aantal = 0
    uitvoer = ''
    for i in range(len(lijst) - 1):
        if lijst[i] - lijst[i+1] == 0:
            uitvoer += str(i+1) + ' en ' + str(i+2) + ' zijn erg verdacht.\n'
            aantal +=1
        elif abs(lijst[i] - lijst[i+1]) <= 5:
            uitvoer += str(i+1) + ' en ' + str(i+2) + ' zijn verdacht.\n'
            aantal +=1
    if aantal == 0:
        uitvoer = 'Er waren geen verdachte situaties.\n'
    return uitvoer


# wis alle gegevens in in.csv
file = open("0.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("0.out", "w")
file.truncate()
file.close()

for i in range(1, 5):
    for k in range(25):  
        lijst = []
        aantal = randint(2, 3*i + 1)
        for j in range(aantal):
            toss = randint(1, 5)
            if toss == 1:
                resultaat1 = randint(0,100)
                resultaat2 = resultaat1
                lijst.append(resultaat1)
                lijst.append(resultaat2)
            elif toss == 2:
                resultaat1 = randint(0,100)
                lijst.append(resultaat1)
                resultaat2 = abs(resultaat1 + randint(-5, 5))
                lijst.append(resultaat2)
            else:
                resultaat1 = randint(0,100)
                lijst.append(resultaat1)
                resultaat2 = randint(0,100)
                lijst.append(resultaat2)
        #print(lijst)
                
        
        with open('0.in', 'a') as file:
            file.write('>>> gespiekt(' + str(lijst) + ')')
            file.write('\n')
            file.write(str(gespiekt_write(lijst)))
            file.write('\n')
        with open('0.out', 'a') as file:
            file.write('---------------------------------------------')
            file.write('\n')
            file.write('used output channel: stdout')
            file.write('\n')
        
        
