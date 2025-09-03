class Pieces:
    def __init__(self, nom, couleur, attribution, debut):
        self.nom = nom
        self.couleur = couleur
        self.attribution = attribution
        self.debut = debut

    def replacer(self, row, col):
        for i in board:
            if self.nom in i:
                row_p = board.index(i)
                col_p = i.index(self.nom)
                board[row][col] = self.nom
                board[row_p][col_p] = vide
                afficher()
                return True

    def placer(self, row, col, row_p, col_p):
        board[row][col] = self.nom
        board[row_p][col_p] = vide
        afficher()
        self.debut += 1
        print(f"{self.nom} se deplace en [{row}][{col}]")

    def meme_couleur(self, row, col):
        if self.couleur == 'Blanc':
            for i in piece_blanche:
                if board[row][col] == i.nom:
                    print("Déplacement impossible")
                    return True
        if self.couleur == 'Noir':
            for i in piece_noire:
                if board[row][col] == i.nom:
                    print("Déplacement impossible")
                    return True

    def diff_couleur(self, row, col):
        for i in piece_blanche:
            if board[row][col] == i.nom:
                print("Déplacement impossible")
                return True
        for i in piece_noire:
            if board[row][col] == i.nom:
                print("Déplacement impossible")
                return True


class Pion(Pieces):

    def placer(self, row, col, row_p, col_p):
        board[row][col] = self.nom
        board[row_p][col_p] = vide
        if self.attribution == "pion":
            if row == 0 or row == 7:
                self.debut += 1
                self.changement_de_piece(row, col)
                return None
        afficher()
        self.debut += 1
        print(f"{self.nom} se deplace en [{row}][{col}]")

    def changement_de_piece(self, row, col):
        liste = ["dame", "tour", "fou", "cavalier"]
        print("Votre pion a atteint la dernière rangée !")
        print("Quel piece voulez-vous ? :")
        user = input("Dame Tour Fou Cavalier : ").lower()
        while user not in liste:
            user = input("Veuillez choisir entre Dame, Tour, Fou ou Cavalier : ").lower()

        if user == "dame":
            if self.couleur == "Blanc":
                reine2_b = Reine(" Reine2_b  ", "Blanc", "reine", self.debut)
                piece_blanche.append(reine2_b.nom)
                reine2_b.replacer(row, col)
            elif self.couleur == "Noir":
                reine2_n = Reine(" Reine2_n  ", "Noir", "reine", self.debut)
                piece_noire.append(reine2_n.nom)
                reine2_n.replacer(row, col)

        elif user == "tour":
            if self.couleur == "Blanc":
                tour3_b = Tour("  Tour3_b  ", "Blanc", "tour", self.debut)
                piece_blanche.append(tour3_b.nom)
                tour3_b.replacer(row, col)
            elif self.couleur == "Noir":
                tour3_n = Tour("  Tour3_n  ", "Noir", "tour", self.debut)
                piece_noire.append(tour3_n.nom)
                tour3_n.replacer(row, col)

        elif user == "fou":
            if self.couleur == "Blanc":
                fou3_b = Fou("  Fou3_b   ", "Blanc", "fou", self.debut)
                piece_blanche.append(fou3_b.nom)
                fou3_b.replacer(row, col)
            elif self.couleur == "Noir":
                fou3_n = Fou("  Fou3_n   ", "Noir", "fou", self.debut)
                piece_noire.append(fou3_n.nom)
                fou3_n.replacer(row, col)

        elif user == "cavalier":
            if self.couleur == "Blanc":
                cavalier3_b = Cavalier("Cavalier3_b", "Blanc", "cavalier", self.debut)
                piece_blanche.append(cavalier3_b.nom)
                cavalier3_b.replacer(row, col)
            elif self.couleur == "Noir":
                cavalier3_n = Cavalier("Cavalier3_n", "Noir", "cavalier", self.debut)
                piece_noire.append(cavalier3_n.nom)
                cavalier3_n.replacer(row, col)
        afficher()

    def se_deplacer(self, row, col):

        if self.meme_couleur(row, col):
            return False

        for i in board:
            if self.nom in i:
                row_p = board.index(i)
                col_p = i.index(self.nom)

                #Mange en passant

                if row == 2 and self.couleur == "Blanc" and col == col_p and row_p - row == 1:
                    for i in piece_noire:
                        if board[row_p][col_p + 1] == i.nom:
                            board[row][col] = self.nom
                            board[row_p][col_p] = vide
                            board[row_p][col_p + 1] = vide
                            self.debut += 1
                            afficher()
                            print(f"{self.nom} mange en passant et se deplace en[{row}][{col}]")
                            return True

                        elif board[row_p][col_p - 1] == i.nom:
                            board[row][col] = self.nom
                            board[row_p][col_p] = vide
                            board[row_p][col_p - 1] = vide
                            self.debut += 1
                            afficher()
                            print(f"{self.nom} mange en passant et se deplace en[{row}][{col}]")
                            return True

                if row == 5 and self.couleur == "Noir" and col == col_p and row - row_p == 1:
                    for i in piece_blanche:
                        if board[row_p][col_p + 1] == i.nom:
                            board[row][col] = self.nom
                            board[row_p][col_p] = vide
                            board[row_p][col_p + 1] = vide
                            self.debut += 1
                            afficher()
                            print(f"{self.nom} mange en passant et se deplace en[{row}][{col}]")
                            return True

                        elif board[row_p][col_p - 1] == i.nom:
                            board[row][col] = self.nom
                            board[row_p][col_p] = vide
                            board[row_p][col_p - 1] = vide
                            self.debut += 1
                            afficher()
                            print(f"{self.nom} mange en passant et se deplace en[{row}][{col}]")
                            return True

                #Deplacement de 2 case au début

                if self.couleur == "Blanc" and self.debut == 0 and row_p - row == 2 and col == col_p:
                    self.placer(row, col, row_p, col_p)
                    return True

                #Deplacement basique

                elif self.couleur == "Blanc" and row_p - row == 1:
                    for i in piece_noire:
                        if board[row][col] == i.nom:
                             if col_p - col == 1 or col_p - col == -1:
                                self.placer(row, col, row_p, col_p)
                                return True

                    if col == col_p:
                        for i in piece_noire:
                            if board[row][col] == i.nom:
                                print("Déplacement impossible")
                                return False

                        self.placer(row, col, row_p, col_p)
                        return True

                    else:
                        print("Déplacement impossible")
                        return False

                elif self.couleur == "Blanc":
                    print("Déplacement impossible")
                    return False

                #Deplacement des pions Noir

                if self.couleur == "Noir" and self.debut == 0 and row - row_p == 2 and col == col_p:
                    self.placer(row, col, row_p, col_p)
                    return True

                elif self.couleur == "Noir" and row - row_p == 1:
                    for i in piece_blanche:
                        if board[row][col] == i.nom:
                             if col_p - col == 1 or col_p - col == -1:
                                self.placer(row, col, row_p, col_p)
                                return True

                    if col == col_p:
                        for i in piece_blanche:
                            if board[row][col] == i.nom:
                                print("Déplacement impossible")
                                return False

                        self.placer(row, col, row_p, col_p)
                        return True

                    else:
                        print("Déplacement impossible")
                        return False

                elif self.couleur == "Noir":
                    print("Déplacement impossible")
                    return False


