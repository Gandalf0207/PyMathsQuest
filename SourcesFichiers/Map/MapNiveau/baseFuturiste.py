from settings import *
from SourcesFichiers.Map.creationMap import *

    
class NiveauBaseFuturiste(GestionNiveauMap):
    def __init__(self):
        super().__init__(150, 75)
        self.obstacle = 75
        self.mapCheckDeplacementPossible = [] # map test vide

    def PlacementBone(self):
        self.makeVarienteSolObj.CreateVarienteSol(300)
    
    def PlacementSalle(self):
        zoneElement = [
                    [(9, 25), (30, 29)],
                    [(52, 0), (80, 6)],
                    [(52, 51), (80, 52)],
                    [(102, 25), (122, 29)],
                    ]

        self.allLiaisons = []
        self.allCoordsSalles = []
        
        salleStructure = [
            ["W", "W", "W", "W", "W", "W", "W", "v", "v", "v", "v", "v", "W", "W", "W", "W", "W", "W", "W"],
            ["W", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W"],
            ["W", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W"],
            ["W", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W"],
            ["W", ".", ".", ".", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", ".", ".", ".", "W"],
            ["W", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "W"],
            ["W", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "W"],
            ["v", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "v"],
            ["v", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "v"],
            ["v", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "v"],
            ["v", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "v"],
            ["v", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "v"],
            ["W", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "W"],
            ["W", ".", ".", ".", "W", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W", ".", ".", ".", "W"],
            ["W", ".", ".", ".", "W", "W", "W", "W", "W", ".", "W", "W", "W", "W", "W", ".", ".", ".", "W"],
            ["W", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W"],
            ["W", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W"],
            ["W", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "v", "v", "v", "v", "v", "W", "W", "W", "W", "W", "W", "W"],
        ]

        for num in range(4):
            coordsSalle = []
            posX1, posY1 = randint(zoneElement[num][0][0], zoneElement[num][1][0]), randint(zoneElement[num][0][1], zoneElement[num][1][1])  # Position de départ aléatoire

            # Placement des champs sur la carte
            for y in range (len(salleStructure)):
                for x in range (len(salleStructure[y])):
                    self.map[posY1 + y][posX1 + x] = salleStructure[y][x]
                    self.baseMap[posY1 + y][posX1 + x] = "." # clear
                    coordsSalle.append([posX1 + x, posY1 + y, salleStructure[y][x]])
            self.allCoordsSalles.append(coordsSalle)
            

            liaison = [
                    [posX1, posY1 + 9],
                    [posX1 + 9, posY1],
                    [posX1 + 18, posY1 + 9],
                    [posX1 + 9 , posY1 + 18],
                ]  
            self.allLiaisons.append(liaison)

    def PlacementCouloir(self):
        # liaison entre les salles
        linkS1S2 = [
            self.allLiaisons[0][1], 
            [self.allLiaisons[0][1][0], self.allLiaisons[1][0][1]],
            [self.allLiaisons[0][1][0]-2, self.allLiaisons[1][0][1]], 
            self.allLiaisons[1][0]]
        
        linkS1S3 = [
            self.allLiaisons[0][3],  
            [self.allLiaisons[0][3][0],self.allLiaisons[2][0][1]],
            [self.allLiaisons[0][3][0] -2,self.allLiaisons[2][0][1]],
            self.allLiaisons[2][0]]

        linkS4S2 = [
            self.allLiaisons[3][1],  
            [self.allLiaisons[3][1][0],self.allLiaisons[1][2][1]],
            [self.allLiaisons[3][1][0] +2,self.allLiaisons[1][2][1]],
            self.allLiaisons[1][2]]
        linkS4S3 = [
            self.allLiaisons[3][3],  
            [self.allLiaisons[3][3][0],self.allLiaisons[2][2][1]],
            [self.allLiaisons[3][3][0] +2,self.allLiaisons[2][2][1]],
            self.allLiaisons[2][2]]

        # liaison spawn salle1
        linkSpawnS1 = [
            [self.allLiaisons[0][0][0] ,self.allLiaisons[0][0][1]],
            [0, self.allLiaisons[0][0][1]],
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
                        self.map[coords[1]][coords[0]] =  "&" 
                        self.baseMap[coords[1]][coords[0]] =  "."
        
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
            self.map[coords[1]][coords[0]] =  "."
            self.baseMap[coords[1]][coords[0]] =  "."

        # clear
        for ordonne in range(len(self.map)):
            for abscisse in range(len(self.map[0])):
                if self.map[ordonne][abscisse] in ["v", "&"]:
                    self.map[ordonne][abscisse] = "W"
                    self.baseMap[ordonne][abscisse] = "-"

    def PlacementObjSpecifique(self):

        # get coords
        allStructuresCoords = []
        allDoorsSallesCoords = []
        for numSalle in range(len(self.allCoordsSalles)):
            ptsRefStruc = self.allCoordsSalles[numSalle][140]
            ptsRefDoors = self.allCoordsSalles[numSalle][275]

            # sécu pos salle
            for y in range(5):
                for x in range(5):
                    self.map[ptsRefStruc[1] + y][ptsRefStruc[0] + x] = "&" # sécu check niveau possible
            self.map[ptsRefDoors[1]][ptsRefDoors[0]] = "V" # clear

            allStructuresCoords.append(ptsRefStruc)
            allDoorsSallesCoords.append(ptsRefDoors)
            
            if numSalle == 0: #salle reacteur
                ptsRefInteraction = self.allCoordsSalles[numSalle][218]
                allStructuresCoords.append(ptsRefInteraction)

        # coords structure salles
        self.coordsReactorStruc = [allStructuresCoords[0][0], allStructuresCoords[0][1], "NiveauBaseFuturiste", "StructureReactor"]
        self.coordsReactorBloc = [allStructuresCoords[1][0], allStructuresCoords[1][1], "NiveauBaseFuturiste", "ReactorBloc"]
        self.coordsCafetStruc = [allStructuresCoords[2][0], allStructuresCoords[2][1], "NiveauBaseFuturiste", "StructureCafet"]
        self.coordsEssenceStruc = [allStructuresCoords[3][0], allStructuresCoords[3][1], "NiveauBaseFuturiste", "StructureEssence"]
        self.coordsLancementStruc = [allStructuresCoords[4][0], allStructuresCoords[4][1], "NiveauBaseFuturiste", "StructureLancement"]
        self.map[self.coordsReactorBloc[1]][self.coordsReactorBloc[0]] = "V" # sécu

        # coords vent
        self.coordsVent1 = [self.allCoordsSalles[0][100][0], self.allCoordsSalles[0][100][1], "NiveauBaseFuturiste", "Vent1"]
        self.coordsVent2 = [self.allCoordsSalles[0][174][0], self.allCoordsSalles[0][174][1], "NiveauBaseFuturiste", "Vent2"]

        coordsVents = [self.coordsVent1, self.coordsVent2]
        for coords in coordsVents:
            self.map[coords[1]][coords[0]] = "v"
        
        # porte salle 
        self.coordsDoorSalle0 = [allDoorsSallesCoords[0][0], allDoorsSallesCoords[0][1], "NiveauBaseFuturiste", "DoorSalle"]
        self.coordsDoorSalle1 = [allDoorsSallesCoords[1][0], allDoorsSallesCoords[1][1], "NiveauBaseFuturiste", "DoorSalle"]
        self.coordsDoorSalle2 = [allDoorsSallesCoords[2][0], allDoorsSallesCoords[2][1], "NiveauBaseFuturiste", "DoorSalle"]
        self.coordsDoorSalle3 = [allDoorsSallesCoords[3][0], allDoorsSallesCoords[3][1], "NiveauBaseFuturiste", "DoorSalle"]

        # portal 
        self.coordsPortal = [self.coordsSpawn[0], self.coordsSpawn[1], "NiveauBaseFuturiste", "Portal"]

        allObjSpecifique = [self.coordsReactorStruc ,self.coordsReactorBloc , self.coordsCafetStruc ,self.coordsEssenceStruc ,self.coordsLancementStruc,
                            self.coordsVent1, self.coordsVent2, self.coordsDoorSalle0,self.coordsDoorSalle1,self.coordsDoorSalle2,self.coordsDoorSalle3,
                            self.coordsPortal]
        AjoutJsonMapValue(allObjSpecifique, "coordsMapObject", "ObjAPlacer")


    def PlacementSpawn(self):
        self.coordsSpawn =[ 2, self.allLiaisons[0][0][1]]
        self.map[self.coordsSpawn[1]][self.coordsSpawn[0]] = "S"
        AjoutJsonMapValue(self.coordsSpawn, "coordsMapObject", "Spawn") # on ajoute les coordonnées du spawn au fichier json

    def PlacementPNJ(self):
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
        self.map[self.coordsSpawn[1]][self.coordsSpawn[0] +8] = "P"
        self.allPNJCoords.append([self.coordsSpawn[0] + 8, self.coordsSpawn[1], "P", 1])

        # pnj 2 / 3 / 4 / 5
        for numSalle in range(len(self.allCoordsSalles)):
            ptsFixe = self.allCoordsSalles[numSalle][100]
            coordsPossiblesPNJ = [(coords[0] + ptsFixe[0], coords[1] + ptsFixe[1]) for coords in coordsPossiblesRefPNJ] 
            
            coordsPNJ = choice(coordsPossiblesPNJ)
            if numSalle !=3: # on ne crée pas de pnj pour le 3
                self.map[coordsPNJ[1]][coordsPNJ[0]] = "P"
            self.allPNJCoords.append([coordsPNJ[0], coordsPNJ[1], "P", numSalle+2])
        
        AjoutJsonMapValue(self.allPNJCoords, "coordsMapObject", "PNJ Coords") # on ajoute les coordonnées du spawn au fichier json

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
            for _ in range(self.obstacle):
                obstaclePos = [randint(0, self.longueur-1), randint(0, self.largeur-1)]
                # Vérifie que la position choisie est valide (case vide et pas dans une zone interdite)
                while self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] != '.'\
                    or self.mapCheckDeplacementPossible[obstaclePos[1]-1][obstaclePos[0]] not in [".", "W", "O", "V"] \
                    or self.mapCheckDeplacementPossible[obstaclePos[1]+1][obstaclePos[0]]  not in [".", "W", "O", "V"] \
                    or self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]+1]  not in [".", "W", "O", "V"] \
                    or self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]-1]  not in [".", "W", "O", "V"] :
                    obstaclePos = [randint(0, self.longueur-1), randint(0, self.largeur-1)]  # Nouvelle tentative
                # Marque la position comme occupée pour les tests
                self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] = "O"  
                listeObstacle.append(obstaclePos)  # Ajoute l'obstacle à la liste

            # Récupère les coordonnées des points clés (par exemple, spawn, passage de la rivière, etc.)
            coordsPts1 = self.coordsSpawn
            coordsPts2 = self.allPNJCoords[0]
            coordsPts3 = self.coordsVent2
            coordsPts4 = self.coordsVent1
            coordsPts5 = self.allPNJCoords[1]
            coordsPts6 = self.coordsReactorBloc
            coordsPts7 = self.allPNJCoords[2]
            coordsPts8 = self.allPNJCoords[3]
            coordsPts9 = self.allPNJCoords[4]


            # Liste des points à vérifier pour les déplacements possibles
            listeOrdrePointCle1 = [coordsPts1, coordsPts2, coordsPts3]
            listeOrdrePointCle2 = [coordsPts4, coordsPts5, coordsPts6, coordsPts7, coordsPts8, coordsPts9]

            # Vérifie la possibilité de déplacements pour chaque liste de points clés
            # Le parcours se fait en trois étapes, en passant par les rivières pour s'assurer que les chemins sont valides
            if self.CheckNiveauPossible(listeOrdrePointCle1, [".", "S", "V", "P", "v"], self.mapCheckDeplacementPossible):  # Vérifie la première partie
                if self.CheckNiveauPossible(listeOrdrePointCle2,  [".", "S", "V", "P", "v"], self.mapCheckDeplacementPossible):  # Vérifie la deuxième partie
                    # Si tout est valide, les obstacles peuvent être placés et les coordonnées sont sauvegardées
                    AjoutJsonMapValue(listeObstacle, "coordsMapObject", "Obstacles Coords")
                    checkDeplacementPasPossible = False  # Arrête la boucle

                    # Place les obstacles sur la carte
                    for coords in listeObstacle:
                        self.map[coords[1]][coords[0]] = "O"  # Placement des obstacles sur la carte
                        self.baseMap[coords[1]][coords[0]] = "."

        ## SECURITE
        # verif si boucle pour relancement
        if compteur < 100:
            self.ERROR_RELANCER = False
        else:
            self.ERROR_RELANCER = True

    def Update(self):
        self.PlacementBone()
        self.PlacementSalle()
        self.PlacementCouloir()
        self.PlacementSpawn()
        self.PlacementObjSpecifique()
        self.PlacementPNJ()
        self.PlacementObstacle()
        self.SaveGlobal()

        # relancer une nouvelle map
        if self.ERROR_RELANCER:
            return None, None, self.ERROR_RELANCER
        
        # Retourne la carte actuelle (map) et la carte de base (baseMap)
        return self.map, self.baseMap, self.ERROR_RELANCER  

class NiveauBaseFuturisteVaisseau(GestionNiveauMap):
    def __init__(self):
        super().__init__(18,17)

    def PlacementMap(self):
        self.map = [
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "W", "V", ".", "V", "W", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "W", ".", ".", ".", "W", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "W", ".", ".", ".", "W", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "W", ".", ".", ".", "W", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "W", "O", ".", ".", "W", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "W", ".", ".", ".", "W", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "W", "W", "V", "W", "W", "-", "-", "-", "-", "-", "-", "-"],
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
            ["-", "-", "-", "-", "-", "-", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", ".", ".", ".", ".", ".", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ] # oui il y a des différences

    def PlacementSpawn(self):
        self.coordsSpawn = [8, 10]
        self.map[self.coordsSpawn[1]][self.coordsSpawn[0]] = "S"
        AjoutJsonMapValue(self.coordsSpawn, "coordsMapObject", "Spawn")

    def PlacementPNJ(self):
        coordsPNJ4 = [8, 6, "P", 6]
        self.allCoordsPNJ = [coordsPNJ4]
        for coords in self.allCoordsPNJ:
            self.map[coords[1]][coords[0]] = "P"
        AjoutJsonMapValue(self.allCoordsPNJ, "coordsMapObject", "PNJ Coords")

    def PlacementObjSpecifique(self):

        # vitre
        self.coordsVitre1 = [7, 5, "NiveauBaseFuturiste", "Vitre"]
        self.coordsVitre2 = [8, 5, "NiveauBaseFuturiste", "Vitre"]
        self.coordsVitre3 = [9, 5, "NiveauBaseFuturiste", "Vitre"]

        # tableau de board
        self.coordsBoard1 = [7, 6, "NiveauBaseFuturiste", "Board"]
        self.coordsBoard2 = [8, 6, "NiveauBaseFuturiste", "Board"]
        self.coordsBoard3 = [9, 6, "NiveauBaseFuturiste", "Board"]

        # siège
        self.coordsSiege1 = [7, 7, "NiveauBaseFuturiste", "Siege"]
        self.coordsSiege2 = [9, 7, "NiveauBaseFuturiste", "Siege"]

        self.coordsDoorFuturisteVaisseau = [8, 11, "NiveauBaseFuturiste", "DoorFuturisteVaisseau"]

        allObjSpecifique = [self.coordsVitre1, self.coordsVitre2, self.coordsVitre3,
                            self.coordsBoard1, self.coordsBoard2, self.coordsBoard3, 
                            self.coordsSiege1, self.coordsSiege2, self.coordsVitre2, self.coordsDoorFuturisteVaisseau]
        AjoutJsonMapValue(allObjSpecifique, "coordsMapObject", "ObjAPlacer")

    def Update(self):
        self.PlacementMap()
        self.PlacementSpawn()
        self.PlacementPNJ()
        self.PlacementObjSpecifique()
        self.SaveGlobal()

        # relancer une nouvelle map
        if self.ERROR_RELANCER:
            return None, None, self.ERROR_RELANCER
        
        # Retourne la carte actuelle (map) et la carte de base (baseMap)
        return self.map, self.baseMap, self.ERROR_RELANCER  
