from settings import *
from Sources.Map.creationMap import *
from Sources.Elements.sprites import *
from Sources.Personnages.player import *
from Sources.Elements.groups import *
from Sources.Personnages.pnj import *



class LoadMapPlaineRiviere(): # nv 0
    def __init__(self, allSprites : any, collisionSprites : any, allpnj : any, interactions) -> None:
        """Méthode initialisation chargement de la map du niveau plaine et rivière. 
        Input : niveau : int, allSprites / collisionsSprites / allpnj : element pygame; Output : None"""
    
        # class des éléments pygame
        self.allPNJ = allpnj
        self.allSprites = allSprites
        self.collisionSprites = collisionSprites
        self.interactions = interactions

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
        self.pont1 = pygame.image.load(join("Images", "Pont", "BridgeTreeW-Ex128.png")).convert_alpha()
        self.pont2 = pygame.image.load(join("Images", "Pont", "BridgePlanksW-Ex128.png")).convert_alpha()
        self.rockExit = pygame.image.load(join("Images", "Obstacle", "ExitRock.png")).convert_alpha()

    def Setup(self) -> None:
        """Méthode de build de tout les éléments sprites de la map jeu.
        Input / Output : None"""

        # création de la map du niveau (sectionnée en deux)
        self.map, self.mapBase = NiveauPlaineRiviere(LONGUEUR, LARGEUR).Update()

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
                                CollisionSprites(pos, self.tree2,"Arbre", (self.allSprites, self.collisionSprites))
                            else:
                                CollisionSprites(pos, self.tree,"Arbre", (self.allSprites, self.collisionSprites))
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
        coordsSpawnList = LoadJsonMapValue("coordsMapObject", "Spawn")

        # parcours et création des spritess
        for coordsElementSpawn in coordsSpawnList:
            pos = (coordsElementSpawn[0]*CASEMAP, coordsElementSpawn[1]*CASEMAP) # calcul coords pygame
            if coordsElementSpawn[2] == "C":
                CollisionSprites(pos, self.campFire, "campFire", (self.allSprites, self.collisionSprites))


    def SetupExit(self):
        """Méthode de placemet de la sortie
        Input / Ouput : None"""

        coords = LoadJsonMapValue("coordsMapObject", "Exit")

        coordsExit = (coords[0] * CASEMAP, coords[1] * CASEMAP)
        CollisionSprites(coordsExit, self.rockExit, "ExitRock", (self.allSprites, self.interactions, self.collisionSprites))
        
        # pont décalé de 1
        coordsPont = (coords[0]*CASEMAP +CASEMAP, coords[1]*CASEMAP)
        # True = element de création exo maths
        CollisionSprites(coordsPont, self.pont2, "pont2", (self.allSprites, self.collisionSprites, self.interactions), True) 

    def SetupPNJ(self) -> None:
        """Méthode de création et position des pnj.
        Input / Output : None"""

        # Récupération des coords + infos pnj
        coordsPNJList = LoadJsonMapValue("coordsMapObject","PNJ Coords")
        
        # parcours et création des sprites pnj
        for coordsPNJ in coordsPNJList:
            pos = (coordsPNJ[0]*CASEMAP, coordsPNJ[1]*CASEMAP) # calcul coords pygame
            if coordsPNJ[3] == 1 : 
                PNJ(pos , "PNJ1", (self.allPNJ, self.allSprites, self.collisionSprites))
            if coordsPNJ[3] == 2 : 
                PNJ(pos , "PNJ2", (self.allPNJ, self.allSprites, self.collisionSprites))
            if coordsPNJ[3] == 3 :
                PNJ(pos , "PNJ3", (self.allPNJ, self.allSprites, self.collisionSprites))
        
    
    def AddPont(self, element : str, coords : tuple) -> None:
        """Méthode placement et ajout de pont sur la map pygame
        Input : element : str, coords : tuple
        Output : None"""

        if element == "pont1":
            CollisionSprites(coords, self.pont1, element, (self.allSprites, self.collisionSprites, self.interactions))
        elif element  == "pont2":
            CollisionSprites(coords, self.pont2, element, (self.allSprites, self.collisionSprites, self.interactions))

                


    def Update(self) -> list:
        """Méthode de mise à jour (utilisation unique) + retour de map.
        Input : None, Output : list"""

        # Appel méthodes créations map + sprites
        self.LoadImages()
        self.Setup()
        self.SetupSpawn()
        self.SetupPNJ()
        self.SetupExit()

        # retour des infos de map
        return self.map, self.mapBase
    

