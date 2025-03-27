#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

from settings import *

class LiaisonAtoB(object):
    """class permettant de relier dans une double liste, un point A à un point B. 
    De manière à suivre la diagonale entre ces deux points en utilisant les déplacement verticaux et horizontaux.
    Cette class, renvera une liste contenant toutes les coordonnées à suivre dans une double liste pour se déplacer 
    du point A au point B"""

    def __init__(self, start, goal) -> None:
        """Initialisation des attributs d'objet de la class"""
        self.compteurX = start[0] # coordonnées qu'on va incrémenter (X)
        self.compteurY = start[1]  # coordonnées qu'on va incrémenter (Y)
        self.pos = [] # initialisation de la liste qui contiendra les positions renvoyés (chemin de A vers B)
        self.start = start # on garde une trace du point de départ
        self.goal = goal # on garde une place du point d'arrivé
        self.vector = self.__getVector__() # calcul du vector du point A ver b  / vector AB
        # calcul du ration (nombre de deplacement x  pour 1 déplacement y (et inversement)
        self.ratio = self.__getRatio__() # en fonction du vecteur, on get le déplacement  faire pour un déplacment sur l'autre axe de 1
        self.directionRatioX = self.__getHorizontalDirection__() # get du déplacement direction sur l'axe x
        self.directionRatioY = self.__getVerticalDirection__() # get du déplacement direction sur l'axe y
        self.sidePrincipal = self.__getValueSide__() # get de la side la plus longue en terme de déplacement (pour y affecteur de ratio lors du déplacement)
       
    def __getVector__(self) -> list:
        """Méthode de création du vecteur"""
        return [self.goal[0] - self.start[0], self.goal[1] - self.start[1]] # renvois du vecteur AB

    def __getRatio__(self) -> Union[int, float]:
        """Méthode de calcul pour détermine le ratio de déplacement"""
        # ternaire pour le calcul du ratio (nb x / 1y) / check pour éviter une division par zéro
        return float("inf") if self.vector[0] == 0 or self.vector[1] ==0 else round(self.vector[1] / self.vector[0]) if abs(self.vector[1]) >= abs(self.vector[0]) else round(self.vector[0] / self.vector[1]) 

    def __getHorizontalDirection__(self)  -> str:  
        """Méthode pour déterminer la direction à prendre sur l'axe x"""  
        return "DirectionGauche" if self.start[0] > self.goal[0] else "DirectionDroite"  # coord : x   ; retour de la direction à prendre

    def __getVerticalDirection__(self)  -> str:
        """Méthode pour déterminer la direction à prendre sur l'axe y"""  
        return "DirectionHaut" if self.start[1] > self.goal[1] else "DirectionBas"  # coord : y ; retour de la direction à prendre

        
    def __getValueSide__(self) -> str:
        """Méthode permettant de déterminer le côté le plus grand pour le déplacement"""
        return "X" if abs(self.vector[0]) > abs(self.vector[1]) else "Y" # retour de ce côté le plus grand ; si égalité, ce n'est pas grave, le ratio est de 1 dans ce cas...

    def __Deplacement__(self) -> None:  
        """Méthode de gestion pour le déplacement """
        # Gérer le cas où on se déplace uniquement verticalement
        if self.ratio == float('inf'):
            if self.start[0] == self.goal[0]: # on est sur la meme ligne : x

                if self.start[1] > self.goal[1]: # On va vers le haut y
                    while self.compteurY != self.goal[1]:
                        self.compteurY -= 1
                        self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]

                elif self.start[1] < self.goal[1]: # on va vers le bas : y
                    while self.compteurY != self.goal[1]:
                        self.compteurY += 1
                        self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]


            elif self.start[1] == self.goal[1]: # on est sur la meme colonne : y

                if self.start[0] > self.goal[0]: # on va vers la gauche
                    while self.compteurX != self.goal[0]:
                        self.compteurX -= 1
                        self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]

                elif self.start[0] < self.goal[0]: # on va vers la droite
                    while self.compteurX != self.goal[0]:
                        self.compteurX += 1
                        self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]

        
        elif self.directionRatioX == "DirectionGauche": # on va à gauche
            if self.directionRatioY == "DirectionBas": # on va en bas
   

                # gros du travail deplacment
                if self.sidePrincipal == "X": 
                    while self.compteurX + self.ratio >= self.goal[0]:
                        for ratio in range(abs(self.ratio)):
                            self.compteurX -= 1
                            self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]

                        if self.compteurY < self.goal[1]:
                            self.compteurY += 1
                            self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]  
                
                else:
                    while self.compteurY + abs(self.ratio) <= self.goal[1]:
                        for ratio in range(abs(self.ratio)):
                            self.compteurY += 1
                            self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]  

                        if self.compteurX > self.goal[0]:
                            self.compteurX -= 1
                            self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]  

                # finition
                while self.compteurX != self.goal[0] or self.compteurY != self.goal[1]:
                    if self.compteurX > self.goal[0]:
                        self.compteurX -= 1
                        self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]  

                    if self.compteurY < self.goal[1]:
                        self.compteurY += 1
                        self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]  

            else: # on va en haut
                # gros du travail deplacment
                if self.sidePrincipal == "X":
                    while self.compteurX - self.ratio >= self.goal[0]: # on soustrait le ratio car il sont tout les deux en négatif (- / - = + ....)
                        for ratio in range(abs(self.ratio)):
                            self.compteurX -= 1
                            self.pos.append([self.compteurX,self.compteurY])
                        
                        if self.compteurY > self.goal[1]:
                            self.compteurY -= 1
                            self.pos.append([self.compteurX,self.compteurY]) # forme [x,y] 
                else:
                    while self.compteurY - self.ratio >= self.goal[1]:
                        for ratio in range(abs(self.ratio)):
                            self.compteurY -= 1
                            self.pos.append([self.compteurX,self.compteurY])

                        if self.compteurX > self.goal[0]:
                            self.compteurX -= 1
                            self.pos.append([self.compteurX,self.compteurY])

                # finition
                while self.compteurX != self.goal[0] or self.compteurY != self.goal[1]:
                    if self.compteurX > self.goal[0]:
                        self.compteurX -= 1
                        self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]  

                    if self.compteurY > self.goal[1]:
                        self.compteurY -= 1
                        self.pos.append([self.compteurX,self.compteurY]) # forme [x,y] 


        elif self.directionRatioX == "DirectionDroite": # on va a droite
            if self.directionRatioY == "DirectionBas": # on va en bas

             # gros du travail deplacment
                if self.sidePrincipal =="X":
                    while self.compteurX + self.ratio <= self.goal[0]:
                        for ratio in range(abs(self.ratio)):
                            self.compteurX += 1
                            self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]

                        if self.compteurY < self.goal[1]:
                            self.compteurY += 1
                            self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]
                else:
                    while self.compteurY + self.ratio <= self.goal[1]:
                        for ratio in range(abs(self.ratio)):
                            self.compteurY += 1
                            self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]

                        if self.compteurX < self.goal[0]:
                            self.compteurX += 1
                            self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]  

                # finition
                while self.compteurX != self.goal[0] or self.compteurY != self.goal[1]:
                    if self.compteurX < self.goal[0]:
                        self.compteurX += 1
                        self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]  

                    if self.compteurY < self.goal[1]:
                        self.compteurY += 1
                        self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]  



            else: # on va en haut
                # gros du travail deplacment
                if self.sidePrincipal == "X":
                    while self.compteurX + abs(self.ratio) <= self.goal[0]:
                        for ratio in range(abs(self.ratio)):
                            self.compteurX += 1
                            self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]

                        if self.compteurY > self.goal[1]:
                            self.compteurY -= 1
                            self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]
                        
                else:
                     while self.compteurY + self.ratio >= self.goal[1]: # le ratio est normalement négatif car on monte dans la liste
                        for ration in range(abs(self.ratio)):
                            self.compteurY -= 1
                            self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]
                        
                        if self.compteurX < self.goal[0]:
                            self.compteurX += 1
                            self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]

                # finition
                while self.compteurX != self.goal[0] or self.compteurY != self.goal[1]:
                    if self.compteurX < self.goal[0]:
                        self.compteurX += 1
                        self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]  

                    if self.compteurY > self.goal[1]:
                        self.compteurY -= 1
                        self.pos.append([self.compteurX,self.compteurY]) # forme [x,y]  


    
    def GetPos(self) -> list:
        """Methode pour retourner les coords de déplacement à faire entre le point A et le point B"""

        self.__Deplacement__() # méthode de calcul
        return self.pos 
    