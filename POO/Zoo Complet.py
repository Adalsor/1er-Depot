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

class Serpent(Animal):
    def se_deplacer(self):
        print("je rampe")

class Oiseau(Animal):
    def __init__(self, poids, taille, altitude_max):
        super().__init__(poids=poids, taille=taille)
        self.altitude_max = altitude_max

    def se_deplacer(self):
        print("je vole")

class Zoo:
    def __init__(self, liste):
        self.liste = liste

    def ajouter_animal(self, animal):
        self.liste.append(animal)

    def __add__(self, other):
        a = self.liste + other.liste
        return Zoo(a)


chien = Animal(30, 150)
#print(chien.poids)
#print(chien.taille)

python = Serpent(8, 110)
aigle = Oiseau(30, 80, 5)
#python.se_deplacer()
#aigle.se_deplacer()

#print(aigle.get_poids())

#lezard = Animal(-54, 10)
#print(lezard.get_poids())

zoo1 = Zoo([chien, python, aigle])
#print(zoo1.liste)
castor = Animal(20, 30)
zoo1.ajouter_animal(castor)
#print(zoo1.liste)

ani = Animal(50, 30)
#print(str(ani))

zoo2 = Zoo([castor, ani])

zoo3 = zoo1 + zoo2
print(zoo3.liste)