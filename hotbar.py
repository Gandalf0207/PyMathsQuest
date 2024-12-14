from settings import *


class MiniMap:

    def __init__(self, mapBase, mapData, screen):
        self.mapBase = mapBase
        self.mapData = mapData
        self.MiniMapSurface = screen
        self.static_surface = pygame.Surface((LONGUEUR * CELL_SIZE, LARGEUR * CELL_SIZE))
        self.player_position = None
        self.ratioImage = CELL_SIZE / CASEMAP / 2

        self.LoadImagesMiniMap()
        self.GenerateStaticMiniMap()

    def LoadImagesMiniMap(self):
        # Chargement des images pour les différents types de terrain
        self.carre1 = pygame.image.load(join("Images", "MiniMap", "Carre1.png")).convert_alpha()
        self.carre2 = pygame.image.load(join("Images", "MiniMap", "Carre2.png")).convert_alpha()
        self.carre3 = pygame.image.load(join("Images", "MiniMap", "Carre3.png")).convert_alpha()
        self.carre4 = pygame.image.load(join("Images", "MiniMap", "Carre4.png")).convert_alpha()
        self.carre5 = pygame.image.load(join("Images", "MiniMap", "Carre5.png")).convert_alpha()
        self.carre6 = pygame.image.load(join("Images", "MiniMap", "Carre6.png")).convert_alpha()
        self.carre7 = pygame.image.load(join("Images", "MiniMap", "Carre8.png")).convert_alpha()

    def GenerateStaticMiniMap(self):
        """
        Génère une fois pour toutes la minimap statique avec le terrain et les objets.
        """
        listpnj = []
        for y, row in enumerate(self.mapBase):
            for x, cell in enumerate(row):
                pos = (x * CELL_SIZE, y * CELL_SIZE)  # Coordonnées des cellules
                if self.mapData[y][x] == "P":
                    listpnj.append(pos)
                elif cell == "#":
                    self.static_surface.blit(self.carre3, pos)
                elif cell == "B":
                    self.static_surface.blit(self.carre7, pos)
                else:
                    self.static_surface.blit(self.carre1, pos)
        
        for pos in listpnj:
            self.static_surface.blit(self.carre6,pos)

    def Update(self, player_pos):
        """
        Met à jour uniquement le joueur sur la minimap.
        """
        # Copier la surface statique dans la surface d'affichage
        self.MiniMapSurface.blit(self.static_surface, (0, 0))

        # Dessiner le joueur (en rouge par exemple)
        player_x, player_y = player_pos
        player_rect = pygame.Rect(
            player_x * CELL_SIZE * self.ratioImage, player_y * CELL_SIZE * self.ratioImage, CELL_SIZE*2, CELL_SIZE*2
        )
        pygame.draw.rect(self.MiniMapSurface, (255, 21, 4), player_rect)


class SettingsAll:
    def __init__(self):
        pass

    def loadImage(self):
        pass

    def Update(self):
        pass