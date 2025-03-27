#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

from settings import *
from SourcesFichiers.ScriptAlgo.astar import *

class Cinematique(object):
    def __init__(self, goal : list, targetObject : any, mapCalcul : list, pathAccessible : list) -> None:
        """Méthode initialisation des valeurs pour la cinématique"""

        # Initialisation des valeurs
        self.targetObject = targetObject

        if NIVEAU["Map"] != "NiveauBaseFuturiste":
            self.pos = self.targetObject.pos  # Position sur la double liste

            # Récupération des attributs graphiques du PNJ
            self.rect = self.targetObject.rect  # Utiliser la hitbox comme référence principale
            self.hitbox = self.targetObject.hitbox  # Synchroniser avec la hitbox du PNJ
        else:
            self.pos = LoadJsonMapValue("coordsMapObject", "Spawn")

            # Récupération des attributs graphiques du PNJ
            self.rect = self.targetObject.rect  # Utiliser la hitbox comme référence principale
            self.hitbox = self.targetObject.hitbox_rect  # Synchroniser avec la hitbox du PNJ

        self.goal = (goal[0], goal[1])
        self.mapCalcul = mapCalcul
        self.pathAccessible = pathAccessible


        # Calcul et définition du chemin
        self.GetPath()
        self.SetPath()



    def GetPath(self) -> None:
        """Calcul du chemin à l'aide de l'algorithme A*"""
        self.pathDeplacement = Astar(self.pos, self.goal, self.mapCalcul, self.pathAccessible).a_star()
        self.pathDeplacement = [(x * CASEMAP, y * CASEMAP) for x, y in self.pathDeplacement]  # Conversion en coordonnées pygame

    def SetPath(self) -> None:
        """Définit un nouveau chemin pour le PNJ"""
        if self.pathDeplacement:  # Vérifier que le chemin n'est pas vide
            self.pointSuivant = self.pathDeplacement.pop(0)  # Prendre le premier point comme cible
        else:
            self.pointSuivant = None  # Pas de chemin à suivre


    def Replacement(self, allPNJ):
        """Replace le PNJ une case au-dessus de la position cible."""

        if NIVEAU["Map"] == "NiveauPlaineRiviere":

            # Positionner le PNJ en fonction de l'objectif
            target_x, target_y = self.goal[0], (self.goal[1] - 1)  # Une case au-dessus

            # Ajuster les positions de la hitbox et du rectangle
            self.hitbox.center = (target_x * CASEMAP +64, target_y * CASEMAP +64)  # Position en pixels
            self.rect.center = self.hitbox.center  # Synchroniser la rect avec la hitbox

            # Mettre à jour la position logique de l'objet PNJ si nécessaire
            self.targetObject.pos = (target_x, target_y)

        elif NIVEAU["Map"] == "NiveauMedievale":
            for pnjObj in allPNJ:
                pnjObj.kill()

        elif NIVEAU["Map"] == "NiveauBaseFuturiste":
            pass



    def Update(self, dt):
        """Méthode update : appel class pnj update pour l'animation et les déplacements"""

        # déplacemement + animation
        
        self.pointSuivant, self.pathDeplacement = self.targetObject.UpdateCinematique(dt, self.pointSuivant, self.pathDeplacement)
        
        # check de fin cinématique ou non.
        if self.pathDeplacement != []:
            return True, False
        else:
            return False, True