from settings import *
from Sources.Map.creationMap import *
from Sources.Elements.sprites import *
from Sources.Personnages.player import *
from Sources.Elements.groups import *
from Sources.Personnages.pnj import *



class LoadMap():
    def __init__(self, allSprites : any, collisionSprites : any, allpnj : any, interactions) -> None:
        """Méthode initialisation chargement de la map du niveau plaine et rivière. 
        Input : niveau : int, allSprites / collisionsSprites / allpnj : element pygame; Output : None"""
    
        # class des éléments pygame
        self.allPNJ = allpnj
        self.allSprites = allSprites
        self.collisionSprites = collisionSprites
        self.interactions = interactions
        self.ERROR_RELANCER = False

    def LoadImages(self) -> None:
        """Méthode de chargement de toutes les images pour la map 
        Input / Output : None """

        # load commun
        if NIVEAU["Map"] in ["NiveauPlaineRiviere", "NiveauMedievale"]:
            self.sol = pygame.image.load(join("Images", "Sol", "Grass", "Grass.png")).convert_alpha()
            self.flowers = pygame.image.load(join("Images", "Sol", "Flower", "Flower.png")).convert_alpha()
            self.tree = pygame.image.load(join("Images", "Obstacle", "Arbre.png")).convert_alpha()
            self.tree2 = pygame.image.load(join("Images", "Obstacle", "Arbre2.png")).convert_alpha()
            self.rock = pygame.image.load(join("Images", "Sol","Rock", "Rock.png")).convert_alpha()
            self.mud = pygame.image.load(join("Images", "Sol","Mud", "Mud.png")).convert_alpha()
            self.montainWE = pygame.image.load(join("Images", "Border","Mountain", "MountainStraighW-Ex128.png")).convert_alpha()
            self.montainWE1 = pygame.image.load(join("Images", "Border","Mountain", "MountainStraighW-Ealt1x128.png")).convert_alpha()
            self.souche = pygame.image.load(join("Images", "Obstacle", "Souche.png")).convert_alpha()
            self.souche2 = pygame.image.load(join("Images", "Obstacle", "Souche2.png")).convert_alpha()
            self.hugeRock = pygame.image.load(join("Images", "Obstacle", "HugeRock.png")).convert_alpha()
            self.pont2 = pygame.image.load(join("Images", "Pont", "BridgePlanksW-Ex128.png")).convert_alpha()
            self.pont3 = pygame.image.load(join("Images", "Pont","BridgePlanksN-S-x128.png" )).convert_alpha()

        # load Spécifique 
        if NIVEAU["Map"] == "NiveauPlaineRiviere":
            self.campFire = pygame.image.load(join("Images", "Obstacle", "Spawn", "campFire.png")).convert_alpha()
            self.pont1 = pygame.image.load(join("Images", "Pont", "BridgeTreeW-Ex128.png")).convert_alpha()

        if NIVEAU["Map"] == "NiveauMedievale":
            self.pathX = pygame.image.load(join("Images", "Sol", "Path", "PathXx128.png")).convert_alpha()
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
            self.MuraillesMountain = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesMountain.png" )).convert_alpha()
            self.MuraillesAngle = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesAngle.png" )).convert_alpha()
            self.tableCraft = pygame.image.load(join("Images", "Obstacle", "TableCraft.png")).convert_alpha()
            self.boat = pygame.image.load(join("Images", "Obstacle", "Boat.png")).convert_alpha()
            self.DoorChateau = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
            self.DoorMurailles =  pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()

            if INFOS["DemiNiveau"] : 
                self.MursAngleWS = pygame.image.load(join("Images", "Chateau", "MursChateau.png")).convert_alpha()
                self.Pilier = pygame.image.load(join("Images", "Chateau", "Piliers.png")).convert_alpha()
                self.Chandelier = pygame.image.load(join("Images", "Chateau", "Chandelier.png")).convert_alpha()
                self.Socle = pygame.image.load(join("Images", "Chateau", "Socle.png")).convert_alpha()
                self.Door = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
                self.Portal = pygame.image.load(join("Images", "Chateau", "Portal.png")).convert_alpha()
                self.Sol = pygame.image.load(join("Images", "Chateau", "SolChateau.png")).convert_alpha()
                self.CerclePortal = pygame.image.load(join("Images", "Chateau", "SolChateau.png")).convert_alpha()
        
        if NIVEAU["Map"] == "NiveauBaseFuturiste":
            self.sol = pygame.image.load(join("Images", "Sol", "Grass", "Grass.png")).convert_alpha()
            self.sol2 = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Floorx128.png")).convert_alpha()
            self.bones = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
            self.vent = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Ventx128.png")).convert_alpha()
            self.wallAngularNE = pygame.image.load(join("Images", "Sol", "Path", "PathN-Ex128.png")).convert_alpha()
            self.wallAngularNW = pygame.image.load(join("Images", "Sol", "Path", "PathN-Wx128.png")).convert_alpha()
            self.wallAngularSE = pygame.image.load(join("Images", "Sol", "Path", "PathE-Sx128.png")).convert_alpha()
            self.wallAngularSW = pygame.image.load(join("Images", "Sol", "Path", "PathW-Sx128.png")).convert_alpha()
            
            self.wallNSGauche = pygame.image.load(join("Images", "Sol", "Path", "PathN-S.png")).convert_alpha()
            self.wallWEHaut = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "WallEWx128.png")).convert_alpha()
            self.wallNSDroite = pygame.image.load(join("Images", "Sol", "Path", "PathN-S.png")).convert_alpha()
            self.wallWEBas = pygame.image.load(join("Images", "Sol", "Path", "PathN-S.png")).convert_alpha()
            
            self.centraleNuc = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Reacteur.png")).convert_alpha()
            self.cafet = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Cafet.png")).convert_alpha()
            self.essence = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Essence.png")).convert_alpha()
            self.salleLancement = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Lancement.png")).convert_alpha()

            self.doorFuturiste = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()


            self.InteractionBlocReactor = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
            self.obstacles = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Crate.png")).convert_alpha()



    def Setup(self) -> None:
        """Méthode de build de tout les éléments sprites de la map jeu.
        Input / Output : None"""

        # création de la map du niveau (sectionnée en deux)
        if NIVEAU["Map"] == "NiveauPlaineRiviere":
            self.map, self.mapBase, self.ERROR_RELANCER = NiveauPlaineRiviere().Update()
        if NIVEAU["Map"] == "NiveauMedievale":
            if not INFOS["DemiNiveau"]:
                self.map, self.mapBase, self.ERROR_RELANCER = NiveauMedievale().Update()
            else:
                self.map, self.mapBase, self.ERROR_RELANCER =  NiveauMedievaleChateau().Update()
        if NIVEAU["Map"] == "NiveauBaseFuturiste":
            if not INFOS["DemiNiveau"]:
                self.map, self.mapBase, self.ERROR_RELANCER = NiveauBaseFuturiste().Update()
            else:
                pass
        
        
        # si erreur : return
        if self.ERROR_RELANCER:
            return None

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
                    Sprites(pos, self.sol, self.allSprites) 
                elif self.mapBase[ordonnees][abscisses] == ".":
                    Sprites(pos, self.sol2, self.allSprites)
                elif self.mapBase[ordonnees][abscisses] == "G":
                    Sprites(pos, self.bones, self.allSprites)

                # === Vérification du type de chemin === aide IA
                elif self.mapBase[ordonnees][abscisses] == "=":

                    def is_path(self, x, y):
                        """ Vérifie si une case est un chemin tout en évitant les erreurs d'index. """
                        return 0 <= x < len(self.mapBase) and 0 <= y < len(self.mapBase[0]) and self.mapBase[x][y] == "="

                    # Récupération des voisins
                    up = is_path(self, ordonnees - 1, abscisses)
                    down = is_path(self, ordonnees + 1, abscisses)
                    left = is_path(self, ordonnees, abscisses - 1)
                    right = is_path(self, ordonnees, abscisses + 1)

                    # === 1. Intersection à 4 branches ===
                    if up and down and left and right:
                        Sprites(pos, self.pathX, self.allSprites)

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

                    # === 6. Fin de chemin SANS contact avec l'eau ===
                    elif not up and not down and not left and right:
                        Sprites(pos, self.pathEndE, self.allSprites)  # Fin Ouest
                    elif not up and not down and left and not right:
                        Sprites(pos, self.pathEndW, self.allSprites)  # Fin Est
                    elif not left and not right and up and not down:
                        Sprites(pos, self.pathEndN, self.allSprites)  # Fin Sud
                    elif not left and not right and not up and down:
                        Sprites(pos, self.pathEndS, self.allSprites)  # Fin Nord
                    
                    # path par défault
                    else:
                        Sprites(pos, self.pathWE, self.allSprites)

                # Toutes les cases rivières
                elif self.mapBase[ordonnees][abscisses] == "#":

                    # Vérification des bords pour éviter les erreurs d'index
                    can_go_up = ordonnees > 0
                    can_go_down = ordonnees < LARGEUR - 1
                    can_go_left = abscisses > 0
                    can_go_right = abscisses < 149

                    def checkBuildUp(can_go_up, can_go_left, can_go_right):
                        if can_go_up:
                            if self.mapBase[ordonnees -1][abscisses] == "#":
                                return True
                            if self.mapBase[ordonnees -1][abscisses] == "C":
                                if can_go_right and can_go_left:
                                    if self.mapBase[ordonnees -2][abscisses-1] == "#" or self.mapBase[ordonnees -2][abscisses] == "#" or self.mapBase[ordonnees -2][abscisses +1] == "#":
                                        return True
                                if can_go_left:
                                    if self.mapBase[ordonnees -2][abscisses-1] == "#" or self.mapBase[ordonnees -2][abscisses] == "#":   
                                        return True
                                if can_go_right:
                                    if self.mapBase[ordonnees -2][abscisses] == "#" or self.mapBase[ordonnees -2][abscisses +1] == "#":   
                                        return True     
                        return False   
                    
                    def checkBuildDown(can_go_down, can_go_left, can_go_right): 
                        if can_go_down:
                            if self.mapBase[ordonnees +1][abscisses] == "#":
                                return True
                            if self.mapBase[ordonnees +1][abscisses] == "C":
                                if can_go_right and can_go_left:
                                    if self.mapBase[ordonnees +2][abscisses-1] == "#" or self.mapBase[ordonnees +2][abscisses] == "#" or self.mapBase[ordonnees +2][abscisses +1] == "#":
                                        return True
                                if can_go_left:
                                    if self.mapBase[ordonnees +2][abscisses-1] == "#" or self.mapBase[ordonnees +2][abscisses] == "#":   
                                        return True
                                if can_go_right:
                                    if self.mapBase[ordonnees +2][abscisses] == "#" or self.mapBase[ordonnees +2][abscisses +1] == "#":   
                                        return True        
                        return False

                    def checkBuildLeft(can_go_left):
                        if can_go_left:
                            if self.mapBase[ordonnees][abscisses - 1] == "#":
                                return True
                        return False
                    
                    def checkBuildRight(can_go_right):
                        if can_go_right:
                            if self.mapBase[ordonnees][abscisses + 1] == "#":
                                return True
                        return False       

                    def checkBuildConflict(can_go_left, can_go_right):
                        if can_go_left and can_go_right:
                            if self.mapBase[ordonnees][abscisses-1] == "B" or self.mapBase[ordonnees][abscisses+1] == "B": 
                                return True
                        if can_go_left:  
                            if self.mapBase[ordonnees][abscisses-1] == "B":
                                return True
                        if can_go_right:  
                            if self.mapBase[ordonnees][abscisses+1] == "B":
                                return True

                        return False
                    
                    can_build_up = checkBuildUp(can_go_up, can_go_left, can_go_right)
                    can_build_down = checkBuildDown(can_go_down,  can_go_left, can_go_right)
                    can_build_left = checkBuildLeft(can_go_left)
                    can_build_right = checkBuildRight(can_go_right)
                    mountainConflict = checkBuildConflict(can_go_left, can_go_right)


                    stateFormat = ""
                    # conflif montain
                    if mountainConflict:
                        stateFormat = "RiverMontainConflictx128"
                        River(pos, (self.allSprites, self.collisionSprites), stateFormat)

                    # Tshape
                    elif can_build_right and can_build_left and can_build_up:
                        stateFormat = "RiverTWN-Ex128"
                        River(pos, (self.allSprites, self.collisionSprites), stateFormat)   
                    elif can_build_right and can_build_left and can_build_down:
                        stateFormat = "RiverTW-SEx128"
                        River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                    elif can_build_down and can_build_up and can_build_left:
                        stateFormat = "RiverTWN-Sx128"
                        River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                    elif can_build_down and can_build_up and can_build_right:
                        stateFormat = "RiverTN-SEx128"
                        River(pos, (self.allSprites, self.collisionSprites), stateFormat)

                    # angular
                    elif can_build_right and can_build_down:
                        stateFormat = "RiverAngularE-Sx128"
                        River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                    elif can_build_right and can_build_up:
                        stateFormat = "RiverAngularN-Ex128"
                        River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                    elif can_build_left and can_build_down:
                        stateFormat = "RiverAngularW-Sx128"
                        River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                    elif can_build_left and can_build_up:
                        stateFormat = "RiverAngularN-Wx128"
                        River(pos, (self.allSprites, self.collisionSprites), stateFormat)

                    # line
                    elif can_build_up or can_build_down:
                        stateFormat = "RiverStraightN-Sx128"
                        River(pos, (self.allSprites, self.collisionSprites), stateFormat)
                    elif can_build_right or can_build_left:
                        stateFormat = "RiverStraightW-Ex128"
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
                                if NIVEAU["Map"] == "NiveauPlaineRiviere": # add interaction arbre
                                    CollisionSprites(pos, self.tree2,"Arbre2", (self.allSprites, self.collisionSprites))
                                else:
                                    CollisionSprites(pos, self.tree2,"Arbre2", (self.allSprites, self.collisionSprites, self.interactions))
                            else:
                                if NIVEAU["Map"] == "NiveauPlaineRiviere":
                                    CollisionSprites(pos, self.tree,"Arbre", (self.allSprites, self.collisionSprites))
                                else:
                                    CollisionSprites(pos, self.tree,"Arbre", (self.allSprites, self.collisionSprites, self.interactions))
                    elif 65 < choixObstacle <= 85:
                        CollisionSprites(pos, self.hugeRock, "HugeRock", (self.allSprites, self.collisionSprites))
                    elif 85 < choixObstacle <= 100:
                        choixSouche = randint(0,11)
                        if choixSouche < 7:
                            if NIVEAU["Map"] == "NiveauPlaineRiviere": # add interaction arbre
                                CollisionSprites(pos, self.souche,"Souche", (self.allSprites, self.collisionSprites))
                            else:
                                CollisionSprites(pos, self.souche,"Souche", (self.allSprites, self.collisionSprites, self.interactions))
                        else:
                            if NIVEAU["Map"] == "NiveauPlaineRiviere":
                                CollisionSprites(pos, self.souche2,"Souche2", (self.allSprites, self.collisionSprites))
                            else:
                                CollisionSprites(pos, self.souche2,"Souche2", (self.allSprites, self.collisionSprites, self.interactions))



                # Abre spécial
                if self.map[ordonnees][abscisses] == "A":
                    CollisionSprites(pos, self.tree,"Arbre",  (self.allSprites, self.collisionSprites))

                # Pont placé
                if self.map[ordonnees][abscisses] == "T":
                    CollisionSprites(pos, self.pont2, "pont2",  (self.allSprites, self.collisionSprites))

                if self.map[ordonnees][abscisses] == "X":
                    CollisionSprites(pos, self.pont3, "pont3",  (self.allSprites, self.collisionSprites, self.interactions))

                # champs
                if self.map[ordonnees][abscisses] == "@":
                    CollisionSprites(pos, self.champ, "Champs",  (self.allSprites, self.collisionSprites))


                # chateau
                if self.map[ordonnees][abscisses] == "C":
                    
                    def case_valide(y, x):
                        """ Vérifie si une case est valide dans la carte."""
                        return 0 <= y < len(self.map) and 0 <= x < len(self.map[0])
                    
                    # Vérification des voisins
                    right = case_valide(ordonnees, abscisses + 1) and self.map[ordonnees][abscisses + 1] in ["C", "d"]
                    left = case_valide(ordonnees, abscisses - 1) and self.map[ordonnees][abscisses - 1] in ["C", "d"]
                    up = case_valide(ordonnees - 1, abscisses) and self.map[ordonnees - 1][abscisses] == "C"
                    down = case_valide(ordonnees + 1, abscisses) and self.map[ordonnees + 1][abscisses] == "C"
                    
                    # Placement du château
                    if down and self.map[ordonnees][abscisses -1] == "B":
                        CollisionSprites(pos, self.MuraillesMountain, "Murailles", (self.allSprites, self.collisionSprites))
                    
                    # Murailles en angle
                    elif up and right:
                        CollisionSprites(pos, self.MuraillesAngle, "MuraillesAngle", (self.allSprites, self.collisionSprites))
                    elif up and left:
                        CollisionSprites(pos, self.MuraillesAngle, "MuraillesAngle", (self.allSprites, self.collisionSprites))
                    
                    # Passage avec de l'eau
                    elif right and left and case_valide(ordonnees - 1, abscisses) and self.map[ordonnees - 1][abscisses] == "#" \
                        and case_valide(ordonnees + 1, abscisses) and self.map[ordonnees + 1][abscisses] == "#":
                        River(pos, (self.allSprites, self.collisionSprites), "CastleWallRiverx128")
                    
                    # Murailles droites
                    elif right or left:
                        CollisionSprites(pos, self.MuraillesWE, "Murailles", (self.allSprites, self.collisionSprites))
                    elif up or down:
                        CollisionSprites(pos, self.MuraillesNS, "Murailles", (self.allSprites, self.collisionSprites))
                    else:
                        # case du blit chateau
                        CollisionSprites(pos, self.chateau, "Chateau", (self.allSprites, self.collisionSprites))



                if self.map[ordonnees][abscisses] == "D":
                    CollisionSprites(pos, self.DoorChateau, "Door", (self.collisionSprites, self.interactions, self.allSprites))
                if self.map[ordonnees][abscisses] == "d":
                    CollisionSprites(pos, self.DoorMurailles, "Door2", (self.collisionSprites, self.allSprites))


                # maisons
                if self.map[ordonnees][abscisses] == "H" : 
                    Sprites(pos, self.sol, self.allSprites) 
                    if self.map[ordonnees+1][abscisses] == "H" and self.map[ordonnees][abscisses +1] == "H":
                        CollisionSprites(pos, self.house, "House", (self.allSprites, self.collisionSprites))


                # puits 
                if self.map[ordonnees][abscisses] == "W" :
                    Sprites(pos, self.sol, self.allSprites) 
                    if self.map[ordonnees-1][abscisses] == "W" and self.map[ordonnees][abscisses +1] == "W":
                        CollisionSprites(pos, self.well, "Well", (self.allSprites, self.collisionSprites))

                if self.map[ordonnees][abscisses] == "E" :
                    CollisionSprites(pos, self.tableCraft, "TableCraft", (self.allSprites, self.collisionSprites, self.interactions))

                # DEMI NIVEAU MEDIEVALE
                # base de la map
                if self.mapBase[ordonnees][abscisses] == "~":
                    Sprites(pos, self.Sol, self.allSprites)
                elif self.mapBase[ordonnees][abscisses] == "o":
                    CollisionSprites(pos, self.MursAngleWS, "Mur", (self.collisionSprites, self.allSprites))
                elif self.mapBase[ordonnees][abscisses] == "U":
                    Sprites(pos, self.Socle, self.allSprites)
                elif self.mapBase[ordonnees][abscisses] == "D" :
                    if self.mapBase[ordonnees][abscisses-1] == "o" and self.mapBase[ordonnees][abscisses+ 1] =="o": # acces uniquemente pour le demi niveau
                        CollisionSprites(pos, self.Door, "Door", (self.collisionSprites, self.allSprites))

                # obstacle de la map
                if self.map[ordonnees][abscisses] == "u":
                    CollisionSprites(pos, self.Portal, "Portal", (self.collisionSprites, self.allSprites))
                elif self.map[ordonnees][abscisses] == "Y":
                    CollisionSprites(pos, self.Pilier, "Pilier",  (self.collisionSprites, self.allSprites))
                elif self.map[ordonnees][abscisses] == "r":
                    CollisionSprites(pos, self.Chandelier, "Chandelier", (self.collisionSprites, self.allSprites))

                # niveau base futuriste
                if self.map[ordonnees][abscisses] == "j":
                    CollisionSprites(pos, self.vent, "Vent", (self.interactions,self.collisionSprites, self.allSprites))

                elif self.map[ordonnees][abscisses] == "m":
                    CollisionSprites(pos, self.doorFuturiste, "DoorFuturiste", (self.allSprites, self.collisionSprites))

                elif self.map[ordonnees][abscisses] == "&":

                    def is_path(self, x, y):
                        """ Vérifie si une case est un chemin tout en évitant les erreurs d'index. """
                        return 0 <= x < len(self.mapBase) and 0 <= y < len(self.mapBase[0]) and self.mapBase[x][y] == "&"

                    # Récupération des voisins
                    up = is_path(self, ordonnees - 1, abscisses)
                    down = is_path(self, ordonnees + 1, abscisses)
                    left = is_path(self, ordonnees, abscisses - 1)
                    right = is_path(self, ordonnees, abscisses + 1)

                    # === 3. Virages (angles) ===
                    if up and right:
                        CollisionSprites(pos, self.wallAngularNE, "Wall", (self.allSprites, self.collisionSprites))
                    elif up and left:
                        CollisionSprites(pos, self.wallAngularNW, "Wall", (self.allSprites, self.collisionSprites))
                    elif down and right:
                        CollisionSprites(pos, self.wallAngularSE, "Wall", (self.allSprites, self.collisionSprites))
                    elif down and left:
                        CollisionSprites(pos, self.wallAngularSW, "Wall", (self.allSprites, self.collisionSprites))

                    # === 4. Lignes droites ===
                    elif left and right:
                        if self.mapBase[ordonnees-1][abscisses] == "." and self.mapBase[ordonnees+1][abscisses] == ".":
                            CollisionSprites(pos, self.wallWEHaut, "Wall", (self.allSprites, self.collisionSprites))
                        elif self.mapBase[ordonnees+1][abscisses] == ".":
                            CollisionSprites(pos, self.wallWEHaut, "Wall", (self.allSprites, self.collisionSprites))
                        elif self.mapBase[ordonnees-1][abscisses] == ".":
                            CollisionSprites(pos, self.wallWEBas, "Wall", (self.allSprites, self.collisionSprites))

                    elif up and down:
                        if self.mapBase[ordonnees][abscisses-1] == ".":
                            CollisionSprites(pos, self.wallNSDroite, "Wall", (self.allSprites, self.collisionSprites))
                        else:
                            CollisionSprites(pos, self.wallNSGauche, "Wall", (self.allSprites, self.collisionSprites))

                    else:
                        CollisionSprites(pos, self.wallWEHaut, "Wall", (self.allSprites, self.collisionSprites))


                elif self.map[ordonnees][abscisses] == "S" and NIVEAU["Map"] == "NiveauBaseFuturiste":
                    AnimatedSprites(pos, (self.allSprites), "PortalGif", join("Images","Portal"))

                elif self.map[ordonnees][abscisses] in ["§", "£", "$", "?"]:
                    if self.map[ordonnees][abscisses] == "§":
                        CollisionSprites(pos, self.centraleNuc, "Reacteur", (self.collisionSprites, self.allSprites))
                    elif self.map[ordonnees][abscisses] == "£":
                        CollisionSprites(pos, self.cafet, "Cafet", (self.allSprites, self.collisionSprites))
                    elif self.map[ordonnees][abscisses] == "$":
                        CollisionSprites(pos, self.essence, "Essence", (self.allSprites, self.collisionSprites))
                    elif self.map[ordonnees][abscisses] == "?":
                        CollisionSprites(pos, self.salleLancement, "Lancement", (self.collisionSprites, self.allSprites))

                elif self.map[ordonnees][abscisses] == "¤":
                    CollisionSprites(pos, self.InteractionBlocReactor, "ReactorBloc", (self.allSprites, self.collisionSprites, self.interactions))

                elif self.map[ordonnees][abscisses] == "k":
                    CollisionSprites(pos, self.obstacles, "Caisses", (self.collisionSprites, self.allSprites))





    def SetupSpawn(self) -> None:
        """Méthode de création du spawn de la map.
        Input / Output : None"""

        # Récupération coords spawn + infos element
        coordsSpawnList = LoadJsonMapValue("coordsMapObject", "Spawn")

        # parcours et création des spritess
        for coordsElementSpawn in coordsSpawnList:
            pos = (coordsElementSpawn[0]*CASEMAP, coordsElementSpawn[1]*CASEMAP) # calcul coords pygame
            if coordsElementSpawn[2] == "J":
                CollisionSprites(pos, self.campFire, "campFire", (self.allSprites, self.collisionSprites))


    def SetupExit(self):
        """Méthode de placemet de la sortie
        Input / Ouput : None"""

        coords = LoadJsonMapValue("coordsMapObject", "Exit")

        coordsExit = (coords[0] * CASEMAP, coords[1] * CASEMAP)
        CollisionSprites(coordsExit, self.hugeRock, "ExitRock", (self.allSprites, self.interactions, self.collisionSprites))
        
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
            pos = (coordsPNJ[0]*CASEMAP + 64, coordsPNJ[1]*CASEMAP + 64) # calcul coords pygame
            if coordsPNJ[3] == 1 : 
                PNJOBJ(pos , "PNJ1", (self.allPNJ, self.allSprites, self.collisionSprites))
            if coordsPNJ[3] == 2 : 
                PNJOBJ(pos , "PNJ2", (self.allPNJ, self.allSprites, self.collisionSprites))
            if coordsPNJ[3] == 3 :
                PNJOBJ(pos , "PNJ3", (self.allPNJ, self.allSprites, self.collisionSprites))
            if coordsPNJ[3] == 4 :
                PNJOBJ(pos, "PNJ4", (self.allPNJ, self.allSprites, self.collisionSprites))
            # pas de pnj 5 car il se déplace

    
    def AddPont(self, element : str, coords : tuple) -> None:
        """Méthode placement et ajout de pont sur la map pygame
        Input : element : str, coords : tuple
        Output : None"""

        if element == "pont1":
            CollisionSprites(coords, self.pont1, element, (self.allSprites, self.collisionSprites, self.interactions))
        elif element  == "pont2":
            CollisionSprites(coords, self.pont2, element, (self.allSprites, self.collisionSprites, self.interactions))
        elif element  == "pont3":
            CollisionSprites(coords, self.pont3, element, (self.allSprites, self.collisionSprites, self.interactions))
    
    def AddBoat(self, element : str, coords : tuple) -> None:
        """Méthode placement et ajout de pont sur la map pygame
        Input : element : str, coords : tuple
        Output : None"""

        if element  == "Boat":
            CollisionSprites(coords, self.boat, element, (self.allSprites, self.collisionSprites, self.interactions))
    
    def AddCerclePortal(self, element, coords):
        CollisionSprites(coords,self.CerclePortal, element, (self.collisionSprites, self.interactions, self.allSprites))


    def Update(self) -> list:
        """Méthode de mise à jour (utilisation unique) + retour de map.
        Input : None, Output : list"""

        # Appel méthodes créations map + sprites
        if NIVEAU["Map"] == "NiveauPlaineRiviere":
            self.LoadImages()
            self.Setup()
            if self.ERROR_RELANCER:
                return None, None, self.ERROR_RELANCER
            self.SetupSpawn()
            self.SetupPNJ()
            self.SetupExit()

        elif NIVEAU["Map"] == "NiveauMedievale":
            self.LoadImages()
            self.Setup()
            if self.ERROR_RELANCER:
                return None, None, self.ERROR_RELANCER
            self.SetupPNJ()

        elif NIVEAU["Map"] == "NiveauBaseFuturiste":
            self.LoadImages()
            self.Setup()
            if self.ERROR_RELANCER:
                return None, None, self.ERROR_RELANCER
            self.SetupPNJ()
        
        # retour des infos de map
        return self.map, self.mapBase, self.ERROR_RELANCER
    
