# ---------------------------------------------- PyMathsQuest ---------------------------------------------- #

# Import des settings
from settings import *

# Import des scripts algo pour placer les par-terre de fleurs; relier 2 points entre eux; 
# check si le niveau est faisable en reliant chaque point clé du niveau entre eux
from SourcesFichiers.ScriptAlgo.jeuDeLaVie import *
from SourcesFichiers.ScriptAlgo.liaisonAtoB import *
from SourcesFichiers.ScriptAlgo.astar import *


class GestionNiveauMap(object):
    def __init__(self, longueur, largeur):

        self.longueur = longueur
        self.largeur = largeur
        self.map = []
        self.baseMap = []
        self.ERROR_RELANCER = False 
        self.data = {
            "coordsMapBase" : {
                "Riviere0 Coords" : None,
                "Riviere1 Coords" : None,
                "Riviere2 Coords" : None,
                "Riviere3 Coords" : None,
                "AllMapInfo" : None,
                "AllMapBase" : None,
            }, 

            "coordsMapObject" : {
                "PNJ Coords" : None,
                "ObjAPlacer" : None,
                "RiverBoatTPChateau coords" : None,
                "Spawn" : None,
                "Exit" : None,
            },
        }

        self.BaseJson(self.data)
        self.BaseMap()

        self.makeRiverObj = RiverCreator(self)
        self.makeFlowerObj = FlowerCreator(self)
        self.makeVarienteSolObj = VarienteSolCreator(self)
        self.getPointSpecifiqueRiver = GetPointSpecifiqueRiver(self)
        self.makeBorder = BorderCreator(self)

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

    def CheckNiveauPossible(self, listOrdrePointCle :list, pathAccessible :list, mapTest) -> bool:
        """Méthode permettant de vérifier si le niveau est possible, suite à la position des obstacle. Utilisation du script A* permettant de trouver un chemin avec les déplacements ZQSD s'il exite entre un point A et B
        Ces points, donnés dans l'ordre d'évolution de la map, représente les coordonnées des éléments que le joueurs doit allé voir (pnj, arbre, entré, sortie..)"""

        for pointCle in range(len(listOrdrePointCle)-1): #
            if  Astar(listOrdrePointCle[pointCle], listOrdrePointCle[pointCle+1], mapTest, pathAccessible).a_star(): 
                continue
            else: # résolution du niveau est impossible
                return False # false pour niveau impossible
        return True # les chemins entre les points données existent  


    def SaveGlobal(self):
        # On charge la map de base
        AjoutJsonMapValue(self.map, "coordsMapBase", "AllMapInfo")

        # On charche la map (collision)
        AjoutJsonMapValue(self.baseMap, "coordsMapBase", "AllMapBase")

        for i in range(len(self.map)):
            print(*self.map[i], sep=" ")

        for j in range(len(self.baseMap)):
            print(*self.baseMap[j], sep=" ")


    def PlacementElements(self, coordsElements, pathJson): 
        """Méthode permettant de placer le spawn du joueur sur la map (collision) et d'ajouter ces coordonnées dans le json"""
        for coordsPlacement in coordsElements: # on parcourt toute la liste de coords
            self.map[coordsPlacement[1]][coordsPlacement[0]] = coordsPlacement[2] # on place les element aux coordonnées sur la map (avec la lettre)
        AjoutJsonMapValue(coordsElements, pathJson[0], pathJson[1]) # on ajoute les coordonnées du spawn au fichier json


