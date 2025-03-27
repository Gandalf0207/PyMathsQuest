#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin


# Script reprenant le jeu de la vie de Conway dans le but de créer une geration de cellules vivantes. 
# Ayant comme surface la taille de la map du jeu. 
# A la fin de la génération x, chaque cellule vivante sera implémentée sous forme de carré d'herbe haute sur la map du joueur

# Ce positionnement de l'herbe est bien evidement une easter egg, et un rappel à ce jeu emblématique, à première vu simple, 
# mais ayant une puissance gigantesque avec un peu de recul


# ---------------------------------------------- PyMathsQuest ---------------------------------------------- #

from settings import *

class JeuDeLaVie(object):
    """Return une map avec les cases vivantes et mortes (jeu de la vie de Conway)"""

    def __init__(self, longueur :int, largeur: int) -> None:
        """Initialisation des attributs d'objets pour la génération du jeu de la vie (double liste)"""
        self.longueur, self.largeur = longueur, largeur # set de la longueur et largeur
        self.Map = [] # initialisation de la variable qui contiendra la double liste de map       
        self.NewMapCoord = []  # initialisation de la liste permettant de stocker les coords des cellules vivantes  
        self.NewMapCoord2 = [] # initialisation de la liste permettant de stocker les coords des cellules mortes 

    def __Base__(self) -> None:
        """Méthode permettant de créer la base des ressources : la map et poser les premières cellules vivantes. 
        On prend des générateur (modèle du jeu de la vie) qui avec des gliders qui entrainent le chaos"""

        # création de la map
        for i in range(self.largeur):
            m = []
            for j in range(self.longueur):
                m.append("-")
            self.Map.append(m)

        # Génération de plusieurs configurations de motifs pour le jeu de la vie
        coords = [self.__GetCoordsPatterns__() for _ in range(5)]
        for partern in coords:
            for coordsPatern in partern:
                self.Map[coordsPatern[1]][coordsPatern[0]] = "#"

    
    def __GetCoordsPatterns__(self) -> list:
        """Méthode pour générer une configuration aléatoire avec des motifs multiples"""
        patterns = []
        
        # Coordonnées de motifs aléatoires (R-pentomino)
        for _ in range(3):  # 3 occurrences de R-pentomino
            x = randint(0, self.longueur - 5)
            y = randint(0, self.largeur - 5)
            r_pentomino_coords = [(x, y + 1), (x, y + 2),
                                (x + 1, y), (x + 1, y + 1),
                                (x + 2, y + 1)]
            patterns.extend(r_pentomino_coords)
        
        # Coordonnées de motifs aléatoires (Acorn)
        for _ in range(2):  # 2 occurrences d'Acorn
            x = randint(0, self.longueur - 5)
            y = randint(0, self.largeur - 9)
            acorn_coords = [(x, y + 1), (x, y + 4),
                            (x + 1, y + 3),
                            (x + 2, y), (x + 2, y + 1), (x + 2, y + 3), (x + 2, y + 4), (x + 2, y + 5)]
            patterns.extend(acorn_coords)

        # Coordonnées de motifs aléatoires (Diehard)
        for _ in range(2):  # 2 occurrences de Diehard
            x = randint(0, self.longueur - 5)
            y = randint(0, self.largeur - 9)
            diehard_coords = [(x, y + 6),
                            (x + 1, y), (x + 1, y + 1),
                            (x + 2, y + 1), (x + 2, y + 5), (x + 2, y + 6), (x + 2, y + 7)]
            patterns.extend(diehard_coords)

        # Coordonnées de motifs aléatoires (Phoenix)
        for _ in range(4):  # 4 occurrences de Phoenix
            x = randint(0, self.longueur - 5)
            y = randint(0, self.largeur - 5)
            phoenix_coords = [(x, y + 1), (x, y + 3),
                            (x + 1, y), (x + 1, y + 2), (x + 1, y + 4),
                            (x + 2, y + 1), (x + 2, y + 3)]
            patterns.extend(phoenix_coords)

        return patterns


    def __Calcul__(self) -> None:
        """Méthode pour calculer la liste des déplacements pour accéder aux 8 voisins (dans le sens horaire autour de la cellule)"""

        checkVoisins = [
            (-1, -1), (-1, 0), (-1, 1),  # voisins en haut
            (0, -1),           (0, 1),     # voisins à gauche et à droite
            (1, -1),  (1, 0),  (1, 1)      # voisins en bas
        ]
        # on regarde si les cellules vie et meurt
        self.NewMapCoord = []    # initialisation de liste pour stocker les valeurs des cellules vivantes
        self.NewMapCoord2 = [] # initialisation de liste pour stocker les valeurs des cellules mortes

        # Parcourt de la map et action à partir des 3 règles du jeu de la vie.
        for ordonnees in range(1, self.largeur-1):
            for abscisses in range(1, self.longueur-1):
                    celluleAutour = 0
                    for dx, dy in checkVoisins:
                        if self.Map[ordonnees + dx][abscisses + dy] == "#":
                            celluleAutour += 1

                    if celluleAutour == 3 :
                        self.NewMapCoord.append([abscisses, ordonnees]) ####
                    elif celluleAutour ==2:
                        if self.Map[ordonnees][abscisses] == "#":
                            self.NewMapCoord.append([abscisses, ordonnees])
                        else:
                            self.NewMapCoord2.append([abscisses,ordonnees])
                    else:
                        self.NewMapCoord2.append([abscisses,ordonnees])

    def __MajMap__(self) -> None:
        """Méthode permettant d'ajouter à la map générale les cellules vivantes et mortes après une génération"""

        for coordsCellulesVivantes in self.NewMapCoord: # ajout des cellules vivantes 
            self.Map[coordsCellulesVivantes[1]][coordsCellulesVivantes[0]] = "#"
        for coordsCellulesMortes in self.NewMapCoord2: # ajout des cellules mortes
            self.Map[coordsCellulesMortes[1]][coordsCellulesMortes[0]]  = "-"



    def GetPos(self) -> list : 
        """Méthode de gestion de la grande génération de la map avec les cellules vivantes / mortes.
        Retourne la liste des coordonnées des cellules vivantes"""
        
        self.__Base__() # setup de la base 
        for generation in range(1000): # boucle de 1000 génération
            self.__Calcul__() # on calcul la future map 
            self.__MajMap__() # on met à jour la map
        
        listCoordsCelluleVivantes = [] # initialisation de la liste des coords des cellules vivantes de la dernière génération (retourné)
        #parcourt de la map, ajout des coord si la cellule est vivante
        for ordonnees in range(len(self.Map)):
            for abscisses in range(len(self.Map[ordonnees])):
                if self.Map[ordonnees][abscisses] == "#":
                    listCoordsCelluleVivantes.append([abscisses,ordonnees])

        for affiche in range(len(self.Map)):  # chek print
            print(*self.Map[affiche], sep=" ")


        return listCoordsCelluleVivantes


    