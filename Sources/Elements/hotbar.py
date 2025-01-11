from settings import *
from Sources.Elements.interface import *


class MiniMap:

    def __init__(self, mapBase : list, mapData : list, screen: any) -> None:
        """Méthode d'initialisation pour la création de la minimap. 
        Input : list *2 = map du niveau, screen = (element pygame); Output : None"""

        # Initialisation 
        self.mapBase = mapBase # sol
        self.mapData = mapData # obstacle
        self.MiniMapSurface = screen

        # Création elements
        self.static_surface = pygame.Surface((LONGUEUR * CELL_SIZE, LARGEUR * CELL_SIZE))
        self.player_position = None
        self.ratioImage = CELL_SIZE / CASEMAP / 2

        self.LoadImagesMiniMap()
        self.GenerateStaticMiniMap() # minimap de base


    def LoadImagesMiniMap(self) -> None:
        """Méthode de chargement des images pour la minimap. Input / Output : None"""

        self.carre1 = pygame.image.load(join("Images", "MiniMap", "Carre1.png")).convert_alpha()
        self.carre3 = pygame.image.load(join("Images", "MiniMap", "Carre3.png")).convert_alpha()
        self.carre6 = pygame.image.load(join("Images", "MiniMap", "Carre6.png")).convert_alpha()
        self.carre7 = pygame.image.load(join("Images", "MiniMap", "Carre8.png")).convert_alpha()


    def GenerateStaticMiniMap(self) -> None:
        """Méthode : Génère une fois pour toute la minimap 
        statique avec le terrain et les objets. Input / Output : None"""

        for y, row in enumerate(self.mapBase):
            for x, cell in enumerate(row):
                pos = (x * CELL_SIZE, y * CELL_SIZE)  # Coordonnées des cellules)
                if cell == "#": # rivière
                    self.static_surface.blit(self.carre3, pos)
                elif cell == "B": # border
                    self.static_surface.blit(self.carre7, pos)
                else: # reste = herbe 
                    self.static_surface.blit(self.carre1, pos)
        

    def Update(self, player_pos: tuple, pnjGroup : any, interactionGroup : any) -> None:
        """Méthode : Met à jour uniquement le joueur sur la minimap. 
        Input : tutple (position du joueur), pnjGroup / interactionGroups : element pygame Output : None """

        # Copier la surface statique dans la surface d'affichage
        self.MiniMapSurface.blit(self.static_surface, (0,0))

        # Dessiner le joueur (en rouge par exemple)
        player_x, player_y = player_pos
        player_rect = pygame.Rect(player_x * CELL_SIZE * self.ratioImage, player_y * CELL_SIZE * self.ratioImage, CELL_SIZE*2, CELL_SIZE*2)
        pygame.draw.rect(self.MiniMapSurface, (255, 21, 4), player_rect)
                
        # placemnt des pnj
        for objectPNJ in pnjGroup:
            pnj_x, pnj_y = objectPNJ.pos[0] * CASEMAP, objectPNJ.pos[1] *CASEMAP
            pnj_rect = pygame.Rect(pnj_x * CELL_SIZE * self.ratioImage, pnj_y * CELL_SIZE * self.ratioImage, CELL_SIZE*2, CELL_SIZE * 2)
            pygame.draw.rect(self.MiniMapSurface, (252, 128, 3), pnj_rect)

        # placemnt des interaction object
        for objectElement in interactionGroup:
            element_x, element_y = objectElement.pos[0], objectElement.pos[1] # coords déja maps
            element_rect = pygame.Rect(element_x * CELL_SIZE * self.ratioImage, element_y * CELL_SIZE * self.ratioImage, CELL_SIZE*2, CELL_SIZE * 2)
            pygame.draw.rect(self.MiniMapSurface, (109, 3, 158), element_rect)


