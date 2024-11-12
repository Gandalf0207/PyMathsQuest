# Ce scrit est celui de la génération des terrains et de ce qui les composent. Une class parent pose les bases, présentes sur chaque map,
# par la suite, chaque niveau possède sa classe enfant lui permetant d'ajouter les élements uniques de chaque niveau.

# On retrouve deux types principaux de map, la map (avec les obstacles mais sans les décors (fleurs..)); une map de base, possédent
# les coordonnées pour afficher les variations de l'herbe par exemple.


# ---------------------------------------------- PyMathsQuest ---------------------------------------------- #

# Import des settings
from settings import *

# Import des scripts algo pour placer les par-terre de fleurs; relier 2 points entre eux; 
# check si le niveau est faisable en reliant chaque point clé du niveau entre eux
from ScriptAlgo.jeuDeLaVie import *
from ScriptAlgo.liaisonAtoB import *
from ScriptAlgo.astar import *

class GestionNiveauMap(object):
    """class mère permettant de créer la base commmune de la map de toutes les
    autres class enfants pour les différents niveau du jeu."""

    def __init__(self, longueur :int, largeur: int) -> None:
        """Initialisation des attributs de la class mère"""
        self.longueur = longueur # longueur de la map
        self.largeur = largeur # largeur de la map
        self.map = [] # map avec les collision, pnj et points clés, sans variation du sol (double liste python)
        self.baseMap = [] # map pour seulement le sol

    def BaseMap(self) -> None:
        """Création de la double liste avec les bordures de la map(map)"""
        # map
        for _ in range(self.largeur): # largeur de la map (y)
            creationMap = [] # liste pour stocker les valeurs des colonnes (x)
            for _ in range(self.longueur): # longueur de la map (x)
                creationMap.append("-") # ajout des valeurs (x)
            self.map.append(creationMap) # ajout de la ligne entière
        
        # map base    | une copy profonde de map serait interessant pour éviter de répéter cette double boucle
        for _ in range(self.largeur): # largeur de la map (y)
            creationMap = [] # liste pour stocker les valeurs des colonnes (x)
            for _ in range(self.longueur): # longueur de la map (x)
                creationMap.append("-") # ajout des valeurs (x)                        
            self.baseMap.append(creationMap) # ajout de la ligne entière
        
        # position des bordure sur la map : 
        listeBordures = [] # stockage des coordonnées de ces bordurees
        for i in range(2):
            for j in range(self.longueur): # position des bordures haut et bas
                self.map[i*(self.largeur-1)][j] = "B" # on ajoute les bordures sur la map
                self.baseMap[i*(self.largeur-1)][j] = "B"  # on ajoute les bordures sur la map de base
                listeBordures.append([i*(self.largeur-1), j]) # ajout des vaeurs dans la liste de stockage

            for j in range(self.largeur): # position des bordures gauche et droites
                self.map[j][i*(self.longueur-1)] = "B" # on ajoute les bordures sur la map
                self.baseMap[j][i*(self.longueur-1)] = "B" # on ajoute les bordures sur la map de base
                listeBordures.append([j, i*(self.longueur-1)]) # ajout des vaeurs dans la liste de stockage

        # on stock les coordonnées des bordures (la liste) dans le json
        self.AjoutJsonMapValue(listeBordures, "coordsMapBase", "Bordures Coords")

    
    def BaseJson(self, data :dict) -> None:
        """Initialisation du fichier Json avec l'arbo du fichier contenu dans la variable data de chaque niveau"""
        with open("AllMapValue.json", "w") as valueFileJson: # Ouvrir le fichier en mode écriture
            json.dump(data, valueFileJson, indent=4) # charger la configuration pour le niveau (on ajotue le dictionnaire data au fichier json)

    def PlacementPNJ(self, coordPNJ :list) -> None:
        """ Selon les coordoonées données, placement des pnj sur la map, ajout de ces cordonnées au ficheir json"""
        for coords in coordPNJ: # On parcour la liste des coordonnées
            self.map[coords[1]][coords[0]] = "P" # On place un pnj sur la map au coordonnées sélectionnées
        self.AjoutJsonMapValue(coordPNJ, "coordsMapObject", "PNJ Coords") # Ajout de toutes les coordonnées au fichier json

    def PlacementSpawn(self, coordsSpawnElement): 
        """Méthode permettant de placer le spawn du joueur sur la map (collision) et d'ajouter ces coordonnées dans le json"""
        for coordsPlacement in coordsSpawnElement: # on parcourt toute la liste de coords
            self.map[coordsPlacement[1]][coordsPlacement[0]] = coordsPlacement[2] # on place les element aux coordonnées sur la map (avec la lettre)
        self.AjoutJsonMapValue(coordsSpawnElement, "coordsMapObject", "CampSpawn Coords") # on ajoute les coordonnées du spawn au fichier json

    def PlacementSortie(self, coordsSortie): 
        """Méthode permettant de placer la sortie sur la map"""

        self.map[coordsSortie[1]][coordsSortie[0]] = "S" # placement de la sortie sur la map
        self.AjoutJsonMapValue(coordsSortie, "coordsMapObject", "ZoneSortie Coords") # stockage dans le json des coords de la sortie de la map

    def AjoutJsonMapValue(self, value :list, index1 :str, index2 :str) -> None:
        """Chargement des données JSON aux index indiqués pour pouvoir les stocker"""
        try: # Si le chargement est possible
            with open("AllMapValue.json", "r") as f: # ouvrir le fichier json en mode lecture
                donnees = json.load(f) # chargement des données
        except (FileNotFoundError, json.JSONDecodeError): # Sinon relève une erreur et arrêt du programme
            assert ValueError("Error load JSON file") # stop du programme avec l'assert (programmation défensive)

        donnees[f"{index1}"][f"{index2}"] = value # Ajout valeurs aux indexs donnés

        # Sauvegarde des données dans le fichier JSON avec une indentation pour un format "lisible"
        with open("AllMapValue.json", "w") as f: # ouverture du fichier json en mode écriture
            json.dump(donnees, f, indent=4) # chargement dans le fichier json de l'élément données (possédent les index de position et les valeurs à stocker)

    def LoadJsonMapValue(self, index1 :str, index2 :str) -> list:
        """Récupération des valeur stockées dans le fichier json pour les renvoyer quand nécéssaire à l'aide des indices données pour les récupérer"""
        # récupération des valeurs stocké dans le json
        with open("AllMapValue.json", "r") as f: # ouvrir le fichier json en mode e lecture
            loadElementJson = json.load(f) # chargement des valeurs
        return loadElementJson[index1].get(index2, None) # on retourne les valeurs aux indices de liste quisont données



