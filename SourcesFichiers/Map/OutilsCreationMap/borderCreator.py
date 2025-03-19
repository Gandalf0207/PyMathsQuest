from settings import *

class BorderCreator(object):
    def __init__(self, gestionnaire):
        self.gestionnaire= gestionnaire
        self.longueur = 150
        self.largeur = 75

    def SetAndSave(self):
        for coords in self.listeBordures:
            self.gestionnaire.map[coords[1]][coords[0]] = "B"  # on ajoute sur la map de test l'objec
            self.gestionnaire.baseMap[coords[1]][coords[0]] = "B"  # on ajoute sur la map de test l'object

    def CreateBorder(self):
        # bordure map  
        self.listeBordures = [] 
        for i in range(2):
            for j in range(self.longueur):
                self.listeBordures.append([j, i*(self.largeur-1)]) 
        self.SetAndSave()