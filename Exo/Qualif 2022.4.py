def keylogger(taille_mdp, chaine):
    a = 0
    lower = False
    upper = False
    digit = False
    ponctuation = False
    while len(chaine) > taille_mdp - 1:
        for i in chaine[:taille_mdp]:
            if i.islower():
                lower = True
            if i.isupper():
                upper = True
            if i.isdigit():
                digit = True
            if i in "\"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
                ponctuation = True
        if lower == True and upper == True and digit == True and ponctuation == True:
            print(chaine[:taille_mdp],"-> Valide")
            a += 1
            lower = False
            upper = False
            digit = False
            ponctuation = False
        else:
            print(chaine[:taille_mdp],"-> Invalide")
            lower = False
            upper = False
            digit = False
            ponctuation = False
        chaine = chaine.replace(chaine, chaine[1:])
    print(a)
    return a


keylogger(6, "G=d:Dl:T=9NS1c$9qC%,^EdUVLnU-7")
