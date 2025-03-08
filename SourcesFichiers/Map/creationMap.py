# ---------------------------------------------- PyMathsQuest ---------------------------------------------- #

# Import des settings
from settings import *

# Import des scripts algo pour placer les par-terre de fleurs; relier 2 points entre eux; 
# check si le niveau est faisable en reliant chaque point clé du niveau entre eux
from SourcesFichiers.ScriptAlgo.jeuDeLaVie import *
from SourcesFichiers.ScriptAlgo.liaisonAtoB import *
from SourcesFichiers.ScriptAlgo.astar import *

class GestionNiveauMap(object):
    """Class parent création map, settings et méthode globales"""

    def __init__(self, longueur :int, largeur: int) -> None:
        """Initialisation des attributs """

        self.longueur = longueur 
        self.largeur = largeur 
        self.map = [] # map collision
        self.baseMap = [] # map sol
        self.ERROR_RELANCER = False
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
                        "ElementsTerre" : "null",
                        "AllMapInfo" : "null",
                        "AllMapBase" : "null"
                    },

                    "coordsMapObject" : {
                        "Obstacles Coords" : "null",
                        "PNJ Coords" : "null",
                        "ArbreSpecial Coords" : "null",
                        "Chateau Coords" : "null",
                        "Champs Coords" : "null",
                        "coords Volcan" : "null",
                        "coords Pont" : "null",
                        "coords Villages" : "null",
                        "coords Puits" : "null",
                        "coords PassageRiver1" : "null",
                        "coords CraftTable" : "null",
                        "RiverBoatTPChateau coords" : "null",
                        "salle1" : "null",
                        "salle2" : "null",
                        "salle3" : "null",
                        "salle4" : "null",
                        "liaisonsSalles" : "null",
                        "coordsVent" : "null",
                        "coordReacteurBloc" : "null",
                        "Spawn" : "null",
                        "Exit" : "null",
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
        with open(join("SourcesFichiers","Ressources","AllMapValue.json"), "w") as valueFileJson: 
            json.dump(data, valueFileJson, indent=4) 

    def PlacementElements(self, coordsElements, pathJson): 
        """Méthode permettant de placer le spawn du joueur sur la map (collision) et d'ajouter ces coordonnées dans le json"""
        for coordsPlacement in coordsElements: # on parcourt toute la liste de coords
            self.map[coordsPlacement[1]][coordsPlacement[0]] = coordsPlacement[2] # on place les element aux coordonnées sur la map (avec la lettre)
        AjoutJsonMapValue(coordsElements, pathJson[0], pathJson[1]) # on ajoute les coordonnées du spawn au fichier json






class NiveauPlaineRiviere(GestionNiveauMap):

    def __init__(self) -> None:
        """Initialisation des attributs de la class enfant"""
        super().__init__(150,75) 
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
        compteur = 0
        while checkDeplacementPasPossible and compteur < 100: 
            compteur += 1


            # copie de la map pour les test
            self.mapCheckDeplacementPossible = []
            self.mapCheckDeplacementPossible = copy.deepcopy(self.map)   # deep copy pour éviter les liaisons des cellules mémoires et donc influer sur la vrai map + eviter d'utiliser une double for

            listeObstacle = [] # liste qui va stocker toutes les coords des obstacles
            for _ in range(self.obstacle): # boucle pour le nombre d'obstacle différents
                obstaclePos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] pos random sur la map, en éviant les bordure
                while self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] != '-' or self.mapCheckDeplacementPossible[obstaclePos[1]+1][obstaclePos[0]] != '-' and self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]-2] != '-': # check de s'il y a déjà des éléments sur la map de test (map).
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

        ## SECURITE
        # verif si boucle pour relancement
        if compteur < 100:
            self.ERROR_RELANCER = False
        else:
            self.ERROR_RELANCER = True



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
        super().PlacementElements([[8,2,"S"], [9, 3, "J"]], ["coordsMapObject", "Spawn"]) 
        coordSortie = self.__PlacementSpecial__("coordsMapBase", "Riviere3 Coords", "S")
        AjoutJsonMapValue(coordSortie, "coordsMapObject", "Exit")

        # pnj
        coordsPNJ2 = self.__PlacementSpecial__("coordsMapBase", "Riviere2 Coords", "P")
        self.coordsPNJ = [[randint(8,((self.longueur//3) -5)), randint(5, self.largeur-5), "P", 1], 
                    [coordsPNJ2[0], coordsPNJ2[1], "P", 2], 
                    [randint(((self.longueur//3)*2 +5), self.longueur-9), randint(5, self.largeur-8), "P", 3]]       
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


        # relancer une nouvelle map
        if self.ERROR_RELANCER:
            return None, None, self.ERROR_RELANCER
        
        # Retourne la carte actuelle (map) et la carte de base (baseMap)
        return self.map, self.baseMap, self.ERROR_RELANCER



class NiveauMedievale(GestionNiveauMap):
    def __init__(self):
        """
        Initialise une instance du niveau médiéval.
        
        Args:
            longueur (int): La longueur de la carte.
            largeur (int): La largeur de la carte.
        """
        super().__init__(150,75)
        self.rock = 300  # Nombre d'éléments "rock" disponibles.
        self.mud = 200   # Nombre d'éléments "mud" disponibles.
        self.obstacle = 1000  # Nombre d'obstacles disponibles.

    def CheckNiveauPossible(self, listOrdrePointCle: list, pathAccessible: list) -> bool:
        """
        Vérifie si le niveau est jouable en testant si un chemin existe entre chaque point clé donné.

        Args:
            listOrdrePointCle (list): Liste des coordonnées des points clés (ex : PNJ, arbres, entrées, sorties).
            pathAccessible (list): Liste des types de terrains où le joueur peut se déplacer.

        Returns:
            bool: True si tous les points sont connectés, sinon False.
        """
        for pointCle in range(len(listOrdrePointCle) - 1):
            # Utilise l'algorithme A* pour vérifier si un chemin existe entre deux points consécutifs.
            if Astar(
                listOrdrePointCle[pointCle],
                listOrdrePointCle[pointCle + 1],
                self.mapCheckDeplacementPossible,
                pathAccessible
            ).a_star():
                continue  # Passe au prochain point s'il existe un chemin.
            else:
                return False  # Retourne False si un chemin est impossible.
        return True  # Tous les chemins sont accessibles.

    def Bordure(self):
        """
        Ajoute une bordure de la carte et stocke ses coordonnées dans un fichier JSON.
        """
        listeBordures = []  # Liste pour stocker les coordonnées des bordures.
        for i in range(2):  # Création des bordures horizontales (haut et bas).
            for j in range(self.longueur):
                self.map[i * (self.largeur - 1)][j] = "B"  # Ajout de bordure sur la carte principale.
                self.baseMap[i * (self.largeur - 1)][j] = "B"  # Ajout sur la carte de base.
                listeBordures.append([i * (self.largeur - 1), j])  # Stockage des coordonnées.

        # Stocke les coordonnées des bordures dans un fichier JSON.
        AjoutJsonMapValue(listeBordures, "coordsMapBase", "Bordures Coords")
   
    def __PlacementRiviere__(self) -> None:

        """
        Génère quatre rivières sur la carte en positionnant des points repères, 
        puis en reliant ces points par des chemins continus. Les rivières sont placées 
        de manière contrôlée mais avec certains aspects aléatoires pour varier leur positionnement.
        """
        for nombreRiviere in range(4):  # Générer 4 rivières
            listeCheminRiviere = []  # Stockage des coordonnées de la rivière entière
            listePointRepere = []   # Points spécifiques servant de repères pour tracer la rivière

            # Initialisation du premier point selon le numéro de la rivière
            if nombreRiviere == 0:  # Rivière 0 : position verticale, bord gauche
                coordsPts1Riviere = [randint(0, 6), 0]
            elif nombreRiviere == 1:  # Rivière 1 : verticale, zone contrôlée au centre gauche 
                coordsPts1Riviere = [randint(((nombreRiviere) * CoupageMapRiviere2 - CouloirRiviere),
                                            ((nombreRiviere) * CoupageMapRiviere2 + CouloirRiviere)), 0]
            elif nombreRiviere == 2:  # Rivière 2 : verticale, bord droit inférieur
                coordsPts1Riviere = [randint(LONGUEUR - 7, LONGUEUR - 2), 25]
            elif nombreRiviere == 3:  # Rivière 3 : débute à partir d'un point aléatoire de la rivière 1
                allCoordsRiviere1 = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")
                coordsPts1Riviere = choice(allCoordsRiviere1)
                while not (25 <= coordsPts1Riviere[1] <= 35):  # Assure que le point est dans une zone spécifique
                    coordsPts1Riviere = choice(allCoordsRiviere1)

            listePointRepere.append(coordsPts1Riviere)  # Ajouter le premier point repère

            # Déterminer le second point repère
            if nombreRiviere != 3:
                coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1] + 4]
            else:
                coordsPts2Riviere = [coordsPts1Riviere[0] + 4, coordsPts1Riviere[1]]
            listePointRepere.append(coordsPts2Riviere)

            # Calcul des points intermédiaires le long de la rivière
            if nombreRiviere in (0, 1):
                nbPts = self.largeur // EspacementPointRepereRiviere
            elif nombreRiviere == 2:
                nbPts = (self.largeur - 25) // EspacementPointRepereRiviere
            else:  # Rivière 3
                nbPts = (self.longueur - 75) // EspacementPointRepereRiviere

            verifLigne5 = randint(1, (nbPts - 1))  # Position pour une section droite spéciale de la rivière

            # Ajout des points repères intermédiaires
            for nbPointRepere in range(1, nbPts):
                if verifLigne5 == nbPointRepere:  # Cas d'une ligne droite pour PNJ et éléments spéciaux
                    if nombreRiviere == 0:
                        pACoordsligne5 = [randint(0, 6), nbPointRepere * EspacementPointRepereRiviere]
                    elif nombreRiviere == 1:
                        pACoordsligne5 = [randint(((nombreRiviere) * CoupageMapRiviere2 - CouloirRiviere),
                                                ((nombreRiviere) * CoupageMapRiviere2 + CouloirRiviere)),
                                        nbPointRepere * EspacementPointRepereRiviere]
                    elif nombreRiviere == 2:
                        pACoordsligne5 = [randint(LONGUEUR - 7, LONGUEUR - 2),
                                        nbPointRepere * EspacementPointRepereRiviere + 25]
                    elif nombreRiviere == 3:
                        pACoordsligne5 = [nbPointRepere * EspacementPointRepereRiviere + 75,
                                        randint((30 - CouloirRiviere), (30 + CouloirRiviere))]
                    
                    listePointRepere.append(pACoordsligne5)  # Ajouter le point A
                    if nombreRiviere != 3:
                        pBcoordsligne5 = [pACoordsligne5[0], pACoordsligne5[1] + 5]
                    else:
                        pBcoordsligne5 = [pACoordsligne5[0] + 5, pACoordsligne5[1]]
                    listePointRepere.append(pBcoordsligne5)  # Ajouter le point B
                else:  # Points repères normaux
                    if nombreRiviere == 0:
                        coords = [randint(0, 6), nbPointRepere * EspacementPointRepereRiviere]
                    elif nombreRiviere == 1:
                        coords = [randint(((nombreRiviere) * CoupageMapRiviere2 - CouloirRiviere),
                                        ((nombreRiviere) * CoupageMapRiviere2 + CouloirRiviere)),
                                nbPointRepere * EspacementPointRepereRiviere]
                    elif nombreRiviere == 2:
                        coords = [randint(LONGUEUR - 7, LONGUEUR - 2),
                                nbPointRepere * EspacementPointRepereRiviere + 25]
                    elif nombreRiviere == 3:
                        coords = [nbPointRepere * EspacementPointRepereRiviere + 75,
                                randint((30 - CouloirRiviere), (30 + CouloirRiviere))]
                    listePointRepere.append(coords)

            # Ajout des derniers points repères (avant-dernier et dernier)
            if nombreRiviere == 0:
                coordsPts3Riviere = [randint(0, 6), self.largeur - 5]
            elif nombreRiviere == 1:
                coordsPts3Riviere = [randint(((nombreRiviere) * CoupageMapRiviere2 - CouloirRiviere),
                                            ((nombreRiviere) * CoupageMapRiviere2 + CouloirRiviere)),
                                    self.largeur - 5]
            elif nombreRiviere == 2:
                coordsPts3Riviere = [randint(LONGUEUR - 7, LONGUEUR - 2), self.largeur - 5]
            elif nombreRiviere == 3:
                allCoordsRiviere2 = LoadJsonMapValue("coordsMapBase", "Riviere2 Coords")
                coordsPts3Riviere = allCoordsRiviere2[0]
            listePointRepere.append(coordsPts3Riviere)

            if nombreRiviere != 3:
                coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1] + 4]
            else:
                x = coordsPts3Riviere[0]
                c = 0
                while x + c < LONGUEUR - 1:
                    c += 1
                coordsPts4Riviere = [x + c, coordsPts3Riviere[1]]
            listePointRepere.append(coordsPts4Riviere)

            # Placement des points repères sur la carte
            for coordsPointRepere in listePointRepere:
                self.map[coordsPointRepere[1]][coordsPointRepere[0]] = "#"  # Rivière sur la carte
                self.baseMap[coordsPointRepere[1]][coordsPointRepere[0]] = "#"  # Rivière sur la carte de base
                listeCheminRiviere.append([coordsPointRepere[0], coordsPointRepere[1]])

            # Relier les points repères entre eux pour former la rivière
            for nbPointRepereRiviere in range(len(listePointRepere) - 1):
                start = listePointRepere[nbPointRepereRiviere]
                goal = listePointRepere[nbPointRepereRiviere + 1]
                path = LiaisonAtoB(start, goal).GetPos()
                for coords in path:
                    self.map[coords[1]][coords[0]] = "#"
                    self.baseMap[coords[1]][coords[0]] = "#"
                    listeCheminRiviere.append([coords[0], coords[1]])

            # Sauvegarder les coordonnées de la rivière dans un fichier JSON
            AjoutJsonMapValue(listeCheminRiviere, "coordsMapBase", f"Riviere{nombreRiviere} Coords")
    
    def __PlacementFleur__(self) -> None:
        """Place des fleurs sur la map en utilisant une génération basée sur le jeu de la vie de Conway.
        Les cellules vivantes correspondent aux emplacements des fleurs sur la map de base."""

        # Récupération des coordonnées des cellules vivantes générées par le jeu de la vie
        getPosFleur = JeuDeLaVie(self.longueur, self.largeur).GetPos()  
        listeFlowerCoords = []  # Liste pour stocker les coordonnées finales des fleurs

        # Parcourt des positions générées pour placer les fleurs
        for posFleur in getPosFleur:
            # Vérification : les fleurs ne doivent pas remplacer des éléments existants sur la map
            if self.map[posFleur[1]][posFleur[0]] == "-":  # Case libre uniquement
                self.baseMap[posFleur[1]][posFleur[0]] = "F"  # Ajout d'une fleur à la map de base
                listeFlowerCoords.append(posFleur)  # Ajout des coordonnées de la fleur à la liste

        # Sauvegarde des coordonnées des fleurs dans un fichier JSON
        AjoutJsonMapValue(listeFlowerCoords, "coordsMapBase", "Flowers Coords")  

    def __PlacementMud__(self):
        """Place de la boue (Mud) sur la map de base en évitant les collisions avec d'autres éléments."""

        listeMud = []  # Liste pour stocker les coordonnées des zones de boue

        # Placement des zones de boue en fonction du nombre défini
        for _ in range(self.mud):
            mudPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)]  # Position aléatoire initiale

            # Vérification des collisions : éviter de placer la boue sur d'autres éléments
            while ((self.baseMap[mudPos[1]][mudPos[0]] != '-') or 
                (self.map[mudPos[1]][mudPos[0]] != '-') or 
                (self.map[mudPos[1]-1][mudPos[0]] == 'O') or 
                ((75 <= mudPos[0] <= 149) and (0 <= mudPos[1] <= 20))):  # Conditions supplémentaires pour éviter des cas spécifiques
                mudPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)]  # Nouvelle tentative si condition non respectée

            # Ajout de la boue sur la map de base
            self.baseMap[mudPos[1]][mudPos[0]] = "M"  
            listeMud.append(mudPos)  # Stockage des coordonnées de la zone de boue

        # Sauvegarde des coordonnées des zones de boue dans un fichier JSON
        AjoutJsonMapValue(listeMud, "coordsMapBase", "Mud Coords")  

    def __PlacementRock__(self):
        """Place des petits rochers (Rock) sur la map de base en évitant les collisions avec d'autres éléments."""

        listeRock = []  # Liste pour stocker les coordonnées des rochers

        # Placement des rochers en fonction du nombre défini
        for _ in range(self.rock):
            rockPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)]  # Position aléatoire initiale

            # Vérification des collisions : éviter de placer le rocher sur d'autres éléments
            while ((self.baseMap[rockPos[1]][rockPos[0]] != '-') or 
                (self.map[rockPos[1]][rockPos[0]] != '-') or 
                (self.map[rockPos[1]-1][rockPos[0]] == 'O') or 
                ((75 <= rockPos[0] <= 149) and (0 <= rockPos[1] <= 20))):  # Conditions supplémentaires pour éviter des cas spécifiques
                rockPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)]  # Nouvelle tentative si condition non respectée

            # Ajout du rocher sur la map de base
            self.baseMap[rockPos[1]][rockPos[0]] = "R"  
            listeRock.append(rockPos)  # Stockage des coordonnées du rocher

        # Sauvegarde des coordonnées des rochers dans un fichier JSON
        AjoutJsonMapValue(listeRock, "coordsMapBase", "Rock Coords")  

    def __PlacementChateau__(self):
        """Place un château avec des murailles extérieures et intérieures sur la map."""

        # easter egg bloc interaction gong
        self.map[1][148] = "a"


        coordsChateau = []  # Liste pour stocker toutes les coordonnées des éléments du château

        # Construction des murailles extérieures
        for i in range(25):  
            coordsChateau.append([69, i])  # Mur gauche
            coordsChateau.append([LONGUEUR - 1, i])  # Mur droit
        for i in range(81):
            coordsChateau.append([69 + i, 24])  # Mur du bas

        coordsChateau.append([104, 0])  # pts ref chateau

        # Placement des éléments sur la map (C pour château, D pour portes)
        for coords in coordsChateau:
            self.map[coords[1]][coords[0]] = "C"  
            self.baseMap[coords[1]][coords[0]] = "C"  

        coordsDoorMurailles = [109, 24]
        self.map[coordsDoorMurailles[1]][coordsDoorMurailles[0]] = "d"  
        self.baseMap[coordsDoorMurailles[1]][coordsDoorMurailles[0]] = "d"

        # placement porte du chateau
        coordsDoor = [109, 10]
        self.map[coordsDoor[1]][coordsDoor[0]] = "D"  
        self.baseMap[coordsDoor[1]][coordsDoor[0]] = "D" 

        coordsChateau.append(coordsDoor)

        # Sauvegarde des coordonnées du château dans un fichier JSON
        AjoutJsonMapValue(coordsChateau, "coordsMapObject", "Chateau Coords")  

    def __PlacementChamps__(self):
        """Méthode qui place des champs sur la carte de manière aléatoire"""
        coordsAllChamps = []
        nbChamps = randint(8, 15)  # Nombre de champs à placer
        for _ in range(nbChamps):
            checkCollideWhile = True
            while checkCollideWhile:
                checkCollideWhile = False
                larg, long = randint(5, 12), randint(5, 12)  # Dimensions aléatoires pour le champ
                posX1, posY1 = randint(12, 55), randint(1, 60)  # Position de départ aléatoire

                # Calcul des coordonnées de la maison du champ
                coordsHouse = [[x, y] for x in range(posX1, posX1 + larg) for y in range(posY1, posY1 + long)]
                coordsSecu = [[x, y] for x in range(posX1 - 1, posX1 + larg + 1) for y in range(posY1 - 1, posY1 + long + 1) if [x, y] not in coordsHouse]

                allCoorsElement = coordsSecu + coordsHouse

                # Vérification des collisions avec d'autres éléments sur la carte
                for coordsE in allCoorsElement:
                    if coordsE in coordsAllChamps or self.map[coordsE[1]][coordsE[0]] != "-":
                        checkCollideWhile = True
                        break

                if not checkCollideWhile:
                    coordsAllChamps.extend(coordsHouse)  # Ajout des coordonnées du champ à la liste

        # Placement des champs sur la carte
        for coords in coordsAllChamps:
            self.map[coords[1]][coords[0]] = "@"
            self.baseMap[coords[1]][coords[0]] = "@"

        # Enregistrement des coordonnées des champs dans le fichier JSON
        AjoutJsonMapValue(coordsAllChamps, "coordsMapObject", "Champs Coords")

    def __PlacementSpawn__(self):
        """Méthode de placement du point de spawn"""
        coordsRiviere1 = LoadJsonMapValue("coordsMapBase", "Riviere0 Coords")  # Récupération des coordonnées de la rivière
        coordsSpawn = choice(coordsRiviere1)  # Sélection d'une position aléatoire pour le spawn

        # Vérification que le spawn est dans une zone valide
        while not (25 <= coordsSpawn[1] <= 35) or self.map[coordsSpawn[1]][coordsSpawn[0]-1] == "#" or self.map[coordsSpawn[1]][coordsSpawn[0]+1] == "#":
            coordsSpawn = choice(coordsRiviere1)  # Sélection d'une autre position si la première est invalide

        # Placement du spawn sur la carte
        super().PlacementElements([[coordsSpawn[0] + 1, coordsSpawn[1], "="]], ["coordsMapObject", "Spawn"]) # chemin element (on spawn dessus...)
        self.map[coordsSpawn[1]][coordsSpawn[0]] = "T"
        self.baseMap[coordsSpawn[1]][coordsSpawn[0] +1 ] = "="

    def __PlacementExit__(self):
        """Méthode de placement de la sortie"""
        coordsExit = (109, 1)  # Coordonnées fixes pour la sortie
        super().PlacementElements([[coordsExit[0], coordsExit[1], "S"]], ["coordsMapObject", "Exit"])

    def __PlacementMaisons__(self):
        """Place les maisons dans différents villages sur la carte"""
        coordsVillage1, coordsVillage2, coordsVillage3 = [], [], []

        # Village 1
        coordsPnj1 = self.coordsPNJ[0]
        coordsHouse = [
            [coordsPnj1[0], coordsPnj1[1] - 2], [coordsPnj1[0] + 1, coordsPnj1[1] - 2],
            [coordsPnj1[0], coordsPnj1[1] - 1], [coordsPnj1[0] + 1, coordsPnj1[1] - 1],
        ]
        coordsVillage1.append(coordsHouse)  # Ajout de la maison du premier village

        # Village 2
        nbHouseV2 = randint(25, 40)  # Nombre de maisons pour le village 2
        coordsPuits = LoadJsonMapValue("coordsMapObject", "coords Puits")  # Récupération des coordonnées du puits
        coordsTableCraft = [coordsPuits[3][0] + 1, coordsPuits[3][1]]  # Coordonnées de la table de craft
        self.map[coordsTableCraft[1]][coordsTableCraft[0]] = "E"  # Placement de la table de craft

        for i in range(nbHouseV2):
            checkCollideWhile = True
            while checkCollideWhile:
                checkCollideWhile = False
                posX1, posY1 = randint(78, 138), randint(36, 72)  # Position aléatoire pour la maison

                # Calcul des coordonnées de la maison et des zones de sécurité autour
                coordsSecu = [
                    [posX1 - 1, posY1 - 1], [posX1, posY1 - 1], [posX1 + 1, posY1 - 1], [posX1 + 2, posY1 - 1],
                    [posX1 - 1, posY1], [posX1 + 2, posY1], [posX1 - 1, posY1 + 1], [posX1 + 2, posY1 + 1],
                    [posX1 - 1, posY1 + 2], [posX1, posY1 + 2], [posX1 + 1, posY1 + 2], [posX1 + 2, posY1 + 2],
                ]
                coordsHouse = [
                    [posX1, posY1], [posX1 + 1, posY1],
                    [posX1, posY1 + 1], [posX1 + 1, posY1 + 1],
                ]

                allCoorsElement = coordsSecu + coordsHouse

                # Vérification des collisions avec d'autres maisons et éléments
                for coordsE in allCoorsElement:
                    for coordsUniqueHouse in coordsVillage2:
                        if coordsE in coordsUniqueHouse:
                            checkCollideWhile = True
                    if self.map[coordsE[1]][coordsE[0]] != "-" or coordsE in coordsPuits:
                        checkCollideWhile = True

                if not checkCollideWhile:
                    coordsVillage2.append(coordsHouse)

        # Village 3
        nbHouseV3 = randint(35, 60)  # Nombre de maisons pour le village 3
        for i in range(nbHouseV3):
            checkCollideWhile = True
            while checkCollideWhile:
                checkCollideWhile = False
                posX1, posY1 = randint(68, 147), randint(1, 21)  # Position aléatoire pour la maison

                # Calcul des coordonnées de la maison et des zones de sécurité autour
                coordsSecu = [
                    [posX1 - 1, posY1 - 1], [posX1, posY1 - 1], [posX1 + 1, posY1 - 1], [posX1 + 2, posY1 - 1],
                    [posX1 - 1, posY1], [posX1 + 2, posY1], [posX1 - 1, posY1 + 1], [posX1 + 2, posY1 + 1],
                    [posX1 - 1, posY1 + 2], [posX1, posY1 + 2], [posX1 + 1, posY1 + 2], [posX1 + 2, posY1 + 2],
                ]
                coordsHouse = [
                    [posX1, posY1], [posX1 + 1, posY1],
                    [posX1, posY1 + 1], [posX1 + 1, posY1 + 1],
                ]

                allCoorsElement = coordsSecu + coordsHouse

                # Vérification des collisions avec d'autres maisons et éléments
                for coordsE in allCoorsElement:
                    for coordsUniqueHouse in coordsVillage3:
                        if coordsE in coordsUniqueHouse:
                            checkCollideWhile = True
                    if self.map[coordsE[1]][coordsE[0]] != "-" or (1 <= coordsE[1] < 13 and 102 <= coordsE[0] <= 113):
                        checkCollideWhile = True

                if not checkCollideWhile:
                    coordsVillage3.append(coordsHouse)

        # Placement des villages sur la carte
        coordsAllHouse = [coordsVillage1, coordsVillage2, coordsVillage3]
        for blocCoords in coordsAllHouse:
            for petitBlocCoords in blocCoords:
                for coords in petitBlocCoords:
                    self.map[coords[1]][coords[0]] = "H"
                    self.baseMap[coords[1]][coords[0]] = "H"

        # Enregistrement des coordonnées des villages et de la table de craft
        AjoutJsonMapValue(coordsTableCraft, "coordsMapObject", "coords CraftTable")        
        AjoutJsonMapValue(coordsAllHouse, "coordsMapObject", "coords Villages")

    def __PlacementPnj__(self):
        # Génère une position aléatoire pour le premier PNJ (personnage non joueur)
        posX1 = randint(15, 60)
        posY1 = randint(10, 62)
        
        # Récupère les coordonnées de la rivière 3 à partir d'un fichier JSON
        coordsRiviere3 = LoadJsonMapValue("coordsMapBase", "Riviere3 Coords")

        # Placement du premier PNJ avec ses coordonnées (X, Y), type "P" et identifiant 1
        coordsPnj1 = [posX1, posY1, "P", 1] 
        
        # Placement du deuxième PNJ
        # Choisit aléatoirement une coordonnée parmi celles de la rivière 3
        getCoords2 = choice(coordsRiviere3)
        # Vérifie que les coordonnées choisies sont valides (autour de la rivière)
        while getCoords2[0] < 85 or getCoords2[0] > 140 or self.map[getCoords2[1]-1][getCoords2[0]] != "-" or self.map[getCoords2[1]-2][getCoords2[0]] != "-" or self.map[getCoords2[1]+1][getCoords2[0]] != "-": 
            getCoords2 = choice(coordsRiviere3)
        # Assigne la position du deuxième PNJ
        coordsPnj2 = [getCoords2[0], getCoords2[1] +1, "P", 2]
        # placement pont du garde
        self.map[coordsPnj2[1]-1][coordsPnj2[0]] = "X"
        
        # Placement fixe du troisième PNJ
        coordsPnj3 = [108, 12, "P", 3]


        # Stocke toutes les coordonnées des PNJ dans une liste
        self.coordsPNJ = [coordsPnj1, coordsPnj2, coordsPnj3]
        
        # Appelle la méthode PlacementElements pour ajouter les PNJ sur la carte
        super().PlacementElements(self.coordsPNJ, ["coordsMapObject", "PNJ Coords"])
        self.baseMap[coordsPnj1[1]][coordsPnj1[0]] = "=" # pathsous les pieds du pnj 1

    def __PlacementPath1__(self):
        # Génère une position aléatoire pour le puits
        x1Puits, y1Puits = randint(90, 120), randint(40, 60)

        # Définit les coordonnées de la zone occupée par le puits
        coordsPuits = [
                [x1Puits, y1Puits], [x1Puits +1, y1Puits],
                [x1Puits, y1Puits +1], [x1Puits +1, y1Puits +1],
            ] 

        # Place le puits sur la carte (dans self.map et self.baseMap) 
        for coords in coordsPuits:
            self.map[coords[1]][coords[0]] = "W"  # Ajout du puits sur la carte (collision)
            self.baseMap[coords[1]][coords[0]] = "W"  # Ajout du puits sur la carte de base

        # Sauvegarde les coordonnées du puits dans un fichier JSON
        AjoutJsonMapValue(coordsPuits, "coordsMapObject", "coords Puits")

        # Liste qui contiendra tous les chemins
        allPath = []

        # Récupère les coordonnées de départ du spawn à partir d'un fichier JSON
        getCoordsSpawn = LoadJsonMapValue("coordsMapObject", "Spawn")
        coordsPts1 = getCoordsSpawn[0]
        
        # Coordonnées du point suivant après le premier PNJ
        coordsPts2 = [self.coordsPNJ[0][0], self.coordsPNJ[0][1]+1]

        # Récupère les coordonnées de la rivière 1 à partir d'un fichier JSON
        getAllCoordsRiver1 = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")
        getCoordsFromRiver1 = choice(getAllCoordsRiver1)
        
        # Vérifie si la position choisie est valide pour le passage de la rivière
        while getCoordsFromRiver1[1] < 38 or self.map[getCoordsFromRiver1[1]][getCoordsFromRiver1[0]-1] == "#" or  self.map[getCoordsFromRiver1[1]][getCoordsFromRiver1[0]+1] == "#":
            getCoordsFromRiver1 = choice(getAllCoordsRiver1)
        
        # Définit les coordonnées du point de la rivière pour le chemin
        coordsPassageRiver1 = [getCoordsFromRiver1[0]-1, getCoordsFromRiver1[1]] 
        coordsPts3 = [getCoordsFromRiver1[0]-3, getCoordsFromRiver1[1]] 

        # Coordonnées du dernier point du chemin
        coordsPts4 = [coordsPassageRiver1[0]+3, coordsPassageRiver1[1]]
        coordsPts5 = coordsPuits[0]

        # Partie gauche du chemin
        linkPoint1 = [coordsPts1, coordsPts2, coordsPts3]
        
        # Crée le chemin entre les trois premiers points et ajoute les coordonnées
        pathToAdd = LiaisonAtoB(linkPoint1[0], linkPoint1[1]).GetPos()
        for coords in pathToAdd:
            allPath.append(coords)

        pathToAdd = LiaisonAtoB(linkPoint1[1], linkPoint1[2]).GetPos()
        for coords in pathToAdd:
            allPath.append(coords)

        # Partie droite du chemin (passage par la rivière)
        linkPoint2 = [coordsPts4, coordsPts5]
        pathToAdd = LiaisonAtoB(linkPoint2[0], linkPoint2[1]).GetPos()
        for coords in pathToAdd:
            allPath.append(coords)

        # Marque les cases du chemin avec "=" pour la rivière et les ajoute à la carte
        for coords in allPath:
            if self.map[coords[1]][coords[0]] in ["-", "F", "M", 'R']:
                self.map[coords[1]][coords[0]] = "="  # Ajout de la rivière sur la carte (collision)
                self.baseMap[coords[1]][coords[0]] = "="  # Ajout de la rivière sur la carte de base

        for element in range(6):
            if self.map[coordsPts3[1]][coordsPts3[0] + element] in ["-", "F", "M", 'R']:
                self.map[coordsPts3[1]][coordsPts3[0] + element] = "="  # Ajout de la rivière sur la carte (collision)
                self.baseMap[coordsPts3[1]][coordsPts3[0] + element] = "="  # Ajout de la rivière sur la carte de base
                allPath.append([coordsPts3[0] + element, coordsPts3[1]])
        # Sauvegarde les coordonnées du passage de la rivière dans un fichier JSON
        AjoutJsonMapValue(coordsPassageRiver1, "coordsMapObject", "coords PassageRiver1")
        
        # Sauvegarde toutes les coordonnées du chemin dans un fichier JSON
        AjoutJsonMapValue(allPath, "coordsMapBase", "coords Path")
        
    def __PlacementPath2__(self):
        # Liste qui contiendra tous les chemins générés
        allPath = []

        # Récupère les coordonnées du puits depuis un fichier JSON
        coordsPuits = LoadJsonMapValue("coordsMapObject", "coords Puits")
        
        # Récupère les coordonnées des villages depuis un fichier JSON et sélectionne le deuxième village
        getAllCoordsVillage2 = LoadJsonMapValue("coordsMapObject", "coords Villages")
        getAllCoordsVillage2 = getAllCoordsVillage2[1]
        
        # Liste des coordonnées des maisons à relier au puits
        coordsToLinkHouse = []
        
        # Choisit un nombre aléatoire de maisons à placer entre 8 et 15
        nbHousePath = randint(8, 15)
        
        # Liste pour stocker les indices des maisons choisies
        indicesHouse = []
        
        # Sélectionne des indices de maisons de manière aléatoire sans répétition
        for _ in range(nbHousePath):
            rand = randint(0, (len(getAllCoordsVillage2)-1))
            while rand in indicesHouse:
                rand = randint(0, (len(getAllCoordsVillage2)-1))
            indicesHouse.append(rand)
        
        # Pour chaque maison, on détermine une coordonnée aléatoire (sur un côté de la maison)
        for i in range(nbHousePath):
            side = randint(0, 3)
            coordsToLinkHouse.append(getAllCoordsVillage2[indicesHouse[i]][side])

        # Pour chaque maison, génère un chemin entre la maison et le puits
        for coordsHouse in coordsToLinkHouse:
            cotePuits = randint(0, 3)  # Sélectionne un côté du puits pour connecter la maison
            pathToAdd = LiaisonAtoB(coordsHouse, coordsPuits[cotePuits]).GetPos()  # Crée le chemin entre la maison et le puits
            for coords in pathToAdd:
                allPath.append(coords)  # Ajoute le chemin à la liste allPath

        # Met à jour la carte avec les chemins générés (rivières représentées par "=")
        for coords in allPath:
            if self.map[coords[1]][coords[0]] == "-":
                self.map[coords[1]][coords[0]] = "="  # Ajout de la rivière sur la carte (collision)
                self.baseMap[coords[1]][coords[0]] = "="  # Ajout de la rivière sur la carte de base

        # Charge tous les chemins existants depuis le fichier JSON et ajoute les nouveaux chemins
        allPath1 = LoadJsonMapValue("coordsMapBase", "coords Path")
        newAllPath = allPath1 + allPath
        # Sauvegarde les nouveaux chemins dans le fichier JSON
        AjoutJsonMapValue(newAllPath, "coordsMapBase", "coords Path")

    def __PlacementObstacles__(self):
        # Placement des obstacles sur la carte
        checkDeplacementPasPossible = True  # Flag pour vérifier si un déplacement est possible
        compteur = 0
        while checkDeplacementPasPossible and compteur < 100: 
            compteur += 1
            # Crée une copie de la carte pour tester les placements sans affecter la carte principale
            self.mapCheckDeplacementPossible = []
            self.mapCheckDeplacementPossible = copy.deepcopy(self.map)  

            # Liste pour stocker les positions des obstacles
            listeObstacle = [] 

            # Place les obstacles aléatoirement sur la carte, en vérifiant qu'ils ne se superposent pas
            for _i_ in range(self.obstacle):
                obstaclePos = [randint(0, self.longueur-1), randint(0, self.largeur-1)]
                # Vérifie que la position choisie est valide (case vide et pas dans une zone interdite)
                while self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] != '-' or self.mapCheckDeplacementPossible[obstaclePos[1]+1][obstaclePos[0]] != '-' or (1 <= obstaclePos[1] < 13 and 102 <= obstaclePos[0] <= 113):
                    obstaclePos = [randint(0, self.longueur-1), randint(0, self.largeur-1)]  # Nouvelle tentative
                # Marque la position comme occupée pour les tests
                self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] = "O"  
                listeObstacle.append(obstaclePos)  # Ajoute l'obstacle à la liste

            # Récupère les coordonnées des points clés (par exemple, spawn, passage de la rivière, etc.)
            getCoordsSpawn = LoadJsonMapValue("coordsMapObject", "Spawn")
            coordsPts1 = getCoordsSpawn[0]
            coordsPts2 = self.coordsPNJ[0]
            coordsPts3 = LoadJsonMapValue("coordsMapObject", "coords PassageRiver1")
            coordsPts4 = [coordsPts3[0]+2, coordsPts3[1]]
            coordsPts5 = LoadJsonMapValue("coordsMapObject", "coords CraftTable")
            
            # Sélectionne un point aléatoire sur la rivière 1
            getAllCoordsRiver1 = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")
            getCoordsRiver1Point = choice(getAllCoordsRiver1)
            while getCoordsRiver1Point[1] < 35 and getCoordsRiver1Point[1] != coordsPts3[1]:
                getCoordsRiver1Point= choice(getAllCoordsRiver1)
            coordsPts6 = [getCoordsRiver1Point[0]+1, getCoordsRiver1Point[1]]
            coordsPts7 = self.coordsPNJ[1]
            getCoordsRiver1Point2 = choice(getAllCoordsRiver1)
            while getCoordsRiver1Point2[1] >= 24 or self.mapCheckDeplacementPossible[getCoordsRiver1Point2[1]][getCoordsRiver1Point2[0]+1] != "-":
                getCoordsRiver1Point2 = choice(getAllCoordsRiver1)
            coordsPts8 =  [getCoordsRiver1Point2[0], getCoordsRiver1Point2[1]] # case river
            coordsPts9 = self.coordsPNJ[2]


            # Liste des points à vérifier pour les déplacements possibles
            listeOrdrePointCle1 = [coordsPts1, coordsPts2, coordsPts3]
            listeOrdrePointCle2 = [coordsPts4, coordsPts5, coordsPts6, coordsPts7]
            listeOrdrePointCle3 = [[coordsPts8[0] + 1, coordsPts8[1]], coordsPts9] # coords pts8 formaté pour ne pas etre sur la river

            # Vérifie la possibilité de déplacements pour chaque liste de points clés
            # Le parcours se fait en trois étapes, en passant par les rivières pour s'assurer que les chemins sont valides
            if self.CheckNiveauPossible(listeOrdrePointCle1, ["-", "A", "P", "S", "=", "E"]):  # Vérifie la première partie
                if self.CheckNiveauPossible(listeOrdrePointCle2,  ["-", "A", "P", "S", "=", "E"]):  # Vérifie la deuxième partie
                    if self.CheckNiveauPossible(listeOrdrePointCle3,  ["-", "A", "P", "S", "=", "E"]):  # Vérifie la troisième partie
                        # Si tout est valide, les obstacles peuvent être placés et les coordonnées sont sauvegardées
                        AjoutJsonMapValue(listeObstacle, "coordsMapObject", "Obstacles Coords")
                        checkDeplacementPasPossible = False  # Arrête la boucle

                        # Place les obstacles sur la carte
                        for coords in listeObstacle:
                            self.map[coords[1]][coords[0]] = "O"  # Placement des obstacles sur la carte

        ## SECURITE
        # verif si boucle pour relancement
        if compteur < 100:
            # Sauvegarde les coordonnées du transport de bateau vers le château dans un fichier JSON
            AjoutJsonMapValue(coordsPts8, "coordsMapObject", "RiverBoatTPChateau coords")
            self.ERROR_RELANCER = False
        else:
            self.ERROR_RELANCER = True

    def __AjustementRiver__(self):
        newCaseRiver = []
        # parcours et création de chaque sprites
        for ordonnees in range(len(self.baseMap)):
            for abscisses in range(len(self.baseMap[ordonnees])):

                if self.baseMap[ordonnees][abscisses] == "#":

                    # Vérification des bords pour éviter les erreurs d'index
                    can_go_up = ordonnees > 0
                    can_go_down = ordonnees < LARGEUR - 1
                    can_go_left = abscisses > 0
                    can_go_right = abscisses < 149

                    def checkBuildUp(can_go_up, can_go_left, can_go_right):
                        if can_go_up:
                            if self.baseMap[ordonnees -1][abscisses] == "C":
                                if can_go_right and can_go_left:
                                    if self.baseMap[ordonnees -2][abscisses-1] == "#" or self.baseMap[ordonnees -2][abscisses] == "#" or self.baseMap[ordonnees -2][abscisses +1] == "#":
                                        self.map[ordonnees -2][abscisses] = "#"
                                        newCaseRiver.append([abscisses, ordonnees -2])
                                elif can_go_left:
                                    if self.baseMap[ordonnees -2][abscisses-1] == "#" or self.baseMap[ordonnees -2][abscisses] == "#":   
                                        self.map[ordonnees -2][abscisses] = "#"
                                        newCaseRiver.append([abscisses, ordonnees -2])

                                elif can_go_right:
                                    if self.baseMap[ordonnees -2][abscisses] == "#" or self.baseMap[ordonnees -2][abscisses +1] == "#":   
                                        self.map[ordonnees -2][abscisses] = "#"  
                                        newCaseRiver.append([abscisses, ordonnees -2])

                    
                    def checkBuildDown(can_go_down, can_go_left, can_go_right): 
                        if can_go_down:
                            if self.baseMap[ordonnees +1][abscisses] == "C":
                                if can_go_right and can_go_left:
                                    if self.baseMap[ordonnees +2][abscisses-1] == "#" or self.baseMap[ordonnees +2][abscisses] == "#" or self.baseMap[ordonnees +2][abscisses +1] == "#":
                                        self.map[ordonnees +2][abscisses] = "#" 
                                        newCaseRiver.append([abscisses, ordonnees +2])
                                elif can_go_left:
                                    if self.baseMap[ordonnees +2][abscisses-1] == "#" or self.baseMap[ordonnees +2][abscisses] == "#":   
                                        self.map[ordonnees +2][abscisses] = "#" 
                                        newCaseRiver.append([abscisses, ordonnees +2])
                                elif can_go_right:
                                    if self.baseMap[ordonnees +2][abscisses] == "#" or self.baseMap[ordonnees +2][abscisses +1] == "#":   
                                        self.map[ordonnees +2][abscisses] = "#"    
                                        newCaseRiver.append([abscisses, ordonnees +2])

                     
                    
                    can_build_up = checkBuildUp(can_go_up, can_go_left, can_go_right)
                    can_build_down = checkBuildDown(can_go_down,  can_go_left, can_go_right)

        # syncronisation
        river1AllCoords = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")
        allRvier1Coords = river1AllCoords + newCaseRiver
        AjoutJsonMapValue(allRvier1Coords, "coordsMapBase", "Riviere1 Coords")
        for coords in newCaseRiver:
            self.baseMap[coords[1]][coords[0]] = "#"

    def Update(self):
        # Place la bordure de la carte (bords extérieurs)
        self.Bordure()

        # Place les rivières sur la carte
        self.__PlacementRiviere__()

        # Place des fleurs sur la carte
        self.__PlacementFleur__()

        # Place de la boue (mud) sur la carte
        self.__PlacementMud__()

        # Place des petits cailloux (rocks) sur la carte (sans collision)
        self.__PlacementRock__()

        # Place le château sur la carte
        self.__PlacementChateau__()

        # Place le point de spawn (l'endroit où le joueur commence)
        self.__PlacementSpawn__()

        # Place le point de sortie (l'endroit où le joueur doit aller)
        self.__PlacementExit__()

        # Place les PNJ (personnages non-joueurs) sur la carte
        self.__PlacementPnj__()

        # Place le premier chemin (path1) sur la carte
        self.__PlacementPath1__()

        # Place les maisons sur la carte
        self.__PlacementMaisons__()

        # Place le deuxième chemin (path2) sur la carte
        self.__PlacementPath2__()

        # Place les champs (zones agricoles ou similaires) sur la carte
        self.__PlacementChamps__()

        # Place les obstacles sur la carte (objets qui bloquent les déplacements)
        self.__PlacementObstacles__()

        # ajustement de la river
        self.__AjustementRiver__()


        # On charge la map de base
        AjoutJsonMapValue(self.map, "coordsMapBase", "AllMapInfo")

        # On charche la map (collision)
        AjoutJsonMapValue(self.baseMap, "coordsMapBase", "AllMapBase")




        # Affiche la carte finale (map) dans la console ligne par ligne pour visualisation
        for i in range(len(self.map)):
            print(*self.map[i], sep=" ")

        # Affiche également la carte de base (baseMap) pour comparaison ou débogage
        for j in range(len(self.baseMap)):
            print(*self.baseMap[j], sep=" ")

        # relancer une nouvelle map
        if self.ERROR_RELANCER:
            return None, None, self.ERROR_RELANCER
        
        # Retourne la carte actuelle (map) et la carte de base (baseMap)
        return self.map, self.baseMap, self.ERROR_RELANCER


