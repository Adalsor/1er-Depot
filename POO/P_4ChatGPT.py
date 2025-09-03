import random

# Plateau global
board = [["     "] * 7 for _ in range(6)]

class Joueur:
    def __init__(self, name, couleur):
        self.name = name
        self.couleur = couleur

    def placer(self, x):
        vide = False
        x = int(x)
        for i in range(5, -1, -1):
            if board[i][x] == "     ":
                board[i][x] = self.couleur
                vide = True
                Bot.afficher()
                if Bot.verification() == 10:
                    return 10
                break
        if not vide:
            print(f"Colonne {x} pleine pour {self.name}")
            return self.jouer() if isinstance(self, IA) else None
        return None

    def afficher(self):
        for i in board:
            print(i)

    def clear(self):
        board[:] = [["     "] * 7 for _ in range(6)]
        Bot.afficher()

    def verification(self):
        for i in range(6):  # lignes
            for l in range(7):  # colonnes
                # Horizontale →
                if l <= 3:
                    if all(board[i][l + k] == "Jaune" for k in range(4)):
                        print("Jaune a gagné ! Félicitations !")
                        return 10
                    elif all(board[i][l + k] == "Rouge" for k in range(4)):
                        print("Rouge a gagné ! Félicitations !")
                        return 10

                # Verticale ↓
                if i <= 2:
                    if all(board[i + k][l] == "Jaune" for k in range(4)):
                        print("Jaune a gagné ! Félicitations !")
                        return 10
                    elif all(board[i + k][l] == "Rouge" for k in range(4)):
                        print("Rouge a gagné ! Félicitations !")
                        return 10

                # Diagonale ↘
                if i <= 2 and l <= 3:
                    if all(board[i + k][l + k] == "Jaune" for k in range(4)):
                        print("Jaune a gagné ! Félicitations !")
                        return 10
                    elif all(board[i + k][l + k] == "Rouge" for k in range(4)):
                        print("Rouge a gagné ! Félicitations !")
                        return 10

                # Diagonale ↗
                if i >= 3 and l <= 3:
                    if all(board[i - k][l + k] == "Jaune" for k in range(4)):
                        print("Jaune a gagné ! Félicitations !")
                        return 10
                    elif all(board[i - k][l + k] == "Rouge" for k in range(4)):
                        print("Rouge a gagné ! Félicitations !")
                        return 10

        return None

# IA améliorée
class IA(Joueur):
    def jouer(self):
        # 1. Vérifie si l'IA peut gagner au prochain coup
        for col in range(7):
            if self.simuler_coup(col, self.couleur):
                print(f"L'IA ({self.couleur}) joue pour GAGNER en colonne {col}")
                return self.placer(str(col))

        # 2. Vérifie si le joueur adverse peut gagner au prochain coup → bloque
        couleur_adverse = "Jaune"
        for col in range(7):
            if self.simuler_coup(col, couleur_adverse):
                print(f"L'IA ({self.couleur}) bloque en colonne {col}")
                return self.placer(str(col))

        # 3. Sinon, joue un coup aléatoire valide
        colonnes_valides = [str(i) for i in range(7) if board[0][i] == "     "]
        if not colonnes_valides:
            print("Plus de coups possibles pour l'IA.")
            return None
        coup = random.choice(colonnes_valides)
        print(f"L'IA ({self.couleur}) joue au hasard en colonne {coup}")
        return self.placer(coup)

    def simuler_coup(self, col, couleur):
        if board[0][col] != "     ":
            return False  # Colonne pleine
        # Copie temporaire du plateau
        temp_board = [row[:] for row in board]
        for row in range(5, -1, -1):
            if temp_board[row][col] == "     ":
                temp_board[row][col] = couleur
                return self.verifie_victoire(temp_board, couleur)
        return False

    def verifie_victoire(self, temp_board, couleur):
        for i in range(6):
            for j in range(7):
                # Horizontale →
                if j <= 3 and all(temp_board[i][j + k] == couleur for k in range(4)):
                    return True
                # Verticale ↓
                if i <= 2 and all(temp_board[i + k][j] == couleur for k in range(4)):
                    return True
                # Diagonale ↘
                if i <= 2 and j <= 3 and all(temp_board[i + k][j + k] == couleur for k in range(4)):
                    return True
                # Diagonale ↗
                if i >= 3 and j <= 3 and all(temp_board[i - k][j + k] == couleur for k in range(4)):
                    return True
        return False

# Création des joueurs
Bot = Joueur("Bot", "     ")
JoueurJaune = Joueur("JoueurJaune", "Jaune")
IA_Rouge = IA("IA_Rouge", "Rouge")

print("Écrire 'jeu()' pour lancer le jeu")

def jeu():
    print("Bienvenue dans le jeu du Puissance 4 !")
    rejouer = 'oui'

    while rejouer == 'oui':
        Bot.clear()

        while True:
            # Tour du joueur Jaune (humain)
            user_jaune = input("Joueur Jaune, sur quelle colonne voulez-vous placer votre jeton ? (0-6 ou 'exit') : ")
            while user_jaune not in ['0', '1', '2', '3', '4', '5', '6', 'exit']:
                user_jaune = input("Veuillez entrer une valeur comprise entre 0 et 6 : ")
            if user_jaune == 'exit':
                rejouer = 'non'
                break
            if JoueurJaune.placer(user_jaune) == 10:
                break

            # Tour de l'IA (Rouge)
            if IA_Rouge.jouer() == 10:
                break

        if rejouer != 'non':
            rejouer = input("Voulez-vous rejouer ? (oui/non) : ").lower()
            while rejouer not in ['oui', 'non']:
                rejouer = input("Veuillez répondre par 'oui' ou 'non' : ")

    print("Fin du jeu.")