class Tour(Pieces):

    def se_deplacer(self, row, col):

        if self.meme_couleur(row, col):
            return False

        for i in board:
            if self.nom in i:
                row_p = board.index(i)
                col_p = i.index(self.nom)

                if row_p == row and col_p != col:
                    if col_p - col > 0:
                        z = col_p - col
                        for i in range(1, z):
                            if self.diff_couleur(row_p,col_p - i):
                                return False
                        self.placer(row, col, row_p, col_p)
                        return True
                    elif col_p - col < 0:
                        z = abs(col_p - col)
                        for i in range(1, z):
                            if self.diff_couleur(row_p, col_p + i):
                                return False
                        self.placer(row, col, row_p, col_p)
                        return True
                elif col_p == col and row_p != row:
                    if row_p - row > 0:
                        z = row_p - row
                        for i in range(1, z):
                            if self.diff_couleur(row_p - i ,col_p):
                                return False
                        self.placer(row, col, row_p, col_p)
                        return True
                    elif row_p - row < 0:
                        z = abs(row_p - row)
                        for i in range(1, z):
                            if self.diff_couleur(row_p + i, col_p):
                                return False
                        self.placer(row, col, row_p, col_p)
                        return True
                else:
                    print("Deplacement impossible")
                    return False


class Cavalier(Pieces):

    def se_deplacer(self, row, col):

        if self.meme_couleur(row, col):
            return False

        for i in board:
            if self.nom in i:
                row_p = board.index(i)
                col_p = i.index(self.nom)

                if abs(row_p - row) == 2 and abs(col_p - col) == 1:
                    self.placer(row, col, row_p, col_p)
                    return True
                elif abs(row_p - row) == 1 and abs(col_p - col) == 2:
                    self.placer(row, col, row_p, col_p)
                    return True
                else:
                    print("Deplacement impossible")
                    return False


