#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

from settings import *

class VarienteSolCreator(object):
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.nbElements = 0
        self.longueur = self.gestionnaire.longueur
        self.largeur = self.gestionnaire.largeur
    
    def SetAndSave(self):
        for coords in self.allCoordsElementVarienteSol:
            self.gestionnaire.baseMap[coords[1]][coords[0]] = 2 # on ajoute sur la map de test l'object

    def CreateVarienteSol(self, nombre):
        self.nbElements = nombre
        self.allCoordsElementVarienteSol = []
        for _ in range(self.nbElements): # boucle pour le nombre d'obstacle différents
            ElementPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] pos random sur la map, en éviant les bordure
            while self.gestionnaire.baseMap[ElementPos[1]][ElementPos[0]] != '-' :
                ElementPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] # on replace si jamais il y a un element
            self.allCoordsElementVarienteSol.append(ElementPos)
        self.SetAndSave()
