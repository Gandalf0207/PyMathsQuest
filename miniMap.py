from settings import *  # Assurez-vous que les constantes sont bien définies dans settings.py
from sprites import *



class MiniMap:
    def __init__(self, mapBase, map, screen, spritesMiniMap):
        self.mapBase = mapBase
        self.map = map
        self.MiniMapSurface = screen
        self.allSpritesMiniMap = spritesMiniMap
        self.LoadImagesMiniMap()


    def LoadImagesMiniMap(self):
        self.carre1 = pygame.image.load(join("Images", "MiniMap", "Carre1.png")).convert_alpha()
        self.carre2 = pygame.image.load(join("Images", "MiniMap", "Carre2.png")).convert_alpha()
        self.carre3 = pygame.image.load(join("Images", "MiniMap", "Carre3.png")).convert_alpha()
        self.carre4 = pygame.image.load(join("Images", "MiniMap", "Carre4.png")).convert_alpha()
        self.carre5 = pygame.image.load(join("Images", "MiniMap", "Carre5.png")).convert_alpha()
        self.carre6 = pygame.image.load(join("Images", "MiniMap", "Carre6.png")).convert_alpha()
        self.carre7 = pygame.image.load(join("Images", "MiniMap", "Carre7.png")).convert_alpha()
        self.carre8 = pygame.image.load(join("Images", "MiniMap", "Carre8.png")).convert_alpha()
        self.carre9 = pygame.image.load(join("Images", "MiniMap", "Carre9.png")).convert_alpha()
     

    def MakeMiniMap(self):
        """
        Génère toute la minimap en réduisant la carte complète.
        """

        for ordonnees in range(len(self.mapBase)):
            for abscisses in range(len(self.mapBase[ordonnees])):
                pos = (abscisses * 7, ordonnees * 7)  # Coordonnées de la case sur la carte
                if self.map[ordonnees][abscisses] == "O":
                    Sprites(pos, self.carre1, self.allSpritesMiniMap)

                elif self.mapBase[ordonnees][abscisses] == "#":   # pos rivière à revoire
                    Sprites(pos, self.carre2, self.allSpritesMiniMap)
            
                elif self.mapBase[ordonnees][abscisses] == "B":
                    Sprites(pos, self.carre3, self.allSpritesMiniMap)
                if self.mapBase[ordonnees][abscisses] == "F":
                    Sprites(pos, self.carre4, self.allSpritesMiniMap)
                elif self.mapBase[ordonnees][abscisses] == "M":
                    Sprites(pos, self.carre5, self.allSpritesMiniMap) 
                elif self.mapBase[ordonnees][abscisses] == "R":
                    Sprites(pos, self.carre6, self.allSpritesMiniMap)
                else:
                    Sprites(pos, self.carre7, self.allSpritesMiniMap)