class InfosTips:

    def __init__(self, screen):

        # initialisation
        self.IdeaTipsSurface = screen
        
        # creation element
        self.font = pygame.font.Font(None, 20)
        self.text = None
        self.indexTexte = 0
        self.loadImage()
        self.GetText()
    
    def loadImage(self):
        self.idea = pygame.image.load(join("Images", "HotBar", "LightBulbIcon.png")).convert_alpha()


    def GetText(self):
        """ infoUpdate permet de déterminer si un evenement à eu lieu : ex traverser un pont. 
        Ce bool permet de séparer deux tips qui se passent dans un meme moment"""
        
        if self.text != TEXTE["Elements"]["HotBar"]["IdeaTips"][f"Niveau{INFOS["Niveau"]}"][STATE_HELP_INFOS[0]]:
            self.indexTexte = 0
        
        self.text = TEXTE["Elements"]["HotBar"]["IdeaTips"][f"Niveau{INFOS["Niveau"]}"][STATE_HELP_INFOS[0]]




    def BuildElement(self):
        # image
        self.IdeaTipsSurface.fill("#ffffff")
        self.IdeaTipsSurface.blit(self.idea, (10,27))
        
        # texte
        # bloc gestion texte 
        if self.indexTexte < len(self.text):
            self.indexTexte += 1
        # Mettre à jour le texte affiché
        self.displayed_text = self.text[:self.indexTexte]

        # Fonction simple pour découper le texte
        def wrap_text(text, font, max_width):
            words = text.split(' ')
            lines = []
            current_line = ''

            for word in words:
                test_line = f"{current_line} {word}".strip()
                if font.size(test_line)[0] <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word
            if current_line:
                lines.append(current_line)
            return lines

        max_width = 400
        wrapped_lines = wrap_text(self.displayed_text, self.font, max_width)

        # Affichage des lignes
        y_offset = 30  # Position Y de départ
        line_height = self.font.size("Tg")[1]  # Hauteur d'une ligne
        for i, line in enumerate(wrapped_lines):
            line_surface = self.font.render(line, True, (0,0,0))
            self.IdeaTipsSurface.blit(line_surface, (120, y_offset + i * line_height))
    
    def Update(self):
        self.GetText()
        self.BuildElement()



