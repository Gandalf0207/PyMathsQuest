#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

from settings import *
from SourcesFichiers.ScriptAlgo.jeuDeLaVie import *


class FlowerCreator(object):
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.longueur = 150
        self.largeur = 75

    def SetAndSave(self):
        for posFleur in self.getPosFleur: # on parcourt la liste de coordonnées
            if self.gestionnaire.map[posFleur[1]][posFleur[0]] =="-": # si sur la map (obstacle) il n'y a rien aux coords indiqués
                self.gestionnaire.baseMap[posFleur[1]][posFleur[0]] = 1 # on ajoute aux meme coordonnées dans la map base une fleur {1}

    def CreateFlower(self):
        self.getPosFleur = JeuDeLaVie(self.longueur, self.largeur).GetPos() # On récupère la liste de coordonnées des cellules vivantes
        self.SetAndSave()