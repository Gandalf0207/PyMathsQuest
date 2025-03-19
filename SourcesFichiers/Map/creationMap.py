# ---------------------------------------------- PyMathsQuest ---------------------------------------------- #

# Import des settings
from settings import *

# Import des scripts algo pour placer les par-terre de fleurs; relier 2 points entre eux; 
# check si le niveau est faisable en reliant chaque point clé du niveau entre eux
from SourcesFichiers.ScriptAlgo.jeuDeLaVie import *
from SourcesFichiers.ScriptAlgo.liaisonAtoB import *
from SourcesFichiers.ScriptAlgo.astar import *

from SourcesFichiers.Map.OutilsCreationMap.borderCreator import *
from SourcesFichiers.Map.OutilsCreationMap.flowerCreator import *
from SourcesFichiers.Map.OutilsCreationMap.getPointSpecifiqueRiver import *
from SourcesFichiers.Map.OutilsCreationMap.riverCreator import *
from SourcesFichiers.Map.OutilsCreationMap.varienteSolCreator import *



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
            
