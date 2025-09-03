def puzzle(n_cote, couleurs, piece):
    a = ""
    b = 0
    for i in range(len(piece)):
        if piece[i][0] == n_cote:
            if piece[i][1] != couleurs:
                a += "O"
                b += 1
            else:
                a += "X"
        else:
            a += "X"
    print(a)
    print(b)
    return a, "\n", b

d = [(5, "blue"), (8, "pink"), (3, "pink"), (6, "blue"), (3, "green"), (5, "pink"), (5, "yellow")]
liste_c = ["blue", "red", "yellow"]

puzzle(3, liste_c, d)


