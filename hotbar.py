from settings import *
from interface import *


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
        self.MiniMapSurface.blit(self.static_surface, (0,0))

        # Dessiner le joueur (en rouge par exemple)
        player_x, player_y = player_pos
        player_rect = pygame.Rect(
            player_x * CELL_SIZE * self.ratioImage, player_y * CELL_SIZE * self.ratioImage, CELL_SIZE*2, CELL_SIZE*2
        )
        pygame.draw.rect(self.MiniMapSurface, (255, 21, 4), player_rect)


class SettingsAll:
    def __init__(self, screen, INTERFACE_OPEN):
        self.allSettingsSurface = screen
        self.INTERFACE_OPEN = INTERFACE_OPEN    
        self.loadImage()
        self.ButtonSize()
        self.interfaceElement = None
        self.InterfaceOpen = False

    def ButtonSize(self):
        # Dimensions des boutons (100x100) et positionnement précis
        self.surfaceButtonWheel = pygame.Surface((100, 100))
        self.surfaceButtonSound = pygame.Surface((100, 100))
        self.surfaceButtonBundle = pygame.Surface((100, 100))
        self.surfaceButtonBook = pygame.Surface((100, 100))

        # Positions des boutons, espacés de 10 pixels, centrés verticalement
        self.ButtonRectWheel =pygame.Rect(0, 25, 100, 100) 
        self.ButtonRectSound = pygame.Rect(106, 25, 100, 100)
        self.ButtonRectBundle = pygame.Rect(212, 25, 100, 100)
        self.ButtonRectBook = pygame.Rect(318, 25, 100, 100)
        


    def loadImage(self):
        # Load images for the buttons
        self.wheel = pygame.image.load(join("Images", "HotBar", "AllSettings", "Wheel.png")).convert_alpha()
        self.sound = pygame.image.load(join("Images", "HotBar", "AllSettings", "Sound.png")).convert_alpha()
        self.bundle = pygame.image.load(join("Images", "HotBar", "AllSettings", "Bundle.png")).convert_alpha()
        self.book = pygame.image.load(join("Images", "HotBar", "AllSettings", "Book.png")).convert_alpha()

    def OpenInterfaceElementClic(self, event, INTERFACE_OPEN):

        self.INTERFACE_OPEN = INTERFACE_OPEN
        # Obtenez les coordonnées globales de l'événement
        global_pos = event.pos  # Coordonnées relatives à la fenêtre

        # Déterminez où la surface `allSettings_surface` est affichée
        surface_rect = self.allSettingsSurface.get_rect(topleft=COORS_BOX_ALL_SETTINGS)  # `x, y` est la position de la surface dans la fenêtre.

        # Convertissez les coordonnées globales en coordonnées locales
        local_pos = (global_pos[0] - surface_rect.x, global_pos[1] - surface_rect.y)

        # Vérifiez si le clic est dans la surface
        if not surface_rect.collidepoint(global_pos):
            return

        # Continuez avec les coordonnées locales pour détecter les boutons
        if self.ButtonRectWheel.collidepoint(local_pos) or event.key == pygame.K_p :
            self.GestionInterfaceSettings()

        elif self.ButtonRectSound.collidepoint(local_pos) or event.key == pygame.K_v : 
            self.GestionInterfaceSound()

        elif self.ButtonRectBundle.collidepoint(local_pos) or event.key == pygame.K_i:
            self.GestionInterfaceBundle()

        elif self.ButtonRectBook.collidepoint(local_pos) or event.key == pygame.K_b : 
            self.GestionInterfaceBook()

        return self.INTERFACE_OPEN
    
    def OpenInterfaceElementClavier(self, event, INTERFACE_OPEN):
        self.INTERFACE_OPEN = INTERFACE_OPEN

        # Continuez avec les coordonnées locales pour détecter les boutons
        if event.key == pygame.K_p :
            self.GestionInterfaceSettings()

        elif event.key == pygame.K_v : 
            self.GestionInterfaceSound()

        elif event.key == pygame.K_i:
            self.GestionInterfaceBundle()

        elif event.key == pygame.K_b : 
            self.GestionInterfaceBook()

        return self.INTERFACE_OPEN

    def GestionInterfaceSettings(self):
        if not self.INTERFACE_OPEN and not self.InterfaceOpen:
            self.InterfaceOpen = True
            self.INTERFACE_OPEN = True
            self.interfaceElement = SettingsInterface(self)
            print("Wheel button clicked!")
        
        elif self.InterfaceOpen:
            self.InterfaceOpen = False
            self.INTERFACE_OPEN = False


    def GestionInterfaceSound(self):
        if not self.INTERFACE_OPEN and not self.InterfaceOpen:
            self.InterfaceOpen = True
            self.INTERFACE_OPEN = True
            self.interfaceElement = SoudInterface(self)
            print("Sound button clicked!")
        
        elif self.InterfaceOpen:
            self.InterfaceOpen = False
            self.INTERFACE_OPEN = False

    def GestionInterfaceBundle(self):
        if not self.INTERFACE_OPEN and not self.InterfaceOpen:
            self.InterfaceOpen = True
            self.INTERFACE_OPEN = True
            self.interfaceElement = BundleInterface(self)
            print("Bundle button clicked!")
        
        elif self.InterfaceOpen:
            self.InterfaceOpen = False
            self.INTERFACE_OPEN = False

    def GestionInterfaceBook(self):
        if not self.INTERFACE_OPEN and not self.InterfaceOpen:
            self.InterfaceOpen = True
            self.INTERFACE_OPEN = True
            self.interfaceElement = BookInterface(self)
            print("Book button clicked!")
        
        elif self.InterfaceOpen:
            self.InterfaceOpen = False
            self.INTERFACE_OPEN = False






    def Update(self):
        self.allSettingsSurface.fill((255,255,255))
        
        # Fill button surfaces with a background color
        self.surfaceButtonBook.fill((200, 200, 200))  # Light gray
        self.surfaceButtonSound.fill((200, 200, 200))
        self.surfaceButtonBundle.fill((200, 200, 200))
        self.surfaceButtonWheel.fill((200, 200, 200))

        # Draw images on button surfaces
        self.surfaceButtonBook.blit(self.book, (0, 0))
        self.surfaceButtonSound.blit(self.sound, (0, 0))
        self.surfaceButtonBundle.blit(self.bundle, (0, 0))
        self.surfaceButtonWheel.blit(self.wheel, (0, 0))

        # Draw button surfaces on the main settings surface
        self.allSettingsSurface.blit(self.surfaceButtonBook, (self.ButtonRectBook.x, self.ButtonRectBook.y))
        self.allSettingsSurface.blit(self.surfaceButtonSound, (self.ButtonRectSound.x, self.ButtonRectSound.y))
        self.allSettingsSurface.blit(self.surfaceButtonBundle, (self.ButtonRectBundle.x,  self.ButtonRectBundle.y))
        self.allSettingsSurface.blit(self.surfaceButtonWheel, (self.ButtonRectWheel.x, self.ButtonRectWheel.y))


        if self.InterfaceOpen:
            self.interfaceElement.Update()
        
        

