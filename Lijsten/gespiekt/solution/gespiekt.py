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
        
