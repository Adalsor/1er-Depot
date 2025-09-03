import random

def generate_random_array(debug=False, N=21):
    """Renvoie un tableau contenant toutes les valeurs entières de 0 (inclus)
    à N (exclus) rangées dans un ordre aléatoire

    Args:
        debug (boolean): quand debug est vrai, la fonction renvoie toujours le
                         même tableau afin de simplifier le débogage de vos
                         algorithmes de tri
        N (int): la taille du tableau à renvoyer

    Returns:
        list[int]: un tableau d'entiers, de taille N, non ordonné
    """

    if debug:
        return [3, 9, 7, 1, 6, 2, 8, 4, 5, 0]

    array = list(range(0, N))
    random.shuffle(array)

    return array


# ----------------
# Fonctions d'aide
# ----------------
def swap(tab, i, j):
    tab[i], tab[j] = tab[j], tab[i]
    """Échange la place des éléments aux indices i et j du tableau"""


# ---------------
# Tris classiques
# ---------------
def bubble_sort(A):
    """Trie le tableau en déplaçant les plus grosses valeurs vers la fin du
        tableau, un peu comme des bulles dans l'eau qui remonteraient à la
        surface"""
    for i in range(len(A), 1, -1):
        for j in range(0, i-1):
            if A[j+1] < A[j]:
                A[j], A[j+1] = A[j+1], A[j]


def insertion_sort(A):
    """Trie le tableau en plaçant l'élément courant à la bonne place dans
    le sous-tableau déjà trié"""
    n = len(A)
    for i in range(1, n):
        x = A[i]
        j = i
        while j > 0 and A[j - 1] > x:
            A[j] = A[j - 1]
            j -= 1
        A[j] = x


def selection_sort(A):
    """Trie le tableau en cherchant le plus petit élément à mettre dans la
    première case, puis le second plus petit à mettre dans la seconde case,
    etc"""
    n = len(A)
    for i in range(n - 2):
        min = i
        for j in range(i + 1, n):
            if A[j] < A[min]:
                min = j
        if min != i:
            A[i], A[min] = A[min], A[i]


# --------------
# Tris récursifs
# --------------
def merge_sort(tab):
    """Trie le tableau via le principe de « diviser pour mieux régner »
    avec l'intelligence du tri qui se trouve au moment de la fusion"""
    """Retourne le tableau si sa longueur est égal à 1."""
    if len(tab) <= 1:
        return tab

    """Divise le tableau en 2, la première moitié à gauche et la deuxième moitié à droite."""
    milieu = len(tab) / 2
    gauche = tab[:int(milieu)]
    droite = tab[int(milieu):]

    """Appel la fonction jusqu'à ce qu'elle retourne queulque chose. Ici elle retorunera le tableau lorsque sa longueur sera égal à 1.
    On a donc une valeur du tableau de gauche dans gauche_triee et idem pour la droite."""
    gauche_triee = merge_sort(gauche)
    droite_triee = merge_sort(droite)

    """Retourne nos resultats triée grace à la 2ème fonction."""
    return merge_sort_r(tab, gauche_triee, droite_triee)


def merge_sort_r(tab, start, end):
    resultat = []

    """On compare la longueur des 2 tableaux, si les 2 ont une longueur supérieur à 0, on ajoute le plus petit premier élements des 2 listes."""
    while len(start) > 0 and len(end) > 0:
        if start[0] <= end[0]:
            resultat.append(start[0])
            start = start[1:]
        else:
            resultat.append(end[0])
            end = end[1:]

    """On ajoute tout les élements restants dans la liste"""
    while len(start) > 0:
        resultat.append(start[0])
        start = start[1:]

    """On ajoute tout les élements restants dans la liste"""
    while len(end) > 0:
        resultat.append(end[0])
        end = end[1:]

    return resultat


def quick_sort(tab, first, last):
    """Divise le tableau en deux, trie chacune des sous-parties et fusionne
    intelligemment les deux sous-parties triées"""
    if first < last:
        index = partition(tab, first, last)
        quick_sort(tab, first, index - 1)
        quick_sort(tab, index + 1, last)

    return tab

def partition(tab, first, last):

    pivot = tab[last]

    index_frontiere = first - 1

    for j in range(first, last):
        if tab[j] <= pivot:
            index_frontiere += 1
            tab[index_frontiere], tab[j] = tab[j], tab[index_frontiere]

    tab[index_frontiere + 1], tab[last] = tab[last], tab[index_frontiere + 1]

    return index_frontiere + 1
