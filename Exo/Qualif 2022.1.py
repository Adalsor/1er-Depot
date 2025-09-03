def frequence(liste):
    liste1 = []
    for i in liste:
        if i % 3 == 0:
            liste1.append(i)

    print(min(liste1))
    return min(liste1)

freq = [138, 13, 25, 333, 28]
frequence(freq)