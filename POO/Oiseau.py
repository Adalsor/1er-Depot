from Animal import *

class Oiseau(Animal):
    def __init__(self, poids, taille, altitude_max):
        super().__init__(poids=poids, taille=taille)
        self.altitude_max = altitude_max

    def se_deplacer(self):
        print("je vole")