class NiveauMedievaleChateau():
    def __init__(self):
       """Méhode initialisation valeur de la création de map demi niveau médievale"""
       
       # relancer si error de generation
       self.ERROR_RELANCER = False

    def Update(self):
        """Map n'est pas généré aléatoirement pour le chateau"""
        self.map = [
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "~", "~", "~", "~", "u", "~", "~", "~", "~", "o"],
            ["o", "~", "Y", "r", "~", "~", "~", "r", "Y", "~", "o"],
            ["o", "~", "~", "~", "~", "~", "~", "~", "~", "~", "o"],
            ["o", "~", "~", "~", "~", "~", "~", "~", "~", "~", "o"],
            ["o", "~", "Y", "r", "~", "~", "~", "r", "Y", "~", "o"],
            ["o", "~", "~", "~", "~", "~", "~", "~", "~", "~", "o"],
            ["o", "~", "~", "~", "~", "P", "~", "~", "~", "~", "o"],
            ["o", "~", "Y", "r", "~", "~", "~", "r", "Y", "~", "o"],
            ["o", "~", "~", "~", "~", "~", "~", "~", "~", "~", "o"],
            ["o", "o", "o", "o", "o", "D", "o", "o", "o", "o", "o"],
        ]

        self.baseMap = [
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "~", "~", "~", "U", "U", "U", "~", "~", "~", "o"],
            ["o", "~", "Y", "~", "U", "U", "U", "~", "Y", "~", "o"],
            ["o", "~", "~", "~", "~", "~", "~", "~", "~", "~", "o"],
            ["o", "~", "~", "~", "~", "~", "~", "~", "~", "~", "o"],
            ["o", "~", "Y", "~", "~", "~", "~", "~", "Y", "~", "o"],
            ["o", "~", "~", "~", "~", "~", "~", "~", "~", "~", "o"],
            ["o", "~", "~", "~", "~", "~", "~", "~", "~", "~", "o"],
            ["o", "~", "Y", "~", "~", "~", "~", "~", "Y", "~", "o"],
            ["o", "~", "~", "~", "~", "~", "~", "~", "~", "~", "o"],
            ["o", "o", "o", "o", "o", "D", "o", "o", "o", "o", "o"],
        ]


        AjoutJsonMapValue([[5, 9]], "coordsMapObject", "Spawn") # on ajoute les coordonnées du spawn au fichier json
        AjoutJsonMapValue([5, 1], "coordsMapObject", "Exit") # on ajoute les coordonnées du spawn au fichier json
        AjoutJsonMapValue([[5, 7, "P", 4]], "coordsMapObject", "PNJ Coords") # on ajoute les coordonnées du spawn au fichier json


        # On charge la map de base
        AjoutJsonMapValue(self.map, "coordsMapBase", "AllMapInfo")

        # On charche la map (collision)
        AjoutJsonMapValue(self.baseMap, "coordsMapBase", "AllMapBase")

        return self.map, self.baseMap, self.ERROR_RELANCER



