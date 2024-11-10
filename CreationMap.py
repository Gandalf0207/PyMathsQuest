from settings import *
from ScriptAlgo.jeuDeLaVie import *
from ScriptAlgo.liaisonAtoB import *
from ScriptAlgo.astar import *

# RAPPEL : les coordonnées sont stocké sous forme de liste
# coords = [x, y]
# il faut donc inverser l'ordre lors des placements: 
# Map[coords[1]][coords[0]]


class GestionNiveauMap(object):
    """class mère permettant de créer la base commmune de toutes les
    autres class enfants pour les différents niveau du jeu."""

    def __init__(self, longueur, largeur) -> None:
        """Initialisation des attributs de la class mère"""
        self.longueur = longueur # longueur de la map
        self.largeur = largeur # largeur de la map
        self.map = [] # map (double liste python)
        self.baseMap = [] # map pour seulement le sol

    def BaseMap(self):
        """Création de la double liste avec les bordures de la map(map)"""
        # map de base
        for _ in range(self.largeur): # largeur de la map (y)
            creationMap = [] # liste pour stocker les valeurs des colonnes (x)
            for _ in range(self.longueur): # longueur de la map (x)
                creationMap.append("-") # ajout des valeurs (x)
            self.map.append(creationMap) # ajout de la ligne entière
            
        for _ in range(self.largeur): # largeur de la map (y)
            creationMap = [] # liste pour stocker les valeurs des colonnes (x)
            for _ in range(self.longueur): # longueur de la map (x)
                creationMap.append("-") # ajout des valeurs (x)                        
            self.baseMap.append(creationMap)
        
        # position des bordure sur la map : 
        listeBordures = []
        for i in range(2):
            for j in range(self.longueur): # position des bordures haut et bas
                self.map[i*(self.largeur-1)][j] = "B"
                self.baseMap[i*(self.largeur-1)][j] = "B" 
                listeBordures.append([i*(self.largeur-1), j])

            for j in range(self.largeur): # position des bordures gauche et droites
                self.map[j][i*(self.longueur-1)] = "B"
                self.baseMap[j][i*(self.longueur-1)] = "B"
                listeBordures.append([j, i*(self.longueur-1)])

        # on stock les coordonnées des bordures, ça peut toujours servir
        self.AjoutJsonMapValue(listeBordures, "coordsMapBase", "Bordures Coords")   # A voir si interessant de le laisser....

    
    def BaseJson(self, data):
        """Initialisation du fichier Json avec l'arbo du fichier contenu dans la variable data"""
        with open("AllMapValue.json", "w") as valueFileJson: # Ouvrir le fichier en mode écriture
            json.dump(data, valueFileJson, indent=4) # charger la configuration pour le niveau

    def PlacementPNJ(self, coordPNJ):
        for coords in coordPNJ:
            self.map[coords[1]][coords[0]] = "P"
        self.AjoutJsonMapValue(coordPNJ, "coordsMapObject", "PNJ Coords")

    def AjoutJsonMapValue(self, value, index1, index2):
        """Chargement des données JSON aux index indiqués pour pouvoir les stocker"""
        try: # Si ça fonctionne
            with open("AllMapValue.json", "r") as f:
                donnees = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError): # Sinon relève une erreur et arrêt du programme
            assert ValueError("Error load JSON file")

        # Ajout valeurs aux indexs donnés
        donnees[f"{index1}"][f"{index2}"] = value

        # Sauvegarde des données dans le fichier JSON avec une indentation pour un format "lisible"
        with open("AllMapValue.json", "w") as f:
            json.dump(donnees, f, indent=4)

    def LoadJsonMapValue(self, index1, index2):
        # récupération des valeurs stocké dans le json
        with open("AllMapValue.json", "r") as f:
            loadElementJson = json.load(f)
        return loadElementJson[index1].get(index2, None)



