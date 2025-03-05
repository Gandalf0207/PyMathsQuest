from settings import *
from Sources.ScriptAlgo.astar import *


class FollowPlayer(object):
    def __init__(self, goal : list, pnjObject : any, mapCalcul : list, pathAccessible : list) -> None:
        """Méthode initialisation des valeurs pour le follow """

        # Initialisation des valeurs
        self.pnjObject = pnjObject

        if NIVEAU["Map"] == "NiveauMordor":
            self.pos = self.pnjObject.pos  # Position sur la double liste
            
            # Récupération des attributs graphiques du PNJ
            self.rect = self.pnjObject.rect  # Utiliser la hitbox comme référence principale
            self.hitbox = self.pnjObject.hitbox  # Synchroniser avec la hitbox du PNJ

        self.goal = (goal[0], goal[1])
        self.mapCalcul = mapCalcul
        self.pathAccessible = pathAccessible


        # Calcul et définition du chemin
        self.GetPath()
        self.SetPath()


    def GetPath(self) -> None:
        """Calcul du chemin à l'aide de l'algorithme A*"""
        self.pathDeplacement = Astar(self.pos, self.goal, self.mapCalcul, self.pathAccessible).a_star()
        if self.pathDeplacement:
            self.pathDeplacement = [(x * CASEMAP, y * CASEMAP) for x, y in self.pathDeplacement]  # Conversion en coordonnées pygame
        else:
            self.pathDeplacement = []
    def SetPath(self) -> None:
        """Définit un nouveau chemin pour le PNJ"""
        if self.pathDeplacement:  # Vérifier que le chemin n'est pas vide
            self.pointSuivant = self.pathDeplacement.pop(0)  # Prendre le premier point comme cible
        else:
            self.pointSuivant = None  # Pas de chemin à suivre

    def Update(self, targetPos, dt):
        """Méthode update : appel class pnj update pour l'animation et les déplacements"""
        targetPos = (int(targetPos[0] // CASEMAP), int(targetPos[1] // CASEMAP))
        if self.goal != targetPos:
            self.pos = self.pnjObject.pos
            self.goal = targetPos
            self.GetPath()

        
        # check de fin follow ou non.
        if self.pathDeplacement != []:
            # déplacemement + animation
            self.pointSuivant, self.pathDeplacement = self.pnjObject.UpdateFollow(dt, self.pointSuivant, self.pathDeplacement)

        # suppression collisoon
        self.pnjObject.hitbox.size = (0,0)

            