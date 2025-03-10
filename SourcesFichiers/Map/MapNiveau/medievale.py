from settings import *
from SourcesFichiers.Map.creationMap import *


class NiveauMedievale(GestionNiveauMap):
    def __init__(self):
        super().__init__(150,75) 
        self.obstacle = 1000
        self.mapCheckDeplacementPossible = [] # map test vide

    def PlacementBordure(self):
        self.makeBorder.CreateBorder()

    def PlacementFleur(self):
        self.makeFlowerObj.CreateFlower()

    def PlacementMudRock(self):
        self.makeVarienteSolObj.CreateVarienteSol(500)

    def PlacementRiver(self):
        for i in range(4):
            match i:
                case 0:
                    self.makeRiverObj.River0CreationVecticale(0)
                case 1:
                    self.makeRiverObj.River1CreationVecticale(1)
                case 2:
                    self.makeRiverObj.River2BisCreationVecticale(2)
                case 3:
                    self.makeRiverObj.River3CreationHorizontale(3)

    def PlacementMuraille(self):
        coordsMuraillesChateau = []  # Liste pour stocker toutes les coordonnées des éléments du château

        # Construction des murailles extérieures
        for i in range(25):  
            coordsMuraillesChateau.append([69, i])  # Mur gauche
            coordsMuraillesChateau.append([LONGUEUR - 1, i])  # Mur droit
        for i in range(81):
            if i != 40: # coord door muraille
                coordsMuraillesChateau.append([69 + i, 24])  # Mur du bas

        for coords in coordsMuraillesChateau:
            self.map[coords[1]][coords[0]] = "W"  
            self.baseMap[coords[1]][coords[0]] = "-"  # clear

        # structure chateau emplacement vide
        for i in range(5):
            for j in range(5): # (109, 1) = pos ref chateau
                self.map[1+ j][109 +i] = "V"
                self.baseMap[1+j][109 +i] = "-" # clear

    def PlacementChamp(self):
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
                    if coordsE in coordsAllChamps or self.map[coordsE[1]][coordsE[0]] != "-" or self.baseMap[coordsE[1]][coordsE[0]] == "=":
                        checkCollideWhile = True
                        break

                if not checkCollideWhile:
                    coordsAllChamps.extend(coordsHouse)  # Ajout des coordonnées du champ à la liste

        # Placement des champs sur la carte
        for coords in coordsAllChamps:
            self.map[coords[1]][coords[0]] = "@"
            self.baseMap[coords[1]][coords[0]] = "-" 

    def PlacementSpawn(self):
        """Méthode de placement du point de spawn"""
        coordsRiviere1 = LoadJsonMapValue("coordsMapBase", "Riviere0 Coords")  # Récupération des coordonnées de la rivière
        coordsRiverCompatible = choice(coordsRiviere1)  # Sélection d'une position aléatoire pour le spawn

        # Vérification que le spawn est dans une zone valide
        while not (25 <= coordsRiverCompatible[1] <= 35) or self.map[coordsRiverCompatible[1]][coordsRiverCompatible[0]-1] == "#" or self.map[coordsRiverCompatible[1]][coordsRiverCompatible[0]+1] == "#":
            coordsRiverCompatible = choice(coordsRiviere1)  # Sélection d'une autre position si la première est invalide

        self.coordsSpawn = [coordsRiverCompatible[0] + 1, coordsRiverCompatible[1]]

        self.map[self.coordsSpawn[1]][self.coordsSpawn[0]] = "S"
        self.baseMap[self.coordsSpawn[1]][self.coordsSpawn[0]] = "-" # clear
        AjoutJsonMapValue(self.coordsSpawn, "coordsMapObject", "Spawn")

    def PlacementExit(self):
        # on affiche pas sur la map car c'est pa porte du chateau
        self.coordsExit = [109, 5]  # Coordonnées fixes pour la sortie
        AjoutJsonMapValue(self.coordsExit, "coordsMapObject", "Exit")

    def PlacementPNJ(self):
        # Génère une position aléatoire pour le premier PNJ (personnage non joueur)
        posX1 = randint(15, 60)
        posY1 = randint(10, 62)
        
        # Récupère les coordonnées de la rivière 3 à partir d'un fichier JSON
        coordsRiviere3 = LoadJsonMapValue("coordsMapBase", "Riviere3 Coords")

        # Placement du premier PNJ avec ses coordonnées (X, Y), type "P" et identifiant 1
        coordsPNJ1 = [posX1, posY1, "P", 1] 
        
        # Placement du deuxième PNJ
        getCoords2 = choice(coordsRiviere3)
        # Vérifie que les coordonnées choisies sont valides (autour de la rivière)
        while getCoords2[0] < 85 or getCoords2[0] > 140 \
            or self.map[getCoords2[1]-1][getCoords2[0]] != "-" \
            or self.map[getCoords2[1]-2][getCoords2[0]] != "-" \
            or self.map[getCoords2[1]+1][getCoords2[0]] != "-": 

            getCoords2 = choice(coordsRiviere3)
        # Assigne la position du deuxième PNJ
        coordsPNJ2 = [getCoords2[0], getCoords2[1] +1, "P", 2]
        
        # Placement fixe du troisième PNJ
        coordsPNJ3 = [108, 12, "P", 3]

        # Stocke toutes les coordonnées des PNJ dans une liste
        self.allCoordsPNJ = [coordsPNJ1, coordsPNJ2, coordsPNJ3]
        
        for coords in self.allCoordsPNJ:
            self.map[coords[1]][coords[0]] = "P"
            self.baseMap[coords[1]][coords[0]] = "-"

        AjoutJsonMapValue(self.allCoordsPNJ, "coordsMapObject", "PNJ Coords")

    def PlacementObjSpecifique(self):

        # easter egg gong
        self.gongCoords = [148, 1, "NiveauMedievale", "Gong"]
        self.map[self.gongCoords[1]][self.gongCoords[0]] = "V"
        self.baseMap[self.gongCoords[1]][self.gongCoords[0]] = "-" # clear

        # chateau elements
        self.coordsChateau = [140, 0, "NiveauMedievale", "Chateau"]
        self.map[self.coordsChateau[1]][self.coordsChateau[0]] = "V"
        self.baseMap[self.coordsChateau[1]][self.coordsChateau[0]] = "-" # clear

        # porte du chateau 
        self.coordsDoorChateau = [109, 5, "NiveauMedievale", "DoorChateau"]
        self.map[self.coordsDoorChateau[1]][self.coordsDoorChateau[0]] = "V"
        self.baseMap[self.coordsDoorChateau[1]][self.coordsDoorChateau[0]] = "-" # clear

        # porte muraille 
        self.coordsDoorMuraille = [109, 24, "NiveauMedievale", "DoorMuraille"]
        self.map[self.coordsDoorMuraille[1]][self.coordsDoorMuraille[0]] = "V"
        self.baseMap[self.coordsDoorMuraille[1]][self.coordsDoorMuraille[0]] = "-" # clear

        # pont spawn
        self.coordsPontSpawn = [self.coordsSpawn[0]-1, self.coordsSpawn[1], "NiveauMedievale", "Pont3", "NoInteraction"]

        # pont garde spawn
        self.coordsPontGarde = [self.allCoordsPNJ[1][0], self.allCoordsPNJ[1][1]-1, "NiveauMedievale", "Pont4", "Interaction"]

        # puits coords
        self.coordsPuits = [randint(90, 120), randint(40, 60), "NiveauMedievale", "Puits"]
        self.map[self.coordsPuits[1]][self.coordsPuits[0]] = "V"
        self.baseMap[self.coordsPuits[1]][self.coordsPuits[0]] = "-" # clear

        # table de craft
        self.coordsTableCraft = [self.coordsPuits[0] + 1, self.coordsPuits[1]]  # Coordonnées de la table de craft
        self.map[self.coordsTableCraft[1]][self.coordsTableCraft[0]] = "V"
        self.baseMap[self.coordsTableCraft[1]][self.coordsTableCraft[0]] = "-" # clear


        allObjSpecifique = [self.gongCoords, self.coordsChateau, self.coordsDoorChateau, self.coordsDoorMuraille,
                            self.coordsPontSpawn, self.coordsPontGarde, self.coordsPuits, self.coordsTableCraft]
        AjoutJsonMapValue(allObjSpecifique, "coordsMapObject", "ObjAPlacer")

    def PlacementPath1(self):

        # Liste qui contiendra tous les chemins
        allPath = []

        # Récupère les coordonnées de départ du spawn à partir d'un fichier JSON
        coordsPts1 = LoadJsonMapValue("coordsMapObject", "Spawn")
        allPath.append(coordsPts1) # premier path
        
        # Coordonnées du point suivant après le premier PNJ
        coordsPts2 = self.allCoordsPNJ[0]

        # Récupère les coordonnées de la rivière 1 à partir d'un fichier JSON
        getAllCoordsRiver1 = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")
        getCoordsFromRiver1 = choice(getAllCoordsRiver1)
        
        # Vérifie si la position choisie est valide pour le passage de la rivière
        while getCoordsFromRiver1[1] < 38 \
            or self.map[getCoordsFromRiver1[1]][getCoordsFromRiver1[0]-1] == "#" \
            or self.map[getCoordsFromRiver1[1]][getCoordsFromRiver1[0]+1] == "#":
            getCoordsFromRiver1 = choice(getAllCoordsRiver1)
        
        # Définit les coordonnées du point de la rivière pour le chemin
        self.coordsPassageRiver1 = [getCoordsFromRiver1[0], getCoordsFromRiver1[1]]  
        coordsPts3 = [getCoordsFromRiver1[0]-4, getCoordsFromRiver1[1]] #-4 : secu ligne droite

        # Coordonnées du dernier point du chemin
        coordsPts4 = [self.coordsPassageRiver1[0]+4, self.coordsPassageRiver1[1]]  # +4 : sécu ligne droite
        coordsPts5 = self.coordsPuits

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
            if self.map[coords[1]][coords[0]] in ["-","P", "S", 1, 2]:
                self.baseMap[coords[1]][coords[0]] = "="  # Ajout de la rivière sur la carte de base

        for element in range(9):
            if self.map[coordsPts3[1]][coordsPts3[0] + element] in ["-", "P", "S", 1, 2]:
                self.baseMap[coordsPts3[1]][coordsPts3[0] + element] = "="  # Ajout de la rivière sur la carte de base
                allPath.append([coordsPts3[0] + element, coordsPts3[1]])

    def PlacementMaison(self):
        """Place les maisons dans différents villages sur la carte"""
        coordsVillage1, coordsVillage2, coordsVillage3 = [], [], []

        # Village 1
        coordsPnj1 = self.allCoordsPNJ[0]
        coordsHouse = [
            [coordsPnj1[0], coordsPnj1[1] - 2], [coordsPnj1[0] + 1, coordsPnj1[1] - 2],
            [coordsPnj1[0], coordsPnj1[1] - 1], [coordsPnj1[0] + 1, coordsPnj1[1] - 1],
        ]
        coordsVillage1.append(coordsHouse)  # Ajout de la maison du premier village

        # Village 2
        nbHouseV2 = randint(25, 40)  # Nombre de maisons pour le village 2

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
                    if self.map[coordsE[1]][coordsE[0]] != "-" or coordsE in self.coordsPuits:
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
        self.coordsAllHouse = [coordsVillage1, coordsVillage2, coordsVillage3]
        for blocCoords in self.coordsAllHouse:
            for petitBlocCoords in blocCoords:
                for i, coords in enumerate(petitBlocCoords):
                    if i ==0:
                        self.map[coords[1]][coords[0]] = "H"
                    else:
                        self.map[coords[1]][coords[0]] = "V" # sécu
                    self.baseMap[coords[1]][coords[0]] = "-" # clear

    def PlacementPath2(self):
        # Liste qui contiendra tous les chemins générés
        allPath = []

        getAllCoordsVillage2 = self.coordsAllHouse[1]
        
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
            pathToAdd = LiaisonAtoB(coordsHouse, self.coordsPuits).GetPos()  # Crée le chemin entre la maison et le puits
            for coords in pathToAdd:
                allPath.append(coords)  # Ajoute le chemin à la liste allPath

        # Met à jour la carte avec les chemins générés (rivières représentées par "=")
        for coords in allPath:
            if self.map[coords[1]][coords[0]] == "-":
                self.baseMap[coords[1]][coords[0]] = "="  # Ajout de la rivière sur la carte de base

    def PlacementObstacle(self):

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
                while self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] not in  ['-', "O"] \
                    or self.mapCheckDeplacementPossible[obstaclePos[1]+1][obstaclePos[0]] not in  ['-', "O"] \
                    or self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]-2] not in ['-', "O"] \
                    or self.baseMap[obstaclePos[1]][obstaclePos[0]] == "=" \
                    or (1 <= obstaclePos[1] < 13 and 102 <= obstaclePos[0] <= 113) :  # check de s'il y a déjà des éléments sur la map de test (map).

                    obstaclePos = [randint(0, self.longueur-2), randint(0, self.largeur-2)]  # Nouvelle tentative
                # Marque la position comme occupée pour les tests
                self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] = "O"  
                listeObstacle.append(obstaclePos)  # Ajoute l'obstacle à la liste

            # Récupère les coordonnées des points clés (par exemple, spawn, passage de la rivière, etc.)
            coordsPts1 = LoadJsonMapValue("coordsMapObject", "Spawn")
            coordsPts2 = self.allCoordsPNJ[0]
            coordsPts3 = [self.coordsPassageRiver1[0]-1, self.coordsPassageRiver1[1]]
            coordsPts4 = [coordsPts3[0]+2, coordsPts3[1]]
            coordsPts5 = self.coordsTableCraft
            
            # Sélectionne un point aléatoire sur la rivière 1
            getAllCoordsRiver1 = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")
            getCoordsRiver1Point = choice(getAllCoordsRiver1)
            while getCoordsRiver1Point[1] < 35 and getCoordsRiver1Point[1] != coordsPts3[1]:
                getCoordsRiver1Point= choice(getAllCoordsRiver1)
            coordsPts6 = [getCoordsRiver1Point[0]+1, getCoordsRiver1Point[1]]
            coordsPts7 = self.allCoordsPNJ[1]
            getCoordsRiver1Point2 = choice(getAllCoordsRiver1)
            while getCoordsRiver1Point2[1] >= 24 or self.mapCheckDeplacementPossible[getCoordsRiver1Point2[1]][getCoordsRiver1Point2[0]+1] != "-":
                getCoordsRiver1Point2 = choice(getAllCoordsRiver1)
            coordsPts8 =  [getCoordsRiver1Point2[0], getCoordsRiver1Point2[1]] # case river
            coordsPts9 = self.allCoordsPNJ[2]


            # Liste des points à vérifier pour les déplacements possibles
            listeOrdrePointCle1 = [coordsPts1, coordsPts2, coordsPts3]
            listeOrdrePointCle2 = [coordsPts4, coordsPts5, coordsPts6, coordsPts7]
            listeOrdrePointCle3 = [[coordsPts8[0] + 1, coordsPts8[1]], coordsPts9] # coords pts8 formaté pour ne pas etre sur la river

            # Vérifie la possibilité de déplacements pour chaque liste de points clés
            # Le parcours se fait en trois étapes, en passant par les rivières pour s'assurer que les chemins sont valides
            if self.CheckNiveauPossible(listeOrdrePointCle1, ["-", "P", "S", "V"], self.mapCheckDeplacementPossible):  # Vérifie la première partie
                if self.CheckNiveauPossible(listeOrdrePointCle2,  ["-", "P", "S", "V"], self.mapCheckDeplacementPossible):  # Vérifie la deuxième partie
                    if self.CheckNiveauPossible(listeOrdrePointCle3,  ["-", "P", "S", "V"], self.mapCheckDeplacementPossible):  # Vérifie la troisième partie
                        checkDeplacementPasPossible = False # on arrête la boucle
                        for coords in listeObstacle: # on met à jour la map (on place les objets dessus)
                            self.map[coords[1]][coords[0]] = "O" # placement aux différents cordonnées 
                            self.baseMap[coords[1]][coords[0]] = "-"

        ## SECURITE
        # verif si boucle pour relancement
        if compteur < 100:
            # Sauvegarde les coordonnées du transport de bateau vers le château dans un fichier JSON
            AjoutJsonMapValue(coordsPts8, "coordsMapObject", "RiverBoatTPChateau coords")
            self.ERROR_RELANCER = False
        else:
            self.ERROR_RELANCER = True

    def AjustementRiver(self):
        newCaseRiver = []
        # parcours et création de chaque sprites
        for ordonnees in range(len(self.map)):
            for abscisses in range(len(self.map[ordonnees])):

                if self.map[ordonnees][abscisses] == "#":

                    # Vérification des bords pour éviter les erreurs d'index
                    can_go_up = ordonnees > 0
                    can_go_down = ordonnees < LARGEUR - 1
                    can_go_left = abscisses > 0
                    can_go_right = abscisses < 149

                    def checkBuildUp(can_go_up, can_go_left, can_go_right):
                        if can_go_up:
                            if self.map[ordonnees -1][abscisses] == "W":
                                if can_go_right and can_go_left:
                                    if self.map[ordonnees -2][abscisses-1] == "#" or self.map[ordonnees -2][abscisses] == "#" or self.map[ordonnees -2][abscisses +1] == "#":
                                        self.map[ordonnees -2][abscisses] = "#"
                                elif can_go_left:
                                    if self.map[ordonnees -2][abscisses-1] == "#" or self.map[ordonnees -2][abscisses] == "#":   
                                        self.map[ordonnees -2][abscisses] = "#"
                                elif can_go_right:
                                    if self.map[ordonnees -2][abscisses] == "#" or self.map[ordonnees -2][abscisses +1] == "#":   
                                        self.map[ordonnees -2][abscisses] = "#"  

                    
                    def checkBuildDown(can_go_down, can_go_left, can_go_right): 
                        if can_go_down:
                            if self.map[ordonnees +1][abscisses] == "W":
                                if can_go_right and can_go_left:
                                    if self.map[ordonnees +2][abscisses-1] == "#" or self.map[ordonnees +2][abscisses] == "#" or self.map[ordonnees +2][abscisses +1] == "#":
                                        self.map[ordonnees +2][abscisses] = "#" 
                                elif can_go_left:
                                    if self.baseMap[ordonnees +2][abscisses-1] == "#" or self.map[ordonnees +2][abscisses] == "#":   
                                        self.map[ordonnees +2][abscisses] = "#" 
                                elif can_go_right:
                                    if self.baseMap[ordonnees +2][abscisses] == "#" or self.map[ordonnees +2][abscisses +1] == "#":   
                                        self.map[ordonnees +2][abscisses] = "#"    

                    can_build_up = checkBuildUp(can_go_up, can_go_left, can_go_right)
                    can_build_down = checkBuildDown(can_go_down,  can_go_left, can_go_right)

    def Update(self):
        self.PlacementBordure()
        self.PlacementRiver()
        self.PlacementFleur()
        self.PlacementMudRock()
        self.PlacementMuraille()
        self.PlacementSpawn()
        self.PlacementExit()
        self.PlacementPNJ()
        self.PlacementObjSpecifique()
        self.PlacementPath1()
        self.PlacementMaison()
        self.PlacementPath2()
        self.PlacementChamp()
        self.PlacementObstacle()
        self.AjustementRiver()
        self.SaveGlobal()


        # relancer une nouvelle map
        if self.ERROR_RELANCER:
            return None, None, self.ERROR_RELANCER
        
        # Retourne la carte actuelle (map) et la carte de base (baseMap)
        return self.map, self.baseMap, self.ERROR_RELANCER  
    