class Fou(Pieces):

    def se_deplacer(self, row, col):

        if self.meme_couleur(row, col):
            return False

        for i in board:
            if self.nom in i:
                row_p = board.index(i)
                col_p = i.index(self.nom)

                x = abs(row_p - row)
                if abs(row_p - row) != abs(col_p - col):
                    print("Deplacement impossible")
                    return False
                elif row_p - row > 0 and col_p - col > 0:
                    for i in range(1, x):
                        if self.diff_couleur(abs(row_p - i), abs(col_p - i)):
                            return False
                    self.placer(row, col, row_p, col_p)
                    return True
                elif row_p - row > 0 and col_p - col < 0:
                    for i in range(1, x):
                        if self.diff_couleur(abs(row_p - i), abs(col_p + i)):
                            return False
                    self.placer(row, col, row_p, col_p)
                    return True
                elif row_p - row < 0 and col_p - col < 0:
                    for i in range(1, x):
                        if self.diff_couleur(abs(row_p + i), abs(col_p + i)):
                            return False
                    self.placer(row, col, row_p, col_p)
                    return True
                elif row_p - row < 0 and col_p - col > 0:
                    for i in range(1, x):
                        if self.diff_couleur(abs(row_p + i), abs(col_p - i)):
                            return False
                    self.placer(row, col, row_p, col_p)
                    return True


class Reine(Pieces):

    def se_deplacer(self, row, col):

        if self.meme_couleur(row, col):
            return False

        for i in board:
            if self.nom in i:
                row_p = board.index(i)
                col_p = i.index(self.nom)

                if row_p == row and col_p != col:
                    if col_p - col > 0:
                        z = col_p - col
                        for i in range(1, z):
                            if self.diff_couleur(row_p,col_p - i):
                                return False
                        self.placer(row, col, row_p, col_p)
                        return True
                    elif col_p - col < 0:
                        z = abs(col_p - col)
                        for i in range(1, z):
                            if self.diff_couleur(row_p, col_p + i):
                                return False
                        self.placer(row, col, row_p, col_p)
                        return True
                elif col_p == col and row_p != row:
                    if row_p - row > 0:
                        z = row_p - row
                        for i in range(1, z):
                            if self.diff_couleur(row_p - i ,col_p):
                                return False
                        self.placer(row, col, row_p, col_p)
                        return True
                    elif row_p - row < 0:
                        z = abs(row_p - row)
                        for i in range(1, z):
                            if self.diff_couleur(row_p + i, col_p):
                                return False
                        self.placer(row, col, row_p, col_p)
                        return True

                x = abs(row_p - row)
                if abs(row_p - row) != abs(col_p - col):
                    print("Deplacement impossible")
                    return False
                elif row_p - row > 0 and col_p - col > 0:
                    for i in range(1, x):
                        if self.diff_couleur(abs(row_p - i), abs(col_p - i)):
                            return False
                    self.placer(row, col, row_p, col_p)
                    return True
                elif row_p - row > 0 and col_p - col < 0:
                    for i in range(1, x):
                        if self.diff_couleur(abs(row_p - i), abs(col_p + i)):
                            return False
                    self.placer(row, col, row_p, col_p)
                    return True
                elif row_p - row < 0 and col_p - col < 0:
                    for i in range(1, x):
                        if self.diff_couleur(abs(row_p + i), abs(col_p + i)):
                            return False
                    self.placer(row, col, row_p, col_p)
                    return True
                elif row_p - row < 0 and col_p - col > 0:
                    for i in range(1, x):
                        if self.diff_couleur(abs(row_p + i), abs(col_p - i)):
                            return False
                    self.placer(row, col, row_p, col_p)
                    return True

                else:
                    print("Deplacement impossible")
                    return False