class NiveauPlaineRiviere(GestionNiveauMap):
    """class du niveau 1, permet de générer les deux map (base et obstacle) en faisant appel à aux méthode de ça class parant. 
    La gestion de la création est faite dans la méthode update de cette class et les valeurs (map) sont stokcé dans la class parent.
    Cette class contient donc les valeurs spécifique à ce niveau et les méthode spécifique également."""

    def __init__(self, longueur :int, largeur :int, obstacle :int) -> None:
        """Initialisation des attributs de la class enfant"""
        super().__init__(longueur, largeur) # on récupère / initialise les valeurs dans la class parent (c'est à ce moment là que la class parent est initialisé)
        self.obstacle = obstacle # on stock le nombre d'obstacle 
        self.coordsPNJ = None # None car la valeurs est modifier par la suite car il est placé en fonction des infops sur la map
        self.mapCheckDeplacementPossible = [] # initialisation de la map de test pour savoir si un niveau est possible
        self.pnj = [] # initialisation de la liste des coords des pnj (placement de certains pnj plus tard en fonction de l'apparence de la map)
        self.data = {
                    "coordsMapBase" : {
                        "Bordures Coords": "null",
                        "Riviere0 Coords" : "null",
                        "Riviere1 Coords" : "null",
                        "Flowers Coords" : "null",
                        "AllMapInfo" : "null",
                        "AllMapBase" : "null"
                    },

                    "coordsMapObject" : {
                        "Obstacles Coords" : "null",
                        "PNJ Coords" : "null",
                        "ArbreSpecial Coords" : "null",
                        "CampSpawn Coords" : "null",
                        "ZoneSortie Coords" : "null"
                    }
                }   # arborescence du fichier json qui sera ajouté par la suite 

    def __CheckPos__(self, indice : list) -> bool:
        """Méthode permettant de regarder et de valider la position d'un element par raport à la riviere (pnj / arbre spécial)"""
        # verification si la position du pnj est possible autour de la riviere (rivière large de 1 uniquement) + eviter de la placer trop haut / bas
        listePosPossible = ["-", "F"] # liste pour indiquer que si la position check est dans la liste alors c'est bon (= fleurs / herbe donc pas de colision)
        # vérification autour de la case rivière sélectionnée, si le placement / déplacement sont possible
        # deux dernière vérif du if :  pour éviter de placer le pnj trop haut / trop bas
        if (self.map[indice[1]][indice[0]-1] in listePosPossible) and (self.map[indice[1]][indice[0]-2] in listePosPossible )and( self.map[indice[1]][indice[0]+1] in listePosPossible) and (indice[1] >=5) and (indice[1] <= 70): 
            return True # on valide le placement
        else:
            return False # on invalide le placement

    def __CheckNiveauPossible__(self, listOrdrePointCle :list, pathAccessible :list) -> bool:
        """Méthode permettant de vérifier si le niveau est possible, suite à la position des obstacle. Utilisation du script A* permettant de trouver un chemin avec les déplacements ZQSD s'il exite entre un point A et B
        Ces points, donnés dans l'ordre d'évolution de la map, représente les coordonnées des éléments que le joueurs doit allé voir (pnj, arbre, entré, sortie..)"""

        for pointCle in range(len(listOrdrePointCle)-1): # On parcours la liste de point donnée avec un indice inférieur de 1 car on veux envoper le point actuel et le point suivant ( n et n+1)
            if  Astar(listOrdrePointCle[pointCle], listOrdrePointCle[pointCle+1],self.mapCheckDeplacementPossible, pathAccessible).a_star(): # si true, alors le chemin est trouvé, et l'on passe au calcul du chemin suivant
                pass
            else: # Si on indique que le chemin n'éxiste pas et que par conséquent, la résolution du niveau est impossible
                return False # false pour niveau impossible
        return True # les chemins entre les points données existent  

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

        super().AjoutJsonMapValue(listeFlowerCoords, "coordsMapBase", "Flowers Coords") # on ajoute au fichier json, la vrai liste de coordonnée des fleurs


    def __PlacementSpecial__(self, index1 : str, index2 : str, element : str) -> list:
        """Méthode permetant de placer spécialement une element sous certaines condition.
        On récupère les coordonnées d'un elelment (ici la riviere), on génère aléatoirement un indice qui sera appliqué à cette liste de coordonnées
        On vérifier si à cet indice le placement (devant gauche) de l'element est possible (__checkPos__)
        Si c'est bon on placement l'element, et on renvoie les coordonnées de l'element placé sur la map (collision), sinon on génère un nouvelle indice, et on recheck jusqu'a trouver"""
        
        listeCoordsElement = super().LoadJsonMapValue(index1, index2) # récupération de la liste de valeurs d'un element (riviere)

        Go = True
        while Go: # tant que go = True on check 
            indice = randint(0, self.largeur-1) # génération aléatoire d'un indice

            # Si true, on arreter la boucle
            if self.__CheckPos__(listeCoordsElement[indice]): # check si à les coords de la liste  l'indice respect les conditions pour poser l'element
                Go = False # Arret de la boucle
        itemCoords = listeCoordsElement[indice] # on crée un copie des coords dans la variable
        self.map[itemCoords[1]][itemCoords[0]-1] = element # on ajoute l'element sur la map (collision)

        return [itemCoords[0]-1,itemCoords[1]] # return [x,y ) coord de l'element
    
    def __PlacementRiviere__(self) -> None:
        """Méthode permettant de créer les deux rivières de la map. Création de points de repère tout les 15 de distance en hauteur dans un couleurs d'une largeur de 9
        Liaison des points entre eux avec un script de LiaisonAtoB fait maison.
        
        Placement également dune zone de sécurité (5 de haut verticalement) pour placer les element spéciaux si jamais
        Placement de ligne aux extrémitées (haut et bas) pour ne pas etre en colision avec les montagnes"""


        # création 2 rivières génération alétoire controlé
        for nombreRiviere in range(2): # 2 tours car 2 riviere
            listeCheminRiviere = [] # initialisation de la liste qui contiendra toutes les coordonnées de la riviere
            listePointRepere = [] # initialisation de la liste des pts repères

            # Points du haut (premier element)
            # permet de créer une ligne pour éviter les collision avec les bordures
            coordsPts1Riviere = [randint(((nombreRiviere+1)*50 -4),((nombreRiviere+1)*50 +4)),1] # on créer le point 1 de la map
            listePointRepere.append(coordsPts1Riviere) # forme [x,y] on ajoute le premier point à la liste
            coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1]+4] # on crée le second point avec une hauteur de + 4
            listePointRepere.append(coordsPts2Riviere) # forme [x,y] on ajoute le second point dans la liste

            # Point de haut en bas
            nbPts = self.largeur // 15    # placement tout les 15 de hauteur ...   
            verifLigne5 = randint(1,(nbPts-1)) # choix du lieu pour la ligne de 5 droite pour sécu pos de pnj spécial et arbre spécial

            for nbPointRepere in range(1, nbPts): # placement de tout les point repère
                if verifLigne5 == nbPointRepere: # ajout du pts A et B pour une ligne de 5 toute droite pour sécu placement des pnj autour de la riviere
                    pACoordsligne5 = [randint(((nombreRiviere+1)*50 -4),((nombreRiviere+1)*50 +4)), nbPointRepere*15] # forme [x,y]
                    listePointRepere.append(pACoordsligne5) # Ajout du point A car il devient un point repère à relier
                    pBcoordsligne5 = [pACoordsligne5[0], nbPointRepere*15 + 5] # forme [x, y]
                    listePointRepere.append(pBcoordsligne5) # Ajout du point B car il devient un point repère à relier

                else:
                    # Tout les autres pts de repère
                    coords = [randint(((nombreRiviere+1)*50 -4),((nombreRiviere+1)*50 +4)),nbPointRepere*15] # forme [x,y]
                    listePointRepere.append(coords) # on ajoute ces points dans la liste des points à relier
            
            
            # Point du bas (dernier element)
            # permet de créer une ligne pour éviter les collisions avec les bordures
            coordsPts3Riviere = [randint(((nombreRiviere+1)*50 -4),((nombreRiviere+1)*50 +4)),self.largeur-5] # on crée l'avant dernier point
            listePointRepere.append(coordsPts3Riviere) # forme [x,y]  on ajoute l'avant dernier point repère
            coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1]+3] # on crée le dernier point avec une huteur de +4
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

            super().AjoutJsonMapValue(listeCheminRiviere, "coordsMapBase", f"Riviere{nombreRiviere} Coords") # stockage des valeurs dans le fichier json

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
            for obstacle in range(self.obstacle): # boucle pour le nombre d'obstacle différents
                obstaclePos = [randint(4, self.longueur-4), randint(4, self.largeur-4)] # forme [x,y] pos random sur la map, en éviant les bordure
                while self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] != '-': # check de s'il y a déjà des éléments sur la map de test (map).
                    obstaclePos = [randint(4, self.longueur-4), randint(4, self.largeur-4)] # forme [x,y] # on replace si jamais il y a un element
                self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] = "O" # on ajoute sur la map de test l'object
                listeObstacle.append(obstaclePos) # forme  [x,y] # on ajoute les coords de l'obstacle dans la liste de stockage

            # base check # GROSSE VERIF : 
            # 3 liste, 3 verif car quand il y az ue rivire il faut d'écaler le point de départ, car un pont sera poser pour permettre au joueur de traverser la riviere
            # spawn, pnj1, arbre spécial, pnj2, pnj3, sortie
            listeOrdrePointCle1 = [ # partie gauche map (avant riviere)
                                [1,1], 
                                self.coordsPNJ[0], 
                                super().LoadJsonMapValue("coordsMapObject", "ArbreSpecial Coords")
                                ]
            
            listeOrdrePointCle2 = [ # partie middle (entre les deux rivieres donc on a passé la premiere riviere (indice + 2))
                                [self.coordsPNJ[1][0] + 2,self.coordsPNJ[1][1]], # +2 car on traverse la riviere
                                self.coordsPNJ[2]
                                ]
            
            listeOrdrePointCle3 = [ # meme chose
                                [self.coordsPNJ[2][0] + 2,self.coordsPNJ[2][1]], # +2 car on traverse la riviere
                                super().LoadJsonMapValue("coordsMapObject", "ZoneSortie Coords")
                                ]
            
            # Pour chacune des listes, on check s'il existe un chemin liant les points entre deux dans l'ordre d'avancement. 
            # Check en trois niveau car la map est divisé en trois par les 2 rivières. Donc on passe les rivières pour pouvoir calculer
            if self.__CheckNiveauPossible__(listeOrdrePointCle1, ["-", "A", "P", "S"]): # Si true (donc possible), on continue 
                if self.__CheckNiveauPossible__(listeOrdrePointCle2,  ["-", "A", "P", "S"] ): # ///
                    if self.__CheckNiveauPossible__(listeOrdrePointCle3,  ["-", "A", "P", "S"] ): # //
                        super().AjoutJsonMapValue(listeObstacle, "coordsMapObject", "Obstacles Coords") # Si la map est possible, on stock les coords des obstacle dans le json
                        checkDeplacementPasPossible = False # on arrête la boucle
                        for coords in listeObstacle: # on met à jour la map (on place les objets dessus)
                            self.map[coords[1]][coords[0]] = "O" # placement aux différents cordonnées

    def Update(self) -> list:
        """Méthode de gestion de la créaion de la map pour le niveau plaine et riviere.
        Cette méthode est à appeler pour pouvoir build la map integralement, elle retourne la map de bas (sol) ainsi que la map avec différents objet (collisions...)"""
        # Attention, l'ordre de génération est important car certaines valeurs, sont dépendantes de d'autres...


        super().BaseJson(self.data) # setup du fichier json
        super().BaseMap()  # setup de la base des deux map (vide)
        self.__PlacementRiviere__() # placement des rivière
        super().PlacementSpawn([[1,1,"S"], [4,2,"b"], [2,4,"b"], [6,4,"b"], [4,6,"b"], [4,4,"C"]]) # coords de tout les élément du spawn evec une lettre indiquant à quoi ils font référence : b = banc, C = feu de camp, S = spawn du joueur) # placement du spawn
        super().PlacementSortie([149, 50]) # coords de la sortie de la map, forme [x,y]) # placement de la sortie
        self.__PlacementFleur__() # placement des varientes d'herbe (fleurs..)
        # Création des cordonnées des pnj (le pnj 2 utilise les information de la map pour pouvoir ce placer. )
        self.coordsPNJ = [[randint(8,((self.longueur//3) -5)), randint(5, self.largeur-5)], # forme [x,y]   # longueur de 8 de base pour éviter de rentrer en collision avec le camp de base
                    self.__PlacementSpecial__("coordsMapBase", "Riviere1 Coords", "P"), # placement pnj (ne tombe jamais sur les coords de la rivière), mais collé à un point de la riviere
                    [randint(((self.longueur//3)*2 +5), self.longueur-5), randint(5, self.largeur-5)]]  # forme [x,y] coords du dernier pnj      
        super().PlacementPNJ(self.coordsPNJ) # placement des pnj sur la map 
        coordsAbre = self.__PlacementSpecial__("coordsMapBase", "Riviere0 Coords", "A") # placement spécial de l'arbre spécial
        super().AjoutJsonMapValue(coordsAbre, "coordsMapObject", "ArbreSpecial Coords") # ajout des coords de l'arbre spécial dans le fichier json
        self.__PlacementObstacle__() # placement des obstacles

                
        # On charge la map de base pour pouvoir refresh tout les x tics et gérer les collisions
        super().AjoutJsonMapValue(self.map, "coordsMapBase", "AllMapInfo")

        # On charche la map (collision) pour pouvoir refresh tout les x tics
        super().AjoutJsonMapValue(self.baseMap, "coordsMapBase", "AllMapBase")

        # On affiche la map pour verif
        for i in range(len(self.map)):
            print(*self.map[i], sep=" ")
        
        for j in range(len(self.baseMap)):
            print(*self.baseMap[j], sep=" ")

        return self.map, self.baseMap # return des deux map pour pouvoir charger et mettre à jours les valeurs de la map


# NiveauPlaineRiviere(150,75,200).Update()