class RiverCreator(object):

    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.longueur = 150 # river uniquement sur les grandes map
        self.largeur = 75
        self.listeCheminRiviere = []
        self.listePointRepere = []
        self.EspacementPointRepereRiviere = 15
        self.CoupageMapRiviere = 50 if NIVEAU["Map"] != "NiveauMedievale" else 75
        self.CouloirRiviere = 4

    def SetAndSave(self, numero):
                    # On ajoute les pts repère sur la map + les point spéciaux (haut et bas ) directement car collision avec montagne, donc il faut une ligne de 4 droite minimum
        for coordsPointRepere in self.listePointRepere: # positions de tout les points repère de la riviere
            self.gestionnaire.map[coordsPointRepere[1]][coordsPointRepere[0]] = "#" # on ajoute les pts repère sur la map normal (comme précédement)
            self.gestionnaire.baseMap[coordsPointRepere[1]][coordsPointRepere[0]] = "#"   # ajoute egalement les points repères de la riviere sur la map de base
            self.listeCheminRiviere.append([coordsPointRepere[0],coordsPointRepere[1]]) # forme [x,y]

        
        # Pour tout les points repère, on lie des points A et B entre eux avec le script crée pour l'occasion ! (confection maison)
        for nbPointRepereRiviere in range(len(self.listePointRepere)-1): # boucle avec indice -1 car on envoie le pts actuelle et le suivant pour les lier (n et  n+1)
            start = [self.listePointRepere[nbPointRepereRiviere][0], self.listePointRepere[nbPointRepereRiviere][1]] # fomre [x,y] start = aux coords du points actuel 
            goal = [self.listePointRepere[nbPointRepereRiviere+1][0], self.listePointRepere[nbPointRepereRiviere+1][1]] # fomre [x,y]   goal = coords du points suivant
            path = LiaisonAtoB(start, goal).GetPos()     # path de coords en [x,y]  script fait maison pour relier les points entre deux, on obtient une liste de position, correspondant au chemin à suivre


            # On recup la list de déplacement et on ajoute la rivière aux deux map
            for coords in path: # parcourt de la liste
                self.gestionnaire.map[coords[1]][coords[0]] = "#"  # ajout de l'element rivière sur la map (collision)
                self.gestionnaire.baseMap[coords[1]][coords[0]] = "#" # ajout de l'element rivière sur la map (base)
                self.listeCheminRiviere.append([coords[0],coords[1]]) # forme [x,y]  # stock des coords de toute la riviere dans la liste des coordonnées

        AjoutJsonMapValue(self.listeCheminRiviere, "coordsMapBase", f"Riviere{numero} Coords") # stockage des valeurs dans le fichier json

    def Reset(self):
        self.listeCheminRiviere = []
        self.listePointRepere = []

    def River0CreationVecticale(self, num):
        self.Reset()
        coordsPts1Riviere = [randint(0,6),0]
        self.listePointRepere.append(coordsPts1Riviere)
        
        coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1]+4] # on crée le second point avec une hauteur de + 4
        self.listePointRepere.append(coordsPts2Riviere) # forme [x,y] on ajoute le second point dans la liste

        # Point de haut en bas
        nbPts = self.largeur // self.EspacementPointRepereRiviere    # placement tout les 15 de hauteur ...   
        verifLigne5 = randint(1,(nbPts-1)) # choix du lieu pour la ligne de 5 droite pour sécu pos de pnj spécial et arbre spécial
        for nbPointRepere in range(1, nbPts):
            if verifLigne5 == nbPointRepere:
                pACoordsligne5 = [randint(0,6),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map pour les rivière de bordure
    
                self.listePointRepere.append(pACoordsligne5) # Ajout du point A car il devient un point repère à relier
                pBcoordsligne5 = [pACoordsligne5[0], nbPointRepere*self.EspacementPointRepereRiviere + 5] # forme [x, y]
                self.listePointRepere.append(pBcoordsligne5) # Ajout du point B car il devient un point repère à relier
            else:
                coords = [randint(0,6),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map pour les rivière de bordure       
                self.listePointRepere.append(coords) # on ajoute ces points dans la liste des points à relier

        coordsPts3Riviere = [randint(0,6),self.largeur-5] # on créer le point 1 de la map pour les rivière de bordure
        
        # Point du bas (dernier element)
        # permet de créer une ligne pour éviter les collisions avec les bordures
        self.listePointRepere.append(coordsPts3Riviere) # forme [x,y]  on ajoute l'avant dernier point repère
        coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1]+4] # on crée le dernier point avec une huteur de +4
        self.listePointRepere.append(coordsPts4Riviere) # forme [x,y] on ajoute le dernier point repère de la riviere
        self.SetAndSave(num)

    def River1CreationVecticale(self, num):
        self.Reset()
        coordsPts1Riviere = [randint((self.CoupageMapRiviere - self.CouloirRiviere),(self.CoupageMapRiviere + self.CouloirRiviere)),0] # on créer le point 1 de la map
        self.listePointRepere.append(coordsPts1Riviere)
        
        coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1]+4] # on crée le second point avec une hauteur de + 4
        self.listePointRepere.append(coordsPts2Riviere) # forme [x,y] on ajoute le second point dans la liste

        # Point de haut en bas
        nbPts = self.largeur // self.EspacementPointRepereRiviere    # placement tout les 15 de hauteur ...   
        verifLigne5 = randint(1,(nbPts-1)) # choix du lieu pour la ligne de 5 droite pour sécu pos de pnj spécial et arbre spécial
        for nbPointRepere in range(1, nbPts):
            if verifLigne5 == nbPointRepere:
                pACoordsligne5 = [randint((self.CoupageMapRiviere - self.CouloirRiviere),(self.CoupageMapRiviere + self.CouloirRiviere)), nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map
    
                self.listePointRepere.append(pACoordsligne5) # Ajout du point A car il devient un point repère à relier
                pBcoordsligne5 = [pACoordsligne5[0], nbPointRepere*self.EspacementPointRepereRiviere + 5] # forme [x, y]
                self.listePointRepere.append(pBcoordsligne5) # Ajout du point B car il devient un point repère à relier
            else:
                coords = [randint((self.CoupageMapRiviere - self.CouloirRiviere),(self.CoupageMapRiviere + self.CouloirRiviere)),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map
                self.listePointRepere.append(coords) # on ajoute ces points dans la liste des points à relier

        coordsPts3Riviere = [randint((self.CoupageMapRiviere - self.CouloirRiviere),(self.CoupageMapRiviere + self.CouloirRiviere)),self.largeur-5] # on créer le point 1 de la map
        # Point du bas (dernier element)
        # permet de créer une ligne pour éviter les collisions avec les bordures
        self.listePointRepere.append(coordsPts3Riviere) # forme [x,y]  on ajoute l'avant dernier point repère
        coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1]+4] # on crée le dernier point avec une huteur de +4
        self.listePointRepere.append(coordsPts4Riviere) # forme [x,y] on ajoute le dernier point repère de la riviere
        self.SetAndSave(num)

    def River2CreationVecticale(self, num):
        self.Reset()
        coordsPts1Riviere = [randint((2*self.CoupageMapRiviere - self.CouloirRiviere),(2*self.CoupageMapRiviere + self.CouloirRiviere)),0] # on créer le point 1 de la map
        self.listePointRepere.append(coordsPts1Riviere)
        
        coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1]+4] # on crée le second point avec une hauteur de + 4
        self.listePointRepere.append(coordsPts2Riviere) # forme [x,y] on ajoute le second point dans la liste

        # Point de haut en bas
        nbPts = self.largeur // self.EspacementPointRepereRiviere    # placement tout les 15 de hauteur ...   
        verifLigne5 = randint(1,(nbPts-1)) # choix du lieu pour la ligne de 5 droite pour sécu pos de pnj spécial et arbre spécial
        for nbPointRepere in range(1, nbPts):
            if verifLigne5 == nbPointRepere:
                pACoordsligne5 = [randint((2*self.CoupageMapRiviere - self.CouloirRiviere),(2*self.CoupageMapRiviere + self.CouloirRiviere)),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map
    
                self.listePointRepere.append(pACoordsligne5) # Ajout du point A car il devient un point repère à relier
                pBcoordsligne5 = [pACoordsligne5[0], nbPointRepere*self.EspacementPointRepereRiviere + 5] # forme [x, y]
                self.listePointRepere.append(pBcoordsligne5) # Ajout du point B car il devient un point repère à relier
            else:
                coords = [randint((2*self.CoupageMapRiviere - self.CouloirRiviere),(2*self.CoupageMapRiviere + self.CouloirRiviere)),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map
                self.listePointRepere.append(coords) # on ajoute ces points dans la liste des points à relier

        coordsPts3Riviere = [randint((2*self.CoupageMapRiviere - self.CouloirRiviere),(2*self.CoupageMapRiviere + self.CouloirRiviere)),self.largeur-5] # on créer le point 1 de la map
        # Point du bas (dernier element)
        # permet de créer une ligne pour éviter les collisions avec les bordures
        self.listePointRepere.append(coordsPts3Riviere) # forme [x,y]  on ajoute l'avant dernier point repère
        coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1]+4] # on crée le dernier point avec une huteur de +4
        self.listePointRepere.append(coordsPts4Riviere) # forme [x,y] on ajoute le dernier point repère de la riviere
        self.SetAndSave(num)

    def River3CreationVecticale(self, num):
        self.Reset()
        coordsPts1Riviere = [randint(LONGUEUR-7, LONGUEUR-2),0]
        self.listePointRepere.append(coordsPts1Riviere)
        
        coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1]+4] # on crée le second point avec une hauteur de + 4
        self.listePointRepere.append(coordsPts2Riviere) # forme [x,y] on ajoute le second point dans la liste

        # Point de haut en bas
        nbPts = self.largeur // self.EspacementPointRepereRiviere    # placement tout les 15 de hauteur ...   
        verifLigne5 = randint(1,(nbPts-1)) # choix du lieu pour la ligne de 5 droite pour sécu pos de pnj spécial et arbre spécial
        for nbPointRepere in range(1, nbPts):
            if verifLigne5 == nbPointRepere:
                pACoordsligne5 = [randint(LONGUEUR-7, LONGUEUR-2),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map
    
                self.listePointRepere.append(pACoordsligne5) # Ajout du point A car il devient un point repère à relier
                pBcoordsligne5 = [pACoordsligne5[0], nbPointRepere*self.EspacementPointRepereRiviere + 5] # forme [x, y]
                self.listePointRepere.append(pBcoordsligne5) # Ajout du point B car il devient un point repère à relier
            else:
                coords = [randint(LONGUEUR-7, LONGUEUR-2),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map
                self.listePointRepere.append(coords) # on ajoute ces points dans la liste des points à relier

        coordsPts3Riviere = [randint(LONGUEUR-7, LONGUEUR-2),self.largeur-5] # on créer le point 1 de la map
        # Point du bas (dernier element)
        # permet de créer une ligne pour éviter les collisions avec les bordures
        self.listePointRepere.append(coordsPts3Riviere) # forme [x,y]  on ajoute l'avant dernier point repère
        coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1]+4] # on crée le dernier point avec une huteur de +4
        self.listePointRepere.append(coordsPts4Riviere) # forme [x,y] on ajoute le dernier point repère de la riviere
        self.SetAndSave(num)
     
    def River2BisCreationVecticale(self, num):
        self.Reset()
        coordsPts1Riviere = [randint(LONGUEUR - 7, LONGUEUR - 2), 25]
        self.listePointRepere.append(coordsPts1Riviere)  # Ajouter le premier point repère

        coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1] + 4]
        self.listePointRepere.append(coordsPts2Riviere)

        nbPts = (self.largeur - 25) // self.EspacementPointRepereRiviere
        verifLigne5 = randint(1, (nbPts - 1))  # Position pour une section droite spéciale de la rivière
        
        # Ajout des points repères intermédiaires
        for nbPointRepere in range(1, nbPts):
            if verifLigne5 == nbPointRepere:  # Cas d'une ligne droite pour PNJ et éléments spéciaux
                pACoordsligne5 = [randint(LONGUEUR - 7, LONGUEUR - 2),nbPointRepere * self.EspacementPointRepereRiviere + 25]
                
                self.listePointRepere.append(pACoordsligne5)  # Ajouter le point A
                pBcoordsligne5 = [pACoordsligne5[0], pACoordsligne5[1] + 5]
                self.listePointRepere.append(pBcoordsligne5)  # Ajouter le point B
            else:
                coords = [randint(LONGUEUR - 7, LONGUEUR - 2),nbPointRepere * self.EspacementPointRepereRiviere + 25]
                self.listePointRepere.append(coords)

        coordsPts3Riviere = [randint(LONGUEUR - 7, LONGUEUR - 2), self.largeur - 5]
        self.listePointRepere.append(coordsPts3Riviere)
        
        coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1] + 4]
        self.listePointRepere.append(coordsPts4Riviere)
        self.SetAndSave(num)

    def River3CreationHorizontale(self, num):
        self.Reset()
        allCoordsRiviere1 = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")
        coordsPts1Riviere = choice(allCoordsRiviere1)
        while not (25 <= coordsPts1Riviere[1] <= 35):  # Assure que le point est dans une zone spécifique
            coordsPts1Riviere = choice(allCoordsRiviere1)
        self.listePointRepere.append(coordsPts1Riviere)  # Ajouter le premier point repère
        
        coordsPts2Riviere = [coordsPts1Riviere[0] + 4, coordsPts1Riviere[1]]
        self.listePointRepere.append(coordsPts2Riviere)

        nbPts = (self.longueur - 75) // self.EspacementPointRepereRiviere
        verifLigne5 = randint(1, (nbPts - 1))  # Position pour une section droite spéciale de la rivière
        
        # Ajout des points repères intermédiaires
        for nbPointRepere in range(1, nbPts):
            if verifLigne5 == nbPointRepere:  # Cas d'une ligne droite pour PNJ et éléments spéciaux
                pACoordsligne5 = [nbPointRepere * self.EspacementPointRepereRiviere + 75,randint((30 - self.CouloirRiviere), (30 + self.CouloirRiviere))]
                
                self.listePointRepere.append(pACoordsligne5)  # Ajouter le point A
                pBcoordsligne5 = [pACoordsligne5[0] + 5, pACoordsligne5[1]]
                self.listePointRepere.append(pBcoordsligne5)  # Ajouter le point B
            else:
                coords = [nbPointRepere * self.EspacementPointRepereRiviere + 75, randint((30 - self.CouloirRiviere), (30 + self.CouloirRiviere))]
                self.listePointRepere.append(coords)

        allCoordsRiviere2 = LoadJsonMapValue("coordsMapBase", "Riviere2 Coords")
        coordsPts3Riviere = allCoordsRiviere2[0]
        self.listePointRepere.append(coordsPts3Riviere)

        x = coordsPts3Riviere[0]
        c = 0
        while x + c < LONGUEUR - 1:
            c += 1
        coordsPts4Riviere = [x + c, coordsPts3Riviere[1]]
        self.listePointRepere.append(coordsPts4Riviere)
        self.SetAndSave(num)

