# ---------------------------------------------- PyMathsQuest ---------------------------------------------- #

# Import des settings
from settings import *

# Import des scripts algo pour placer les par-terre de fleurs; relier 2 points entre eux; 
# check si le niveau est faisable en reliant chaque point clé du niveau entre eux
from ScriptAlgo.jeuDeLaVie import *
from ScriptAlgo.liaisonAtoB import *
from ScriptAlgo.astar import *

class GestionNiveauMap(object):
    """Class parent création map, settings et méthode globales"""

    def __init__(self, longueur :int, largeur: int) -> None:
        """Initialisation des attributs """

        self.longueur = longueur 
        self.largeur = largeur 
        self.map = [] # map collision
        self.baseMap = [] # map sol
        self.data = {
                    "coordsMapBase" : {
                        "Bordures Coords": "null",
                        "Riviere0 Coords" : "null",
                        "Riviere1 Coords" : "null",
                        "Riviere2 Coords" : "null",
                        "Riviere3 Coords" : "null",
                        "Flowers Coords" : "null",
                        "Mud Coords" : "null",
                        "Rock Coords" : "null",
                        "coords Path" : "null",
                        "AllMapInfo" : "null",
                        "AllMapBase" : "null"
                    },

                    "coordsMapObject" : {
                        "Obstacles Coords" : "null",
                        "PNJ Coords" : "null",
                        "ArbreSpecial Coords" : "null",
                        "Chateau Coords" : "null",
                        "Champs Coords" : "null",
                        "coords Villages" : "null",
                        "coords Puits" : "null",
                        "coords PassageRiver1" : "null",
                        "coords CraftTable" : "null",
                        "RiverBoatTPChateau coords" : "null",
                        "Spawn" : "null",
                        "Exit" : "null"
                    }
                }   # arborescence fichier json
        self.BaseJson(self.data)
        self.BaseMap()

    def BaseMap(self) -> None:
        """Méthode création base map (sol et collision)"""

        # map  (150, 75)
        for _ in range(self.largeur): 
            creationMap = [] 
            for _ in range(self.longueur): 
                creationMap.append("-") 
            self.map.append(creationMap) 
        
        # map base   (150, 75)
        for _ in range(self.largeur): 
            creationMap = [] 
            for _ in range(self.longueur): 
                creationMap.append("-")            
            self.baseMap.append(creationMap) 
        
    def BaseJson(self, data :dict) -> None:
        """Initialisation du fichier Json"""

        # ouverture en écriture
        with open(join("Sources","Ressources","AllMapValue.json"), "w") as valueFileJson: 
            json.dump(data, valueFileJson, indent=4) 

    def PlacementElements(self, coordsElements, pathJson): 
        """Méthode permettant de placer le spawn du joueur sur la map (collision) et d'ajouter ces coordonnées dans le json"""
        for coordsPlacement in coordsElements: # on parcourt toute la liste de coords
            self.map[coordsPlacement[1]][coordsPlacement[0]] = coordsPlacement[2] # on place les element aux coordonnées sur la map (avec la lettre)
        AjoutJsonMapValue(coordsElements, pathJson[0], pathJson[1]) # on ajoute les coordonnées du spawn au fichier json