#def menace marche mais deplace le pion en question(nomalment mais pas verifiée) faire une copie du board pour contrer ca
#boucle infini a cause de fonction recursive  dans se_deplacer de Roi
#pas de verif de victoire
class Roi(Pieces):

    def se_deplacer(self, row, col):

        if self.meme_couleur(row, col):
            return False

        for i in board:
            if self.nom in i:
                row_p = board.index(i)
                col_p = i.index(self.nom)

                if not self.menace(row, col):

                    #Rock

                    if self.debut == 0:
                        if col == 6:
                            if self.couleur == "Blanc":
                                if board[7][5] == vide and board[7][6] == vide:
                                    if tour2_b.debut == 0:
                                        self.placer(7, 6, row_p, col_p)
                                        tour2_b.placer(7, 5, row_p, col_p)
                                        return True
                            if self.couleur == "Noir":
                                if board[0][5] == vide and board[0][6] == vide:
                                    if tour2_n.debut == 0:
                                        self.placer(0, 6, row_p, col_p)
                                        tour2_n.placer(0, 5, row_p, col_p)
                                        return True
                        if col == 2:
                            if self.couleur == "Blanc":
                                if board[7][2] == vide and board[7][3] == vide:
                                    if tour1_b.debut == 0:
                                        self.placer(7, 2, row_p, col_p)
                                        tour1_b.placer(7, 3, row_p, col_p)
                                        return True
                            if self.couleur == "Noir":
                                if board[0][2] == vide and board[0][3] == vide:
                                    if tour1_n.debut == 0:
                                        self.placer(0, 2, row_p, col_p)
                                        tour1_n.placer(0, 3, row_p, col_p)
                                        return True


                    if abs(row_p - row) > 1 or abs(col_p - col) > 1:
                        print("Deplacement impossible")
                        return False

                    else:
                        self.placer(row, col, row_p, col_p)
                        return True

    def menace(self, row, col):
        if self.couleur == "Blanc":
            for i in piece_noire:
                if i.se_deplacer(row, col):
                    print(f"Cette case est menacée par {i.nom}")
                    return True
                return False
        if self.couleur == "Noir":
            for i in piece_blanche:
                if i.se_deplacer(row, col):
                    print(f"Cette case est menace par {i.nom}")
                    return True
                return False


def afficher():
    w = 0
    print(" |      0       |      1       |      2       |      3       |      4       |      5       |      6       |      7      |")
    for i in board:
        print(f"{w}{i}")
        w += 1


