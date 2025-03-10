
from settings import *
from SourcesFichiers.Map.creationMap import *

class NiveauMordor(GestionNiveauMap):
    def __init__(self):
        super().__init__(150, 75) 
        self.obstacle = 800
        self.mapCheckDeplacementPossible = [] # map test vide
    
    def PlacementBordure(self):
        self.makeBorder.CreateBorder()

    def PlacementRiver(self):
        for i in range(4):
            match i:
                case 0:
                    self.makeRiverObj.River0CreationVecticale(0)
                case 1:
                    self.makeRiverObj.River1CreationVecticale(1)
                case 2:
                    self.makeRiverObj.River2CreationVecticale(2)
                case 3:
                    self.makeRiverObj.River3CreationVecticale(3)

    def PlacementRockCratere(self):
        self.makeVarienteSolObj.CreateVarienteSol(700)

    def PlacementMuraille(self):
        # prisions
        self.prisonStructure = [
            ["W", "-", "-", "-", "-", "W", "-", "-", "V", "W", "-", "-", "-", "W", "-", "-", "-", "-", "W"],
            ["W", "-", "-", "-", "-", "W", "-", "V", "-", "W", "-", "-", "-", "W", "-", "-", "-", "-", "W"],
            ["W", "-", "-", "-", "-", "W", "-", "-", "-", "W", "-", "-", "-", "W", "-", "-", "-", "-", "W"],
            ["W", "-", "-", "-", "-", "W", "V", "V", "V", "W", "V", "V", "V", "W", "-", "-", "-", "-", "W"],
            ["W", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "W"],
            ["W", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "W"],
            ["W", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "W"],
            ["W", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W", "W", "V", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
        ]
        
        coordsStartPrison = [65, 1]
        for ordonne in range(len(self.prisonStructure)):
            for abscisse in range(len(self.prisonStructure[ordonne])):
                self.map[coordsStartPrison[1] + ordonne][coordsStartPrison[0] + abscisse] = self.prisonStructure[ordonne][abscisse]
                self.baseMap[coordsStartPrison[1] + ordonne][coordsStartPrison[0] + abscisse] = "-"

    def PlacementObjSpecifique(self):
        # placement pont 
        allCoordsRiver1 = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")
        allCoordsRiver2 = LoadJsonMapValue("coordsMapBase", "Riviere2 Coords")
        getCoords1 = choice(allCoordsRiver1)
            # Vérifie que les coordonnées choisies sont valides (autour de la rivière)
        while getCoords1[1] < 5 or getCoords1[1] > 70 \
            or self.map[getCoords1[1]][getCoords1[0]-1] != "-" \
            or self.map[getCoords1[1]][getCoords1[0]-2] != "-" \
            or self.map[getCoords1[1]][getCoords1[0]+1] != "-": 
            getCoords1 = choice(allCoordsRiver1)

        getCoords2 = choice(allCoordsRiver2)
            # Vérifie que les coordonnées choisies sont valides (autour de la rivière)
        while getCoords2[1] < 5 or getCoords2[1] > 70 \
            or self.map[getCoords2[1]][getCoords2[0]-1] != "-" \
            or self.map[getCoords2[1]][getCoords2[0]-2] != "-" \
            or self.map[getCoords2[1]][getCoords2[0]+1] != "-": 
            getCoords2 = choice(allCoordsRiver2)
        self.coordsPont1 = [getCoords1[0], getCoords1[1], "NiveauMedievale", "Pont5", "NoInteraction"]
        self.coordsPont2 = [getCoords2[0], getCoords2[1], "NiveauMedievale", "Pont5", "Interaction"]

        # placement vaisseau
        self.coordsVaisseau = [randint(8, 25), randint(3, 64)]
        for ordonne in range(5):
            for abscisse in range(5):
                self.map[self.coordsVaisseau[1] + ordonne][self.coordsVaisseau[0] + abscisse] = "V"
                self.baseMap[self.coordsVaisseau[1] + ordonne][self.coordsVaisseau[0] + abscisse] = "-" # clear

        # placement pot prison
        self.coordsPotPrision = [72, 2, "NiveauMordor", "Pot"]

        # placement parchemin prison
        self.coordsParcheminPrison = [73, 1, "NiveauMordor", "Parchemin"]

        # placement door prison
        self.coordsDoorCellule1 = [72, 4, "NiveauMordor", "DoorCellule"]
        self.coordsDoorCellule2 = [76, 4, "NiveauMordor", "DoorCellule"]
        self.coordsDoorPrison = [74, 9, "NiveauMordor", "DoorCellule"]

        # barreaux prison
        self.coordsBarreaux1 = [71, 4, "NiveauMordor", "Barreaux"]
        self.coordsBarreaux2 = [73, 4, "NiveauMordor", "Barreaux"]
        self.coordsBarreaux3 = [75, 4, "NiveauMordor", "Barreaux"]
        self.coordsBarreaux4 = [77, 4, "NiveauMordor", "Barreaux"]

        # placement volcan 
        self.coordsVolcan = [randint(110, 135), randint(3, 64)]
        for ordonne in range(5):
            for abscisse in range(5):
                self.map[self.coordsVolcan[1] + ordonne][self.coordsVolcan[0] + abscisse] = "&"
                self.baseMap[self.coordsVolcan[1] + ordonne][self.coordsVolcan[0] + abscisse] = "-"

        # placement porte volcan
        self.coordsDoorVolcan = [self.coordsVolcan[0] + 2, self.coordsVolcan[1] + 4]
        

        allObjSpecifique = [self.coordsPont1, self.coordsPont2]
        AjoutJsonMapValue(allObjSpecifique, "coordsMapObject", "ObjAPlacer")
    
    def PlacementSpawn(self):
        # spawn
        self.coordsSpawn = [self.coordsVaisseau[1] + 7, self.coordsVaisseau[0] +3]
        self.map[self.coordsSpawn[1]][self.coordsSpawn[0]] = "S"
        self.map[self.coordsSpawn[1]][self.coordsSpawn[0]] = "-"
        AjoutJsonMapValue([self.coordsSpawn], "coordsMapObject", "Spawn") # on ajoute les coordonnées du spawn au fichier json      

    def PlacementPNJ(self):
        coordsPNJ1 = [self.coordsPont1[0] -1, self.coordsPont1[1], "P", 1]
        coordsPNJ2 = [76, 1, "P", 2] # dans la cellule de droite
        coordsPNJ3 = [74, 8, "P", 3]

        xPNJ4 = randint((self.coordsVolcan[0] -15), (self.coordsVolcan[0] -1))
        yPNJ4 = randint((self.coordsVolcan[1] -15), (self.coordsVolcan[1] + 20)) 
        
        while xPNJ4 <= 108 or yPNJ4 >= 70 or yPNJ4 <= 4 or self.map[yPNJ4][xPNJ4] != "-":
            xPNJ4 = randint((self.coordsVolcan[0] -15), (self.coordsVolcan[0] -1))
            yPNJ4 = randint((self.coordsVolcan[1] -15), (self.coordsVolcan[1]+ 20))    
        # placement pnj 4 autour du volcan
        coordsPNJ4 = [xPNJ4, yPNJ4, "P", 4]

        self.allCoordsPNJ = [coordsPNJ1, coordsPNJ2, coordsPNJ3, coordsPNJ4]
        
        for CoordPNJ in self.allCoordsPNJ:
            self.map[CoordPNJ[1]][CoordPNJ[0]] = "P"
            self.baseMap[CoordPNJ[1]][CoordPNJ[0]] = "-"

        AjoutJsonMapValue(self.allCoordsPNJ, "coordsMapObject", "PNJ Coords") # placement des pnj sur la map  

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
                obstaclePos = [randint(0, self.longueur-2), randint(0, self.largeur-1)]
                # Vérifie que la position choisie est valide (case vide et pas dans une zone interdite)
                while self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] != '-' \
                    or self.mapCheckDeplacementPossible[obstaclePos[1]-1][obstaclePos[0]] != '-' \
                    or self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]+1] != '-' \
                    or (1 <= obstaclePos[1] < 11 and 64 <= obstaclePos[0] <= 85):
                    obstaclePos = [randint(0, self.longueur-2), randint(0, self.largeur-1)]  # Nouvelle tentative
                # Marque la position comme occupée pour les tests
                self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] = "O"  
                listeObstacle.append(obstaclePos)  # Ajoute l'obstacle à la liste

            # Récupère les coordonnées des points clés (par exemple, spawn, passage de la rivière, etc.)
            
            #spawn
            coordsPts1 = self.coordsSpawn

            #pnj 1
            coordsPts2 = self.allCoordsPNJ[0]

            # prison
            coordsPts3 = [66,1]
            coordsPts4 = self.allCoordsPNJ[1]
            coordsPts5 = self.allCoordsPNJ[2]
            #pont passage vers dernier pnj
            coordsPts6 = self.allCoordsPNJ[3]

            # porte volcan
            coordsPts7 = self.coordsDoorVolcan

            # Liste des points à vérifier pour les déplacements possibles
            listeOrdrePointCle1 = [coordsPts1, coordsPts2]
            listeOrdrePointCle2 = [coordsPts3, coordsPts4, coordsPts5, coordsPts6, coordsPts7]

            # Vérifie la possibilité de déplacements pour chaque liste de points clés
            # Le parcours se fait en trois étapes, en passant par les rivières pour s'assurer que les chemins sont valides
            if self.CheckNiveauPossible(listeOrdrePointCle1, ["-", "P", "S", "V"], self.mapCheckDeplacementPossible):  # Vérifie la première partie
                if self.CheckNiveauPossible(listeOrdrePointCle2,  ["-", "P", "S", "V"], self.mapCheckDeplacementPossible):  # Vérifie la deuxième partie
                    # Si tout est valide, les obstacles peuvent être placés et les coordonnées sont sauvegardées
                    AjoutJsonMapValue(listeObstacle, "coordsMapObject", "Obstacles Coords")
                    checkDeplacementPasPossible = False  # Arrête la boucle

                    # Place les obstacles sur la carte
                    for coords in listeObstacle:
                        self.map[coords[1]][coords[0]] = "O"  # Placement des obstacles sur la carte
                        self.baseMap[coords[1]][coords[0]] = "-"

        ## SECURITE
        # verif si boucle pour relancement
        if compteur < 100:
            # Sauvegarde les coordonnées du transport de bateau vers le château dans un fichier JSON
            self.ERROR_RELANCER = False
        else:
            self.ERROR_RELANCER = True

    def Update(self):
        self.PlacementBordure()
        self.PlacementRiver()
        self.PlacementRockCratere()
        self.PlacementMuraille()
        self.PlacementObjSpecifique()
        self.PlacementSpawn()
        self.PlacementPNJ()
        self.PlacementObstacle()
        self.SaveGlobal()
        

        # relancer une nouvelle map
        if self.ERROR_RELANCER:
            return None, None, self.ERROR_RELANCER
        
        # Retourne la carte actuelle (map) et la carte de base (baseMap)
        return self.map, self.baseMap, self.ERROR_RELANCER  