class NiveauBaseFuturiste(GestionNiveauMap):
    def __init__(self):
        """
        Initialise une instance du niveau médiéval. """
        super().__init__(150,75)
        self.longueur = 150
        self.largeur = 75
        self.elementsTerre = 300
        self.obstacle = 75

    def CheckNiveauPossible(self, listOrdrePointCle: list, pathAccessible: list) -> bool:
        """
        Vérifie si le niveau est jouable en testant si un chemin existe entre chaque point clé donné.

        Args:
            listOrdrePointCle (list): Liste des coordonnées des points clés (ex : PNJ, arbres, entrées, sorties).
            pathAccessible (list): Liste des types de terrains où le joueur peut se déplacer.

        Returns:
            bool: True si tous les points sont connectés, sinon False.
        """
        for pointCle in range(len(listOrdrePointCle) - 1):
            # Utilise l'algorithme A* pour vérifier si un chemin existe entre deux points consécutifs.
            if Astar(
                listOrdrePointCle[pointCle],
                listOrdrePointCle[pointCle + 1],
                self.mapCheckDeplacementPossible,
                pathAccessible
            ).a_star():
                continue  # Passe au prochain point s'il existe un chemin.
            else:
                return False  # Retourne False si un chemin est impossible.
        return True  # Tous les chemins sont accessibles.


    def __PlacementElementsTerre__(self):
        """Place des petits rochers (Rock) sur la map de base en évitant les collisions avec d'autres éléments."""

        listeElementTerre = []  # Liste pour stocker les coordonnées des zones de boue

        # Placement des zones de boue en fonction du nombre défini
        for _ in range(self.elementsTerre):
            mudPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)]  # Position aléatoire initiale

            # Vérification des collisions : éviter de placer la boue sur d'autres éléments
            while ((self.baseMap[mudPos[1]][mudPos[0]] != '-') or (self.map[mudPos[1]][mudPos[0]] != '-') or self.map[mudPos[1]-1][mudPos[0]] == '$'):
                mudPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)]  # Nouvelle tentative si condition non respectée

            # Ajout de la boue sur la map de base
            self.baseMap[mudPos[1]][mudPos[0]] = "G"  
            listeElementTerre.append(mudPos)  # Stockage des coordonnées de la zone de boue

        # Sauvegarde des coordonnées des zones de boue dans un fichier JSON
        AjoutJsonMapValue(listeElementTerre, "coordsMapBase", "ElementsTerre Coords")  

    def __PlacementSalles__(self):
        """Méthode qui place des champs sur la carte de manière aléatoire"""

        # zone de map (pour placr les salles)
        zoneElement = [
                    [(9, 25), (30, 29)],
                    [(52, 0), (80, 6)],
                    [(52, 51), (80, 52)],
                    [(102, 25), (122, 29)],
                    ]
        allLiaisons = []
        
        salleBasiqueSol = [
            ["V", "V", "V", "V", "V", "V", "V", "v", "v", "v", "v", "v", "V", "V", "V", "V", "V", "V", "V"],
            ["V", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V"],
            ["V", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V"],
            ["V", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V"],
            ["V", ".", ".", ".", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", ".", ".", ".", "V"],
            ["V", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "V"],
            ["V", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "V"],
            ["v", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "v"],
            ["v", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "v"],
            ["v", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "v"],
            ["v", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "v"],
            ["v", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "v"],
            ["V", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "V"],
            ["V", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "V"],
            ["V", ".", ".", ".", "V", "V", "V", "V", "V", ".", "V", "V", "V", "V", "V", ".", ".", ".", "V"],
            ["V", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V"],
            ["V", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V"],
            ["V", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V"],
            ["V", "V", "V", "V", "V", "V", "V", "v", "v", "v", "v", "v", "V", "V", "V", "V", "V", "V", "V"],
        ]



        salleBasiqueCollision = [
            ["V", "V", "V", "V", "V", "V", "V", "v", "v", "v", "v", "v", "V", "V", "V", "V", "V", "V", "V"],
            ["V", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V"],
            ["V", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V"],
            ["V", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V"],
            ["V", ".", ".", ".", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", "V", ".", ".", ".", "V"],
            ["V", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "V"],
            ["V", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "V"],
            ["v", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "v"],
            ["v", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "v"],
            ["v", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "v"],
            ["v", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "v"],
            ["v", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "v"],
            ["V", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "V"],
            ["V", ".", ".", ".", "V", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V", ".", ".", ".", "V"],
            ["V", ".", ".", ".", "V", "V", "V", "V", "V", "m", "V", "V", "V", "V", "V", ".", ".", ".", "V"],
            ["V", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V"],
            ["V", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V"],
            ["V", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "V"],
            ["V", "V", "V", "V", "V", "V", "V", "v", "v", "v", "v", "v", "V", "V", "V", "V", "V", "V", "V"],
        ]

        for num in range(4):
            coordsSalle = []
            posX1, posY1 = randint(zoneElement[num][0][0], zoneElement[num][1][0]), randint(zoneElement[num][0][1], zoneElement[num][1][1])  # Position de départ aléatoire

            # Placement des champs sur la carte
            for y in range (len(salleBasiqueSol)):
                for x in range (len(salleBasiqueSol[y])):
                    self.map[posY1 + y][posX1 + x] = salleBasiqueCollision[y][x]
                    self.baseMap[posY1 + y][posX1 + x] = salleBasiqueSol[y][x]
                    coordsSalle.append([posX1 + x, posY1 + y, salleBasiqueCollision[y][x]])
            
            AjoutJsonMapValue(coordsSalle, "coordsMapObject", f"salle{num}")

            liaison = [
                    [posX1, posY1 + 9],
                    [posX1 + 9, posY1],
                    [posX1 + 18, posY1 + 9],
                    [posX1 + 9 , posY1 + 18],
                ]  
            allLiaisons.append(liaison)

        AjoutJsonMapValue(allLiaisons, "coordsMapObject", "liaisonsSalles")


    def __PlacementCouloirs__(self):
        allLisaison = LoadJsonMapValue("coordsMapObject", "liaisonsSalles")

        # liaison entre les salles
        linkS1S2 = [
            allLisaison[0][1], 
            [allLisaison[0][1][0], allLisaison[1][0][1]],
            [allLisaison[0][1][0]-2, allLisaison[1][0][1]], 
            allLisaison[1][0]]
        
        linkS1S3 = [
            allLisaison[0][3],  
            [allLisaison[0][3][0],allLisaison[2][0][1]],
            [allLisaison[0][3][0] -2,allLisaison[2][0][1]],
            allLisaison[2][0]]

        linkS4S2 = [
            allLisaison[3][1],  
            [allLisaison[3][1][0],allLisaison[1][2][1]],
            [allLisaison[3][1][0] +2,allLisaison[1][2][1]],
            allLisaison[1][2]]
        linkS4S3 = [
            allLisaison[3][3],  
            [allLisaison[3][3][0],allLisaison[2][2][1]],
            [allLisaison[3][3][0] +2,allLisaison[2][2][1]],
            allLisaison[2][2]]

        # liaison spawn salle1
        linkSpawnS1 = [
            [allLisaison[0][0][0] ,allLisaison[0][0][1]],
            [0, allLisaison[0][0][1]],
        ]



        allLinkElement = [linkS1S2, linkS1S3, linkS4S2, linkS4S3, linkSpawnS1]


        for i in range(len(allLinkElement)):
            for j in range(len(allLinkElement[i])-1):
                start = allLinkElement[i][j]
                goal = allLinkElement[i][j+1]
                mapAcces = self.map
                pathAcces = ["v", "-", "&"]
                path = Astar2(start, goal, mapAcces, pathAcces, 2).a_star()

                if path:
                    for coords in path:
                        self.map[coords[1]][coords[0]] =  "&" # ternaire choix sol
                        self.baseMap[coords[1]][coords[0]] =  "&"
        # checkVerif
        allPathCouloirs = []
        for ordonnes in range(len(self.map)):
            for abscisse in range (len(self.map[0])):
                if self.map[ordonnes][abscisse] == "&":
                    IsN =  self.map[ordonnes-1][abscisse] in ["&", "."]
                    IsS =  self.map[ordonnes+1][abscisse] in ["&", "."]
                    IsE =  self.map[ordonnes][abscisse-1] in ["&", "."]
                    IsW =  self.map[ordonnes][abscisse+1] in ["&", "."]
                    
                    IsNW = self.map[ordonnes-1][abscisse-1] in ["&", "."]
                    IsSW = self.map[ordonnes+1][abscisse-1] in ["&", "."]
                    IsNE = self.map[ordonnes-1][abscisse+1] in ["&", "."]
                    IsSE = self.map[ordonnes+1][abscisse+1] in ["&", "."]

                    listAllBuild = [IsN, IsW, IsS, IsE, IsNE, IsNW, IsSE, IsSW]
                    nb = listAllBuild.count(True)
                    if nb >7:
                        allPathCouloirs.append((abscisse, ordonnes))

        for coords in allPathCouloirs:
            self.map[coords[1]][coords[0]] =  "." # ternaire choix sol
            self.baseMap[coords[1]][coords[0]] =  "."


    def __PlacementVent__(self):
        allCoordsSalle0 = LoadJsonMapValue("coordsMapObject", "salle0")
        coordsVent1 = allCoordsSalle0[100]
        coordsVent2 = allCoordsSalle0[174]

        coordsVents = [coordsVent1, coordsVent2]
        for coords in coordsVents:
            self.map[coords[1]][coords[0]] = "j"

        AjoutJsonMapValue(coordsVents, "coordsMapObject", "coordsVent")


    def __PlacementSpawn__(self):
        allLisaison = LoadJsonMapValue("coordsMapObject", "liaisonsSalles")
        coordsSpawn =[ 2, allLisaison[0][0][1]]
        self.map[coordsSpawn[1]][coordsSpawn[0]] = "S"

        AjoutJsonMapValue([coordsSpawn], "coordsMapObject", "Spawn") # on ajoute les coordonnées du spawn au fichier json


    def __PlacementStructureSalles__(self):
        allCoordsSalle0 = LoadJsonMapValue("coordsMapObject", "salle0")
        allCoordsSalle1 = LoadJsonMapValue("coordsMapObject", "salle1")
        allCoordsSalle2 = LoadJsonMapValue("coordsMapObject", "salle2")
        allCoordsSalle3 = LoadJsonMapValue("coordsMapObject", "salle3")

        allSalles = [allCoordsSalle0, allCoordsSalle1, allCoordsSalle2, allCoordsSalle3]
        
        allStructuresName = ["§", "£", "$", "?"]
        allStructures = []
        for numSalle in range(len(allSalles)):
            ptsRef = allSalles[numSalle][140]

            # sécu pos salle
            for y in range(5):
                for x in range(5):
                    self.map[ptsRef[1] + y][ptsRef[0] + x] = "è"

            self.map[ptsRef[1]][ptsRef[0]] = allStructuresName[numSalle]
            
            if allStructuresName[numSalle] == "§":
                ptsRefInteraction = allSalles[numSalle][218]
                self.map[ptsRefInteraction[1]][ptsRefInteraction[0]] = "¤"    
                AjoutJsonMapValue(ptsRefInteraction, "coordsMapObject", "coordReacteurBloc")

            allStructures.append([ptsRef[0], ptsRef[1], allStructuresName[numSalle]])

    def __PlacementPNJ__(self):
        allCoordsSalle0 = LoadJsonMapValue("coordsMapObject", "salle0")
        allCoordsSalle1 = LoadJsonMapValue("coordsMapObject", "salle1")
        allCoordsSalle2 = LoadJsonMapValue("coordsMapObject", "salle2")
        allCoordsSalle3 = LoadJsonMapValue("coordsMapObject", "salle3")

        allSalles = [allCoordsSalle0, allCoordsSalle1, allCoordsSalle2, allCoordsSalle3]
        coordsPossiblesRefPNJ = [
                              (3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
            (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),
            (0,2),(1,2),                              (7,2),(8,2),
            (0,3),(1,3),                              (7,3),(8,3),
            (0,4),(1,4),                              (7,4),(8,4),
            (0,5),(1,5),                              (7,5),(8,5),
            (0,6),(1,6),                              (7,6),(8,6),
            (0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7),
            (0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8),
        ]
        
        self.allPNJCoords = []

        # pnj 1
        coordsSpawn = LoadJsonMapValue("coordsMapObject", "Spawn")
        self.map[coordsSpawn[0][1]][coordsSpawn[0][0] +8] = "P"
        self.allPNJCoords.append([coordsSpawn[0][0] + 8, coordsSpawn[0][1], "P", 1])

        # pnj 2 / 3 / 4 / 5
        for numSalle in range(len(allSalles)):
            ptsFixe = allSalles[numSalle][100]
            coordsPossiblesPNJ = [(coords[0] + ptsFixe[0], coords[1] + ptsFixe[1]) for coords in coordsPossiblesRefPNJ] 
            
            coordsPNJ = choice(coordsPossiblesPNJ)
            if numSalle !=3: # on ne crée pas de pnj pour le 3
                self.map[coordsPNJ[1]][coordsPNJ[0]] = "P"
            self.allPNJCoords.append([coordsPNJ[0], coordsPNJ[1], "P", numSalle+2])
        
        AjoutJsonMapValue(self.allPNJCoords, "coordsMapObject", "PNJ Coords") # on ajoute les coordonnées du spawn au fichier json

    def __ClearMapCaracteres__(self):

        for ordonnees in range(len(self.map)):
            for abscisses in range(len(self.map[ordonnees])):
                if self.map[ordonnees][abscisses] in ["V", "v"]:
                    self.map[ordonnees][abscisses] = "&"
                    self.baseMap[ordonnees][abscisses] = "&"


    def __PlacementObstacles__(self):
        # Placement des obstacles sur la carte
        checkDeplacementPasPossible = True  # Flag pour vérifier si un déplacement est possible
        compteur = 0
        while checkDeplacementPasPossible and compteur < 100: 
            compteur += 1
            # Crée une copie de la carte pour tester les placements sans affecter la carte principale
            self.mapCheckDeplacementPossible = []
            self.mapCheckDeplacementPossible = copy.deepcopy(self.map)  

            # Liste pour stocker les positions des obstacles
            listeObstacle = [] 

            # Place les obstacles aléatoirement sur la carte, en vérifiant qu'ils ne se superposent pas
            for _i_ in range(self.obstacle):
                obstaclePos = [randint(0, self.longueur-1), randint(0, self.largeur-1)]
                # Vérifie que la position choisie est valide (case vide et pas dans une zone interdite)
                while self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] != '.'\
                    or self.mapCheckDeplacementPossible[obstaclePos[1]-1][obstaclePos[0]] not in [".", "k", "&"] \
                    or self.mapCheckDeplacementPossible[obstaclePos[1]+1][obstaclePos[0]]  not in [".", "k", "&"] \
                    or self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]+1]  not in [".", "k", "&"] \
                    or self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]-1]  not in [".", "k", "&"] :
                    obstaclePos = [randint(0, self.longueur-1), randint(0, self.largeur-1)]  # Nouvelle tentative
                # Marque la position comme occupée pour les tests
                self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] = "k"  
                listeObstacle.append(obstaclePos)  # Ajoute l'obstacle à la liste

            # Récupère les coordonnées des points clés (par exemple, spawn, passage de la rivière, etc.)
            getCoordsSpawn = LoadJsonMapValue("coordsMapObject", "Spawn")
            coordsPts1 = getCoordsSpawn[0]
            coordsPts2 = self.allPNJCoords[0]
            coordsAllVent = LoadJsonMapValue("coordsMapObject", "coordsVent")
            coordsPts3 = coordsAllVent[1] 
            coordsPts4 = coordsAllVent[0]
            coordsPts5 = self.allPNJCoords[1]
            coordsPts6 = LoadJsonMapValue("coordsMapObject", "coordReacteurBloc")
            coordsPts7 = self.allPNJCoords[2]
            coordsPts8 = self.allPNJCoords[3]
            coordsPts9 = self.allPNJCoords[4]


            # Liste des points à vérifier pour les déplacements possibles
            listeOrdrePointCle1 = [coordsPts1, coordsPts2, coordsPts3]
            listeOrdrePointCle2 = [coordsPts4, coordsPts5, coordsPts6, coordsPts7, coordsPts8, coordsPts9]

            # Vérifie la possibilité de déplacements pour chaque liste de points clés
            # Le parcours se fait en trois étapes, en passant par les rivières pour s'assurer que les chemins sont valides
            if self.CheckNiveauPossible(listeOrdrePointCle1, [".", "S", "j", "m", "P", "¤"]):  # Vérifie la première partie
                if self.CheckNiveauPossible(listeOrdrePointCle2,  [".", "S", "j", "m", "P", "¤"]):  # Vérifie la deuxième partie
                    # Si tout est valide, les obstacles peuvent être placés et les coordonnées sont sauvegardées
                    AjoutJsonMapValue(listeObstacle, "coordsMapObject", "Obstacles Coords")
                    checkDeplacementPasPossible = False  # Arrête la boucle

                    # Place les obstacles sur la carte
                    for coords in listeObstacle:
                        self.map[coords[1]][coords[0]] = "k"  # Placement des obstacles sur la carte

        ## SECURITE
        # verif si boucle pour relancement
        if compteur < 100:
            self.ERROR_RELANCER = False
        else:
            self.ERROR_RELANCER = True


    def Update(self):

        
        
        self.__PlacementElementsTerre__()
        
        self.__PlacementSalles__()

        self.__PlacementCouloirs__()

        self.__PlacementVent__()

        self.__PlacementSpawn__()

        self.__PlacementStructureSalles__()

        self.__PlacementPNJ__()

        self.__ClearMapCaracteres__()

        self.__PlacementObstacles__()

        # le check générale du niveau n'est pas obligatoire car les chemin font une boucle (a voir si des obstacles sont ajoutés)


        # Affiche la carte finale (map) dans la console ligne par ligne pour visualisation
        for i in range(len(self.map)):
            print(*self.map[i], sep=" ")

        print(end="")
        # Affiche également la carte de base (baseMap) pour comparaison ou débogage
        for j in range(len(self.baseMap)):
            print(*self.baseMap[j], sep=" ")



        # relancer une nouvelle map
        if self.ERROR_RELANCER:
            return None, None, self.ERROR_RELANCER
        
        # Retourne la carte actuelle (map) et la carte de base (baseMap)
        return self.map, self.baseMap, self.ERROR_RELANCER  

    

class NiveauBaseFuturisteVaisseau():
    def __init__(self):
       """Méhode initialisation valeur de la création de map demi niveau base futursite vaisseau"""
       # relancer si error de generation
       self.ERROR_RELANCER = False

    def Update(self):
        self.map = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", "b", "b", "b", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", "i", "i", "i", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", "^", "P", "^", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", ".", ".", ".", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", "k", ".", ".", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", ".", ".", ".", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", "&", "m", "&", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ]

        self.baseMap = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", "b", "b", "b", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", "i", "i", "i", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", "^", ".", "^", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", ".", ".", ".", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", ".", ".", ".", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", ".", ".", ".", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "&", "&", "m", "&", "&", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ]
        AjoutJsonMapValue([[8, 10]], "coordsMapObject", "Spawn") # on ajoute les coordonnées du spawn au fichier json
        AjoutJsonMapValue([[8, 6, "P", 6]], "coordsMapObject", "PNJ Coords") # on ajoute les coordonnées du spawn au fichier json


        # On charge la map de base
        AjoutJsonMapValue(self.map, "coordsMapBase", "AllMapInfo")

        # On charche la map (collision)
        AjoutJsonMapValue(self.baseMap, "coordsMapBase", "AllMapBase")

        return self.map, self.baseMap, self.ERROR_RELANCER




class NiveauMordor(GestionNiveauMap):
    def __init__(self):
        """
        Initialise une instance du niveau médiéval. """
        super().__init__(150,75)
        self.longueur = 150
        self.largeur = 75
        self.rock = 350
        self.mud = 350
        self.obstacle = 800

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

    def __PlacementPont__(self):
        allCoordsRiver1 = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")
        allCoordsRiver2 = LoadJsonMapValue("coordsMapBase", "Riviere2 Coords")

        getCoords1 = choice(allCoordsRiver1)
        # Vérifie que les coordonnées choisies sont valides (autour de la rivière)
        while getCoords1[1] < 5 or getCoords1[1] > 70 or self.map[getCoords1[1]][getCoords1[0]-1] != "-" or self.map[getCoords1[1]][getCoords1[0]+1] != "-": 
            getCoords1 = choice(allCoordsRiver1)

        getCoords2 = choice(allCoordsRiver2)
        # Vérifie que les coordonnées choisies sont valides (autour de la rivière)
        while getCoords2[1] < 5 or getCoords2[1] > 70 or self.map[getCoords2[1]][getCoords2[0]-1] != "-" or self.map[getCoords2[1]][getCoords2[0]+1] != "-": 
            getCoords2 = choice(allCoordsRiver2)

        self.map[getCoords1[1]][getCoords1[0]] = "T" # pas interactions
        self.map[getCoords2[1]][getCoords2[0]] = "X" # interactions

        allPontCoords = [getCoords1, getCoords2]
        AjoutJsonMapValue(allPontCoords, "coordsMapObject", "coords Pont")
        

    def __PlacementStructures__(self):
        
        # vaisseau
        coordX, coordY = randint(8, 25), randint(3, 64)
        for ordonne in range(5):
            for abscisse in range(5):
                self.map[coordY + ordonne][coordX + abscisse] = "%"

        # spawn
        coordsSpawn = [coordX + 7, coordY +3]
        self.map[coordsSpawn[1]][coordsSpawn[0]] = "S"
        AjoutJsonMapValue([coordsSpawn], "coordsMapObject", "Spawn") # on ajoute les coordonnées du spawn au fichier json

        # prisions
        self.prisonStructure = [
            ["C", "-", "-", "-", "-", "C", "-", "-", "/", "C", "-", "-", "-", "C", "-", "-", "-", "-", "C"],
            ["C", "-", "-", "-", "-", "C", "-", "+", "-", "C", "-", "-", "-", "C", "-", "-", "-", "-", "C"],
            ["C", "-", "-", "-", "-", "C", "-", "-", "-", "C", "-", "-", "-", "C", "-", "-", "-", "-", "C"],
            ["C", "-", "-", "-", "-", "C", "c", "l", "c", "C", "c", "l", "c", "C", "-", "-", "-", "-", "C"],
            ["C", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "C"],
            ["C", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "C"],
            ["C", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "C"],
            ["C", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "C"],
            ["C", "C", "C", "C", "C", "C", "C", "C", "C", "D", "C", "C", "C", "C", "C", "C", "C", "C", "C"],
        ]
        
        coordsStartPrison = [65, 1]
        for ordonne in range(len(self.prisonStructure)):
            for abscisse in range(len(self.prisonStructure[ordonne])):
                self.map[coordsStartPrison[1] + ordonne][coordsStartPrison[0] + abscisse] = self.prisonStructure[ordonne][abscisse]


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


    def __PlacementCrateres__(self):
        """ Méthode permettant de placer la boue sur la map de base"""
        listeMud = [] # liste qui va stocker toutes les coords des obstacles
        for _ in range(self.mud): # boucle pour le nombre d'obstacle différents
            mudPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] pos random sur la map, en éviant les bordure

            while ((self.baseMap[mudPos[1]][mudPos[0]] != '-') or (self.map[mudPos[1]][mudPos[0]] != '-') or (self.map[mudPos[1]-1][mudPos[0]] == 'O') ): # check de s'il y a déjà des éléments pour ne pas avoir de visuel nul  # dernier element pour checl pour savoir s'il y a un arbre au dessus, car pas beau cr arbre plusieurs cases
                mudPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] # on replace si jamais il y a un element
            self.baseMap[mudPos[1]][mudPos[0]] = "M" # on ajoute sur la map de test l'object
            listeMud.append(mudPos) # forme  [x,y] # on ajoute les coords de l'obstacle dans la liste de stockage

        AjoutJsonMapValue(listeMud, "coordsMapBase", "Mud Coords") # on ajoute au fichier json, la vrai liste de coordonnée des mud

    def __PlacementVolcan__(self):
        allCoordsVolcan = []
        # volcan
        coordX, coordY = randint(110, 135), randint(3, 64)
        for ordonne in range(5):
            for abscisse in range(5):
                self.map[coordY + ordonne][coordX + abscisse] = "ù"
                allCoordsVolcan.append([coordX + abscisse, coordY + ordonne])

        # placement porte volcan
        self.map[coordY + 4][coordX + 2] = "f"

        AjoutJsonMapValue(allCoordsVolcan,"coordsMapObject", "coords Volcan")

    def __PlacementPNJ__(self):
        allCoordsPont = LoadJsonMapValue("coordsMapObject", "coords Pont")
        coordsPNJ1 = [allCoordsPont[0][0]-1, allCoordsPont[0][1], "P", 1]
        coordsPNJ2 = [76, 1, "P", 2] # dans la cellule de droite
        coordsPNJ3 = [74, 8, "P", 3]

        allCoordsVolcan = LoadJsonMapValue("coordsMapObject", "coords Volcan")
        ptsRefVolcan = allCoordsVolcan[0]

        xPNJ4 = randint((ptsRefVolcan[0] -15), (ptsRefVolcan[0] -1))
        yPNJ4 = randint((ptsRefVolcan[1] -15), (ptsRefVolcan[1] + 20)) 
        
        while xPNJ4 <= 108 or yPNJ4 >= 70 or yPNJ4 <= 4 or self.map[yPNJ4][xPNJ4] != "-":
            xPNJ4 = randint((ptsRefVolcan[0] -15), (ptsRefVolcan[0] -1))
            yPNJ4 = randint((ptsRefVolcan[1] -15), (ptsRefVolcan[1]+ 20))    
        # placement pnj 4 autour du volcan
        coordsPNJ4 = [xPNJ4, yPNJ4, "P", 4]

        allCoordsPNJ = [coordsPNJ1, coordsPNJ2, coordsPNJ3, coordsPNJ4]
        
        for CoordPNJ in allCoordsPNJ:
            self.map[CoordPNJ[1]][CoordPNJ[0]] = "P"

        AjoutJsonMapValue(allCoordsPNJ, "coordsMapObject", "PNJ Coords") # placement des pnj sur la map 
    
    
    def CheckNiveauPossible(self, listOrdrePointCle :list, pathAccessible :list) -> bool:
        """Méthode permettant de vérifier si le niveau est possible, suite à la position des obstacle. Utilisation du script A* permettant de trouver un chemin avec les déplacements ZQSD s'il exite entre un point A et B
        Ces points, donnés dans l'ordre d'évolution de la map, représente les coordonnées des éléments que le joueurs doit allé voir (pnj, arbre, entré, sortie..)"""

        for pointCle in range(len(listOrdrePointCle)-1): #
            if  Astar(listOrdrePointCle[pointCle], listOrdrePointCle[pointCle+1],self.mapCheckDeplacementPossible, pathAccessible).a_star(): 
                continue
            else: # résolution du niveau est impossible
                return False # false pour niveau impossible
        return True # les chemins entre les points données existent  


    def __PlacementObstacles__(self):
        # Placement des obstacles sur la carte
        checkDeplacementPasPossible = True  # Flag pour vérifier si un déplacement est possible
        compteur = 0
        while checkDeplacementPasPossible and compteur < 100: 
            compteur += 1
            # Crée une copie de la carte pour tester les placements sans affecter la carte principale
            self.mapCheckDeplacementPossible = []
            self.mapCheckDeplacementPossible = copy.deepcopy(self.map)  

            # Liste pour stocker les positions des obstacles
            listeObstacle = [] 

            # Place les obstacles aléatoirement sur la carte, en vérifiant qu'ils ne se superposent pas
            for _i_ in range(self.obstacle):
                obstaclePos = [randint(0, self.longueur-2), randint(0, self.largeur-1)]
                # Vérifie que la position choisie est valide (case vide et pas dans une zone interdite)
                while self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] != '-' or self.mapCheckDeplacementPossible[obstaclePos[1]-1][obstaclePos[0]] != '-' or self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]+1] != '-' or (1 <= obstaclePos[1] < 11 and 64 <= obstaclePos[0] <= 85):
                    obstaclePos = [randint(0, self.longueur-2), randint(0, self.largeur-1)]  # Nouvelle tentative
                # Marque la position comme occupée pour les tests
                self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] = "O"  
                listeObstacle.append(obstaclePos)  # Ajoute l'obstacle à la liste

            # Récupère les coordonnées des points clés (par exemple, spawn, passage de la rivière, etc.)
            
            #spawn
            getCoordsSpawn = LoadJsonMapValue("coordsMapObject", "Spawn")
            coordsPts1 = getCoordsSpawn[0]

            #pnj 1
            allPNJcoords = LoadJsonMapValue("coordsMapObject", "PNJ Coords")
            coordsPts2 = allPNJcoords[0]

            # prison
            coordsPts3 = [66,1]
            coordsPts4 = allPNJcoords[1]
            coordsPts5 = allPNJcoords[2]
            #pont passage vers dernier pnj
            coordsPts6 = allPNJcoords[3]
            # porte volcan
            allCoordsVolcan = LoadJsonMapValue("coordsMapObject", "coords Volcan")
            coordsPts7 = allCoordsVolcan[22]

            # Liste des points à vérifier pour les déplacements possibles
            listeOrdrePointCle1 = [coordsPts1, coordsPts2]
            listeOrdrePointCle2 = [coordsPts3, coordsPts4, coordsPts5, coordsPts6, coordsPts7]

            # Vérifie la possibilité de déplacements pour chaque liste de points clés
            # Le parcours se fait en trois étapes, en passant par les rivières pour s'assurer que les chemins sont valides
            if self.CheckNiveauPossible(listeOrdrePointCle1, ["-", "P", "f", "T", "X", "S", "D", "l"]):  # Vérifie la première partie
                if self.CheckNiveauPossible(listeOrdrePointCle2,  ["-", "P", "f", "T", "X", "S", "D", "l"]):  # Vérifie la deuxième partie
                    # Si tout est valide, les obstacles peuvent être placés et les coordonnées sont sauvegardées
                    AjoutJsonMapValue(listeObstacle, "coordsMapObject", "Obstacles Coords")
                    checkDeplacementPasPossible = False  # Arrête la boucle

                    # Place les obstacles sur la carte
                    for coords in listeObstacle:
                        self.map[coords[1]][coords[0]] = "O"  # Placement des obstacles sur la carte

        ## SECURITE
        # verif si boucle pour relancement
        if compteur < 100:
            # Sauvegarde les coordonnées du transport de bateau vers le château dans un fichier JSON
            self.ERROR_RELANCER = False
        else:
            self.ERROR_RELANCER = True



    def Update(self):

        # bordure
        self.Bordure()

        # riviere
        self.__PlacementRiviere__() 

        # pont
        self.__PlacementPont__()

        # structures
        self.__PlacementStructures__()

        # rock 
        self.__PlacementRock__()

        # mud 
        self.__PlacementCrateres__()

        # volcan 
        self.__PlacementVolcan__()

        #pnj
        self.__PlacementPNJ__()
        
        # obstalce 
        self.__PlacementObstacles__()
        

        # le check générale du niveau n'est pas obligatoire car les chemin font une boucle (a voir si des obstacles sont ajoutés)


        # Affiche la carte finale (map) dans la console ligne par ligne pour visualisation
        for i in range(len(self.map)):
            print(*self.map[i], sep=" ")

        print(end="")
        # Affiche également la carte de base (baseMap) pour comparaison ou débogage
        for j in range(len(self.baseMap)):
            print(*self.baseMap[j], sep=" ")



        # relancer une nouvelle map
        if self.ERROR_RELANCER:
            return None, None, self.ERROR_RELANCER
        
        # Retourne la carte actuelle (map) et la carte de base (baseMap)
        return self.map, self.baseMap, self.ERROR_RELANCER  

# mapp, baseMap =  NiveauPlaineRiviere(150,75,200, 200, 200).Update()

# mapp, baseMap, error = NiveauMordor().Update()

# mapp, baseMap, error = NiveauBaseFuturiste().Update()
# for i in range(25):
#     mapp, baseMap = NiveauMedievale(150, 75).Update()
#     time.sleep(1)

# mapp, baseMap = NiveauMedievale(150,75).Update()
