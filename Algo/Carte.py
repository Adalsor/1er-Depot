import pickle

with open(r"C:\Users\Adrien\Documents\Data\Algo\jeu_54cards.pkl", 'rb') as f:
    liste_a_trier = pickle.load(f)



def trier_carte(liste_carte):
    type = {'Carreau': [], 'Coeur': [], 'Pique': [], 'Trèfle': []}
    liste_total = []

    for carte in liste_carte:
        for key in type.keys():
            if key in carte:
                type[key].append(carte)

    for el in type.values():
        l = trier(el)
        for carte in l:
            liste_total.append(carte)

    return liste_total



def trier(liste_carte):
    liste = []
    liste_intermediaire=[]
    d = {"Valet": 11, "Dame": 12, "Roi": 13}

    for carte in liste_carte:
        value = carte.split(" ")[0]
        if value.isnumeric():
            liste_intermediaire.append(int(value))
        else:
            liste_intermediaire.append(d[value])

    for l in range(len(liste_intermediaire)):
        carte = liste_carte[mini(liste_intermediaire)[1]]
        liste.append(carte)
        liste_carte.remove(carte)
        liste_intermediaire.remove(mini(liste_intermediaire)[0])

    return liste



def mini(liste):
    min_i = 0
    x = liste[min_i]
    for i in range(len(liste)):
        if liste[i] < x:
            x = liste[i]
            min_i = i
    return (x, min_i)

print(trier_carte(liste_a_trier))