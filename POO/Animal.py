class Animal:
    def __init__(self, poids, taille):
        self.set_poids(poids)
        self.taille = taille

    def se_deplacer(self):
        pass

    def __str__(self):
        return f"Poids: {self.get_poids()}, Taille: {self.taille}"

    def get_poids(self):
        return self.__poids

    def set_poids(self, poids):
        if poids > 0:
            self.__poids = poids
        else:
            raise ValueError("Le poids ne peut être négatif")