class SettingsAll:

    def __init__(self, screen : any, INTERFACE_OPEN : bool) -> None:
        """Méthode initialisation de la box d'accès à tout les settings et utilitaires (bundle, settings, sound, book).
        Input : screen = (element pygame), boolean = check interface global """

        # Initialisation
        self.allSettingsSurface = screen
        self.INTERFACE_OPEN = INTERFACE_OPEN

        # Création éléments
        self.InterfaceOpen = False # bool de vérification
        self.interfaceElement = None # object

        # Chargement images + éléments button pygame
        self.loadImage()
        self.ButtonSize()
        

    def ButtonSize(self) -> None:
        """Méthode : Création des spécifications 
        des buttons pygame. Input / Output : None"""

        # Dimensions des boutons (100x100)
        self.surfaceButtonWheel = pygame.Surface((100, 100))
        self.surfaceButtonSound = pygame.Surface((100, 100))
        self.surfaceButtonBundle = pygame.Surface((100, 100))
        self.surfaceButtonBook = pygame.Surface((100, 100))

        # Positions des boutons, espacés de 6 pixels, centrés verticalement
        self.ButtonRectWheel =pygame.Rect(0, 25, 100, 100) 
        self.ButtonRectSound = pygame.Rect(106, 25, 100, 100)
        self.ButtonRectBundle = pygame.Rect(212, 25, 100, 100)
        self.ButtonRectBook = pygame.Rect(318, 25, 100, 100)
        

    def loadImage(self) -> None:
        """Méthode : Chargement des texture des 
        4 button pygame. Input / Output : None"""

        self.wheel = pygame.image.load(join("Images", "HotBar", "AllSettings", "Wheel.png")).convert_alpha()
        self.sound = pygame.image.load(join("Images", "HotBar", "AllSettings", "Sound.png")).convert_alpha()
        self.bundle = pygame.image.load(join("Images", "HotBar", "AllSettings", "Bundle.png")).convert_alpha()
        self.book = pygame.image.load(join("Images", "HotBar", "AllSettings", "Book.png")).convert_alpha()


    def OpenInterfaceElementClic(self, event : any, INTERFACE_OPEN : bool) -> bool:
        """Méthode : Appel des méthode de gestion des interfaces par clic souris.
        Input : event = (element pygame), bool = checl interface global; Output : bool"""

        self.INTERFACE_OPEN = INTERFACE_OPEN

        if not self.INTERFACE_OPEN: # sécurité
            self.openInterface = False 

        # Obtenez les coordonnées globales de l'événement
        global_pos = event.pos  # Coordonnées relatives à la fenêtre

        # Déterminez où la surface `allSettings_surface` est affichée
        surface_rect = self.allSettingsSurface.get_rect(topleft=COORS_BOX_ALL_SETTINGS)  # `x, y` est la position de la surface dans la fenêtre.

        # Convertissez les coordonnées globales en coordonnées locales
        local_pos = (global_pos[0] - surface_rect.x, global_pos[1] - surface_rect.y)

        # Vérifiez si le clic est dans la surface
        if not surface_rect.collidepoint(global_pos):
            return self.INTERFACE_OPEN

        # Si collision au clic avec la box, alors on appel la méthode de la gestion de l'interface en question
        if self.ButtonRectWheel.collidepoint(local_pos):
            self.GestionInterfaceSettings()

        elif self.ButtonRectSound.collidepoint(local_pos): 
            self.GestionInterfaceSound()

        elif self.ButtonRectBundle.collidepoint(local_pos):
            self.GestionInterfaceBundle()

        elif self.ButtonRectBook.collidepoint(local_pos): 
            self.GestionInterfaceBook()

        return self.INTERFACE_OPEN # mise à jour de l'interface check général
    

    def OpenInterfaceElementClavier(self, event : any, INTERFACE_OPEN : bool) -> bool:
        """Méthode : Appel des méthode de gestion des interfaces par touches clavier.
        Input : event = (element pygame), bool = checl interface global; Output : bool"""

        self.INTERFACE_OPEN = INTERFACE_OPEN

        if not self.INTERFACE_OPEN: # sécurité
            self.openInterface = False 

        # appel des méthode quand touche du clavier correspondante
        if event.key == pygame.K_p :
            self.GestionInterfaceSettings()

        elif event.key == pygame.K_v : 
            self.GestionInterfaceSound()

        elif event.key == pygame.K_i:
            self.GestionInterfaceBundle()

        elif event.key == pygame.K_b : 
            self.GestionInterfaceBook()

        return self.INTERFACE_OPEN # mise à jour de l'interface check général


    def GestionInterfaceSettings(self) -> None:
        """Méthode de gestion spécifique interface ouverture / fermeture
        Input / Output : None"""

        if not self.INTERFACE_OPEN and not self.InterfaceOpen: # check interface déjà ouvert ou non
            self.InterfaceOpen = True
            self.INTERFACE_OPEN = True
            self.interfaceElement = SettingsInterface(self)
        
        elif self.InterfaceOpen: # fermeture interface actuel
            self.InterfaceOpen = False
            self.INTERFACE_OPEN = False


    def GestionInterfaceSound(self) -> None:
        """Méthode de gestion spécifique interface ouverture / fermeture
        Input / Output : None"""

        if not self.INTERFACE_OPEN and not self.InterfaceOpen: # check interface déjà ouvert ou non
            self.InterfaceOpen = True
            self.INTERFACE_OPEN = True
            self.interfaceElement = SoudInterface(self)
        
        elif self.InterfaceOpen: # fermeture interface actuel
            self.InterfaceOpen = False
            self.INTERFACE_OPEN = False

    def GestionInterfaceBundle(self) -> None:
        """Méthode de gestion spécifique interface ouverture / fermeture
        Input / Output : None"""

        if not self.INTERFACE_OPEN and not self.InterfaceOpen: # check interface déjà ouvert ou non
            self.InterfaceOpen = True
            self.INTERFACE_OPEN = True
            self.interfaceElement = BundleInterface(self)
        
        elif self.InterfaceOpen: # fermeture interface actuel
            self.InterfaceOpen = False
            self.INTERFACE_OPEN = False

    def GestionInterfaceBook(self) -> None:
        """Méthode de gestion spécifique interface ouverture / fermeture
        Input / Output : None"""

        if not self.INTERFACE_OPEN and not self.InterfaceOpen: # check interface déjà ouvert ou non
            self.InterfaceOpen = True
            self.INTERFACE_OPEN = True
            self.interfaceElement = BookInterface(self)
        
        elif self.InterfaceOpen: # fermeture interface actuel
            self.InterfaceOpen = False
            self.INTERFACE_OPEN = False


    def Update(self, event) -> None:
        """Méthode de mise à jout de la box settings all + interface sur ouvert.
        Input / Output : None"""
        
        # fond box 
        self.allSettingsSurface.fill((255,255,255))
        
        # Remplissage couleur
        self.surfaceButtonBook.fill((50,50,50))  # blanc
        self.surfaceButtonSound.fill((50,50,50))
        self.surfaceButtonBundle.fill((50,50,50))
        self.surfaceButtonWheel.fill((50,50,50))

        # Dessin des images sur les boutons
        self.surfaceButtonBook.blit(self.book, (0, 0))
        self.surfaceButtonSound.blit(self.sound, (0, 0))
        self.surfaceButtonBundle.blit(self.bundle, (0, 0))
        self.surfaceButtonWheel.blit(self.wheel, (0, 0))

        # Affichage des bouutons sur la surface allsettings
        self.allSettingsSurface.blit(self.surfaceButtonBook, (self.ButtonRectBook.x, self.ButtonRectBook.y))
        self.allSettingsSurface.blit(self.surfaceButtonSound, (self.ButtonRectSound.x, self.ButtonRectSound.y))
        self.allSettingsSurface.blit(self.surfaceButtonBundle, (self.ButtonRectBundle.x,  self.ButtonRectBundle.y))
        self.allSettingsSurface.blit(self.surfaceButtonWheel, (self.ButtonRectWheel.x, self.ButtonRectWheel.y))

        # Si interface, alors mise à jour de l'interface
        if self.InterfaceOpen:
            self.interfaceElement.Update(event)
        
        

