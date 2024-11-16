from settings import *
from creationMap import *
from sprites import *
from player import *
from groups import *



class LoadMapPlaineRiviere(): # nv 0
    def __init__(self, niveau, allSprites, collisionSprites) -> None:
        self.niveau = niveau
        self.allSprites = allSprites
        self.collisionSprites = collisionSprites

        self.Update()


    def LoadImages(self):
        self.grass = pygame.image.load(join("Images", "Sol", "Grass", "Grass.png")).convert_alpha()
        self.flowers = pygame.image.load(join("Images", "Sol", "Flower", "Flower.png")).convert_alpha()
        self.tree = pygame.image.load(join("Images", "Obstacle", "Arbre.png")).convert_alpha()
        self.tree2 = pygame.image.load(join("Images", "Obstacle", "Arbre2.png")).convert_alpha()
        self.rock = pygame.image.load(join("Images", "Sol","Rock", "Rock.png")).convert_alpha()
        self.mud = pygame.image.load(join("Images", "Sol","Mud", "Mud.png")).convert_alpha()
        self.montainWE = pygame.image.load(join("Images", "Border","Mountain", "MountainStraighW-Ex128.png")).convert_alpha()
        self.montainWE1 = pygame.image.load(join("Images", "Border","Mountain", "MountainStraighW-Ealt1x128.png")).convert_alpha()
     

    def Setup(self):
        self.map, self.mapBase = NiveauPlaineRiviere(LONGUEUR, LARGEUR, 650,200,300).Update()

        for ordonnees in range(len(self.mapBase)):
            for abscisses in range(len(self.mapBase[ordonnees])):
                pos = (abscisses * CASEMAP, ordonnees * CASEMAP)  # Coordonnées de la case sur la carte
                if self.map[ordonnees][abscisses] == "O":
                    if randint(0,3) > 2:
                        CollisionSprites(pos, self.tree2, (self.allSprites, self.collisionSprites))
                    else:
                        CollisionSprites(pos, self.tree, (self.allSprites, self.collisionSprites))

                elif self.mapBase[ordonnees][abscisses] == "#":   # pos rivière à revoire
                    stateFormat = ""
                    if  ordonnees not in [0, LARGEUR-1] and abscisses not in [0,149]:
                        if self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                            stateFormat = "RiverAngularN-Ex128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees+1][abscisses] =="#":
                            stateFormat = "RiverAngularE-Sx128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                            stateFormat = "RiverAngularN-Wx128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees+1][abscisses] =="#":
                            stateFormat = "RiverAngularW-Sx128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees][abscisses-1] =="#":
                            stateFormat = "RiverStraightW-Ex128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif self.mapBase[ordonnees+1][abscisses] =="#" and self.mapBase[ordonnees-1][abscisses] =="#": 
                            stateFormat = "RiverStraightN-Sx128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                    else:
                        if ordonnees in [0, LARGEUR-1]: 
                            stateFormat = "RiverMontainConflictx128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif abscisses ==0:
                            if self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                                stateFormat = "RiverAngularN-Ex128"
                                River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                            elif self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees+1][abscisses] =="#":
                                stateFormat = "RiverAngularE-Sx128"
                                River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                            elif self.mapBase[ordonnees+1][abscisses] =="#" and self.mapBase[ordonnees-1][abscisses] =="#": 
                                stateFormat = "RiverStraightN-Sx128"
                                River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif abscisses == LARGEUR-1:
                            if self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                                stateFormat = "RiverAngularN-Wx128"
                                River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                            elif self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees+1][abscisses] =="#":
                                stateFormat = "RiverAngularW-Sx128"
                                River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                            elif self.mapBase[ordonnees+1][abscisses] =="#" and self.mapBase[ordonnees-1][abscisses] =="#": 
                                stateFormat = "RiverStraightN-Sx128"
                                River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                
                elif self.mapBase[ordonnees][abscisses] == "B":
                    if (ordonnees == 0 or ordonnees == (LARGEUR-1) ):
                        if choice([True, False]):
                            CollisionSprites(pos, self.montainWE, (self.allSprites, self.collisionSprites))
                        else:
                            CollisionSprites(pos, self.montainWE1, (self.allSprites, self.collisionSprites))


                if self.mapBase[ordonnees][abscisses] == "F":
                    Sprites(pos, self.flowers, self.allSprites)
                elif self.mapBase[ordonnees][abscisses] == "M":
                    Sprites(pos, self.mud, self.allSprites) 
                elif self.mapBase[ordonnees][abscisses] == "R":
                    Sprites(pos, self.rock, self.allSprites) 
                else:
                    Sprites(pos, self.grass, self.allSprites) 


    def Update(self):
        self.LoadImages()
        self.Setup()
