from settings import *


class MiniMap:
    def __init__(self, mapBase: list, mapData: list, screen: any, allInteraction) -> None:
        """Initialisation de la minimap avec rendu en rectangles de couleur."""
        self.mapBase = mapBase  # sol
        self.mapData = mapData  # obstacles
        self.MiniMapSurface = screen
        self.allInteractionGroup = allInteraction

        self.static_surface = pygame.Surface((LONGUEUR * CELL_SIZE, LARGEUR * CELL_SIZE))
        self.player_position = None
        self.ratioImage = CELL_SIZE / CASEMAP / 2

        self.GenerateStaticMiniMap()

    def GenerateStaticMiniMap(self) -> None:
        """Génère la minimap statique avec des rectangles colorés."""
        if NIVEAU["Map"] != "NiveauBaseFuturiste":
            if NIVEAU["Map"] == "NiveauMordor":
                colorSol = (82, 59, 40)
            else:
                colorSol = (99, 173, 105)
        else:
            colorSol = (156, 125, 86)  # Herbe (vert clair) 
        colorSol2 = (145, 142, 135)
        colorRiver = (83, 205, 230) if NIVEAU["Map"] != "NiveauMordor" else (255, 81, 0)
        color_mapping = {
            "#": colorRiver,  # Rivière (bleu)
            "B": (105, 105, 105),  # Bordure (gris foncé)
            "=": (156, 125, 86),  # Chemin (gris clair)
            "H": (29, 34, 69),  # Maison (marron)
            "W": (99, 99, 99),  # Puits (noir)
            "@": (189, 186, 13),  # Champs (jaune)
            "-": colorSol,
            1  : colorSol,
            2  : colorSol,
            ".": colorSol2, # sol base (gris)
        }
        for ordonnee in range(len(self.mapBase)):
            for abscisse in range(len(self.mapBase[0])):

                if self.mapBase[ordonnee][abscisse] in [1, 2, "-", "=", "B"]:
                    cell = self.mapBase[ordonnee][abscisse] 
                    color = color_mapping.get(cell, colorSol)  # Vert foncé par défaut
                    rect = pygame.Rect(abscisse * CELL_SIZE, ordonnee * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(self.static_surface, color, rect)

                if self.mapData[ordonnee][abscisse] in ["H", "#", "@", "W"]:
                    cell = self.mapData[ordonnee][abscisse] 
                    color = color_mapping.get(cell, colorSol)  # Vert foncé par défaut
                    rect = pygame.Rect(abscisse * CELL_SIZE, ordonnee * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(self.static_surface, color, rect)


    def Update(self, player_pos: tuple, pnjGroup: any, interactionGroup: any) -> None:
        """Met à jour uniquement les entités mobiles sur la minimap."""
        self.MiniMapSurface.blit(self.static_surface, (0, 0))

        # Dessiner le joueur en rouge
        player_x, player_y = player_pos
        player_rect = pygame.Rect(player_x * CELL_SIZE * self.ratioImage, player_y * CELL_SIZE * self.ratioImage, CELL_SIZE * 2, CELL_SIZE * 2)
        pygame.draw.rect(self.MiniMapSurface, (255, 21, 4), player_rect)

        # Dessiner les PNJ en orange
        for objectPNJ in pnjGroup:
            pnj_x, pnj_y = objectPNJ.pos[0] * CASEMAP, objectPNJ.pos[1] * CASEMAP
            pnj_rect = pygame.Rect(pnj_x * CELL_SIZE * self.ratioImage, pnj_y * CELL_SIZE * self.ratioImage, CELL_SIZE * 2, CELL_SIZE * 2)
            pygame.draw.rect(self.MiniMapSurface, (252, 128, 3), pnj_rect)

        # Dessiner les objets d'interaction en bleu foncé
        for objectIntrac in interactionGroup:
            if objectIntrac.id not in ["Arbre", "Arbre1", "Souche", "Souche1", "HugeRock"]:
                element_x, element_y = objectIntrac.pos[0], objectIntrac.pos[1]
                element_rect = pygame.Rect(element_x * CELL_SIZE * self.ratioImage, element_y * CELL_SIZE * self.ratioImage, CELL_SIZE * 2, CELL_SIZE * 2)
                pygame.draw.rect(self.MiniMapSurface, (34, 5, 71), element_rect)    

class InfosTips:

    def __init__(self, screen : any) -> None:
        """Méthode initialisation des valeurs pour la box d'information de guidage pour le player
        Input : screen (surface infos tips)
        Output : None"""

        # initialisation
        self.IdeaTipsSurface = screen
        
        # creation element
        self.text = None
        self.indexTexte = 0
        self.loadImage()
        self.GetText()
    
    def loadImage(self) -> None:
        """Méthode chargement des images
        Input / Ouput : None"""
        try :
            self.idea = pygame.image.load(join("Image", "HotBar", "LightBulbIcon.png")).convert_alpha()
        except:
            INFOS["ErrorLoadElement"] = True

    def GetText(self) -> None:
        """Méthode de récupération du texte en foonc de l'état de STATE_HELP_INFOS"""
        
        if self.text != TEXTE["Elements"]["HotBar"]["IdeaTips"][NIVEAU["Map"]][STATE_HELP_INFOS[0]]: # si texte différents
            self.indexTexte = 0 # on reset l'écriture index
        
        self.text = TEXTE["Elements"]["HotBar"]["IdeaTips"][NIVEAU["Map"]][STATE_HELP_INFOS[0]] # texte / nouveau texte


    def BuildElement(self) -> None:
        """Méthode de constrcution de l'interface tips (bas centre page)
        Input / Ouput : None"""

        # image
        self.IdeaTipsSurface.fill((0,0,0,0)) # clear
        self.IdeaTipsSurface.blit(self.idea, (10,15))
        
        # texte
            # bloc gestion texte 
        if self.indexTexte < len(self.text):
            self.indexTexte += 1
            # Mettre à jour le texte affiché
        self.displayed_text = self.text[:self.indexTexte]

            
        # get lines 
        max_width = 400
        wrapped_lines = wrap_text(self.displayed_text, FONT["FONT22"], max_width)

        # Affichage des lignes
        y_offset = 40  # Position Y de départ
        line_height = FONT["FONT22"].size("Tg")[1]  # Hauteur d'une ligne
        for i, line in enumerate(wrapped_lines):
            line_surface = FONT["FONT22"].render(line, True, (255,255,255))
            self.IdeaTipsSurface.blit(line_surface, (95, y_offset + i * line_height))
    
    def Update(self) -> None:
        """Méthode update des infos tips, get du texte puis affichage de ce dernier
        Input / Ouput : None"""

        self.GetText()
        self.BuildElement()

class SettingsAll:

    def __init__(self, screen : any, gestionSound, gameInterfaces, gestionnaire) -> None:
        """Méthode initialisation de la box d'accès à tout les settings et utilitaires (bundle, settings, sound, book).
        Input : screen = (element pygame), boolean = check interface global """

        # Initialisation
        self.allSettingsSurface = screen
        self.gestionSound = gestionSound
        self.gestionnaire = gestionnaire
        self.gameInterfaces = gameInterfaces


        # Chargement images + éléments button pygame
        self.loadImage()
        self.ButtonSize()
        

    def ButtonSize(self) -> None:
        """Méthode : Création des spécifications 
        des buttons pygame. Input / Output : None"""

        # Dimensions des boutons (100x100)
        self.surfaceButtonWheel = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.surfaceButtonSound = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.surfaceButtonBundle = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.surfaceButtonBook = pygame.Surface((100, 100), pygame.SRCALPHA)

        # Positions des boutons, espacés de 6 pixels, centrés verticalement
        self.ButtonRectWheel =pygame.Rect(0, 25, 100, 100) 
        self.ButtonRectSound = pygame.Rect(106, 25, 100, 100)
        self.ButtonRectBundle = pygame.Rect(212, 25, 100, 100)
        self.ButtonRectBook = pygame.Rect(318, 25, 100, 100)
        

    def loadImage(self) -> None:
        """Méthode : Chargement des texture des 
        4 button pygame. Input / Output : None"""
        try :
            self.wheel = pygame.image.load(join("Image", "HotBar", "AllSettings", "Wheel.png")).convert_alpha()
            self.sound = pygame.image.load(join("Image", "HotBar", "AllSettings", "Sound.png")).convert_alpha()
            self.bundle = pygame.image.load(join("Image", "HotBar", "AllSettings", "Bundle.png")).convert_alpha()
            self.book = pygame.image.load(join("Image", "HotBar", "AllSettings", "Book.png")).convert_alpha()
        except:
            INFOS["ErrorLoadElement"] = True

    def OpenInterfaceElementClic(self, event : any) -> bool:
        """Méthode : Appel des méthode de gestion des interfaces par clic souris.
        Input : event = (element pygame), bool = checl interface global; Output : bool"""

        # Obtenez les coordonnées globales de l'événement
        global_pos = event.pos  # Coordonnées relatives à la fenêtre

        # Déterminez où la surface `allSettings_surface` est affichée
        surface_rect = self.allSettingsSurface.get_rect(topleft=COORS_BOX_ALL_SETTINGS)  # `x, y` est la position de la surface dans la fenêtre.

        # Convertissez les coordonnées globales en coordonnées locales
        local_pos = (global_pos[0] - surface_rect.x, global_pos[1] - surface_rect.y)

        # Vérifiez si le clic est dans la surface
        if not surface_rect.collidepoint(global_pos):
            return 

        # Si collision au clic avec la box, alors on appel la méthode de la gestion de l'interface en question
        if self.ButtonRectWheel.collidepoint(local_pos):
            self.gameInterfaces.GestionInterfaceSpecifique("Settings", self)

        elif self.ButtonRectSound.collidepoint(local_pos): 
            self.gameInterfaces.GestionInterfaceSpecifique("Sound", self)

        elif self.ButtonRectBundle.collidepoint(local_pos):
            self.gameInterfaces.GestionInterfaceSpecifique("Bundle", self)

        elif self.ButtonRectBook.collidepoint(local_pos): 
            self.gameInterfaces.GestionInterfaceSpecifique("Book", self)

    def HoverElement(self, event):

        # Obtenir la position de la souris dans l'écran
        global_pos = event.pos  # Position absolue (dans la fenêtre)

        # Récupérer la position de la surface dans l'écran
        surface_rect = self.allSettingsSurface.get_rect(topleft=COORS_BOX_ALL_SETTINGS)

        # Convertir la position globale en locale
        local_pos = (global_pos[0] - surface_rect.x, global_pos[1] - surface_rect.y)

        # Vérifier le survol des boutons
        allBox = [self.ButtonRectWheel, self.ButtonRectBundle, self.ButtonRectSound, self.ButtonRectBook]

        check = False
        if not INFOS["HideHotBar"]:
            if surface_rect.collidepoint(event.pos): # vérifie que l'on est sur la surface all settings
                for element in allBox:
                    if element.collidepoint(local_pos):  # Vérifier la position locale
                        check = True
                INFOS["Hover"] = check   
                        

    





    def Update(self) -> None:
        """Méthode de mise à jout de la box settings all + interface sur ouvert.
        Input / Output : None"""
        
        # fond box 
        self.allSettingsSurface.fill((0,0,0,0)) # transparent
        
        # Remplissage couleur
        self.surfaceButtonBook.fill((0,0,0,0))  # transparent
        self.surfaceButtonSound.fill((0,0,0,0))
        self.surfaceButtonBundle.fill((0,0,0,0))
        self.surfaceButtonWheel.fill((0,0,0,0))

        # Dessin des images sur les boutons
        self.surfaceButtonBook.blit(self.book, (2, 2)) # 2, 2 pour center
        self.surfaceButtonSound.blit(self.sound, (2, 2))
        self.surfaceButtonBundle.blit(self.bundle, (2, 2))
        self.surfaceButtonWheel.blit(self.wheel, (2, 2))

        # Affichage des bouutons sur la surface allsettings
        self.allSettingsSurface.blit(self.surfaceButtonBook, (self.ButtonRectBook.x, self.ButtonRectBook.y))
        self.allSettingsSurface.blit(self.surfaceButtonSound, (self.ButtonRectSound.x, self.ButtonRectSound.y))
        self.allSettingsSurface.blit(self.surfaceButtonBundle, (self.ButtonRectBundle.x,  self.ButtonRectBundle.y))
        self.allSettingsSurface.blit(self.surfaceButtonWheel, (self.ButtonRectWheel.x, self.ButtonRectWheel.y))