class LoadMedievale(): # nv1 
    def __init__(self, allSprites : any, collisionSprites : any, allpnj : any, interactions) -> None:
        """Méthode initialisation chargement de la map du niveau médievale 
        Input : niveau : int, allSprites / collisionsSprites / allpnj : element pygame; Output : None"""
    
        # class des éléments pygame
        self.allPNJ = allpnj
        self.allSprites = allSprites
        self.collisionSprites = collisionSprites
        self.interactions = interactions

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
        self.pont1 = pygame.image.load(join("Images", "Pont", "BridgeTreeW-Ex128.png")).convert_alpha()
        self.pont2 = pygame.image.load(join("Images", "Pont", "BridgePlanksW-Ex128.png")).convert_alpha()
        self.pont3 = pygame.image.load(join("Images", "Pont","BridgePlanksN-S-x128.png" )).convert_alpha()
        self.rockExit = pygame.image.load(join("Images", "Obstacle", "ExitRock.png")).convert_alpha()



        self.pathTshapeNSE = pygame.image.load(join("Images", "Sol", "Path", "PathN-SEx128.png")).convert_alpha()
        self.pathTshapeWES = pygame.image.load(join("Images", "Sol", "Path", "PathW-ESx128.png")).convert_alpha()
        self.pathTshapeWNS = pygame.image.load(join("Images", "Sol", "Path", "PathWN-Sx128.png")).convert_alpha()
        self.pathTshapeNEW = pygame.image.load(join("Images", "Sol", "Path", "PathN-EWx128.png")).convert_alpha()
        self.pathAngularNE = pygame.image.load(join("Images", "Sol", "Path", "PathN-Ex128.png")).convert_alpha()
        self.pathAngularNW = pygame.image.load(join("Images", "Sol", "Path", "PathN-Wx128.png")).convert_alpha()
        self.pathAngularSE = pygame.image.load(join("Images", "Sol", "Path", "PathE-Sx128.png")).convert_alpha()
        self.pathAngularSW = pygame.image.load(join("Images", "Sol", "Path", "PathW-Sx128.png")).convert_alpha()
        self.pathNS = pygame.image.load(join("Images", "Sol", "Path", "PathN-S.png")).convert_alpha()
        self.pathWE = pygame.image.load(join("Images", "Sol", "Path", "PathW-E.png")).convert_alpha()
        self.pathEndN = pygame.image.load(join("Images", "Sol", "Path", "PathNx128.png")).convert_alpha()
        self.pathEndS = pygame.image.load(join("Images", "Sol", "Path", "PathSx128.png")).convert_alpha()
        self.pathEndE = pygame.image.load(join("Images", "Sol", "Path", "PathEx128.png")).convert_alpha()
        self.pathEndW = pygame.image.load(join("Images", "Sol", "Path", "PathWx128.png")).convert_alpha()


        self.champ = pygame.image.load(join("Images", "Sol", "Champs.png")).convert_alpha()
        self.house = pygame.image.load(join("Images", "Obstacle", "Structures", "House.png")).convert_alpha()
        self.well = pygame.image.load(join("Images", "Obstacle", "Structures", "Puits.png")).convert_alpha()
        self.chateau = pygame.image.load(join("Images", "Obstacle", "Structures", "Chateau.png")).convert_alpha()
        self.MuraillesWE = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesWE.png" )).convert_alpha()
        self.MuraillesNS = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesNS.png" )).convert_alpha()
        self.MuraillesNE = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesNE.png" )).convert_alpha()
        self.MuraillesNW = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesNW.png" )).convert_alpha()
        self.MuraillesEAU = pygame.image.load(join("Images", "Obstacle", "Structures", "Chateau", "MuraillesEAU.png" )).convert_alpha()
        self.tableCraft = pygame.image.load(join("Images", "Obstacle", "TableCraft.png")).convert_alpha()
        self.boat = pygame.image.load(join("Images", "Obstacle", "Boat.png")).convert_alpha()




    def Setup(self) -> None:
        """Méthode de build de tout les éléments sprites de la map jeu.
        Input / Output : None"""

        # création de la map du niveau (sectionnée en deux)
        self.map, self.mapBase = NiveauMedievale(LONGUEUR, LARGEUR).Update()

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

                # === Vérification du type de chemin === aide IA
                elif self.mapBase[ordonnees][abscisses] == "=":

                    def is_path(self, x, y):
                        """ Vérifie si une case est un chemin tout en évitant les erreurs d'index. """
                        return 0 <= x < len(self.mapBase) and 0 <= y < len(self.mapBase[0]) and self.mapBase[x][y] == "="

                    def is_water(self, x, y):
                        """ Vérifie si une case est une rivière. """
                        return 0 <= x < len(self.mapBase) and 0 <= y < len(self.mapBase[0]) and self.mapBase[x][y] == "#"

                    # Récupération des voisins
                    up = is_path(self, ordonnees - 1, abscisses)
                    down = is_path(self, ordonnees + 1, abscisses)
                    left = is_path(self, ordonnees, abscisses - 1)
                    right = is_path(self, ordonnees, abscisses + 1)

                    water_up = is_water(self, ordonnees - 1, abscisses)
                    water_down = is_water(self, ordonnees + 1, abscisses)
                    water_left = is_water(self, ordonnees, abscisses - 1)
                    water_right = is_water(self, ordonnees, abscisses + 1)


                    # === 1. Intersection à 4 branches ===
                    if up and down and left and right:
                        Sprites(pos, self.pathTshapeNEW, self.allSprites)

                    # === 2. Formes en "T" ===
                    elif up and down and left:
                        Sprites(pos, self.pathTshapeWNS, self.allSprites)
                    elif up and down and right:
                        Sprites(pos, self.pathTshapeNSE, self.allSprites)
                    elif up and right and left:
                        Sprites(pos, self.pathTshapeNEW, self.allSprites)
                    elif down and right and left:
                        Sprites(pos, self.pathTshapeWES, self.allSprites)

                    # === 3. Virages (angles) ===
                    elif up and right:
                        Sprites(pos, self.pathAngularNE, self.allSprites)
                    elif up and left:
                        Sprites(pos, self.pathAngularNW, self.allSprites)
                    elif down and right:
                        Sprites(pos, self.pathAngularSE, self.allSprites)
                    elif down and left:
                        Sprites(pos, self.pathAngularSW, self.allSprites)

                    # === 4. Lignes droites ===
                    elif up and down:
                        Sprites(pos, self.pathNS, self.allSprites)
                    elif left and right:
                        Sprites(pos, self.pathWE, self.allSprites)

                    # # === 5. Fin de chemin au contact de l'eau ===
                    # elif water_up and not down:
                    #     if left:
                    #         Sprites(pos, self.pathEndSW, self.allSprites)  # Courbe sud-ouest
                    #     elif right:
                    #         Sprites(pos, self.pathEndSE, self.allSprites)  # Courbe sud-est
                    #     else:
                    #         Sprites(pos, self.pathEndS, self.allSprites)  # Fin droite sud

                    # elif water_down and not up:
                    #     if left:
                    #         Sprites(pos, self.pathEndNW, self.allSprites)  # Courbe nord-ouest
                    #     elif right:
                    #         Sprites(pos, self.pathEndNE, self.allSprites)  # Courbe nord-est
                    #     else:
                    #         Sprites(pos, self.pathEndN, self.allSprites)  # Fin droite nord

                    # elif water_left and not right:
                    #     if up:
                    #         Sprites(pos, self.pathEndNE, self.allSprites)  # Courbe nord-est
                    #     elif down:
                    #         Sprites(pos, self.pathEndSE, self.allSprites)  # Courbe sud-est
                    #     else:
                    #         Sprites(pos, self.pathEndE, self.allSprites)  # Fin droite est

                    # elif water_right and not left:
                    #     if up:
                    #         Sprites(pos, self.pathEndNW, self.allSprites)  # Courbe nord-ouest
                    #     elif down:
                    #         Sprites(pos, self.pathEndSW, self.allSprites)  # Courbe sud-ouest
                    #     else:
                    #         Sprites(pos, self.pathEndW, self.allSprites)  # Fin droite ouest


                    # === 6. Fin de chemin SANS contact avec l'eau ===
                    elif not up and not down and not left and right:
                        Sprites(pos, self.pathEndE, self.allSprites)  # Fin Ouest
                    elif not up and not down and left and not right:
                        Sprites(pos, self.pathEndW, self.allSprites)  # Fin Est
                    elif not left and not right and up and not down:
                        Sprites(pos, self.pathEndN, self.allSprites)  # Fin Sud
                    elif not left and not right and not up and down:
                        Sprites(pos, self.pathEndS, self.allSprites)  # Fin Nord

                        

                # Toutes les cases rivières
                elif self.mapBase[ordonnees][abscisses] == "#":
                    stateFormat = ""
                    if  ordonnees not in [0, LARGEUR-1] and abscisses not in [0,149]:
                        
                        # tshape
                        if (self.mapBase[ordonnees - 1][abscisses] =="#" or self.mapBase[ordonnees- 1][abscisses] =="C") and self.mapBase[ordonnees+ 1][abscisses] =="#" and self.mapBase[ordonnees][abscisses -1] =="#" and (self.mapBase[ordonnees-2][abscisses] =="#" or self.mapBase[ordonnees-1][abscisses] =="#"):
                            stateFormat = "RiverTWN-Sx128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif (self.mapBase[ordonnees - 1][abscisses] =="#" or self.mapBase[ordonnees - 1][abscisses] =="C")  and self.mapBase[ordonnees+1][abscisses] =="#" and self.mapBase[ordonnees][abscisses +1] =="#" and (self.mapBase[ordonnees-2][abscisses] =="#" or self.mapBase[ordonnees-1][abscisses] =="#"):
                            stateFormat = "RiverTN-SEx128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif (self.mapBase[ordonnees - 1][abscisses] =="#" or self.mapBase[ordonnees- 1][abscisses] =="C")  and self.mapBase[ordonnees][abscisses- 1] =="#" and self.mapBase[ordonnees][abscisses +1] =="#" and (self.mapBase[ordonnees-2][abscisses] =="#" or self.mapBase[ordonnees-1][abscisses] =="#"):
                            stateFormat = "RiverTWN-Ex128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif self.mapBase[ordonnees +1][abscisses] =="#"  and self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees][abscisses +1] =="#" :
                            stateFormat = "RiverTW-SEx128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)

                        elif self.mapBase[ordonnees][abscisses+1] =="#" and ((self.mapBase[ordonnees-1][abscisses] =="#" or self.mapBase[ordonnees-1][abscisses] =="C") or (self.mapBase[ordonnees-2][abscisses] =="#" or self.mapBase[ordonnees-1][abscisses] =="#")):
                            stateFormat = "RiverAngularN-Ex128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif self.mapBase[ordonnees][abscisses+1] =="#" and ((self.mapBase[ordonnees+1][abscisses] =="#" or self.mapBase[ordonnees+1][abscisses] =="C") or (self.mapBase[ordonnees+2][abscisses] =="#" or self.mapBase[ordonnees+1][abscisses] =="#")):
                            stateFormat = "RiverAngularE-Sx128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif self.mapBase[ordonnees][abscisses-1] =="#" and ((self.mapBase[ordonnees-1][abscisses] =="#" or self.mapBase[ordonnees-1][abscisses] =="C") or (self.mapBase[ordonnees-2][abscisses] =="#" or self.mapBase[ordonnees-1][abscisses] =="#")):
                            stateFormat = "RiverAngularN-Wx128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif self.mapBase[ordonnees][abscisses-1] =="#" and ((self.mapBase[ordonnees+1][abscisses] =="#" or self.mapBase[ordonnees+1][abscisses] =="C") or (self.mapBase[ordonnees+2][abscisses] =="#" or self.mapBase[ordonnees+1][abscisses] =="#")):
                            stateFormat = "RiverAngularW-Sx128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees][abscisses-1] =="#":
                            stateFormat = "RiverStraightW-Ex128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif self.mapBase[ordonnees-1][abscisses] =="#" and (self.mapBase[ordonnees+1][abscisses] or self.mapBase[ordonnees+1][abscisses] =="C"): 
                            stateFormat = "RiverStraightN-Sx128"
                            River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                        elif self.mapBase[ordonnees+1][abscisses] =="#" and self.mapBase[ordonnees-1][abscisses] =="C": # chateau collision
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
                            if self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees+1][abscisses] !="#" and self.mapBase[ordonnees-1][abscisses] =="C":
                                stateFormat = "RiverStraightW-Ex128"
                                River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                            elif self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
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
                                CollisionSprites(pos, self.tree,"Arbre", (self.allSprites, self.collisionSprites, self.interactions))
                            else:
                                CollisionSprites(pos, self.tree2,"Arbre2", (self.allSprites, self.collisionSprites, self.interactions))
                    elif 65 < choixObstacle <= 85:
                        CollisionSprites(pos, self.hugeRock, "HugeRock", (self.allSprites, self.collisionSprites))
                    elif 85 < choixObstacle <= 100:
                        CollisionSprites(pos, self.souche, "Souche", (self.allSprites, self.collisionSprites))

                # Pont placé
                if self.map[ordonnees][abscisses] == "T":
                    CollisionSprites(pos, self.pont2, "pont2",  (self.allSprites, self.collisionSprites))
                    print(self.allSprites)

                if self.map[ordonnees][abscisses] == "X":
                    CollisionSprites(pos, self.pont3, "pont3",  (self.allSprites, self.collisionSprites, self.interactions))
                    print(self.allSprites)

                # champs
                if self.map[ordonnees][abscisses] == "@":
                    CollisionSprites(pos, self.champ, "Champs",  (self.allSprites, self.collisionSprites))

                # chateau  # check aide IA
                if self.map[ordonnees][abscisses] == "C":

                    # Vérification des limites avant chaque accès à la carte
                    def case_valide(y, x):
                        return 0 <= y < len(self.map) and 0 <= x < len(self.map[0])

                    if case_valide(ordonnees, abscisses + 1) and self.map[ordonnees][abscisses + 1] == "B" and \
                    case_valide(ordonnees, abscisses - 1) and self.map[ordonnees][abscisses - 1] == "B" and \
                    self.map[ordonnees+1][abscisses] != "C":
                        # pts ref placement chateau
                        CollisionSprites(pos, self.chateau, "Chateau", (self.allSprites, self.collisionSprites))

                    elif case_valide(ordonnees - 1, abscisses) and self.map[ordonnees - 1][abscisses] == "C" and \
                        case_valide(ordonnees, abscisses + 1) and self.map[ordonnees][abscisses + 1] == "C":
                        CollisionSprites(pos, self.MuraillesNE, "Murailles", (self.allSprites, self.collisionSprites))

                    elif case_valide(ordonnees - 1, abscisses) and self.map[ordonnees - 1][abscisses] == "C" and \
                        case_valide(ordonnees, abscisses - 1) and self.map[ordonnees][abscisses - 1] == "C":
                        CollisionSprites(pos, self.MuraillesNW, "Murailles", (self.allSprites, self.collisionSprites))

                    # passage eau
                    elif case_valide(ordonnees, abscisses + 1) and self.map[ordonnees][abscisses + 1] == "C" and \
                        case_valide(ordonnees, abscisses - 1) and self.map[ordonnees][abscisses - 1] == "C" and \
                        case_valide(ordonnees - 1, abscisses) and self.map[ordonnees - 1][abscisses] == "#" and \
                        case_valide(ordonnees + 1, abscisses) and self.map[ordonnees + 1][abscisses] == "#":
                        CollisionSprites(pos, self.MuraillesEAU, "Murailles", (self.allSprites, self.collisionSprites))

                    elif case_valide(ordonnees, abscisses + 1) and self.map[ordonnees][abscisses + 1] == "C" or \
                        case_valide(ordonnees, abscisses - 1) and self.map[ordonnees][abscisses - 1] == "C":
                        CollisionSprites(pos, self.MuraillesWE, "Murailles", (self.allSprites, self.collisionSprites))

                    elif case_valide(ordonnees + 1, abscisses) and self.map[ordonnees + 1][abscisses] == "C" or \
                        case_valide(ordonnees - 1, abscisses) and self.map[ordonnees - 1][abscisses] == "C":
                        CollisionSprites(pos, self.MuraillesNS, "Murailles", (self.allSprites, self.collisionSprites))




                # maisons
                if self.map[ordonnees][abscisses] == "H" : 
                    Sprites(pos, self.grass, self.allSprites) 
                    if self.map[ordonnees+1][abscisses] == "H" and self.map[ordonnees][abscisses +1] == "H":
                        CollisionSprites(pos, self.house, "House", (self.allSprites, self.collisionSprites))


                # puits 
                if self.map[ordonnees][abscisses] == "W" :
                    Sprites(pos, self.grass, self.allSprites) 
                    if self.map[ordonnees-1][abscisses] == "W" and self.map[ordonnees][abscisses +1] == "W":
                        CollisionSprites(pos, self.well, "Well", (self.allSprites, self.collisionSprites))

                if self.map[ordonnees][abscisses] == "E" :
                    CollisionSprites(pos, self.tableCraft, "TableCraft", (self.allSprites, self.collisionSprites, self.interactions))


    def SetupExit(self):
        """Méthode de placemet de la sortie
        Input / Ouput : None"""

        coords = LoadJsonMapValue("coordsMapObject", "Exit")


    def SetupPNJ(self) -> None:
        """Méthode de création et position des pnj.
        Input / Output : None"""

        # Récupération des coords + infos pnj
        coordsPNJList = LoadJsonMapValue("coordsMapObject","PNJ Coords")
        
        # parcours et création des sprites pnj
        for coordsPNJ in coordsPNJList:
            pos = (coordsPNJ[0]*CASEMAP, coordsPNJ[1]*CASEMAP) # calcul coords pygame
            if coordsPNJ[3] == 1 : 
                PNJ(pos , "PNJ1", (self.allPNJ, self.allSprites, self.collisionSprites))
            if coordsPNJ[3] == 2 : 
                pos = (pos[0]+64, pos[1]+64)
                PNJ(pos , "PNJ2", (self.allPNJ, self.allSprites, self.collisionSprites))
            if coordsPNJ[3] == 3 :
                PNJ(pos , "PNJ3", (self.allPNJ, self.allSprites, self.collisionSprites))
            if coordsPNJ[3] == 4 :
                PNJ(pos , "PNJ4", (self.allPNJ, self.allSprites, self.collisionSprites))
        
    
    def AddPont(self, element : str, coords : tuple) -> None:
        """Méthode placement et ajout de pont sur la map pygame
        Input : element : str, coords : tuple
        Output : None"""

        if element  == "pont2" or element == "pont3":
            CollisionSprites(coords, self.pont2, element, (self.allSprites, self.collisionSprites, self.interactions))


    def AddBoat(self, element : str, coords : tuple) -> None:
        """Méthode placement et ajout de pont sur la map pygame
        Input : element : str, coords : tuple
        Output : None"""

        if element  == "Boat":
            CollisionSprites(coords, self.boat, element, (self.allSprites, self.collisionSprites, self.interactions))



    def Update(self) -> list:
        """Méthode de mise à jour (utilisation unique) + retour de map.
        Input : None, Output : list"""

        # Appel méthodes créations map + sprites
        self.LoadImages()
        self.Setup()
        self.SetupPNJ()
        self.SetupExit()

        # retour des infos de map
        return self.map, self.mapBase