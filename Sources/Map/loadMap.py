from settings import *
from Sources.Map.creationMap import *
from Sources.Elements.sprites import *
from Sources.Personnages.player import *
from Sources.Elements.groups import *
from Sources.Personnages.pnj import *



class LoadMapPlaineRiviere(): # nv 0
    def __init__(self, allSprites : any, collisionSprites : any, allpnj : any) -> None:
        """Méthode initialisation chargement de la map du niveau plaine et rivière. 
        Input : niveau : int, allSprites / collisionsSprites / allpnj : element pygame; Output : None"""
    


        # class des éléments pygame
        self.allPNJ = allpnj
        self.allSprites = allSprites
        self.collisionSprites = collisionSprites


    def LoadJsonMapValue(self, index1 :str, index2 :str) -> list:
        """Récupération des valeur stockées dans le fichier json pour les renvoyer quand nécéssaire 
        à l'aide des indices données.
        Input : index1 / index2 = str   , Output : list"""
        
        with open(join("Sources","Ressources","AllMapValue.json"), "r") as f: # ouverture lecture
            loadElementJson = json.load(f) # chargement des valeurs
        return loadElementJson[index1].get(index2, None) # retour valeurs


    def LoadImages(self) -> None:
        """Méthode de chargement de toutes les images pour la map 
        Input / Output : None """

        self.grass = pygame.image.load(join("Images", "Sol", "Grass", "Grass.png")).convert_alpha()
        self.flowers = pygame.image.load(join("Images", "Sol", "Flower", "Flower.png")).convert_alpha()
        self.tree = pygame.image.load(join("Images", "Obstacle", "Arbre.png")).convert_alpha()
        self.tree2 = pygame.image.load(join("Images", "Obstacle", "Arbre2.png")).convert_alpha()
        self.rock = pygame.image.load(join("Images", "Sol","Rock", "Rock.png")).convert_alpha()
        self.mud = pygame.image.load(join("Images", "Sol","Mud", "Mud.png")).convert_alpha()
        self.montainWE = pygame.image.load(join("Images", "Border","Mountain", "MountainStraighW-Ex128.png")).convert_alpha()
        self.montainWE1 = pygame.image.load(join("Images", "Border","Mountain", "MountainStraighW-Ealt1x128.png")).convert_alpha()
        self.souche = pygame.image.load(join("Images", "Obstacle", "Souche.png")).convert_alpha()
        self.hugeRock = pygame.image.load(join("Images", "Obstacle", "HugeRock.png")).convert_alpha()
        self.campFire = pygame.image.load(join("Images", "Obstacle", "Spawn", "campFire.png")).convert_alpha()
        self.banc = pygame.image.load(join("Images", "Obstacle", "Spawn", "banc.png")).convert_alpha()  
        self.pont1 = pygame.image.load(join("Images", "Pont", "BridgeTreeW-Ex128.png")).convert_alpha()
        self.pont2 = pygame.image.load(join("Images", "Pont", "BridgePlanksW-Ex128.png")).convert_alpha()

    def Setup(self) -> None:
        """Méthode de build de tout les éléments sprites de la map jeu.
        Input / Output : None"""

        # création de la map du niveau (sectionnée en deux)
        self.map, self.mapBase = NiveauPlaineRiviere(LONGUEUR, LARGEUR, 1000,200,300).Update()

        # parcours et création de chaque sprites
        for ordonnees in range(len(self.mapBase)):
            for abscisses in range(len(self.mapBase[ordonnees])):
                pos = (abscisses * CASEMAP, ordonnees * CASEMAP)  # Coordonnées de la case sur la carte
                
                # Sol
                if self.mapBase[ordonnees][abscisses] == "F":
                    Sprites(pos, self.flowers, self.allSprites)
                elif self.mapBase[ordonnees][abscisses] == "M":
                    Sprites(pos, self.mud, self.allSprites) 
                elif self.mapBase[ordonnees][abscisses] == "R":
                    Sprites(pos, self.rock, self.allSprites) 
                elif self.mapBase[ordonnees][abscisses] == "-" :
                    Sprites(pos, self.grass, self.allSprites) 

                # Toutes les cases rivières
                elif self.mapBase[ordonnees][abscisses] == "#":
                    stateFormat = ""
                    if  ordonnees not in [0, LARGEUR-1] and abscisses not in [0,149]:
                        if self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                            stateFormat = "RiverAngularN-Ex128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees+1][abscisses] =="#":
                            stateFormat = "RiverAngularE-Sx128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                            stateFormat = "RiverAngularN-Wx128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees+1][abscisses] =="#":
                            stateFormat = "RiverAngularW-Sx128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees][abscisses-1] =="#":
                            stateFormat = "RiverStraightW-Ex128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif self.mapBase[ordonnees+1][abscisses] =="#" and self.mapBase[ordonnees-1][abscisses] =="#": 
                            stateFormat = "RiverStraightN-Sx128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                    else:
                        if ordonnees in [0, LARGEUR-1]: 
                            stateFormat = "RiverMontainConflictx128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif abscisses ==0:
                            if self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                                stateFormat = "RiverAngularN-Ex128"
                                River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                            elif self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees+1][abscisses] =="#":
                                stateFormat = "RiverAngularE-Sx128"
                                River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                            elif self.mapBase[ordonnees+1][abscisses] =="#" and self.mapBase[ordonnees-1][abscisses] =="#": 
                                stateFormat = "RiverStraightN-Sx128"
                                River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif abscisses == LARGEUR-1:
                            if self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                                stateFormat = "RiverAngularN-Wx128"
                                River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                            elif self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees+1][abscisses] =="#":
                                stateFormat = "RiverAngularW-Sx128"
                                River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                            elif self.mapBase[ordonnees+1][abscisses] =="#" and self.mapBase[ordonnees-1][abscisses] =="#": 
                                stateFormat = "RiverStraightN-Sx128"
                                River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                
                # Bordure Montagne
                elif self.mapBase[ordonnees][abscisses] == "B":
                    if (ordonnees == 0 or ordonnees == (LARGEUR-1) ):
                        
                        if ordonnees == 0:
                            if choice([True, False]):
                                CollisionSprites(pos, self.montainWE,"BorderTop",  (self.allSprites, self.collisionSprites))
                            else:
                                CollisionSprites(pos, self.montainWE1, "BorderTop", (self.allSprites, self.collisionSprites))

                        else:
                            if choice([True, False]):
                                CollisionSprites(pos, self.montainWE, "BorderBottom", (self.allSprites, self.collisionSprites))
                            else:
                                CollisionSprites(pos, self.montainWE1,"BorderBottom",  (self.allSprites, self.collisionSprites))
                
                # Tout les obstales
                if self.map[ordonnees][abscisses] == "O":
                    choixObstacle = randint(0,100)
                    if choixObstacle <= 65:
                            if randint(0,3) > 2:
                                CollisionSprites(pos, self.tree2,"Abre", (self.allSprites, self.collisionSprites))
                            else:
                                CollisionSprites(pos, self.tree,"Abre", (self.allSprites, self.collisionSprites))
                    elif 65 < choixObstacle <= 85:
                        CollisionSprites(pos, self.hugeRock, "HugeRock", (self.allSprites, self.collisionSprites))
                    elif 85 < choixObstacle <= 100:
                        CollisionSprites(pos, self.souche, "Souche", (self.allSprites, self.collisionSprites))

                # Abre spécial
                if self.map[ordonnees][abscisses] == "A":
                    CollisionSprites(pos, self.tree,"Arbre",  (self.allSprites, self.collisionSprites))


    def SetupSpawn(self) -> None:
        """Méthode de création du spawn de la map.
        Input / Output : None"""

        # Récupération coords spawn + infos element
        coordsSpawnList = self.LoadJsonMapValue("coordsMapObject", "CampSpawn Coords")
        
        # parcours et création des spritess
        for coordsElementSpawn in coordsSpawnList:
            pos = (coordsElementSpawn[0]*CASEMAP, coordsElementSpawn[1]*CASEMAP) # calcul coords pygame
            if coordsElementSpawn[2] == "C":
                CollisionSprites(pos, self.campFire, "campFire", (self.allSprites, self.collisionSprites))
            elif coordsElementSpawn[2] == "b":
                CollisionSprites(pos, self.banc, "banc", (self.allSprites, self.collisionSprites) )


    def SetupPNJ(self) -> None:
        """Méthode de création et position des pnj.
        Input / Output : None"""

        # Récupération des coords + infos pnj
        coordsPNJList = self.LoadJsonMapValue("coordsMapObject","PNJ Coords")
        
        # parcours et création des sprites pnj
        for coordsPNJ in coordsPNJList:
            pos = (coordsPNJ[0]*CASEMAP, coordsPNJ[1]*CASEMAP) # calcul coords pygame
            if coordsPNJ[2] == 1 : 
                PNJ(pos , "PNJ1", (self.allPNJ, self.allSprites, self.collisionSprites))
            if coordsPNJ[2] == 2 : 
                PNJ(pos , "PNJ2", (self.allPNJ, self.allSprites, self.collisionSprites))
            if coordsPNJ[2] == 3 :
                PNJ(pos , "PNJ3", (self.allPNJ, self.allSprites, self.collisionSprites))
        
    
    def AddPont(self, groupPont, element, coords) -> None:
        if element == "pont1":
            CollisionSprites(coords, self.pont1, element, (self.allSprites, self.collisionSprites, groupPont))
        elif element  == "pont2":
            CollisionSprites(coords, self.pont2, element, (self.allSprites, self.collisionSprites, groupPont))


    def Update(self) -> list:
        """Méthode de mise à jour (utilisation unique) + retour de map.
        Input : None, Output : list"""

        # Appel méthodes créations map + sprites
        self.LoadImages()
        self.Setup()
        self.SetupSpawn()
        self.SetupPNJ()

        # retour des infos de map
        return self.map, self.mapBase