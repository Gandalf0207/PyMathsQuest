from settings import *
from ScriptAlgo.jeuDeLaVie import *
from ScriptAlgo.LiaisonAtoB import *

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

    def BaseMap(self):
        """Création de la double liste avec les bordures de la map(map)"""
        # map de base
        for _ in range(self.largeur): # largeur de la map (y)
            creationMap = [] # liste pour stocker les valeurs des colonnes (x)
            for _ in range(self.longueur): # longueur de la map (x)
                creationMap.append("-") # ajout des valeurs (x)
            self.map.append(creationMap) # ajout de la ligne entière
        
        # position des bordure sur la map : 
        listeBordures = []
        for i in range(2):
            for j in range(self.longueur): # position des bordures haut et bas
                self.map[i*(self.largeur-1)][j] = "B"
                listeBordures.append([i*(self.largeur-1), j])

            for j in range(self.largeur): # position des bordures gauche et droites
                self.map[j][i*(self.longueur-1)] = "B"
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
        self.pnj = []
        self.data = {
                    "coordsMapBase" : {
                        "Bordures Coords": "null",
                        "Riviere0 Coords" : "null",
                        "Riviere1 Coords" : "null",
                        "Flowers Coords" : "null",
                        "AllMap" : "null"
                    },

                    "coordsMapObject" : {
                        "Obstacles Coords" : "null",
                        "PNJ Coords" : "null",
                        "ArbreSpecial Coords" : "null"
                    }
                }

    def __CheckPos__(self, indice):
        # verification si la position du pnj est possible autour de la riviere (rivière large de 1 uniquement) + eviter de la placer trop haut / bas
        if (self.map[indice[1]][indice[0]-1] =="-") and (self.map[indice[1]][indice[0]-2] =="-" )and( self.map[indice[1]][indice[0]+1] =="-") and (indice[1] >=5) and (indice[1] <= 70):
            return True
        else:
            return False
        
    def PlacementFleur(self):
        # placement de l'herbe (Alt 1 et 2 et 3) avec jeu de la vie
        getPosFleur = JeuDeLaVie().GetPos()
        listeFlowerCoords = []
        for posFleur in getPosFleur:
            if self.map[posFleur[1]][posFleur[0]] =="-":
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
                listeCheminRiviere.append([listePointRepere[0][0], 5-ordonnees]) # forme [x,y]

            for coordsPointRepere in listePointRepere: # positions de tout les points repère de la riviere
                self.map[coordsPointRepere[1]][coordsPointRepere[0]] = "#" 
                listeCheminRiviere.append([coordsPointRepere[0],coordsPointRepere[1]]) # forme [x,y]

            for ordonnees in range(0,5): # derniere ligne de 5 pour arrivr sur le bas de la map
                self.map[self.largeur-5 +ordonnees][listePointRepere[-1][0]] = "#" #   y pour changer de ligne, x pour se positionner sur la meme colone que le dernier point repère de la rivire
                listeCheminRiviere.append([listePointRepere[-1][0], self.largeur-5 + ordonnees])  # forme [x,y]


            
            # Pour tout les points repère, on lie des point A et B entre eux avec le script crée pour l'occasion
            for nbPointRepereRiviere in range(len(listePointRepere)-1):
                start = [listePointRepere[nbPointRepereRiviere][0], listePointRepere[nbPointRepereRiviere][1]] # fomre [x,y]
                goal = [listePointRepere[nbPointRepereRiviere+1][0], listePointRepere[nbPointRepereRiviere+1][1]] # fomre [x,y]   
                path = LiaisonAtoB(start, goal).GetPos()     ########


                # On recup la list de déplacement et on ajoute la rivière à la map
                for coords in path:
                    self.map[coords[0]][coords[1]] = "#"
                    listeCheminRiviere.append([coords[0],coords[1]])

            super().AjoutJsonMapValue(listeCheminRiviere, "coordsMapBase", f"Riviere{i} Coords") # add value to json file

    def PlacementObstacle(self):
        #placement des obstacle sur la map
        listeObstacle = []
        for i in range(self.obstacle):
            pos = [randint(4, self.largeur-4), randint(4, self.longueur-4)]
            while self.map[pos[0]][pos[1]] != '-': # check de s'il y a déjà des éléments sur la map.
                pos = [randint(4, self.largeur-4), randint(4, self.longueur-4)]
            self.map[pos[0]][pos[1]] = "O"
            listeObstacle.append(pos)

        super().AjoutJsonMapValue(listeObstacle, "coordsMapObject", "Obstacles Coords")



    def Update(self):
        super().BaseJson(self.data)
        super().BaseMap()  
        self.PlacementRiviere()
        self.PlacementFleur()
        self.PlacementObstacle()
        coordsPNJ = [[randint(5, self.largeur-5), randint(1+5,((self.longueur//3) -5))], 
                    self.PlacementSpecial("coordsMapBase", "Riviere1 Coords", "P"), # placement pnj (ne tombre jamais sur les coords de la rivière)
                    [randint(5, self.largeur-5), randint(((self.longueur//3)*2 +5), self.longueur-5)]]           
        super().PlacementPNJ(coordsPNJ)
        coordsAbre = self.PlacementSpecial("coordsMapBase", "Riviere0 Coords", "A")
        super().AjoutJsonMapValue(coordsAbre, "coordsMapObject", "AbreSpecial Coords")

                
        
        # On affiche la map pour verif
        for i in range(len(self.map)):
            print(*self.map[i], sep=" ")
            
           #
           # 
           #      writeJsonValue(Map, "coordsMapBase", "AllMap")

        

NiveauPlaineRiviere(150,75,200).Update()




        

# passage niveau suivant (cailloux)



