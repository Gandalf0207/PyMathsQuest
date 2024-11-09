# Script reprenant le jeu de la vie de Conway dans le but de créer une geration de cellules vivantes. 
# Ayant comme surface la taille de la map du jeu. 
# A la fin de la génération x, chaque cellule vivante sera implémentée sous forme de carré d'herbe haute sur la map du joueur

# Ce positionnement de l'herbe est bien evidement une easter egg, et un rappel à ce jeu emblématique, à première vu simple, 
# mais ayant une puissance gigantesque avec un peu de recul


# ---------------------------------------------- PyMathsQuest ---------------------------------------------- #

from settings import *
import random

class JeuDeLaVie(object):
    """Return une map avec les cases vivantes et mortes (jeu de la vie de Conway)"""

    def __init__(self) -> None:
        self.longueur, self.largeur = 150, 75
        self.Map = []        
        self.NewMapCoord = []
        self.NewMaoCoord2 = []

    def Base(self):
        for i in range(self.largeur):
            m = []
            for j in range(self.longueur):
                m.append("-")
            self.Map.append(m)

        # Génération de plusieurs configurations de motifs pour le jeu de la vie
        coords = [self.GetCoordsPatterns(self.largeur, self.longueur) for _ in range(5)]
        for partern in coords:
            for coordsPatern in partern:
                self.Map[coordsPatern[0]][coordsPatern[1]] = "#"

    # Fonction pour générer une configuration aléatoire avec des motifs multiples
    def GetCoordsPatterns(self, rows, cols):
        patterns = []
        
        # Coordonnées de motifs aléatoires (R-pentomino)
        for _ in range(3):  # 3 occurrences de R-pentomino
            x = random.randint(0, rows - 5)
            y = random.randint(0, cols - 5)
            r_pentomino_coords = [(x, y + 1), (x, y + 2),
                                (x + 1, y), (x + 1, y + 1),
                                (x + 2, y + 1)]
            patterns.extend(r_pentomino_coords)
        
        # Coordonnées de motifs aléatoires (Acorn)
        for _ in range(2):  # 2 occurrences d'Acorn
            x = random.randint(0, rows - 5)
            y = random.randint(0, cols - 9)
            acorn_coords = [(x, y + 1), (x, y + 4),
                            (x + 1, y + 3),
                            (x + 2, y), (x + 2, y + 1), (x + 2, y + 3), (x + 2, y + 4), (x + 2, y + 5)]
            patterns.extend(acorn_coords)

        # Coordonnées de motifs aléatoires (Diehard)
        for _ in range(2):  # 2 occurrences de Diehard
            x = random.randint(0, rows - 5)
            y = random.randint(0, cols - 9)
            diehard_coords = [(x, y + 6),
                            (x + 1, y), (x + 1, y + 1),
                            (x + 2, y + 1), (x + 2, y + 5), (x + 2, y + 6), (x + 2, y + 7)]
            patterns.extend(diehard_coords)

        # Coordonnées de motifs aléatoires (Phoenix)
        for _ in range(4):  # 4 occurrences de Phoenix
            x = random.randint(0, rows - 5)
            y = random.randint(0, cols - 5)
            phoenix_coords = [(x, y + 1), (x, y + 3),
                            (x + 1, y), (x + 1, y + 2), (x + 1, y + 4),
                            (x + 2, y + 1), (x + 2, y + 3)]
            patterns.extend(phoenix_coords)

        return patterns


    def Calcul(self):
        # on regarde si les cellules vie et meurt
        self.NewMapCoord = []
        self.NewMaoCoord2 = []
        for i in range(1, self.largeur-1):
            for j in range(1, self.longueur-1):
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



    def GetPos(self): 
        self.Base()
        for i in range(1000):
            self.Calcul()
            self.MajMap()
        
        listCoordsCelluleVivantes = []
        for i in range(len(self.Map)):
            for j in range(len(self.Map[i])):
                if self.Map[i][j] == "#":
                    listCoordsCelluleVivantes.append([i,j])

        for i in range(len(self.Map)):
            print(*self.Map[i], sep=" ")


        return listCoordsCelluleVivantes


    