# Script reprenant le jeu de la vie de Conway dans le but de créer une geration de cellules vivantes. 
# Ayant comme surface la taille de la map du jeu. 
# A la fin de la génération x, chaque cellule vivante sera implémentée sous forme de carré d'herbe haute sur la map du joueur

# Ce positionnement de l'herbe est bien evidement une easter egg, et un rappel à ce jeu emblématique, à première vu simple, 
# mais ayant une puissance gigantesque avec un peu de recul


# ---------------------------------------------- PyMathsQuest ---------------------------------------------- #

from setting import *

class JeuDeLaVie(object):
    """
    Return une map avec les cases vivantes et mortes (jeu de la vie de Conway)"""

    def __init__(self) -> None:
        self.longueur, self.largeur = 15, 15
        self.Map = []        
        self.NewMapCoord = []
        self.NewMaoCoord2 = []

    def Base(self):
        for i in range(self.longueur):
            m = []
            for j in range(self.largeur):
                m.append("-")
            self.Map.append(m)

        coords = [(4,4), (3,3), (5,3), (5,4), (4,5)]
        for i in coords:
            self.Map[i[0]][i[1]] = "#"


    def Calcul(self):
        # on regarde si les cellules vie et meurt
        self.NewMapCoord = []
        self.NewMaoCoord2 = []
        for i in range(1, self.longueur-1):
            for j in range(1, self.largeur-1):
                    celluleAutour = 0
                    if self.Map[i-1][j-1] =="#":
                        celluleAutour+=1
                    if self.Map[i][j-1] =="#":
                        celluleAutour+=1
                    if self.Map[i+1][j-1] =="#":
                        celluleAutour+=1
                    if self.Map[i-1][j] =="#":
                        celluleAutour+=1
                    if self.Map[i+1][j] =="#":
                        celluleAutour+=1
                    if self.Map[i-1][j+1] =="#":
                        celluleAutour+=1
                    if self.Map[i][j+1] =="#":
                        celluleAutour+=1
                    if self.Map[i+1][j+1] =="#":
                        celluleAutour+=1

                    if celluleAutour == 3 :
                        self.NewMapCoord.append([i, j])
                    elif celluleAutour ==2:
                        if self.Map[i][j] == "#":
                            self.NewMapCoord.append([i, j])
                        else:
                            self.NewMaoCoord2.append([i,j])
                    else:
                        self.NewMaoCoord2.append([i,j])

    def MajMap(self):
        for i in self.NewMapCoord:
            self.Map[i[0]][i[1]] = "#"
        for i in self.NewMaoCoord2:
            self.Map[i[0]][i[1]]  = "-"



    def Update(self): 
        self.Calcul()
        self.MajMap()
        return self.Map


a = JeuDeLaVie()
a.Base()
for i in range(200):
    Map = a.Update()
    for i in range(len(Map)):
        print(*Map[i], sep=" ")
    time.sleep(0.5)
    os.system('cls')