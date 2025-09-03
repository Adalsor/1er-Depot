def filiaire(signaux, fils, start, end, q):
    liste_result = []
    for f in fils:
        print(q, "/", start, end, "/", f[0], f[1])
        if start == f[0]:
            liste_result.append((signaux[f[0]], signaux[f[1]]))
        if end != f[1]:
            start = f[1]
        else:
            break

    result = liste_result[0][0] * liste_result[0][1]
    for r in range(1, len(liste_result)):
        result *= liste_result[r][1]

    return result

def pour1(signaux, fils, start, end, liste_result2):
    liste_result2.append(("", ""))
    for f in fils:
        if start == f[0] and end == f[1]:
            liste_result2.pop(-1)
            liste_result2.append((signaux[f[0]], signaux[f[1]]))
        elif end == f[0] and start == f[1]:
            liste_result2.pop(-1)
            liste_result2.append((signaux[f[1]], signaux[f[0]]))

    return liste_result2

def coffre_fort(signaux, fils, questions):
    final = []
    liste_result2 = []

    for q in questions:
        start = q[0]
        end = q[1]

        liste_result2 = pour1(signaux, fils, start, end, liste_result2)
        result = filiaire(signaux, fils, start, end, q)

        final.append(result)

    for l in liste_result2:
        if l[0] != "":
            a = l[0] * l[1]
            b = liste_result2.index(l)
            final[b] = a

    print(final)
    return final

liste1 = [4, 9, 7, 2, 3, 0]
liste2 = [(0, 1), (1, 3), (1, 2), (2, 4), (4, 5)]
liste3 = [(0, 3), (1, 3), (0, 4), (0, 5), (1, 2)]
liste4 = [1671404010, 1671404009, 1371404010, 1, 3, 8, 2, 7, 10, 4, 0, 6]
liste5 = [(0, 1), (2, 0), (3,2), (3, 4), (9, 3), (5, 3), (7, 5), (5, 6), (8, 4), (9, 10), (11, 10)]
liste6 = [(1, 8), (7, 7), (6, 8), (9, 7), (2, 10)]
coffre_fort(liste1, liste2, liste3)
coffre_fort(liste4, liste5, liste6)







