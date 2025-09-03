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
            print("Placement impossible")

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


Bot = Joueur("Bot", "     ")
JoueurRouge = Joueur("JoueurRouge", "Rouge")
JoueurJaune = Joueur("JoueurJaune", "Jaune")
board = [["     "] * 7 for _ in range(6)]
print("Ecrire 'jeu()' pour lancer le jeu")

def jeu():
    print("Bienvenue dans le jeu du Puissance 4 !")
    user_jaune = 0
    user_rouge = 0
    user = 'oui'
    while user == 'oui':
        Bot.clear()
        if user == "non":
            break

        while user_jaune != 10 or user_rouge != 10:
            user_jaune = input("Joueur Jaune, sur quelle colonne voulez-vous placez votre jeton ? : ")
            while user_jaune not in ['0', '1', '2', '3', '4', '5', '6', 'exit']:
                user_jaune = input("Veuillez rentrez une valeur comprise entre 0 et 6")
            if user_jaune == 'exit':
                user = 'non'
                break
            if JoueurJaune.placer(user_jaune) == 10:
                user = input("Voulez vous rejouez ?").lower()
                while user != 'oui' and user != 'non':
                    user = input("Veuillez choisir une réponse valide !").lower()
                break


            user_rouge = input("Joueur Rouge, sur quelle colonne voulez-vous placez votre jeton ? : ")
            while user_rouge not in ['0', '1', '2', '3', '4', '5', '6', 'exit']:
                user_rouge = input("Veuillez rentrez une valeur comprise entre 0 et 6")
            if user_rouge == 'exit':
                user = 'non'
                break
            if JoueurRouge.placer(user_rouge) == 10:
                user = input("Voulez vous rejouez ?").lower()
                while user != 'oui' and user != 'non':
                    user = input("Veuillez choisir une réponse valide !").lower()
                break

    print("Fin du jeu")