class NiveauPlaineRiviere(GestionNiveauMap):

    def __init__(self, longueur :int, largeur :int) -> None:
        """Initialisation des attributs de la class enfant"""
        super().__init__(longueur, largeur) 
        self.obstacle = 1000 
        self.rock = 300
        self.mud = 200
        self.coordsPNJ = None 
        self.mapCheckDeplacementPossible = [] # map test vide

    def __CheckPosRiviere__(self, indice : list) -> bool:
        """Méthode permettant de regarder et de valider la position d'un element par raport à la riviere (pnj / arbre spécial)"""
        
        listePosPossible = ["-", "F", "M", "R"] #path possible

        if indice[0] == 149: # position de la sortir sur la bordure de map (donc condition de check diférentes)
            if (self.map[indice[1]][indice[0]-1] in listePosPossible) and (self.map[indice[1]][indice[0]-2] in listePosPossible )and (indice[1] >=5) and (indice[1] <= 70) and (self.map[indice[1]-1][indice[0]-1] in listePosPossible): 
                return True # on valide le placement
        elif (self.map[indice[1]][indice[0]-1] in listePosPossible) and (self.map[indice[1]][indice[0]-2] in listePosPossible )and(self.map[indice[1]][indice[0]+1] in listePosPossible) and (indice[1] >=5) and (indice[1] <= 70) and (self.map[indice[1]-1][indice[0]-1] in listePosPossible): 
            return True # on valide le placement
        else:
            return False # on invalide le placement

    def CheckNiveauPossible(self, listOrdrePointCle :list, pathAccessible :list) -> bool:
        """Méthode permettant de vérifier si le niveau est possible, suite à la position des obstacle. Utilisation du script A* permettant de trouver un chemin avec les déplacements ZQSD s'il exite entre un point A et B
        Ces points, donnés dans l'ordre d'évolution de la map, représente les coordonnées des éléments que le joueurs doit allé voir (pnj, arbre, entré, sortie..)"""

        for pointCle in range(len(listOrdrePointCle)-1): #
            if  Astar(listOrdrePointCle[pointCle], listOrdrePointCle[pointCle+1],self.mapCheckDeplacementPossible, pathAccessible).a_star(): 
                continue
            else: # résolution du niveau est impossible
                return False # false pour niveau impossible
        return True # les chemins entre les points données existent  


    def Bordure(self):

        # bordure map  
        listeBordures = [] 
        for i in range(2):
            for j in range(self.longueur):
                self.map[i*(self.largeur-1)][j] = "B" 
                self.baseMap[i*(self.largeur-1)][j] = "B"  
                listeBordures.append([i*(self.largeur-1), j]) 

        # on stock les coordonnées des bordures (la liste) dans le json
        AjoutJsonMapValue(listeBordures, "coordsMapBase", "Bordures Coords")

    def __PlacementFleur__(self) -> None:
        """A partir d'une génération du jeu de la vie de conway, les cellules vivantes correspondent à l'emplacement 
        des fleurs sur la map (base) du jeu"""

        getPosFleur = JeuDeLaVie(self.longueur, self.largeur).GetPos() # On récupère la liste de coordonnées des cellules vivantes
        listeFlowerCoords = [] # initialisation de la liste pour les coordonnées finales de position des fleurs
        for posFleur in getPosFleur: # on parcourt la liste de coordonnées
            # verif pour éviter de remplacer un bout de riviere / bordure / autre....
            if self.map[posFleur[1]][posFleur[0]] =="-": # si sur la map (obstacle) il n'y a rien aux coords indiqués
                self.baseMap[posFleur[1]][posFleur[0]] = "F" # on ajoute aux meme coordonnées dans la map base une fleur ("F")
                listeFlowerCoords.append(posFleur) # on stock les coordonnées de la fleur ajouté dans la liste

        AjoutJsonMapValue(listeFlowerCoords, "coordsMapBase", "Flowers Coords") # on ajoute au fichier json, la vrai liste de coordonnée des fleurs

    def __PlacementSpecial__(self, index1 : str, index2 : str, element : str, *args) -> list:
        """Méthode permetant de placer spécialement une element sous certaines condition.
        On récupère les coordonnées d'un elelment (ici la riviere), on génère aléatoirement un indice qui sera appliqué à cette liste de coordonnées
        On vérifier si à cet indice le placement (devant gauche) de l'element est possible (__checkPos__)
        Si c'est bon on placement l'element, et on renvoie les coordonnées de l'element placé sur la map (collision), sinon on génère un nouvelle indice, et on recheck jusqu'a trouver"""
        
        listeCoordsElement = LoadJsonMapValue(index1, index2) # récupération de la liste de valeurs d'un element (riviere)

        Go = True
        while Go: # tant que go = True on check 
            indice = randint(0, self.largeur-1) # génération aléatoire d'un indice
            # Si true, on arreter la boucle
            if self.__CheckPosRiviere__(listeCoordsElement[indice]): # check si à les coords de la liste  l'indice respect les conditions pour poser l'element
                Go = False # Arret de la boucle
                
        itemCoords = listeCoordsElement[indice] # on crée un copie des coords dans la variable
        self.map[itemCoords[1]][itemCoords[0]-1] = element # on ajoute l'element sur la map (collision)

        return itemCoords[0]-1,itemCoords[1] # return [x,y ) coord de l'element
    
    def __PlacementRiviere__(self) -> None:
        """Méthode permettant de créer les deux rivières de la map. Création de points de repère tout les 15 de distance en hauteur dans un couleurs d'une largeur de 9
        Liaison des points entre eux avec un script de LiaisonAtoB fait maison.
        
        Placement également dune zone de sécurité (5 de haut verticalement) pour placer les element spéciaux si jamais
        Placement de ligne aux extrémitées (haut et bas) pour ne pas etre en colision avec les montagnes"""


        # création 2 rivières génération alétoire controlé
        for nombreRiviere in range(4): # 4 tours car 4 riviere
            listeCheminRiviere = [] # initialisation de la liste qui contiendra toutes les coordonnées de la riviere
            listePointRepere = [] # initialisation de la liste des pts repères

            # Points du haut (premier element)
            # permet de créer une ligne pour éviter les collision avec les bordures
            if nombreRiviere != 0 and nombreRiviere != 3: 
                coordsPts1Riviere = [randint(((nombreRiviere)*CoupageMapRiviere - CouloirRiviere),((nombreRiviere)*CoupageMapRiviere + CouloirRiviere)),0] # on créer le point 1 de la map
            else:
                if nombreRiviere == 0:
                    coordsPts1Riviere = [randint(0,6),0] # on créer le point 1 de la map pour les rivière de bordure
                else:
                    coordsPts1Riviere = [randint(LONGUEUR-7, LONGUEUR-2),0] # on créer le point 1 de la map

            listePointRepere.append(coordsPts1Riviere) # forme [x,y] on ajoute le premier point à la liste
            coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1]+4] # on crée le second point avec une hauteur de + 4
            listePointRepere.append(coordsPts2Riviere) # forme [x,y] on ajoute le second point dans la liste

            # Point de haut en bas
            nbPts = self.largeur // EspacementPointRepereRiviere    # placement tout les 15 de hauteur ...   
            verifLigne5 = randint(1,(nbPts-1)) # choix du lieu pour la ligne de 5 droite pour sécu pos de pnj spécial et arbre spécial

            for nbPointRepere in range(1, nbPts): # placement de tout les point repère
                if verifLigne5 == nbPointRepere: # ajout du pts A et B pour une ligne de 5 toute droite pour sécu placement des pnj autour de la riviere
                    if nombreRiviere != 0 and nombreRiviere != 3: 
                        pACoordsligne5 = [randint(((nombreRiviere)*CoupageMapRiviere - CouloirRiviere),((nombreRiviere)*CoupageMapRiviere + CouloirRiviere)),nbPointRepere*EspacementPointRepereRiviere] # on créer le point 1 de la map
                    else:
                        if nombreRiviere == 0:
                            pACoordsligne5 = [randint(0,6),nbPointRepere*EspacementPointRepereRiviere] # on créer le point 1 de la map pour les rivière de bordure
                        else:
                            pACoordsligne5 = [randint(LONGUEUR-7, LONGUEUR-2),nbPointRepere*EspacementPointRepereRiviere] # on créer le point 1 de la map
                    
                    listePointRepere.append(pACoordsligne5) # Ajout du point A car il devient un point repère à relier
                    pBcoordsligne5 = [pACoordsligne5[0], nbPointRepere*EspacementPointRepereRiviere + 5] # forme [x, y]
                    listePointRepere.append(pBcoordsligne5) # Ajout du point B car il devient un point repère à relier

                else:
                    if nombreRiviere != 0 and nombreRiviere != 3: 
                        coords = [randint(((nombreRiviere)*CoupageMapRiviere - CouloirRiviere),((nombreRiviere)*CoupageMapRiviere + CouloirRiviere)),nbPointRepere*EspacementPointRepereRiviere] # on créer le point 1 de la map
                    else:
                        if nombreRiviere == 0:
                            coords = [randint(0,6),nbPointRepere*EspacementPointRepereRiviere] # on créer le point 1 de la map pour les rivière de bordure
                        else:
                            coords = [randint(LONGUEUR-7, LONGUEUR-2),nbPointRepere*EspacementPointRepereRiviere] # on créer le point 1 de la map
                    
                    # Tout les autres pts de repère
                    listePointRepere.append(coords) # on ajoute ces points dans la liste des points à relier
            

            # on crée l'avant dernier point
            if nombreRiviere != 0 and nombreRiviere != 3: 
                coordsPts3Riviere = [randint(((nombreRiviere)*CoupageMapRiviere - CouloirRiviere),((nombreRiviere)*CoupageMapRiviere + CouloirRiviere)),self.largeur-5] # on créer le point 1 de la map
            else:
                if nombreRiviere == 0:
                    coordsPts3Riviere = [randint(0,6),self.largeur-5] # on créer le point 1 de la map pour les rivière de bordure
                else:
                    coordsPts3Riviere = [randint(LONGUEUR-7, LONGUEUR-2),self.largeur-5] # on créer le point 1 de la map
                     
            # Point du bas (dernier element)
            # permet de créer une ligne pour éviter les collisions avec les bordures
            listePointRepere.append(coordsPts3Riviere) # forme [x,y]  on ajoute l'avant dernier point repère
            coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1]+4] # on crée le dernier point avec une huteur de +4
            listePointRepere.append(coordsPts4Riviere) # forme [x,y] on ajoute le dernier point repère de la riviere


            # On ajoute les pts repère sur la map + les point spéciaux (haut et bas ) directement car collision avec montagne, donc il faut une ligne de 4 droite minimum
            for coordsPointRepere in listePointRepere: # positions de tout les points repère de la riviere
                self.map[coordsPointRepere[1]][coordsPointRepere[0]] = "#" # on ajoute les pts repère sur la map normal (comme précédement)
                self.baseMap[coordsPointRepere[1]][coordsPointRepere[0]] = "#"   # ajoute egalement les points repères de la riviere sur la map de base
                listeCheminRiviere.append([coordsPointRepere[0],coordsPointRepere[1]]) # forme [x,y]

            
            # Pour tout les points repère, on lie des points A et B entre eux avec le script crée pour l'occasion ! (confection maison)
            for nbPointRepereRiviere in range(len(listePointRepere)-1): # boucle avec indice -1 car on envoie le pts actuelle et le suivant pour les lier (n et  n+1)
                start = [listePointRepere[nbPointRepereRiviere][0], listePointRepere[nbPointRepereRiviere][1]] # fomre [x,y] start = aux coords du points actuel 
                goal = [listePointRepere[nbPointRepereRiviere+1][0], listePointRepere[nbPointRepereRiviere+1][1]] # fomre [x,y]   goal = coords du points suivant
                path = LiaisonAtoB(start, goal).GetPos()     # path de coords en [x,y]  script fait maison pour relier les points entre deux, on obtient une liste de position, correspondant au chemin à suivre


                # On recup la list de déplacement et on ajoute la rivière aux deux map
                for coords in path: # parcourt de la liste
                    self.map[coords[1]][coords[0]] = "#"  # ajout de l'element rivière sur la map (collision)
                    self.baseMap[coords[1]][coords[0]] = "#" # ajout de l'element rivière sur la map (base)
                    listeCheminRiviere.append([coords[0],coords[1]]) # forme [x,y]  # stock des coords de toute la riviere dans la liste des coordonnées

            AjoutJsonMapValue(listeCheminRiviere, "coordsMapBase", f"Riviere{nombreRiviere} Coords") # stockage des valeurs dans le fichier json

    def __PlacementMud__(self):
        """ Méthode permettant de placer la boue sur la map de base"""
        listeMud = [] # liste qui va stocker toutes les coords des obstacles
        for _ in range(self.mud): # boucle pour le nombre d'obstacle différents
            mudPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] pos random sur la map, en éviant les bordure

            while ((self.baseMap[mudPos[1]][mudPos[0]] != '-') or (self.map[mudPos[1]][mudPos[0]] != '-') or (self.map[mudPos[1]-1][mudPos[0]] == 'O') ): # check de s'il y a déjà des éléments pour ne pas avoir de visuel nul  # dernier element pour checl pour savoir s'il y a un arbre au dessus, car pas beau cr arbre plusieurs cases
                mudPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] # on replace si jamais il y a un element
            self.baseMap[mudPos[1]][mudPos[0]] = "M" # on ajoute sur la map de test l'object
            listeMud.append(mudPos) # forme  [x,y] # on ajoute les coords de l'obstacle dans la liste de stockage

        AjoutJsonMapValue(listeMud, "coordsMapBase", "Mud Coords") # on ajoute au fichier json, la vrai liste de coordonnée des mud

    def __PlacementRock__(self):
        """Méthode permettant de placer les petits rochers sur la map de base"""
        listeRock = [] # liste qui va stocker toutes les coords des obstacles
        for _ in range(self.rock): # boucle pour le nombre d'obstacle différents
            rockPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] pos random sur la map, en éviant les bordure
            while ((self.baseMap[rockPos[1]][rockPos[0]] != '-') or (self.map[rockPos[1]][rockPos[0]] != '-') or (self.map[rockPos[1]-1][rockPos[0]] == 'O')): # check de s'il y a déjà des éléments pour ne pas avoir de visuel nul
                rockPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] # on replace si jamais il y a un element
            self.baseMap[rockPos[1]][rockPos[0]] = "R" # on ajoute sur la map de test l'object
            listeRock.append(rockPos) # forme  [x,y] # on ajoute les coords de l'obstacle dans la liste de stockage

        AjoutJsonMapValue(listeRock, "coordsMapBase", "Rock Coords") # on ajoute au fichier json, la vrai liste de coordonnée des rock

    def __PlacementObstacle__(self) -> None:
        """Méthode permettant de placer aléatoirement les obstacles sur la map. Cette méthode contient également un systhème de vérification vis à vis de la possibilit de réalise le niveau.
        Grâce à un script reprenant l'algo A*, tout les points importants de la map dans l'ordre de déroulement, sont relier un par un, si tout les points ont pu etre relier, alors la map et faisable, sinon non.
        Alors on regénère les obstacles jusqu'a ce que la map soit faisable par le joueur. """

        #placement des obstacle sur la map
        checkDeplacementPasPossible = True
        while checkDeplacementPasPossible: # boucle tant que la map n'est pas finissable par le joueur 
            
            # copie de la map pour les test
            self.mapCheckDeplacementPossible = []
            self.mapCheckDeplacementPossible = copy.deepcopy(self.map)   # deep copy pour éviter les liaisons des cellules mémoires et donc influer sur la vrai map + eviter d'utiliser une double for

            listeObstacle = [] # liste qui va stocker toutes les coords des obstacles
            for _ in range(self.obstacle): # boucle pour le nombre d'obstacle différents
                obstaclePos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] pos random sur la map, en éviant les bordure
                while self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] != '-' or self.mapCheckDeplacementPossible[obstaclePos[1]+1][obstaclePos[0]] != '-': # check de s'il y a déjà des éléments sur la map de test (map).
                    obstaclePos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] # on replace si jamais il y a un element
                self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] = "O" # on ajoute sur la map de test l'object


                listeObstacle.append(obstaclePos) # forme  [x,y] # on ajoute les coords de l'obstacle dans la liste de stockage

            # base check # GROSSE VERIF : 
            # 3 liste, 3 verif car quand il y az ue rivire il faut d'écaler le point de départ, car un pont sera poser pour permettre au joueur de traverser la riviere
            # spawn, pnj1, arbre spécial, pnj2, pnj3, sortie
            listeOrdrePointCle1 = [ # partie gauche map (avant riviere)
                                [8,2],  
                                [self.coordsPNJ[0][0], self.coordsPNJ[0][1]],
                                LoadJsonMapValue("coordsMapObject", "ArbreSpecial Coords")
                                ]
            
            coordsApresPont1 = LoadJsonMapValue("coordsMapObject", "ArbreSpecial Coords")
            listeOrdrePointCle2 = [ # partie middle (entre les deux rivieres donc on a passé la premiere riviere (indice + 2))
                                [coordsApresPont1[0] + 2, coordsApresPont1[1]],
                                self.coordsPNJ[1], # +2 car on traverse la riviere
                                ]
            
            listeOrdrePointCle3 = [ # meme chose
                                [self.coordsPNJ[1][0] + 2, self.coordsPNJ[1][1]],
                                [self.coordsPNJ[2][0],self.coordsPNJ[2][1]], # +2 car on traverse la riviere
                                LoadJsonMapValue("coordsMapObject", "Exit")
                                ]

            # Pour chacune des listes, on check s'il existe un chemin liant les points entre deux dans l'ordre d'avancement. 
            # Check en trois niveau car la map est divisé en trois par les 2 rivières. Donc on passe les rivières pour pouvoir calculer
            if self.CheckNiveauPossible(listeOrdrePointCle1, ["-", "A", "P", "S"]): # Si true (donc possible), on continue 
                if self.CheckNiveauPossible(listeOrdrePointCle2,  ["-", "A", "P", "S"] ): # ///
                    if self.CheckNiveauPossible(listeOrdrePointCle3,  ["-", "A", "P", "S"] ): # //
                        AjoutJsonMapValue(listeObstacle, "coordsMapObject", "Obstacles Coords") # Si la map est possible, on stock les coords des obstacle dans le json
                        checkDeplacementPasPossible = False # on arrête la boucle
                        for coords in listeObstacle: # on met à jour la map (on place les objets dessus)
                            self.map[coords[1]][coords[0]] = "O" # placement aux différents cordonnées

    def Update(self) -> list:
        """Méthode de gestion de la créaion de la map pour le niveau plaine et riviere.
        Cette méthode est à appeler pour pouvoir build la map integralement, elle retourne la map de bas (sol) ainsi que la map avec différents objet (collisions...)"""
        # Attention, l'ordre de génération est important car certaines valeurs, sont dépendantes de d'autres...

        # map
        self.Bordure()
        self.__PlacementRiviere__() 
        self.__PlacementFleur__()
        self.__PlacementMud__()
        self.__PlacementRock__() # placement des petits cailloux sur la map (pas de collision)
        
        # spawn / exit
        super().PlacementElements([[8,2,"S"]], ["coordsMapObject", "Spawn"]) 
        coordSortie = self.__PlacementSpecial__("coordsMapBase", "Riviere3 Coords", "S")
        AjoutJsonMapValue(coordSortie, "coordsMapObject", "Exit")

        # pnj
        coordsPNJ2 = self.__PlacementSpecial__("coordsMapBase", "Riviere2 Coords", "P")
        self.coordsPNJ = [[randint(8,((self.longueur//3) -5)), randint(5, self.largeur-5), "P", 1], 
                    [coordsPNJ2[0], coordsPNJ2[1], "P", 2], 
                    [randint(((self.longueur//3)*2 +5), self.longueur-5), randint(5, self.largeur-8), "P", 3]]       
        super().PlacementElements(self.coordsPNJ, ["coordsMapObject", "PNJ Coords"]) # placement des pnj sur la map 

        # arbre interaction pnj
        coordsAbre = self.__PlacementSpecial__("coordsMapBase", "Riviere1 Coords", "A") 
        AjoutJsonMapValue(coordsAbre, "coordsMapObject", "ArbreSpecial Coords") 

        # tout les obstacles
        self.__PlacementObstacle__() 
        
                
        # On charge la map de base
        AjoutJsonMapValue(self.map, "coordsMapBase", "AllMapInfo")

        # On charche la map (collision)
        AjoutJsonMapValue(self.baseMap, "coordsMapBase", "AllMapBase")


        for i in range(len(self.map)):
            print(*self.map[i], sep=" ")

        for j in range(len(self.baseMap)):
            print(*self.baseMap[j], sep=" ")

        return self.map, self.baseMap # return des deux map pour pouvoir charger et mettre à jours les valeurs de la map



class NiveauMedievale(GestionNiveauMap):
    def __init__(self, longueur, largeur):
        super().__init__(longueur, largeur)
        self.rock = 300
        self.mud = 200 
        self.obstacle = 1000

    def CheckNiveauPossible(self, listOrdrePointCle :list, pathAccessible :list) -> bool:
        """Méthode permettant de vérifier si le niveau est possible, suite à la position des obstacle. Utilisation du script A* permettant de trouver un chemin avec les déplacements ZQSD s'il exite entre un point A et B
        Ces points, donnés dans l'ordre d'évolution de la map, représente les coordonnées des éléments que le joueurs doit allé voir (pnj, arbre, entré, sortie..)"""

        for pointCle in range(len(listOrdrePointCle)-1): #
            if  Astar(listOrdrePointCle[pointCle], listOrdrePointCle[pointCle+1],self.mapCheckDeplacementPossible, pathAccessible).a_star(): 
                continue
            else: # résolution du niveau est impossible
                return False # false pour niveau impossible
        return True # les chemins entre les points données existent  

    def Bordure(self):


        # bordure map  
        listeBordures = [] 
        for i in range(2):
            for j in range(self.longueur):
                self.map[i*(self.largeur-1)][j] = "B" 
                self.baseMap[i*(self.largeur-1)][j] = "B"  
                listeBordures.append([i*(self.largeur-1), j]) 

        # on stock les coordonnées des bordures (la liste) dans le json
        AjoutJsonMapValue(listeBordures, "coordsMapBase", "Bordures Coords")

   
    def __PlacementRiviere__(self) -> None:

        # création 2 rivières génération alétoire controlé
        for nombreRiviere in range(4): # 4 tours car 4 riviere
            listeCheminRiviere = [] # initialisation de la liste qui contiendra toutes les coordonnées de la riviere
            listePointRepere = [] # initialisation de la liste des pts repères

            # creation riviere 0 vertical
            if nombreRiviere == 0:
                    coordsPts1Riviere = [randint(0,6),0] # on créer le point 1 de la map pour les rivière de bordure

            # riviere 1 vertical
            if nombreRiviere == 1: 
                coordsPts1Riviere = [randint(((nombreRiviere)*CoupageMapRiviere2 - CouloirRiviere),((nombreRiviere)*CoupageMapRiviere2 + CouloirRiviere)),0] # on créer le point 1 de la map
            
            # riviere 2 vertical (moitié)
            if  nombreRiviere == 2:
                coordsPts1Riviere = [randint(LONGUEUR-7, LONGUEUR-2),25] # on créer le point 1 de la map

            if nombreRiviere == 3:
                allCoordsRiviere1 = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")
                coordsPts1Riviere = choice(allCoordsRiviere1)
                while not (25 <= coordsPts1Riviere[1] <= 35):
                    coordsPts1Riviere = choice(allCoordsRiviere1)

            listePointRepere.append(coordsPts1Riviere) # forme [x,y] on ajoute le premier point à la liste
            if nombreRiviere != 3:
                coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1]+4] # on crée le second point avec une hauteur de + 4
            else:
                coordsPts2Riviere = [coordsPts1Riviere[0] + 4, coordsPts1Riviere[1]] # on crée le second point avec une hauteur de + 4
            listePointRepere.append(coordsPts2Riviere) # forme [x,y] on ajoute le second point dans la liste

            # Point de haut en bas
            if nombreRiviere == 0 or nombreRiviere == 1 :
                nbPts = self.largeur // EspacementPointRepereRiviere    # placement tout les 15 de hauteur ...   
                verifLigne5 = randint(1,(nbPts-1)) # choix du lieu pour la ligne de 5 droite pour sécu pos de pnj spécial et arbre spécial
            else:
                if nombreRiviere == 2:
                    nbPts = (self.largeur-25) // EspacementPointRepereRiviere
                    verifLigne5 = randint(1,(nbPts-1)) 
                elif nombreRiviere == 3:
                    nbPointRepere = (self.longueur - 75) // EspacementPointRepereRiviere
                    verifLigne5 = randint(1,(nbPts-1)) 


            for nbPointRepere in range(1, nbPts): # placement de tout les point repère
                if verifLigne5 == nbPointRepere: # ajout du pts A et B pour une ligne de 5 toute droite pour sécu placement des pnj autour de la riviere
                    if nombreRiviere == 0 : 
                        pACoordsligne5 = [randint(0,6),nbPointRepere*EspacementPointRepereRiviere] # on créer le point 1 de la map pour les rivière de bordure
                    if nombreRiviere == 1:
                        pACoordsligne5 = [randint(((nombreRiviere)*CoupageMapRiviere2 - CouloirRiviere),((nombreRiviere)*CoupageMapRiviere2 + CouloirRiviere)),nbPointRepere*EspacementPointRepereRiviere ] # on créer le point 1 de la map
                    if nombreRiviere == 2:
                        pACoordsligne5 = [randint(LONGUEUR-7, LONGUEUR-2),nbPointRepere*EspacementPointRepereRiviere + 25] # on créer le point 1 de la map
                    if nombreRiviere == 3:
                        pACoordsligne5 = [nbPointRepere*EspacementPointRepereRiviere + 75, randint((30 - CouloirRiviere),(30 + CouloirRiviere))] # on créer le point 1 de la map

                    
                    listePointRepere.append(pACoordsligne5) # Ajout du point A car il devient un point repère à relier
                    if nombreRiviere != 3:
                        if nombreRiviere != 2:
                            pBcoordsligne5 = [pACoordsligne5[0], nbPointRepere*EspacementPointRepereRiviere + 5] # forme [x, y]
                        else:
                            pBcoordsligne5 = [pACoordsligne5[0], nbPointRepere*EspacementPointRepereRiviere + 5 + 25] # forme [x, y]

                    else:
                        pBcoordsligne5 = [nbPointRepere*EspacementPointRepereRiviere + 5 + 75, pACoordsligne5[1]] # forme [x, y]
                    listePointRepere.append(pBcoordsligne5) # Ajout du point B car il devient un point repère à relier

                else:
                    if nombreRiviere == 0 : 
                        coords = [randint(0,6),nbPointRepere*EspacementPointRepereRiviere] # on créer le point 1 de la map pour les rivière de bordure
                    if nombreRiviere == 1:
                        coords = [randint(((nombreRiviere)*CoupageMapRiviere2 - CouloirRiviere),((nombreRiviere)*CoupageMapRiviere2 + CouloirRiviere)),nbPointRepere*EspacementPointRepereRiviere ] # on créer le point 1 de la map
                    if nombreRiviere == 2:
                        coords = [randint(LONGUEUR-7, LONGUEUR-2),nbPointRepere*EspacementPointRepereRiviere + 25] # on créer le point 1 de la map
                    if nombreRiviere == 3:
                        coords = [nbPointRepere*EspacementPointRepereRiviere + 75, randint((30 - CouloirRiviere),(30 + CouloirRiviere))] # on créer le point 1 de la map

                    # Tout les autres pts de repère
                    listePointRepere.append(coords) # on ajoute ces points dans la liste des points à relier
            
            

            # on crée l'avant dernier point
            if nombreRiviere == 0: 
                coordsPts3Riviere = [randint(0,6),self.largeur-5] # on créer le point 1 de la map pour les rivière de bordure
            elif nombreRiviere == 1:
                coordsPts3Riviere = [randint(((nombreRiviere)*CoupageMapRiviere2 - CouloirRiviere),((nombreRiviere)*CoupageMapRiviere2 + CouloirRiviere)),self.largeur-5] # on créer le point 1 de la map
            elif nombreRiviere == 2: 
                coordsPts3Riviere = [randint(LONGUEUR-7, LONGUEUR-2),self.largeur-5] # on créer le point 1 de la map
            elif nombreRiviere == 3:
                allCoordsRiviere2 = LoadJsonMapValue("coordsMapBase", "Riviere2 Coords")
                coordsPts3Riviere = allCoordsRiviere2[0]

            # Point du bas (dernier element)
            # permet de créer une ligne pour éviter les collisions avec les bordures
            listePointRepere.append(coordsPts3Riviere) # forme [x,y]  on ajoute l'avant dernier point repère


            if nombreRiviere != 3:
                coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1]+4] # on crée le dernier point avec une huteur de +4
            else:
                x = coordsPts3Riviere[0]
                c = 0
                while x + c < LONGUEUR -1:
                    c+= 1
                coordsPts4Riviere = [coordsPts3Riviere[0]+ c, coordsPts3Riviere[1]] # on crée le dernier point avec une huteur de +4


            listePointRepere.append(coordsPts4Riviere) # forme [x,y] on ajoute le dernier point repère de la riviere

            print(nombreRiviere, listePointRepere)

            # On ajoute les pts repère sur la map + les point spéciaux (haut et bas ) directement car collision avec montagne, donc il faut une ligne de 4 droite minimum
            for coordsPointRepere in listePointRepere: # positions de tout les points repère de la riviere
                self.map[coordsPointRepere[1]][coordsPointRepere[0]] = "#" # on ajoute les pts repère sur la map normal (comme précédement)
                self.baseMap[coordsPointRepere[1]][coordsPointRepere[0]] = "#"   # ajoute egalement les points repères de la riviere sur la map de base
                listeCheminRiviere.append([coordsPointRepere[0],coordsPointRepere[1]]) # forme [x,y]

            
            # Pour tout les points repère, on lie des points A et B entre eux avec le script crée pour l'occasion ! (confection maison)
            for nbPointRepereRiviere in range(len(listePointRepere)-1): # boucle avec indice -1 car on envoie le pts actuelle et le suivant pour les lier (n et  n+1)
                start = [listePointRepere[nbPointRepereRiviere][0], listePointRepere[nbPointRepereRiviere][1]] # fomre [x,y] start = aux coords du points actuel 
                goal = [listePointRepere[nbPointRepereRiviere+1][0], listePointRepere[nbPointRepereRiviere+1][1]] # fomre [x,y]   goal = coords du points suivant
                path = LiaisonAtoB(start, goal).GetPos()     # path de coords en [x,y]  script fait maison pour relier les points entre deux, on obtient une liste de position, correspondant au chemin à suivre


                # On recup la list de déplacement et on ajoute la rivière aux deux map
                for coords in path: # parcourt de la liste
                    self.map[coords[1]][coords[0]] = "#"  # ajout de l'element rivière sur la map (collision)
                    self.baseMap[coords[1]][coords[0]] = "#" # ajout de l'element rivière sur la map (base)
                    listeCheminRiviere.append([coords[0],coords[1]]) # forme [x,y]  # stock des coords de toute la riviere dans la liste des coordonnées

            AjoutJsonMapValue(listeCheminRiviere, "coordsMapBase", f"Riviere{nombreRiviere} Coords") # stockage des valeurs dans le fichier json
    
    def __PlacementFleur__(self) -> None:
        """A partir d'une génération du jeu de la vie de conway, les cellules vivantes correspondent à l'emplacement 
        des fleurs sur la map (base) du jeu"""

        getPosFleur = JeuDeLaVie(self.longueur, self.largeur).GetPos() # On récupère la liste de coordonnées des cellules vivantes
        listeFlowerCoords = [] # initialisation de la liste pour les coordonnées finales de position des fleurs
        for posFleur in getPosFleur: # on parcourt la liste de coordonnées
            # verif pour éviter de remplacer un bout de riviere / bordure / autre....
            if self.map[posFleur[1]][posFleur[0]] =="-": # si sur la map (obstacle) il n'y a rien aux coords indiqués
                self.baseMap[posFleur[1]][posFleur[0]] = "F" # on ajoute aux meme coordonnées dans la map base une fleur ("F")
                listeFlowerCoords.append(posFleur) # on stock les coordonnées de la fleur ajouté dans la liste

        AjoutJsonMapValue(listeFlowerCoords, "coordsMapBase", "Flowers Coords") # on ajoute au fichier json, la vrai liste de coordonnée des fleurs

    
    def __PlacementMud__(self):
        """ Méthode permettant de placer la boue sur la map de base"""
        listeMud = [] # liste qui va stocker toutes les coords des obstacles
        for _ in range(self.mud): # boucle pour le nombre d'obstacle différents
            mudPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] pos random sur la map, en éviant les bordure

            while ((self.baseMap[mudPos[1]][mudPos[0]] != '-') or (self.map[mudPos[1]][mudPos[0]] != '-') or (self.map[mudPos[1]-1][mudPos[0]] == 'O') or ( (75 <= mudPos[0] <= 149) and  (0 <= mudPos[1] <= 20)) ): # check de s'il y a déjà des éléments pour ne pas avoir de visuel nul  # dernier element pour checl pour savoir s'il y a un arbre au dessus, car pas beau cr arbre plusieurs cases
                mudPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] # on replace si jamais il y a un element
            self.baseMap[mudPos[1]][mudPos[0]] = "M" # on ajoute sur la map de test l'object
            listeMud.append(mudPos) # forme  [x,y] # on ajoute les coords de l'obstacle dans la liste de stockage

        AjoutJsonMapValue(listeMud, "coordsMapBase", "Mud Coords") # on ajoute au fichier json, la vrai liste de coordonnée des mud

    def __PlacementRock__(self):
        """Méthode permettant de placer les petits rochers sur la map de base"""
        listeRock = [] # liste qui va stocker toutes les coords des obstacles
        for _ in range(self.rock): # boucle pour le nombre d'obstacle différents
            rockPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] pos random sur la map, en éviant les bordure
            while ((self.baseMap[rockPos[1]][rockPos[0]] != '-') or (self.map[rockPos[1]][rockPos[0]] != '-') or (self.map[rockPos[1]-1][rockPos[0]] == 'O') or ( (75 <= rockPos[0] <= 149) and (0 <= rockPos[1] <= 20))): # check de s'il y a déjà des éléments pour ne pas avoir de visuel nul
                rockPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] # on replace si jamais il y a un element
            self.baseMap[rockPos[1]][rockPos[0]] = "R" # on ajoute sur la map de test l'object
            listeRock.append(rockPos) # forme  [x,y] # on ajoute les coords de l'obstacle dans la liste de stockage

        AjoutJsonMapValue(listeRock, "coordsMapBase", "Rock Coords") # on ajoute au fichier json, la vrai liste de coordonnée des rock

    def __PlacementChateau__(self):
        """"""
        
        coordsChateau = []
        ## muraille extérieur
            # coté gauche
        for i in range(25):
            pos = [69, i]
            coordsChateau.append(pos)

            # coté droite
        for i in range(25):
            pos = [LONGUEUR -1, i]
            coordsChateau.append(pos)

            # bas
        for i in range(81):
            pos = [69+i, 24]
            coordsChateau.append(pos)
        
        ## muraille interne
            # coté gauche
        for i in range(12):
            pos = [104, i]
            coordsChateau.append(pos)

            # coté droite
        for i in range(12):
            pos = [LONGUEUR -36, i]
            coordsChateau.append(pos)

            # bas
        for i in range(11):
            pos = [104+i, 11]
            coordsChateau.append(pos)
  

        coordsPorte = [[108,24],[109,24], [109,11]]
        # On recup la list de déplacement et on ajoute la rivière aux deux map
        for coords in coordsChateau: # parcourt de la liste
            if coords in coordsPorte:
                self.map[coords[1]][coords[0]] = "D"  # ajout de l'element rivière sur la map (collision)
                self.baseMap[coords[1]][coords[0]] = "D" # ajout de l'element rivière sur la map (base)
            else:
                self.map[coords[1]][coords[0]] = "C"  # ajout de l'element rivière sur la map (collision)
                self.baseMap[coords[1]][coords[0]] = "C" # ajout de l'element rivière sur la map (base)
        AjoutJsonMapValue(coordsChateau, "coordsMapObject", "Chateau Coords") # on ajoute au fichier json, la vrai liste de coordonnée des rock

    def __PlacementChamps__(self):
        
        coordsAllChamps = []
        nbChamps = randint(8,15)
        for i in range(nbChamps):


            checkCollideWhile = True

            while checkCollideWhile:
                checkCollideWhile = False
                larg = randint(5,12)
                long = randint(5,12)

                posX1 = randint(12, 55)
                posY1 = randint(1, 60)

                coordsHouse = []
                for x in range(posX1, posX1 + larg):
                    for y in range(posY1, posY1 + long):
                        coordsHouse.append([x, y])


                coordsSecu = []
                for x in range(posX1 - 1, posX1 + larg + 1):
                    for y in range(posY1 - 1, posY1 + long + 1):
                        # Ajouter uniquement les coordonnées qui ne font pas partie de la maison
                        if [x, y] not in coordsHouse:
                            coordsSecu.append([x, y])

            
                allCoorsElement = coordsSecu + coordsHouse

                for coordsE in allCoorsElement:
                    if coordsE in coordsAllChamps or self.map[coordsE[1]][coordsE[0]] != "-":
                        checkCollideWhile = True

                if not checkCollideWhile:
                    for co in coordsHouse:
                        coordsAllChamps.append(co)
       
        for coords in coordsAllChamps: # parcourt de la liste
            self.map[coords[1]][coords[0]] = "@"  # ajout de l'element rivière sur la map (collision)
            self.baseMap[coords[1]][coords[0]] = "@" # ajout de l'element rivière sur la map (base) 
        
        AjoutJsonMapValue(coordsAllChamps, "coordsMapObject", "Champs Coords")

    def __PlacementSpawn__(self):
        """Méthode de placement du spawn"""
        coordsRiviere1 = LoadJsonMapValue("coordsMapBase", "Riviere0 Coords")
        coordsSpawn = choice(coordsRiviere1)
        while not (25 <= coordsSpawn[1] <= 35) or self.map[coordsSpawn[1]][coordsSpawn[0]-1] == "#": # verif pont 1
            coordsSpawn = choice(coordsRiviere1)
        super().PlacementElements([[coordsSpawn[0]+1, coordsSpawn[1], "S"]], ["coordsMapObject", "Spawn"])
        self.map[coordsSpawn[1]][coordsSpawn[0]] = "T"

    def __PlacementExit__(self):
        coordsExit = (109, 1)
        super().PlacementElements([[coordsExit[0], coordsExit[1],"S"]], ["coordsMapObject", "Exit"])

    def __PlacementMaisons__(self):
       
    
        coordsVillage1 = []
        coordsVillage2 = []
        coordsVillage3 = []
       
        # village 1

        coordsPnj1 = self.coordsPNJ[0]
        checkCollideWhile = True

        while checkCollideWhile:
            checkCollideWhile = False

                    
            coordsHouse = [
                [coordsPnj1[0], coordsPnj1[1]-2], [coordsPnj1[0] +1, coordsPnj1[1]-2],
                [coordsPnj1[0], coordsPnj1[1] -1], [coordsPnj1[0] +1, coordsPnj1[1] -1],
            ]

            coordsVillage1.append(coordsHouse)
       
        # village 2
        nbHouseV2 = randint(25,40)
        coordsPuits = LoadJsonMapValue("coordsMapObject", "coords Puits")
        coordsTableCraft = [coordsPuits[3][0] +1, coordsPuits[3][1]]
        self.map[coordsTableCraft[1]][coordsTableCraft[0]] = "E"

        for i in range(nbHouseV2):
            
            checkCollideWhile = True

            while checkCollideWhile:
                checkCollideWhile = False
                posX1 = randint(78, 138)
                posY1 = randint(26, 72)

                coordsSecu = [
                    [posX1 -1, posY1 -1], [posX1, posY1 -1], [posX1+1, posY1-1],  [posX1 +2, posY1 -1],
                    [posX1 -1, posY1],                                            [posX1 +2, posY1], 
                    [posX1 -1, posY1 +1],                                         [posX1 +2, posY1 +1], 
                    [posX1 -1, posY1 +2], [posX1, posY1 +2], [posX1+1, posY1 +2], [posX1 +2, posY1 +2],
                ]
                coordsHouse = [
                    [posX1, posY1], [posX1 +1, posY1],
                    [posX1, posY1 +1], [posX1 +1, posY1 +1],
                ]

                allCoorsElement = coordsSecu + coordsHouse
                for coordsE in allCoorsElement:
                    for coordsUniqueHouse in coordsVillage2: # double list donc on rentre 
                        if coordsE in coordsUniqueHouse:
                            checkCollideWhile = True
                    if self.map[coordsE[1]][coordsE[0]] != "-" or coordsE in coordsPuits:
                        checkCollideWhile = True

                if not checkCollideWhile:
                    coordsVillage2.append(coordsHouse)
       
        # village 3
        nbHouseV3 = randint(35, 60)
        for i in range(nbHouseV3):
            
            checkCollideWhile = True

            while checkCollideWhile:
                checkCollideWhile = False
                posX1 = randint(68, 147)
                posY1 = randint(1, 21)

                coordsSecu = [
                    [posX1 -1, posY1 -1], [posX1, posY1 -1], [posX1+1, posY1-1],  [posX1 +2, posY1 -1],
                    [posX1 -1, posY1],                                            [posX1 +2, posY1], 
                    [posX1 -1, posY1 +1],                                         [posX1 +2, posY1 +1], 
                    [posX1 -1, posY1 +2], [posX1, posY1 +2], [posX1+1, posY1 +2], [posX1 +2, posY1 +2],
                ]
                coordsHouse = [
                    [posX1, posY1], [posX1 +1, posY1],
                    [posX1, posY1 +1], [posX1 +1, posY1 +1],
                ]

                allCoorsElement = coordsSecu + coordsHouse
                for coordsE in allCoorsElement:
                    for coordsUniqueHouse in coordsVillage3: # double list donc on rentre 
                        if coordsE in coordsUniqueHouse:
                            checkCollideWhile = True
                    if self.map[coordsE[1]][coordsE[0]] != "-" or (1 <= coordsE[1] < 13 and 102 <= coordsE[0] <= 113):
                        checkCollideWhile = True

                if not checkCollideWhile:
                    coordsVillage3.append(coordsHouse)
       
       

        coordsAllHouse = [coordsVillage1, coordsVillage2, coordsVillage3]              
        for blocCoords in coordsAllHouse: # parcourt de la liste
            for petitBlocCoords in blocCoords:
                for coords  in petitBlocCoords:
                    self.map[coords[1]][coords[0]] = "H"  # ajout de l'element rivière sur la map (collision)
                    self.baseMap[coords[1]][coords[0]] = "H" # ajout de l'element rivière sur la map (base) 


        AjoutJsonMapValue(coordsTableCraft, "coordsMapObject", "coords CraftTable")
        AjoutJsonMapValue(coordsAllHouse, "coordsMapObject", "coords Villages")
        
    def __PlacementPnj__(self):
        posX1 = randint(15, 60)
        posY1 = randint(10, 62)
        coordsRiviere3 = LoadJsonMapValue("coordsMapBase", "Riviere3 Coords")

        #pnj1
        coordsPnj1 = [posX1, posY1, "P", 1] 
        
        #pnj2
        getCoords2 = choice(coordsRiviere3)
        while getCoords2[0] < 85 or getCoords2[0] > 140 or self.map[getCoords2[1]-1][getCoords2[0]] != "-" or self.map[getCoords2[1]-2][getCoords2[0]] != "-" or self.map[getCoords2[1]+1][getCoords2[0]] != "-": 
            getCoords2 = choice(coordsRiviere3)
        coordsPnj2 = [getCoords2[0], getCoords2[1] +1, "P", 2]
        
        #pnj3
        coordsPnj3 = [108, 12, "P", 3]

        #pnj4
        coordsPnj4 = [109, 2, "P", 4] 

        self.coordsPNJ = [coordsPnj1, coordsPnj2, coordsPnj3, coordsPnj4]
        super().PlacementElements(self.coordsPNJ, ["coordsMapObject", "PNJ Coords"]) # placement des pnj sur la map 

    def __PlacementPath1__(self):
                
        # placement puits en avance pour pouvoir reier le path
        x1Puits, y1Puits = randint(90, 120), randint(40, 60)

        coordsPuits = [
                [x1Puits, y1Puits], [x1Puits +1, y1Puits],
                [x1Puits, y1Puits +1], [x1Puits +1, y1Puits +1],
            ] 

        for coords in coordsPuits:
            self.map[coords[1]][coords[0]] = "W"  # ajout de l'element PUITS sur la map (collision)
            self.baseMap[coords[1]][coords[0]] = "W" # ajout de l'element PUITS sur la map (base) 

            
        AjoutJsonMapValue(coordsPuits, "coordsMapObject", "coords Puits")

        
        allPath = []

        getCoordsSpawn = LoadJsonMapValue("coordsMapObject", "Spawn")
        coordsPts1 = getCoordsSpawn[0]
        coordsPts2 = [self.coordsPNJ[0][0], self.coordsPNJ[0][1]+1]

        getAllCoordsRiver1 = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")
        getCoordsFromRiver1 = choice(getAllCoordsRiver1)
        while getCoordsFromRiver1[1] < 38 or self.map[getCoordsFromRiver1[1]][getCoordsFromRiver1[0]-1] == "#" or  self.map[getCoordsFromRiver1[1]][getCoordsFromRiver1[0]+1] == "#":
            getCoordsFromRiver1 = choice(getAllCoordsRiver1)
        coordsPts3 = [getCoordsFromRiver1[0]-1,getCoordsFromRiver1[1]] 


        coordsPts4 = [coordsPts3[0]+2, coordsPts3[1]]
        coordsPts5 = coordsPuits[0]


        # partie gauche
        linkPoint1 = [coordsPts1, coordsPts2, coordsPts3]
        pathToAdd = LiaisonAtoB(linkPoint1[0], linkPoint1[1]).GetPos()
        for coords in pathToAdd:
            allPath.append(coords)

        pathToAdd = LiaisonAtoB(linkPoint1[1], linkPoint1[2]).GetPos()
        for coords in pathToAdd:
            allPath.append(coords)

        # parti droite bas
        linkPoint2 = [coordsPts4, coordsPts5] # passage river
        pathToAdd = LiaisonAtoB(linkPoint2[0], linkPoint2[1]).GetPos()
        for coords in pathToAdd:
            allPath.append(coords)

        for coords in allPath:
            if self.map[coords[1]][coords[0]] == "-":
                self.map[coords[1]][coords[0]] = "="  # ajout de l'element rivière sur la map (collision)
                self.baseMap[coords[1]][coords[0]] = "=" # ajout de l'element rivière sur la map (base) 
            
        AjoutJsonMapValue(coordsPts3, "coordsMapObject", "coords PassageRiver1")

        AjoutJsonMapValue(allPath, "coordsMapBase", "coords Path")
        
    def __PlacementPath2__(self):
        allPath = []
        coordsPuits = LoadJsonMapValue("coordsMapObject", "coords Puits")
        getAllCoordsVillage2 = LoadJsonMapValue("coordsMapObject", "coords Villages")
        getAllCoordsVillage2 = getAllCoordsVillage2[1]
        
        coordsToLinkHouse = []
        nbHousePath = randint(8, 15)
        indicesHouse = []
        for _ in range(nbHousePath):
            rand = randint(0, (len(getAllCoordsVillage2)-1))
            while rand in indicesHouse:
                rand = randint(0, (len(getAllCoordsVillage2)-1))
            indicesHouse.append(rand)
        
            
        for i in range(nbHousePath):
            side = randint(0,3)
            coordsToLinkHouse.append(getAllCoordsVillage2[indicesHouse[i]][side])

        for coordsHouse in coordsToLinkHouse:
            cotePuits = randint(0,3)
            pathToAdd = LiaisonAtoB(coordsHouse, coordsPuits[cotePuits]).GetPos()
            for coords in pathToAdd:
                allPath.append(coords)

        for coords in allPath:
            if self.map[coords[1]][coords[0]] == "-":
                self.map[coords[1]][coords[0]] = "="  # ajout de l'element rivière sur la map (collision)
                self.baseMap[coords[1]][coords[0]] = "=" # ajout de l'element rivière sur la map (base) 
        
        allPath1 = LoadJsonMapValue("coordsMapBase", "coords Path")
        newAllPath = allPath1 + allPath
        AjoutJsonMapValue(newAllPath, "coordsMapBase", "coords Path")

    def __PlacementObstacles__(self):

        #placement des obstacle sur la map
        checkDeplacementPasPossible = True
        while checkDeplacementPasPossible: 
            
            # copie de la map pour les test
            self.mapCheckDeplacementPossible = []
            self.mapCheckDeplacementPossible = copy.deepcopy(self.map)  

            listeObstacle = [] 
            for _ in range(self.obstacle):
                obstaclePos = [randint(0, self.longueur-1), randint(0, self.largeur-1)]
                while self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] != '-' or self.mapCheckDeplacementPossible[obstaclePos[1]+1][obstaclePos[0]] != '-' or (1 <= obstaclePos[1] < 13 and 102 <= obstaclePos[0] <= 113) : # check de s'il y a déjà des éléments sur la map de test (map).
                    obstaclePos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] 
                self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] = "O" 


                listeObstacle.append(obstaclePos) # forme  [x,y]
            # all coords : 
            getCoordsSpawn = LoadJsonMapValue("coordsMapObject", "Spawn")
            coordsPts1 = getCoordsSpawn[0]
            coordsPts2 = self.coordsPNJ[0]
            coordsPts3 = LoadJsonMapValue("coordsMapObject", "coords PassageRiver1")
            coordsPts4 = [coordsPts3[0]+2, coordsPts3[1]]
            coordsPts5 = LoadJsonMapValue("coordsMapObject", "coords CraftTable")
            getAllCoordsRiver1 = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")
            coordsPts6 = choice(getAllCoordsRiver1)
            while coordsPts6[0] < 35:
                coordsPts6 = choice(getAllCoordsRiver1)
            coordsPts7 = self.coordsPNJ[1]
            coordsPts8 = choice(getAllCoordsRiver1)
            while coordsPts8[1] >= 24 or self.map[coordsPts8[1]][coordsPts8[0]+1] != "-":
                coordsPts8 = choice(getAllCoordsRiver1)
            coordsPts9 = self.coordsPNJ[2]


            self.map[coordsPts8[1]][coordsPts8[0]] = "Z"



            # # verif deplacmeent possivlze
            listeOrdrePointCle1 = [ # partie gauche map (avant riviere)
                                coordsPts1,  
                                coordsPts2,
                                coordsPts3
                                ]
            
            listeOrdrePointCle2 = [ 
                                coordsPts4,
                                coordsPts5, # +2 car on traverse la riviere
                                coordsPts6,
                                coordsPts7
                                ]
            
            listeOrdrePointCle3 = [ # meme chose
                                coordsPts8,
                                coordsPts9
                                ]


            for i in range(len(self.map)):
                print(*self.map[i], sep=" ")

            for j in range(len(self.baseMap)):
                print(*self.baseMap[j], sep=" ")


            # Pour chacune des listes, on check s'il existe un chemin liant les points entre deux dans l'ordre d'avancement. 
            # Check en trois niveau car la map est divisé en trois par les 2 rivières. Donc on passe les rivières pour pouvoir calculer
            if self.CheckNiveauPossible(listeOrdrePointCle1, ["-", "A", "P", "S", "=", "Z"]): # Si true (donc possible), on continue 
                if self.CheckNiveauPossible(listeOrdrePointCle2,  ["-", "A", "P", "S", "=", "Z"] ): # ///
                    if self.CheckNiveauPossible(listeOrdrePointCle3,  ["-", "A", "P", "S", "=", "Z"] ): # //
                        AjoutJsonMapValue(listeObstacle, "coordsMapObject", "Obstacles Coords") # Si la map est possible, on stock les coords des obstacle dans le json
                        checkDeplacementPasPossible = False # on arrête la boucle
                        for coords in listeObstacle: # on met à jour la map (on place les objets dessus)
                            self.map[coords[1]][coords[0]] = "O" # placement aux différents cordonnées


        AjoutJsonMapValue(coordsPts8, "coordsMapObject", "RiverBoatTPChateau coords")

    def Update(self):

        self.Bordure()
        self.__PlacementRiviere__() 
        self.__PlacementFleur__()
        self.__PlacementMud__()
        self.__PlacementRock__() # placement des petits cailloux sur la map (pas de collision)
        
        self.__PlacementChateau__()

        # spawn / exit
        self.__PlacementSpawn__()
        self.__PlacementExit__()

        # pnj
        self.__PlacementPnj__()

        # path1
        self.__PlacementPath1__()
        
        # maisons
        self.__PlacementMaisons__()

        # path2
        self.__PlacementPath2__()

        # champs
        self.__PlacementChamps__()


        # obstacles 
        self.__PlacementObstacles__()



        for i in range(len(self.map)):
            print(*self.map[i], sep=" ")

        for j in range(len(self.baseMap)):
            print(*self.baseMap[j], sep=" ")

        return self.map, self.baseMap
    



# mapp, baseMap =  NiveauPlaineRiviere(150,75,200, 200, 200).Update()


# for i in range(50):
#     mapp, baseMap = NiveauMedievale(150,75).Update()
#     time.sleep(1)

mapp, baseMap = NiveauMedievale(150,75).Update()


# On affiche la map pour verif