class FlowerCreator(object):
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.longueur = 150
        self.largeur = 75

    def SetAndSave(self):
        for posFleur in self.getPosFleur: # on parcourt la liste de coordonnées
            if self.gestionnaire.map[posFleur[1]][posFleur[0]] =="-": # si sur la map (obstacle) il n'y a rien aux coords indiqués
                self.gestionnaire.baseMap[posFleur[1]][posFleur[0]] = 1 # on ajoute aux meme coordonnées dans la map base une fleur {1}

    def CreateFlower(self):
        self.getPosFleur = JeuDeLaVie(self.longueur, self.largeur).GetPos() # On récupère la liste de coordonnées des cellules vivantes
        self.SetAndSave()

class VarienteSolCreator(object):
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.nbElements = 0
        self.longueur = 150
        self.largeur = 75
    
    def SetAndSave(self):
        for coords in self.allCoordsElementVarienteSol:
            self.gestionnaire.baseMap[coords[1]][coords[0]] = 2 # on ajoute sur la map de test l'object

    def CreateVarienteSol(self, nombre):
        self.nbElements = nombre
        self.allCoordsElementVarienteSol = []
        for _ in range(self.nbElements): # boucle pour le nombre d'obstacle différents
            ElementPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] pos random sur la map, en éviant les bordure
            while self.gestionnaire.baseMap[ElementPos[1]][ElementPos[0]] != '-' :
                ElementPos = [randint(0, self.longueur-1), randint(0, self.largeur-1)] # forme [x,y] # on replace si jamais il y a un element
            self.allCoordsElementVarienteSol.append(ElementPos)
        self.SetAndSave()

