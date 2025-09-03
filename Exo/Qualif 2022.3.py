def jesaispascommentfaire(nombre, liste):
    i = 0
    liste_somme_liste = []
    while i < len(liste):
        liste_intermediaire = []
        i += 1
        for l in liste:
            liste_intermediaire.append(l)
        liste_somme_liste.append(sum(liste_intermediaire))
    print(liste_somme_liste)


nombre_magique = 105
liste_code = [1, 2, 3, 4, 5]
jesaispascommentfaire(nombre_magique, liste_code)