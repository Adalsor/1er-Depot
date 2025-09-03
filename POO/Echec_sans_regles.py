class Pieces:
    def __init__(self, nom):
        self.nom = nom

    def replacer(self, row, col):
        board[row][col] = self.nom

class Pion(Pieces):
    def se_deplacer(self, row, col):
        for i in board:
            if self.nom in i:
                board[row][col] = self.nom
                board[board.index(i)][i.index(self.nom)] = vide
                afficher()
                print(f"{self.nom} se deplace en [{row}][{col}]")
                break


class Tour(Pieces):
    def se_deplacer(self, row, col):
        for i in board:
            if self.nom in i:
                board[row][col] = self.nom
                board[board.index(i)][i.index(self.nom)] = vide
                afficher()
                print(f"{self.nom} se deplace en [{row}][{col}]")
                break


class Cavalier(Pieces):
    def se_deplacer(self, row, col):
        for i in board:
            if self.nom in i:
                board[row][col] = self.nom
                board[board.index(i)][i.index(self.nom)] = vide
                afficher()
                print(f"{self.nom} se deplace en [{row}][{col}]")
                break


class Fou(Pieces):
    def se_deplacer(self, row, col):
        for i in board:
            if self.nom in i:
                board[row][col] = self.nom
                board[board.index(i)][i.index(self.nom)] = vide
                afficher()
                print(f"{self.nom} se deplace en [{row}][{col}]")
                break


class Reine(Pieces):
    def se_deplacer(self, row, col):
        for i in board:
            if self.nom in i:
                board[row][col] = self.nom
                board[board.index(i)][i.index(self.nom)] = vide
                afficher()
                print(f"{self.nom} se deplace en [{row}][{col}]")
                break


class Roi(Pieces):
    def se_deplacer(self, row, col):
        for i in board:
            if self.nom in i:
                board[row][col] = self.nom
                board[board.index(i)][i.index(self.nom)] = vide
                afficher()
                print(f"{self.nom} se deplace en [{row}][{col}]")
                break


def afficher():
    for i in board:
        print(i)


pion1_b = Pion("  Pion1_b  ")
pion2_b = Pion("  Pion2_b  ")
pion3_b = Pion("  Pion3_b  ")
pion4_b = Pion("  Pion4_b  ")
pion5_b = Pion("  Pion5_b  ")
pion6_b = Pion("  Pion6_b  ")
pion7_b = Pion("  Pion7_b  ")
pion8_b = Pion("  Pion8_b  ")
tour1_b = Tour("  Tour1_b  ")
tour2_b = Tour("  Tour2_b  ")
cavalier1_b = Cavalier("Cavalier1_b")
cavalier2_b = Cavalier("Cavalier2_b")
fou1_b = Fou("  Fou1_b   ")
fou2_b = Fou("  Fou2_b   ")
reine_b = Reine("  Reine_b  ")
roi_b = Roi("   Roi_b   ")
pion1_n = Pion("  Pion1_n  ")
pion2_n = Pion("  Pion2_n  ")
pion3_n = Pion("  Pion3_n  ")
pion4_n = Pion("  Pion4_n  ")
pion5_n = Pion("  Pion5_n  ")
pion6_n = Pion("  Pion6_n  ")
pion7_n = Pion("  Pion7_n  ")
pion8_n = Pion("  Pion8_n  ")
tour1_n = Tour("  Tour1_n  ")
tour2_n = Tour("  Tour2_n  ")
cavalier1_n = Cavalier("Cavalier1_n")
cavalier2_n = Cavalier("Cavalier2_n")
fou1_n = Fou("  Fou1_n   ")
fou2_n = Fou("  Fou2_n   ")
reine_n = Reine("  Reine_n  ")
roi_n = Roi("   Roi_n   ")
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


afficher()