class GetPointSpecifiqueRiver(object):
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.longueur = 150
        self.largeur = 75

    def CheckPosRiviere(self, indice : list) -> bool:
        """Méthode permettant de regarder et de valider la position d'un element par raport à la riviere (pnj / arbre spécial)"""
        
        listePosPossible = ["-", "1", "2"] #path possible

        if indice[0] == 149: # position de la sortir sur la bordure de map (donc condition de check diférentes)
            if (self.gestionnaire.map[indice[1]][indice[0]-1] in listePosPossible) and (self.gestionnaire.map[indice[1]][indice[0]-2] in listePosPossible )and (indice[1] >=5) and (indice[1] <= 70) and (self.gestionnaire.map[indice[1]-1][indice[0]-1] in listePosPossible): 
                return True # on valide le placement
        elif (self.gestionnaire.map[indice[1]][indice[0]-1] in listePosPossible) and (self.gestionnaire.map[indice[1]][indice[0]-2] in listePosPossible )and(self.gestionnaire.map[indice[1]][indice[0]+1] in listePosPossible) and (indice[1] >=5) and (indice[1] <= 70) and (self.gestionnaire.map[indice[1]-1][indice[0]-1] in listePosPossible): 
            return True # on valide le placement
        else:
            return False # on invalide le placement

    def PlacementSpecial(self, index1, index2):
        listeCoordsElement = LoadJsonMapValue(index1, index2) # récupération de la liste de valeurs d'un element (riviere)

        Go = True
        while Go: # tant que go = True on check 
            indice = randint(0, self.largeur-1) # génération aléatoire d'un indice
            # Si true, on arreter la boucle
            if self.CheckPosRiviere(listeCoordsElement[indice]): # check si à les coords de la liste  l'indice respect les conditions pour poser l'element
                Go = False # Arret de la boucle
                
        itemCoords = listeCoordsElement[indice] # on crée un copie des coords dans la variable
        return itemCoords # return (x,y ) coord de l'element

class BorderCreator(object):
    def __init__(self, gestionnaire):
        self.gestionnaire= gestionnaire
        self.longueur = 150
        self.largeur = 75

    def SetAndSave(self):
        for coords in self.listeBordures:
            self.gestionnaire.map[coords[1]][coords[0]] = "B"  # on ajoute sur la map de test l'objec
            self.gestionnaire.baseMap[coords[1]][coords[0]] = "B"  # on ajoute sur la map de test l'object

    def CreateBorder(self):
        # bordure map  
        self.listeBordures = [] 
        for i in range(2):
            for j in range(self.longueur):
                self.listeBordures.append([j, i*(self.largeur-1)]) 
        self.SetAndSave()



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
        self.map[self.coordsCampFire[1]][self.coordsCampFire[0]] = "V"
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
a, b, c = NiveauMedievale().Update()