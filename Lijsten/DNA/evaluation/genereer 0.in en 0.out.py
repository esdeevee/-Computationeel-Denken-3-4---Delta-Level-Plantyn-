from random import randint

def DNA(lijst1, lijst2):
    
    for i in range(len(lijst1) - len(lijst2) +1 ):
        resultaat = True
        for j in range(len(lijst2)):
            #print(i, j, lijst1[i+j], lijst2[j])
            if lijst1[i+j] != lijst2[j]:
                resultaat = resultaat and False
        if resultaat:
            return (True, i)
        #print('\n')
    return False  


        


# wis alle gegevens in in.csv
file = open("0.in", "w")
file.truncate()
file.close()
# wis alle gegevens in in.csv
file = open("0.out", "w")
file.truncate()
file.close()

def genereer_streng(lengte_DNA):
    DNA = []
    for i in range(lengte_DNA):
        toss = randint(1, 4)
        if toss == 1:
            DNA.append('A')
        elif toss == 2:
            DNA.append('C')
        elif toss == 3:
            DNA.append('G')
        else:
            DNA.append('T')
    return DNA

for i in range(10):
    for j in range(10):
        lengte_DNA = randint(10 + i*5, 15 + i*5)
        lijst1 = genereer_streng(lengte_DNA)
        lengte_gen = randint(3, int(lengte_DNA/2))
        toss = randint(1,2)
        if toss == 1:
            lijst2 = genereer_streng(lengte_gen)
        else:
            lengte_gen = randint(2, lengte_DNA-5)
            begin = randint(0, lengte_DNA - lengte_gen - 1)
            lijst2 = lijst1[begin : begin+lengte_gen]
        #print(lijst1, lijst2, DNA(lijst1,lijst2))
        with open('0.in', 'a') as file:
            file.write('>>> DNA(' + str(lijst1) + ', ' + str(lijst2) + ')')
            file.write('\n')
            file.write(str(DNA(lijst1, lijst2)))
            file.write('\n')

