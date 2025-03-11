from settings import *

from SourcesFichiers.Map.MapNiveau.plaineRiviere import *
from SourcesFichiers.Map.MapNiveau.medievale import *
from SourcesFichiers.Map.MapNiveau.baseFuturiste import *
from SourcesFichiers.Map.MapNiveau.mordor import *

from SourcesFichiers.Elements.sprites import *
from SourcesFichiers.Personnages.player import *
from SourcesFichiers.Elements.groups import *
from SourcesFichiers.Personnages.pnj import *


class LoadMapGestion():
    def __init__(self, allSprites : any, collisionSprites : any, allpnj : any, interactions) -> None:
        """Méthode initialisation chargement de la map du niveau plaine et rivière. 
        Input : niveau : int, allSprites / collisionsSprites / allpnj : element pygame; Output : None"""
    
        # class des éléments pygame
        self.allPNJ = allpnj
        self.allSprites = allSprites
        self.collisionSprites = collisionSprites
        self.interactions = interactions
        self.ERROR_RELANCER = False


    def LoadImagesNiveauPlaineRiviere(self):
        self.sol = pygame.image.load(join("Image", "Sol", "Grass.png")).convert_alpha()
        self.sol1 = pygame.image.load(join("Image", "Sol", "Flower.png")).convert_alpha()
        self.sol2 = pygame.image.load(join("Image", "Sol", "Rock.png")).convert_alpha()
        self.sol3 = pygame.image.load(join("Image", "Sol", "Mud.png")).convert_alpha()

        self.obstacle = pygame.image.load(join("Image", "Obstacle", "Arbre.png")).convert_alpha()
        self.obstacle1 = pygame.image.load(join("Image", "Obstacle", "Arbre2.png")).convert_alpha()
        self.obstacle2 = pygame.image.load(join("Image", "Obstacle", "Souche.png")).convert_alpha()
        self.obstacle3 = pygame.image.load(join("Image", "Obstacle", "Souche2.png")).convert_alpha()
        self.HugeRock = pygame.image.load(join("Image", "Obstacle", "HugeRock.png")).convert_alpha()

        self.montainWE = pygame.image.load(join("Image", "Mur","Mountain", "MountainStraighW-Ex128.png")).convert_alpha()
        self.montainWE1 = pygame.image.load(join("Image", "Mur","Mountain", "MountainStraighW-Ealt1x128.png")).convert_alpha()

        self.pont1 = pygame.image.load(join("Image", "Structure", "Pont", "Pont1.png")).convert_alpha()
        self.pont2 = pygame.image.load(join("Image", "Structure", "Pont", "Pont2.png")).convert_alpha()

        self.campFire = pygame.image.load(join("Image", "Obstacle", "campFire.png")).convert_alpha()

    def LoadImagesNiveauMedievale(self):
        self.sol = pygame.image.load(join("Images", "Sol", "Grass", "Grass.png")).convert_alpha()
        self.sol1 = pygame.image.load(join("Images", "Sol", "Flower", "Flower.png")).convert_alpha()
        self.sol2 = pygame.image.load(join("Images", "Sol","Rock", "Rock.png")).convert_alpha()
        self.sol3 = pygame.image.load(join("Images", "Sol","Mud", "Mud.png")).convert_alpha()
        self.obstacle = pygame.image.load(join("Images", "Obstacle", "Arbre.png")).convert_alpha()
        self.obstacle1 = pygame.image.load(join("Images", "Obstacle", "Arbre2.png")).convert_alpha()
        self.obstacle2 = pygame.image.load(join("Images", "Obstacle", "Souche.png")).convert_alpha()
        self.obstacle3 = pygame.image.load(join("Images", "Obstacle", "Souche2.png")).convert_alpha()
        self.HugeRock = pygame.image.load(join("Images", "Obstacle", "HugeRock.png")).convert_alpha()
        self.montainWE = pygame.image.load(join("Images", "Border","Mountain", "MountainStraighW-Ex128.png")).convert_alpha()
        self.montainWE1 = pygame.image.load(join("Images", "Border","Mountain", "MountainStraighW-Ealt1x128.png")).convert_alpha()
        self.pont1 = pygame.image.load(join("Images", "Pont", "BridgeTreeW-Ex128.png")).convert_alpha()
        self.pont2 = pygame.image.load(join("Images", "Pont", "BridgePlanksW-Ex128.png")).convert_alpha()

        # path
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
        self.house1 = pygame.image.load(join("Images", "Obstacle", "Structures", "House.png")).convert_alpha()
        self.house2 = pygame.image.load(join("Images", "Obstacle", "Structures", "House.png")).convert_alpha()
        self.house3 = pygame.image.load(join("Images", "Obstacle", "Structures", "House.png")).convert_alpha()

        self.chateau = pygame.image.load(join("Images", "Obstacle", "Structures", "Chateau.png")).convert_alpha()

        self.MurWE = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesWE.png" )).convert_alpha()
        self.MurNS = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesNS.png" )).convert_alpha()
        self.MurMountain = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesMountain.png" )).convert_alpha()
        self.MurAngle = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesAngle.png" )).convert_alpha()

        self.well = pygame.image.load(join("Images", "Obstacle", "Structures", "Puits.png")).convert_alpha()
        self.tableCraft = pygame.image.load(join("Images", "Obstacle", "TableCraft.png")).convert_alpha()
        self.boat = pygame.image.load(join("Images", "Obstacle", "Boat.png")).convert_alpha()
        self.Door = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
        self.Door2 =  pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()

    def LoadImagesDemiNiveauChateau(self):
        self.Sol = pygame.image.load(join("Images", "Chateau", "SolChateau.png")).convert_alpha()
        self.Socle = pygame.image.load(join("Images", "Chateau", "Socle.png")).convert_alpha()
        self.MursAnglularSW = pygame.image.load(join("Images", "Chateau", "MursChateau.png")).convert_alpha()
        self.Pilier = pygame.image.load(join("Images", "Chateau", "Piliers.png")).convert_alpha()
        self.Chandelier = pygame.image.load(join("Images", "Chateau", "Chandelier.png")).convert_alpha()
        self.DoorChateau = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
        self.Portal = pygame.image.load(join("Images", "Chateau", "Portal.png")).convert_alpha()
        self.CerclePortal = pygame.image.load(join("Images", "Chateau", "SolChateau.png")).convert_alpha()

    def LoadImagesNiveauBaseFuturiste(self):
        self.sol = pygame.image.load(join("Images", "Sol", "Dirt", "Dirtx128.png")).convert_alpha()
        self.sol2 = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Floorx128.png")).convert_alpha()
        self.sol3 = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
        self.vent = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Ventx128.png")).convert_alpha()
        self.MurAngularNE = pygame.image.load(join("Images", "Sol", "Path", "PathN-Ex128.png")).convert_alpha()
        self.MurAngularNW = pygame.image.load(join("Images", "Sol", "Path", "PathN-Wx128.png")).convert_alpha()
        self.MurAngularSE = pygame.image.load(join("Images", "Sol", "Path", "PathE-Sx128.png")).convert_alpha()
        self.MurAngularSW = pygame.image.load(join("Images", "Sol", "Path", "PathW-Sx128.png")).convert_alpha()
        
        self.MurNSGauche = pygame.image.load(join("Images", "Sol", "Path", "PathN-S.png")).convert_alpha()
        self.MurWEHaut = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "WallEWx128.png")).convert_alpha()
        self.MurNSDroite = pygame.image.load(join("Images", "Sol", "Path", "PathN-S.png")).convert_alpha()
        self.MurWEBas = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Wallbackx128.png")).convert_alpha()
        
        self.centraleNuc = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Reacteur.png")).convert_alpha()
        self.cafet = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Cafet.png")).convert_alpha()
        self.essence = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Essence.png")).convert_alpha()
        self.salleLancement = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Lancement.png")).convert_alpha()

        self.doorFuturiste = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
    
    def LoadImagesDemiNiveauVaisseau(self):
        self.sol = pygame.image.load(join("Images", "Obstacle", "Structures", "BaseFuturiste", "Floorx128.png")).convert_alpha()

        self.MurAngularNE = pygame.image.load(join("Images", "Sol", "Path", "PathN-Ex128.png")).convert_alpha()
        self.MurAngularNW = pygame.image.load(join("Images", "Sol", "Path", "PathN-Wx128.png")).convert_alpha()
        self.MurAngularSE = pygame.image.load(join("Images", "Sol", "Path", "PathE-Sx128.png")).convert_alpha()
        self.MurAngularSW = pygame.image.load(join("Images", "Sol", "Path", "PathW-Sx128.png")).convert_alpha()

        self.tableauDeBord = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
        self.siege = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
        self.vitre = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()

        self.doorFuturisteDemiNiveau = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()

    def LoadImagesNiveauMordor(self):
        self.sol = pygame.image.load(join("Images", "Sol", "Grass", "Grass.png")).convert_alpha()
        self.sol2 = pygame.image.load(join("Images", "Sol","Mud", "Mud.png")).convert_alpha() # cratere
        self.sol3 = pygame.image.load(join("Images", "Sol","Mud", "Mud.png")).convert_alpha() # cratere

        self.montainWE = pygame.image.load(join("Images", "Border","Mountain", "MountainStraighW-Ex128.png")).convert_alpha()
        self.montainWE1 = pygame.image.load(join("Images", "Border","Mountain", "MountainStraighW-Ealt1x128.png")).convert_alpha()

        self.MurWE = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesWE.png" )).convert_alpha()
        self.MurNS = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesNS.png" )).convert_alpha()
        self.MurMountain = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesMountain.png" )).convert_alpha()
        self.MurAngle = pygame.image.load(join("Images", "Obstacle",  "Structures", "Chateau", "MuraillesAngle.png" )).convert_alpha()  

        self.Door = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
        self.Door2 = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
        self.Door3 =pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha() 
        
        self.obstacle = pygame.image.load(join("Images", "Obstacle", "HugeRock.png")).convert_alpha()
        self.doorFuturiste = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()

        self.pont5 = pygame.image.load(join("Images", "Pont","BridgePlanksN-S-x128.png" )).convert_alpha()

        self.pot  = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
        self.parchemin = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()
        self.volcan = pygame.image.load(join("Images", "Obstacle", "Structures", "Volcan.png")).convert_alpha()

        self.vaisseauCrash = pygame.image.load(join("Images", "Obstacle", "Structures", "Volcan.png")).convert_alpha()
        self.bareaux = pygame.image.load(join("Images", "Chateau", "Door.png")).convert_alpha()

    def LoadImagesDemiNiveauVolcan(self):
        pass


    def LoadImagesGestion(self) -> None:
        gc.collect() # clear img

        if not INFOS["DemiNiveau"]:
            if NIVEAU["Map"] == "NiveauPlaineRiviere":
                self.LoadImagesNiveauPlaineRiviere()
            elif NIVEAU["Map"] == "NiveauMedievale":
                self.LoadImagesNiveauMedievale()
            elif NIVEAU["Map"] == "NiveauBaseFuturiste":
                self.LoadImagesNiveauBaseFuturiste()
            elif NIVEAU["Map"] == "NiveauMordor":
                self.LoadImagesNiveauMordor()
        else:
            if NIVEAU["Map"] == "NiveauMedievale":
                self.LoadImagesDemiNiveauChateau()
            elif NIVEAU["Map"] == "NiveauBaseFuturiste":
                self.LoadImagesDemiNiveauVaisseau()
            elif NIVEAU["Map"] == "NiveauMordor":
                self.LoadImagesDemiNiveauVolcan()

    def Setup(self):

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
                self.map, self.mapBase, self.ERROR_RELANCER = NiveauBaseFuturisteVaisseau().Update()
        if NIVEAU["Map"] == "NiveauMordor":
            if not INFOS["DemiNiveau"]:
                self.map, self.mapBase, self.ERROR_RELANCER = NiveauMordor().Update()
            else:
                pass       
        
        # si erreur : return
        if self.ERROR_RELANCER:
            return None
        
        # parcours et création de chaque sprites
        for ordonnees in range(len(self.mapBase)):
            for abscisses in range(len(self.mapBase[ordonnees])):
                pos = (abscisses * CASEMAP, ordonnees * CASEMAP)  # Coordonnées de la case sur la carte
                
                # sol
                if self.map[ordonnees][abscisses] ==".":
                    Sprites(pos, self.sol, "Sol", self.allSprites)
                elif self.mapBase[ordonnees][abscisses] == 2:
                    if randint(1, 10) < 7:
                        Sprites(pos, self.sol2, "Sol2", self.allSprites)
                    else:
                        Sprites(pos, self.sol3, "Sol3", self.allSprites)
                elif self.mapBase[ordonnees][abscisses] == 1:
                    Sprites(pos, self.sol1, "Sol3", self.allSprites)
                elif self.mapBase[ordonnees][abscisses] == "-":
                        Sprites(pos, self.sol, "Sol", self.allSprites)
                
                # riviere
                if self.map[ordonnees][abscisses] == "#":

                    # Vérification des bords pour éviter les erreurs d'index
                    can_go_up = ordonnees > 0
                    can_go_down = ordonnees < LARGEUR - 1
                    can_go_left = abscisses > 0
                    can_go_right = abscisses < 149

                    def checkBuildUp(can_go_up, can_go_left, can_go_right):
                        if can_go_up:
                            if self.mapBase[ordonnees -1][abscisses] == "#":
                                return True
                            if self.mapBase[ordonnees -1][abscisses] == "W":
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
                            if self.mapBase[ordonnees +1][abscisses] == "W":
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


                    riverPath = ""
                    # conflif montain
                    if mountainConflict:
                        riverPath = join("Image","Obstacle","Riviere","RiverMontainConflictx128")
                        AnimatedCollisionSprites(pos, riverPath, "River", (self.allSprites, self.collisionSprites), layer=1)

                    # Tshape
                    elif can_build_right and can_build_left and can_build_up:
                        riverPath = join("Image","Obstacle","Riviere","RiverTWN-Ex128")
                        AnimatedCollisionSprites(pos, riverPath, "River", (self.allSprites, self.collisionSprites), layer=1)   
                    elif can_build_right and can_build_left and can_build_down:
                        riverPath = join("Image","Obstacle","Riviere","RiverTW-SEx128")
                        AnimatedCollisionSprites(pos, riverPath, "River", (self.allSprites, self.collisionSprites), layer=1)
                    elif can_build_down and can_build_up and can_build_left:
                        riverPath = join("Image","Obstacle","Riviere","RiverTWN-Sx128")
                        AnimatedCollisionSprites(pos, riverPath, "River", (self.allSprites, self.collisionSprites), layer=1)
                    elif can_build_down and can_build_up and can_build_right:
                        riverPath = join("Image","Obstacle","Riviere","RiverTN-SEx128")
                        AnimatedCollisionSprites(pos, riverPath, "River", (self.allSprites, self.collisionSprites), layer=1)

                    # angular
                    elif can_build_right and can_build_down:
                        riverPath = join("Image","Obstacle","Riviere","RiverAngularE-Sx128")
                        AnimatedCollisionSprites(pos, riverPath, "River", (self.allSprites, self.collisionSprites), layer=1)
                    elif can_build_right and can_build_up:
                        riverPath = join("Image","Obstacle","Riviere","RiverAngularN-Ex128")
                        AnimatedCollisionSprites(pos, riverPath, "River", (self.allSprites, self.collisionSprites), layer=1)
                    elif can_build_left and can_build_down:
                        riverPath = join("Image","Obstacle","Riviere","RiverAngularW-Sx128")
                        AnimatedCollisionSprites(pos, riverPath, "River", (self.allSprites, self.collisionSprites), layer=1)
                    elif can_build_left and can_build_up:
                        riverPath = join("Image","Obstacle","Riviere","RiverAngularN-Wx128")
                        AnimatedCollisionSprites(pos, riverPath, "River", (self.allSprites, self.collisionSprites), layer=1)

                    # line
                    elif can_build_up or can_build_down:
                        riverPath = join("Image","Obstacle","Riviere","RiverStraightN-Sx128")
                        AnimatedCollisionSprites(pos, riverPath, "River", (self.allSprites, self.collisionSprites), layer=1)
                    elif can_build_right or can_build_left:
                        riverPath = join("Image","Obstacle","Riviere","RiverStraightW-Ex128")
                        AnimatedCollisionSprites(pos, riverPath, "River", (self.allSprites, self.collisionSprites), layer=1)

                # Bordure Montagne
                elif self.map[ordonnees][abscisses] == "B":
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
                
                # murs structure
                elif self.map[ordonnees][abscisses] == "W":
                    
                    def case_valide(y, x):
                        """ Vérifie si une case est valide dans la carte."""
                        return 0 <= y < len(self.map) and 0 <= x < len(self.map[0])
                    
                    # Vérification des voisins
                    right = case_valide(ordonnees, abscisses + 1) and self.map[ordonnees][abscisses + 1] in ["C", "&", "V", "c"]
                    left = case_valide(ordonnees, abscisses - 1) and self.map[ordonnees][abscisses - 1] in ["C", "&", "V", "c"]
                    up = case_valide(ordonnees - 1, abscisses) and self.map[ordonnees - 1][abscisses] == "C"
                    down = case_valide(ordonnees + 1, abscisses) and self.map[ordonnees + 1][abscisses] == "C"
                    
                    # === 3. Virages (angles) ===
                    if up and right:
                        CollisionSprites(pos, self.MurAngularNE, "Wall", (self.allSprites, self.collisionSprites))
                    elif up and left:
                        CollisionSprites(pos, self.MurAngularNW, "Wall", (self.allSprites, self.collisionSprites))

                    # Passage avec de l'eau
                    elif right and left and case_valide(ordonnees - 1, abscisses) and self.map[ordonnees - 1][abscisses] == "#" \
                        and case_valide(ordonnees + 1, abscisses) and self.map[ordonnees + 1][abscisses] == "#":
                        pathRiver = join("Image","Obstacle","Riviere","CastleWallRiverx128")
                        AnimatedCollisionSprites(pos,pathRiver, "River", (self.allSprites, self.collisionSprites),layer=1)
                        
                    elif down and right:
                        CollisionSprites(pos, self.MurAngularSE, "Wall", (self.allSprites, self.collisionSprites))
                    elif down and left:
                        CollisionSprites(pos, self.MurAngularSW, "Wall", (self.allSprites, self.collisionSprites))

                    # === 4. Lignes droites ===
                    elif left and right:
                        if self.mapBase[ordonnees-1][abscisses] == "." and self.mapBase[ordonnees+1][abscisses] == ".":
                            CollisionSprites(pos, self.MurWEHaut, "Wall", (self.allSprites, self.collisionSprites))
                        elif self.mapBase[ordonnees+1][abscisses] == ".":
                            CollisionSprites(pos, self.MurWEHaut, "Wall", (self.allSprites, self.collisionSprites))
                        elif self.mapBase[ordonnees-1][abscisses] == ".":
                            # add pre sol car collision mur bas sprite différents
                            Sprites(pos, self.sol2,"Sol", self.allSprites)
                            CollisionSprites(pos, self.MurWEBas, "Wall2", (self.allSprites, self.collisionSprites))

                    elif up and down:
                        if self.mapBase[ordonnees][abscisses-1] == ".":
                            CollisionSprites(pos, self.MurNSDroite, "Wall", (self.allSprites, self.collisionSprites))
                        else:
                            CollisionSprites(pos, self.MurNSGauche, "Wall", (self.allSprites, self.collisionSprites))

                    else:
                        CollisionSprites(pos, self.MurWEHaut, "Wall", (self.allSprites, self.collisionSprites))

                elif self.map[ordonnees][abscisses] == "H":
                    choix = randint(1, 3)
                    if choix == 1:
                        CollisionSprites(pos, self.house1, "House", (self.allSprites, self.collisionSprites))
                    elif choix == 2:
                        CollisionSprites(pos, self.house2, "House", (self.allSprites, self.collisionSprites))
                    else:
                        CollisionSprites(pos, self.house3, "House", (self.allSprites, self.collisionSprites))

    def SetupPNJ(self):
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
            if coordsPNJ[3] == 5 :
                PNJOBJ(pos, "PNJ5", (self.allPNJ, self.allSprites, self.collisionSprites))
            if coordsPNJ[3] == 6: # pnj 5 deplacement nv 3 | demi niveau
                PNJOBJ(pos, "PNJ6", (self.allPNJ, self.allSprites, self.collisionSprites))
        
    def SetupObj(self):
        pass


    def Update(self):
        self.LoadImagesGestion()
        self.Setup()
        if self.ERROR_RELANCER:
            return None, None, self.ERROR_RELANCER
        self.SetupPNJ()
        self.SetupObj()

        # retour des infos de map
        return self.map, self.mapBase, self.ERROR_RELANCER