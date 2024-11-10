from settings import *

class LiaisonAtoB(object):
    """class permettant de relier dans une double liste, un point A à un point B. 
    De manière à suivre la diagonale entre ces deux points en utilisant les déplacement verticaux et horizontaux.
    Cette class, renvera une liste contenant toutes les coordonnées à suivre dans une double liste pour se déplacer 
    du point  au point B"""

    def __init__(self, start, goal) -> None:
        self.compteurX = start[0] # coordonnées qu'on va incrémenter (X)
        self.compteurY = start[1]  # coordonnées qu'on va incrémenter (Y)
        self.pos = [] # initialisation de la liste qui contiendra les positions renvoyés (chemin de A vers B)
        self.start = start # on garde une trace du point de départ
        self.goal = goal # on garde une place du point d'arrivé
        self.vector = self.__getVector__() # calcul du vector du point A ver b  / vector AB
        # clacul du ration (nombre de deplacement x  pour 1 déplacement y (et inversement)
        self.ratio = self.__getRatio__()
        self.directionRatioX = self.__getHorizontalDirection__() # get de si le ratio est pour l'axe x
        self.directionRatioY = self.__getVerticalDirection__()
        self.sidePrincipal = self.__getValueSide__()
       
    def __getVector__(self):
        return [self.goal[0] - self.start[0], self.goal[1] - self.start[1]]

    def __getRatio__(self):
        return float("inf") if self.vector[0] == 0 or self.vector[1] ==0 else round(self.vector[1] / self.vector[0]) if abs(self.vector[1]) >= abs(self.vector[0]) else round(self.vector[0] / self.vector[1]) # ternaire pour le calcul du ratio (nb x / 1y) / check pour éviter une division par zéro

    def __getHorizontalDirection__(self):    
        return "DirectionGauche" if self.start[0] > self.goal[0] else "DirectionDroite"  # coord : x

    def __getVerticalDirection__(self):
        return "DirectionHaut" if self.start[1] > self.goal[1] else "DirectionBas"  # coord : y

        
    def __getValueSide__(self):
        # Fonction pour connaitre la valeur du ratio (et agir en fonction)
        return "X" if abs(self.vector[0]) > abs(self.vector[1]) else "Y"

    def __Deplacement__(self):  
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

        
        elif self.directionRatioX == "DirectionGauche": # On decend / monte    # script optimisable largement
            if self.directionRatioY == "DirectionBas":
   

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

            else:
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


        elif self.directionRatioX == "DirectionDroite":
            if self.directionRatioY == "DirectionBas":

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



            else:
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


    
    def GetPos(self):
        self.__Deplacement__()
        return self.pos
    


# coordsA = [[5,12],[30,20],[10,10],[5,20],[45,5],[20,12],[15,8],[0,24]]
# coordsB = [[45,12],[30,5],[40,20],[35,5],[10,20],[25,12],[15,15],[49,0]]

# for i in range(len(coordsA)):

#     map = []

#     for _ in range(25): # largeur de la map (y)
#         creationMap = [] # liste pour stocker les valeurs des colonnes (x)
#         for _ in range(50): # longueur de la map (x)
#             creationMap.append("-") # ajout des valeurs (x)
#         map.append(creationMap) # ajout de la ligne entière



#     call = LiaisonAtoB(coordsA[i], coordsB[i]).GetPos()

#     for coords in call:
#         map[coords[1]][coords[0]] = "#"

#     for affiche in range(len(map)):
#         print(*map[affiche], sep=" ")

#     print(end="\n")
#     print("---------------------------")
#     print(end="\n")