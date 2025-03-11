from settings import *
from SourcesFichiers.Map.creationMap import *


class NiveauPlaineRiviere(GestionNiveauMap):
    def __init__(self):
        super().__init__(150,75) 
        self.obstacle = 1000
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
    
    def PlacementFleur(self):
        self.makeFlowerObj.CreateFlower()

    def PlacementMudRock(self):
        self.makeVarienteSolObj.CreateVarienteSol(500)

    def PlacementSpawn(self):
        self.coordsSpawn = [8,2]
        self.map[self.coordsSpawn[1]][self.coordsSpawn[0]] = "S"
        self.baseMap[self.coordsSpawn[1]][self.coordsSpawn[0]] = "-" # clear
        AjoutJsonMapValue(self.coordsSpawn, "coordsMapObject", "Spawn")

    def PlacementExit(self):
        ptsRiverCompatible = self.getPointSpecifiqueRiver.PlacementSpecial("coordsMapBase", "Riviere3 Coords")
        self.coordsExit = [ptsRiverCompatible[0]-1, ptsRiverCompatible[1]]
        self.map[self.coordsExit[1]][self.coordsExit[0]] = "S"
        self.baseMap[self.coordsExit[1]][self.coordsExit[0]] = "-" # clear
        AjoutJsonMapValue(self.coordsExit, "coordsMapObject", "Spawn")

    def PlacementPNJ(self):
        ptsRiverCompatible = self.getPointSpecifiqueRiver.PlacementSpecial("coordsMapBase", "Riviere2 Coords")
        
        coordsPNJ1 = [randint(8,((self.longueur//3) -5)), randint(5, self.largeur-5), "P", 1]
        coordsPNJ2 = [ptsRiverCompatible[0]-1, ptsRiverCompatible[1], "P", 2]
        coordsPNJ3 = [randint(((self.longueur//3)*2 +5), self.longueur-9), randint(5, self.largeur-8), "P", 3]

        self.allCoordsPNJ = [coordsPNJ1, coordsPNJ2, coordsPNJ3]
        for coords in self.allCoordsPNJ:
            self.map[coords[1]][coords[0]] = "P"
            self.baseMap[coords[1]][coords[0]] = "-"

        AjoutJsonMapValue(self.allCoordsPNJ, "coordsMapObject", "PNJ Coords")

    def PlacementObjSpecifique(self):

        # camp fire
        self.coordsCampFire = [9,3,"NiveauPlaineRiviere", "CampFire"]
        self.map[self.coordsCampFire[1]][self.coordsCampFire[0]] = "&"
        self.baseMap[self.coordsCampFire[1]][self.coordsCampFire[0]] = "-"

        # arbre interaction pnj
        ptsRiverCompatible = self.getPointSpecifiqueRiver.PlacementSpecial("coordsMapBase", "Riviere1 Coords")
        self.coordsArbreBucheron = [ptsRiverCompatible[0]-1, ptsRiverCompatible[1], "NiveauPlaineRiviere", "ArbreBucheron" ]
        self.map[self.coordsArbreBucheron[1]][self.coordsArbreBucheron[0]] = "V"
        self.baseMap[self.coordsArbreBucheron[1]][self.coordsArbreBucheron[0]] = "-"

        allObjSpecifique = [self.coordsCampFire, self.coordsArbreBucheron]
        AjoutJsonMapValue(allObjSpecifique, "coordsMapObject", "ObjAPlacer")

    def PlacementObstacles(self):
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
                obstaclePos = [randint(0, self.longueur-2), randint(0, self.largeur-2)] # forme [x,y] pos random sur la map, en éviant les bordure
                while self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] not in ['-', "O"] \
                    or self.mapCheckDeplacementPossible[obstaclePos[1]+1][obstaclePos[0]] not in ['-', "O"] \
                    or self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]-2] not in ['-', "O"]: # check de s'il y a déjà des éléments sur la map de test (map).
                    obstaclePos = [randint(0, self.longueur-2), randint(0, self.largeur-2)] # forme [x,y] # on replace si jamais il y a un element
                self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] = "O" # on ajoute sur la map de test l'object


                listeObstacle.append(obstaclePos) # forme  [x,y] # on ajoute les coords de l'obstacle dans la liste de stockage

            # base check # GROSSE VERIF : 
            # 3 liste, 3 verif car quand il y az ue rivire il faut d'écaler le point de départ, car un pont sera poser pour permettre au joueur de traverser la riviere
            # spawn, pnj1, arbre spécial, pnj2, pnj3, sortie
            listeOrdrePointCle1 = [ # partie gauche map (avant riviere)
                                [8,2],  
                                [self.allCoordsPNJ[0][0], self.allCoordsPNJ[0][1]],
                                self.coordsArbreBucheron,
                                ]
            
            listeOrdrePointCle2 = [ # partie middle (entre les deux rivieres donc on a passé la premiere riviere (indice + 2))
                                [self.coordsArbreBucheron[0]+2, self.coordsArbreBucheron[1]],
                                self.allCoordsPNJ[1], # +2 car on traverse la riviere
                                ]
            
            listeOrdrePointCle3 = [ # meme chose
                                [self.allCoordsPNJ[1][0] + 2, self.allCoordsPNJ[1][1]],
                                self.allCoordsPNJ[2], # +2 car on traverse la riviere
                                self.coordsExit,
                                ]

            # Pour chacune des listes, on check s'il existe un chemin liant les points entre deux dans l'ordre d'avancement. 
            # Check en trois niveau car la map est divisé en trois par les 2 rivières. Donc on passe les rivières pour pouvoir calculer
            if self.CheckNiveauPossible(listeOrdrePointCle1, ["-", "P", "V", "S"], self.mapCheckDeplacementPossible): # Si true (donc possible), on continue 
                if self.CheckNiveauPossible(listeOrdrePointCle2,  ["-", "P", "V", "S"], self.mapCheckDeplacementPossible): # ///
                    if self.CheckNiveauPossible(listeOrdrePointCle3,  ["-", "P", "V", "S"], self.mapCheckDeplacementPossible): # //
                        checkDeplacementPasPossible = False # on arrête la boucle
                        for coords in listeObstacle: # on met à jour la map (on place les objets dessus)
                            self.map[coords[1]][coords[0]] = "O" # placement aux différents cordonnées
                            self.baseMap[coords[1]][coords[0]] = "-"

        ## SECURITE
        # verif si boucle pour relancement
        if compteur < 100:
            self.ERROR_RELANCER = False
        else:
            self.ERROR_RELANCER = True

    def Update(self):
        self.PlacementBordure()
        self.PlacementRiver()
        self.PlacementFleur()
        self.PlacementMudRock()
        self.PlacementSpawn()
        self.PlacementExit()
        self.PlacementPNJ()
        self.PlacementObjSpecifique()
        self.PlacementObstacles()
        self.SaveGlobal()
        

        # relancer une nouvelle map
        if self.ERROR_RELANCER:
            return None, None, self.ERROR_RELANCER
        
        # Retourne la carte actuelle (map) et la carte de base (baseMap)
        return self.map, self.baseMap, self.ERROR_RELANCER