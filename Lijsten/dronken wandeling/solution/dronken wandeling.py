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