class NiveauMedievaleChateau(GestionNiveauMap):
    def __init__(self):
        super().__init__(11,11) 
    
    def PlacementMap(self):
        self.map = [
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "-", "-", "-", "-", "V", "-", "-", "-", "-", "W"],
            ["W", "-", "Y", "y", "-", "-", "-", "y", "Y", "-", "W"],
            ["W", "-", "-", "-", "-", "-", "-", "-", "-", "-", "W"],
            ["W", "-", "-", "-", "-", "-", "-", "-", "-", "-", "W"],
            ["W", "-", "Y", "y", "-", "-", "-", "y", "Y", "-", "W"],
            ["W", "-", "-", "-", "-", "-", "-", "-", "-", "-", "W"],
            ["W", "-", "-", "-", "-", "P", "-", "-", "-", "-", "W"],
            ["W", "-", "Y", "y", "-", "-", "-", "y", "Y", "-", "W"],
            ["W", "-", "-", "-", "-", "-", "-", "-", "-", "-", "W"],
            ["W", "W", "W", "W", "W", "V", "W", "W", "W", "W", "W"],
        ]

        self.baseMap = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ]

    def PlacementSpawn(self):
        self.coordsSpawn = [5, 9]
        self.map[self.coordsSpawn[1]][self.coordsSpawn[0]] = "S"
        AjoutJsonMapValue(self.coordsSpawn, "coordsMapObject", "Spawn")

    def PlacementExit(self):
        self.coordsExit = [5, 1]
        AjoutJsonMapValue(self.coordsExit, "coordsMapObject", "Exit")

    def PlacementPNJ(self):
        coordsPNJ4 = [5, 7, "P", 4]
        self.allCoordsPNJ = [coordsPNJ4]
        for coords in self.allCoordsPNJ:
            self.map[coords[1]][coords[0]] = "P"
        AjoutJsonMapValue(self.allCoordsPNJ, "coordsMapObject", "PNJ Coords")

    def PlacementObjSpecifique(self):
        # portal
        self.coordsPortal = [5, 1, "NiveauMedievale", "Portal"]

        # socle
        self.coordsSocle = [4, 1, "NiveauMedievale", "Socle"]

        allObjSpecifique = [self.coordsPortal, self.coordsSocle]
        AjoutJsonMapValue(allObjSpecifique, "coordsMapObject", "ObjAPlacer")

    def Update(self):
        self.PlacementMap()
        self.PlacementSpawn()
        self.PlacementExit()
        self.PlacementPNJ()
        self.PlacementObjSpecifique()
        self.SaveGlobal()

        # relancer une nouvelle map
        if self.ERROR_RELANCER:
            return None, None, self.ERROR_RELANCER
        
        # Retourne la carte actuelle (map) et la carte de base (baseMap)
        return self.map, self.baseMap, self.ERROR_RELANCER  
    