pion1_b = Pion("  Pion1_b  ","Blanc", "pion",  0)
pion2_b = Pion("  Pion2_b  ","Blanc", "pion", 0)
pion3_b = Pion("  Pion3_b  ","Blanc", "pion", 0)
pion4_b = Pion("  Pion4_b  ","Blanc", "pion", 0)
pion5_b = Pion("  Pion5_b  ","Blanc", "pion", 0)
pion6_b = Pion("  Pion6_b  ","Blanc", "pion", 0)
pion7_b = Pion("  Pion7_b  ","Blanc", "pion", 0)
pion8_b = Pion("  Pion8_b  ","Blanc", "pion", 0)
tour1_b = Tour("  Tour1_b  ","Blanc", "tour",  0)
tour2_b = Tour("  Tour2_b  ","Blanc", "tour",  0)
cavalier1_b = Cavalier("Cavalier1_b","Blanc", "cavalier",  0)
cavalier2_b = Cavalier("Cavalier2_b","Blanc", "cavalier",  0)
fou1_b = Fou("  Fou1_b   ","Blanc", "fou",  0)
fou2_b = Fou("  Fou2_b   ","Blanc", "fou",  0)
reine_b = Reine("  Reine_b  ","Blanc", "reine",  0)
roi_b = Roi("   Roi_b   ","Blanc", "roi",  0)
pion1_n = Pion("  Pion1_n  ","Noir", "pion", 0)
pion2_n = Pion("  Pion2_n  ","Noir", "pion", 0)
pion3_n = Pion("  Pion3_n  ","Noir", "pion", 0)
pion4_n = Pion("  Pion4_n  ","Noir", "pion", 0)
pion5_n = Pion("  Pion5_n  ","Noir", "pion", 0)
pion6_n = Pion("  Pion6_n  ","Noir", "pion", 0)
pion7_n = Pion("  Pion7_n  ","Noir", "pion", 0)
pion8_n = Pion("  Pion8_n  ","Noir", "pion", 0)
tour1_n = Tour("  Tour1_n  ","Noir", "tour",  0)
tour2_n = Tour("  Tour2_n  ","Noir", "tour",  0)
cavalier1_n = Cavalier("Cavalier1_n","Noir", "cavalier",  0)
cavalier2_n = Cavalier("Cavalier2_n","Noir", "cavalier",  0)
fou1_n = Fou("  Fou1_n   ","Noir", "fou",  0)
fou2_n = Fou("  Fou2_n   ","Noir", "fou",  0)
reine_n = Reine("  Reine_n  ","Noir", "reine",  0)
roi_n = Roi("   Roi_n   ","Noir", "roi",  0)
vide = "           "
board = [[vide] * 8 for i in range(8)]
board[6][0] = pion1_b.nom
board[6][1] = pion2_b.nom
board[6][2] = pion3_b.nom
board[6][3] = pion4_b.nom
board[6][4] = pion5_b.nom
board[6][5] = pion6_b.nom
board[6][6] = pion7_b.nom
board[6][7] = pion8_b.nom
board[7][0] = tour1_b.nom
board[7][1] = cavalier1_b.nom
board[7][2] = fou1_b.nom
board[7][3] = reine_b.nom
board[7][4] = roi_b.nom
board[7][5] = fou2_b.nom
board[7][6] = cavalier2_b.nom
board[7][7] = tour2_b.nom
board[1][0] = pion1_n.nom
board[1][1] = pion2_n.nom
board[1][2] = pion3_n.nom
board[1][3] = pion4_n.nom
board[1][4] = pion5_n.nom
board[1][5] = pion6_n.nom
board[1][6] = pion7_n.nom
board[1][7] = pion8_n.nom
board[0][0] = tour1_n.nom
board[0][1] = cavalier1_n.nom
board[0][2] = fou1_n.nom
board[0][3] = reine_n.nom
board[0][4] = roi_n.nom
board[0][5] = fou2_n.nom
board[0][6] = cavalier2_n.nom
board[0][7] = tour2_n.nom
piece_blanche = [pion1_b, pion2_b, pion3_b, pion4_b, pion5_b, pion6_b, pion7_b, pion8_b, tour1_b, cavalier1_b, fou1_b, reine_b, roi_b, fou2_b, cavalier2_b, tour2_b]
piece_noire = [pion1_n, pion2_n, pion3_n, pion4_n, pion5_n, pion6_n, pion7_n, pion8_n, tour1_n, cavalier1_n, fou1_n, reine_n, roi_n, fou2_n, cavalier2_n, tour2_n]

afficher()