class NiveauPlaineRiviere(GestionNiveauMap):

    def __init__(self, longueur, largeur, obstacle) -> None:
        super().__init__(longueur, largeur)
        self.obstacle = obstacle
        self.coordsPNJ = None # None car la valeurs est modifier par la suite car il est placé en fonction des infops sur la map
        self.mapCheckDeplacementPossible = []
        self.pnj = []
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
                }

    def __CheckPos__(self, indice):
        # verification si la position du pnj est possible autour de la riviere (rivière large de 1 uniquement) + eviter de la placer trop haut / bas
        listePosPossible = ["-", "F"]
        if (self.map[indice[1]][indice[0]-1] in listePosPossible) and (self.map[indice[1]][indice[0]-2] in listePosPossible )and( self.map[indice[1]][indice[0]+1] in listePosPossible) and (indice[1] >=5) and (indice[1] <= 70):
            return True
        else:
            return False

    def __CheckNiveauPossible__(self, listOrdrePointCle, pathAccessible):
        for pointCle in range(len(listOrdrePointCle)-1):
            if Astar(listOrdrePointCle[pointCle], listOrdrePointCle[pointCle+1],self.mapCheckDeplacementPossible, pathAccessible).a_star():
                pass
            else:
                return False
        return True

    def PlacementSpawn(self):
        coordsSpawnElement = [[1,1,"S"], [4,2,"b"], [2,4,"b"], [6,4,"b"], [4,6,"b"], [4,4,"C"]]
        for coordsPlacement in coordsSpawnElement:
            self.map[coordsPlacement[1]][coordsPlacement[0]] = coordsPlacement[2]
        super().AjoutJsonMapValue(coordsSpawnElement, "coordsMapObject", "CampSpawn Coords")

    def PlacementFleur(self):
        # placement de l'herbe (Alt 1 et 2 et 3) avec jeu de la vie
        getPosFleur = JeuDeLaVie().GetPos()
        listeFlowerCoords = []
        for posFleur in getPosFleur:
            if self.map[posFleur[1]][posFleur[0]] =="-":
                self.baseMap[posFleur[1]][posFleur[0]] = "F"
                listeFlowerCoords.append(posFleur) ####

        super().AjoutJsonMapValue(listeFlowerCoords, "coordsMapBase", "Flowers Coords")


    def PlacementSpecial(self, index1, index2, element):
        listeCoordsElement = super().LoadJsonMapValue(index1, index2)

        Go = True
        while Go:
            indice = randint(0, self.largeur-1)
            if self.__CheckPos__(listeCoordsElement[indice]):
                Go = False
        itemCoords = listeCoordsElement[indice]
        self.map[itemCoords[1]][itemCoords[0]-1] = element

        return [itemCoords[0]-1,itemCoords[1]] # return [x,y ] pour l'élément à poser
    
    def PlacementRiviere(self):
        # création 2 rivières génération alétoire controlé
        for nombreRiviere in range(2):
            listeCheminRiviere = []
            listePointRepere = [] # initialisation de la list des pts repères

            # Point du haut (premier element)
            listePointRepere.append([randint(((nombreRiviere+1)*50 -4),((nombreRiviere+1)*50 +4)),4]) # forme [x,y]

            # Point de haut en bas
            nbPts = self.largeur // 15      
            verifLigne5 = randint(1,(nbPts-1)) # choix du lieu pour la ligne de 5 droite pour sécu pos de pnj spécial et arbre spécial

            for nbPointRepere in range(1, nbPts):
                if verifLigne5 == nbPointRepere: # ajout du pts A et B pour une ligne de 5 toute droite pour sécu placement des pnj autour de la riviere
                    pACoordsligne5 = [randint(((nombreRiviere+1)*50 -4),((nombreRiviere+1)*50 +4)), nbPointRepere*15] # forme [x,y]
                    listePointRepere.append(pACoordsligne5)
                    pBcoordsligne5 = [pACoordsligne5[0], nbPointRepere*15 + 5] # forme [x, y]
                    listePointRepere.append(pBcoordsligne5)

                else:
                    # Tout les autres pts de repère
                    coords = [randint(((nombreRiviere+1)*50 -4),((nombreRiviere+1)*50 +4)),nbPointRepere*15] # forme [x,y]
                    listePointRepere.append(coords)
            
            
            # Point du bas (dernier element)
            listePointRepere.append([randint(((nombreRiviere+1)*50 -4),((nombreRiviere+1)*50 +4)),self.largeur-4]) # forme [x,y]

            # On ajoute les pts repère sur la map + les point spéciaux (haut et bas ) directement car collision avec montagne, donc il faut une ligne de 4 droite minimum
            for ordonnees in range(1,5): # premiere ligne de 5 partant du haut de la map
                self.map[5 -ordonnees][listePointRepere[0][0]] = "#" # y pour changer de ligne, x pour se positionner sur la meme colone que le premier point repère de la rivire
                self.baseMap[5 -ordonnees][listePointRepere[0][0]] = "#"
                listeCheminRiviere.append([listePointRepere[0][0], 5-ordonnees]) # forme [x,y]

            for coordsPointRepere in listePointRepere: # positions de tout les points repère de la riviere
                self.map[coordsPointRepere[1]][coordsPointRepere[0]] = "#" 
                self.baseMap[coordsPointRepere[1]][coordsPointRepere[0]] = "#" 
                listeCheminRiviere.append([coordsPointRepere[0],coordsPointRepere[1]]) # forme [x,y]

            for ordonnees in range(0,5): # derniere ligne de 5 pour arrivr sur le bas de la map
                self.map[self.largeur-5 +ordonnees][listePointRepere[-1][0]] = "#" #   y pour changer de ligne, x pour se positionner sur la meme colone que le dernier point repère de la rivire
                self.baseMap[self.largeur-5 +ordonnees][listePointRepere[-1][0]] = "#"
                listeCheminRiviere.append([listePointRepere[-1][0], self.largeur-5 + ordonnees])  # forme [x,y]


            
            # Pour tout les points repère, on lie des point A et B entre eux avec le script crée pour l'occasion
            for nbPointRepereRiviere in range(len(listePointRepere)-1):
                start = [listePointRepere[nbPointRepereRiviere][0], listePointRepere[nbPointRepereRiviere][1]] # fomre [x,y]
                goal = [listePointRepere[nbPointRepereRiviere+1][0], listePointRepere[nbPointRepereRiviere+1][1]] # fomre [x,y]   
                path = LiaisonAtoB(start, goal).GetPos()     # path de coords en [x,y]


                # On recup la list de déplacement et on ajoute la rivière à la map
                for coords in path:
                    self.map[coords[1]][coords[0]] = "#"
                    self.baseMap[coords[1]][coords[0]] = "#"
                    listeCheminRiviere.append([coords[0],coords[1]]) # forme [x,y]

            super().AjoutJsonMapValue(listeCheminRiviere, "coordsMapBase", f"Riviere{nombreRiviere} Coords") # add value to json file 


    # ADD VERIF POUR ETRE SUR QUE L4ELEMENT SOIT ACCESSIBLE ---------------------------------------------
    def PlacementObstacle(self):
        #placement des obstacle sur la map
        checkDeplacementPasPossible = True
        while checkDeplacementPasPossible:
            
            # copie de la map
            self.mapCheckDeplacementPossible = []
            self.mapCheckDeplacementPossible = copy.deepcopy(self.map)   

            listeObstacle = []
            for obstacle in range(self.obstacle):
                obstaclePos = [randint(4, self.longueur-4), randint(4, self.largeur-4)] # forme [x,y]
                while self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] != '-': # check de s'il y a déjà des éléments sur la map.
                    obstaclePos = [randint(4, self.longueur-4), randint(4, self.largeur-4)] # forme [x,y]
                self.mapCheckDeplacementPossible[obstaclePos[1]][obstaclePos[0]] = "O"
                listeObstacle.append(obstaclePos) # forme  [x,y]

            # base check : 
            # spawn, pnj1, arbre spécial, pnj2, pnj3, sortie
            listeOrdrePointCle1 = [ # partie gauche map (avant riviere)
                                [1,1], 
                                self.coordsPNJ[0], 
                                super().LoadJsonMapValue("coordsMapObject", "ArbreSpecial Coords")
                                ]
            
            listeOrdrePointCle2 = [ # partie middle (entre les deux riviere donc on a passé la premiere riviere (indice + 2))
                                [self.coordsPNJ[1][0] + 2,self.coordsPNJ[1][1]],
                                self.coordsPNJ[2]
                                ]
            
            listeOrdrePointCle3 = [ # meme chose
                                [self.coordsPNJ[2][0] + 2,self.coordsPNJ[2][1]],
                                super().LoadJsonMapValue("coordsMapObject", "ZoneSortie Coords")
                                ]
            
            if self.__CheckNiveauPossible__(listeOrdrePointCle1, ["-", "A", "P", "S"]):
                if self.__CheckNiveauPossible__(listeOrdrePointCle2,  ["-", "A", "P", "S"] ):
                    if self.__CheckNiveauPossible__(listeOrdrePointCle3,  ["-", "A", "P", "S"] ):
                        super().AjoutJsonMapValue(listeObstacle, "coordsMapObject", "Obstacles Coords")
                        checkDeplacementPasPossible = False
                        for coords in listeObstacle:
                            self.map[coords[1]][coords[0]] = "O"


    def PlacementSortie(self): # A implémenter
        coordsSortie = [149, 50]
        self.map[coordsSortie[1]][coordsSortie[0]] = "S"
        super().AjoutJsonMapValue(coordsSortie, "coordsMapObject", "ZoneSortie Coords")

    def Update(self):
        super().BaseJson(self.data)
        super().BaseMap()  
        self.PlacementRiviere()
        self.PlacementSpawn() 
        self.PlacementSortie() # # A implmenter
        self.PlacementFleur()
        self.coordsPNJ = [[randint(8,((self.longueur//3) -5)), randint(5, self.largeur-5)], # forme [x,y]   # longuer de 8 de base pour éviter de rentrer en collision avec le camp de base
                    self.PlacementSpecial("coordsMapBase", "Riviere1 Coords", "P"), # placement pnj (ne tombre jamais sur les coords de la rivière)
                    [randint(((self.longueur//3)*2 +5), self.longueur-5), randint(5, self.largeur-5)]]      # forme [x,y]       
        super().PlacementPNJ(self.coordsPNJ)
        coordsAbre = self.PlacementSpecial("coordsMapBase", "Riviere0 Coords", "A")
        super().AjoutJsonMapValue(coordsAbre, "coordsMapObject", "ArbreSpecial Coords")
        self.PlacementObstacle()

                
        # On charche la map de base pour pouvoir refresh tout les x tics
        super().AjoutJsonMapValue(self.map, "coordsMapBase", "AllMapInfo")

        super().AjoutJsonMapValue(self.baseMap, "coordsMapBase", "AllMapBase")

        # On affiche la map pour verif
        for i in range(len(self.map)):
            print(*self.map[i], sep=" ")
        
        for j in range(len(self.baseMap)):
            print(*self.baseMap[j], sep=" ")

        
            
           #
           # 
           #      writeJsonValue(Map, "coordsMapBase", "AllMap")

        

NiveauPlaineRiviere(150,75,200).Update()






