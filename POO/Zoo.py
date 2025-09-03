from Animal import *
from Oiseau import *
from Serpent import *

class Zoo:
    def __init__(self, liste):
        self.liste = liste

    def ajouter_animal(self, animal):
        self.liste.append(animal)

    def __add__(self, other):
        a = self.liste + other.liste
        return Zoo(a)