from settings import *

class LiaisonAtoB(object):
    """class permettant de relier dans une double liste, un point A à un point B. 
    De manière à suivre la diagonale entre ces deux points en utilisant les déplacement verticaux et horizontaux.
    Cette class, renvera une liste contenant toutes les coordonnées à suivre dans une double liste pour se déplacer 
    du point  au point B"""

    def __init__(self, start, goal) -> None:
        self.vector = [goal[0] - start[0], goal[1] - start[1]] # calcul du vector du point A ver b  / vector AB
        self.ratio = float("inf") if self.vector[0] == 0 else round(self.vector[1] / self.vector[0]) # ternaire pour le calcul du ratio (nb x / 1y) / check pour éviter une division par zéro
        self.absoluteRatio = abs(self.ratio) # récupération de la valeur positive du ratio (inverse donc si ratio négatif)
        self.compteurX = start[0] # coordonnées du point de départ (point référence A) 
        self.compteurY = start[1] # coordonnées du point de départ (point référence A) 
        self.pos = [] # initialisation de la liste qui contiendra les posotion renvoyés (chemin de A vers B)
        self.start = start # on garde un e trace du point de départ
        self.goal = goal # on garde une place du point d'arrivé

    def __CheckValueRatio__(self):
        # Fonction pour connaitre la valeur du ratio (et agir en fonction)
        return "Positif" if self.ratio > 0 else "Negatif"

    def __Deplacement__(self):
        # Gérer le cas où on se déplace uniquement verticalement
        if self.ratio == float('inf'):
            while self.compteurY <= self.goal[1]:
                self.pos.append([self.compteurY,self.compteurX])
                self.compteurY += 1
            return self.pos

        # gros du travail deplacment
        while self.compteurY + self.absoluteRatio <= self.goal[1]:
            self.pos.append([self.compteurY,self.compteurX])
            for i in range(self.absoluteRatio):
                self.compteurY += 1
                self.pos.append([self.compteurY,self.compteurX])

            self.pos.append([self.compteurY,self.compteurX])
            if self.ratio > 0:
                self.compteurX += 1
                self.pos.append([self.compteurY,self.compteurX])
            elif self.ratio < 0:
                self.compteurX -= 1
                self.pos.append([self.compteurY,self.compteurX])
        
        # finition
        if self.__CheckValueRatio__() == "Positif":

            while self.compteurY + 1 <= self.goal[1] or self.compteurX <= self.goal[0]:
                self.pos.append([self.compteurY,self.compteurX])
                if self.compteurY <= self.goal[1]:
                    self.compteurY += 1
                    self.pos.append([self.compteurY,self.compteurX])
                    
                if self.compteurX <= self.goal[0]:
                    self.pos.append([self.compteurY,self.compteurX])   
                    self.compteurX += 1
                    self.pos.append([self.compteurY,self.compteurX])
        else:
            while self.compteurY + 1 <= self.goal[1] or self.compteurX >= self.goal[0]:
                self.pos.append([self.compteurY,self.compteurX])
                if self.compteurY <= self.goal[1]:
                    self.compteurY += 1
                    self.pos.append([self.compteurY,self.compteurX])
                    
                if self.compteurX >= self.goal[0]:
                    self.pos.append([self.compteurY,self.compteurX])    
                    self.compteurX -= 1
                    self.pos.append([self.compteurY,self.compteurX])
    
    def GetPos(self):
        self.__Deplacement__()
        return self.pos