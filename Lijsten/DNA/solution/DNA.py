def DNA(lijst1, lijst2):
    for i in range(len(lijst1) - len(lijst2) +1 ):
        resultaat = True
        for j in range(len(lijst2)):
            if lijst1[i+j] != lijst2[j]:
                resultaat = resultaat and False
        if resultaat:
            return (True, i)
    return False 
