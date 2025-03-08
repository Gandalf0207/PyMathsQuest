from settings import *

class SoundInterface(object):

    def __init__(self, gestionnaire: any) ->None:
        """Méthode initialisation de l'interface de sound.
        Input : gestionnaire = self méthode d'appel"""
        
        # Initialisation
        self.gestionnaire = gestionnaire
        
        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),  pygame.SRCALPHA)
        self.interfaceSurface.fill("#ffffff")

        # Propriétés des sliders
        self.slider_x = 50  # Position X des sliders
        self.slider_width = 540
        self.slider_height = 20
        self.cursor_width = 10

        # Définition des sliders (Musique, Effets, Voix)
        self.sliders = [
            {"label": "Musique", "y": 100, "Element" : "BandeSon"},
            {"label": "Voix", "y": 300, "Element" : "Dialogue"},  
            {"label": "Effets Sonores", "y": 200, "Element" : "EffetSonore"},  
        ]
        self.dragging = None

        # close interface cross
        self.surfaceCloseCross = pygame.Surface((24,24))
        self.isCrossCloseHover = False
        self.crossClose = pygame.image.load(join("Images", "Croix", "x-mark.png")).convert_alpha()
        self.crossClose2 = pygame.image.load(join("Images", "Croix", "x-mark2.png")).convert_alpha()



    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill("#ffffff")
        text = FONT["FONT36"].render(TEXTE["Elements"]["HotBar"]["Sound"]["Title"], True, (0,0,0))
        self.interfaceSurface.blit(text, (10,10))

        for i, slider in enumerate(self.sliders):
            # Position du curseur
            cursor_x = self.slider_x + int(SOUND[slider["Element"]] * (self.slider_width - self.cursor_width))

            # Dessiner le titre du slider
            text = FONT["FONT20"].render(slider["label"], True, (0, 0, 0))
            self.interfaceSurface.blit(text, (self.slider_x, slider["y"] - 45))

            # Dessiner la barre de volume
            pygame.draw.rect(self.interfaceSurface, (200, 200, 200), (self.slider_x, slider["y"], self.slider_width, self.slider_height))

            # Dessiner le curseur
            pygame.draw.rect(self.interfaceSurface, (255, 0, 0), (cursor_x, slider["y"] - 5, self.cursor_width, self.slider_height + 10))

            # Afficher le volume en %
            volume_percent = int(SOUND[slider["Element"]] * 100)
            volume_text = FONT["FONT20"].render(f"{volume_percent}%", True, (0, 0, 0))
            text_rect = volume_text.get_rect(center=(cursor_x + self.cursor_width // 2, slider["y"] - 20))
            self.interfaceSurface.blit(volume_text, text_rect)

        # close element
        self.surfaceCloseCross.fill("#ffffff")
        self.rectCloseCross = pygame.Rect(self.interfaceSurface.get_width() - 34, 10, 24, 24)
        if self.isCrossCloseHover:
            self.surfaceCloseCross.blit(self.crossClose2, (0,0))
        else:
            self.surfaceCloseCross.blit(self.crossClose, (0,0))
        self.interfaceSurface.blit(self.surfaceCloseCross, (self.rectCloseCross.x, self.rectCloseCross.y))

    def Update(self, event) -> None:
        """Mise à jour de l'interface et gestion des interactions."""
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (320,180))



        if event.type == pygame.MOUSEBUTTONDOWN:
            local_pos = GetLocalPos(event, self.interfaceSurface, (320, 180))
            if local_pos:
                mouse_x, mouse_y = local_pos
                for i, slider in enumerate(self.sliders):
                    if self.slider_x <= mouse_x <= self.slider_x + self.slider_width and \
                    slider["y"] - 5 <= mouse_y <= slider["y"] + self.slider_height + 5:
                        self.dragging = i  # On stocke l'index du slider actif
            
                # check pour le clos interface cross
                if self.rectCloseCross.collidepoint(local_pos):
                    # fermeture interface
                    self.gestionnaire.CloseAllInterface()


        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = None  # On arrête le glissement

        elif event.type == pygame.MOUSEMOTION and self.dragging is not None:
            local_pos = GetLocalPos(event, self.interfaceSurface, (320, 180))
            if local_pos:
                mouse_x, _ = local_pos
                slider = self.sliders[self.dragging]

                # Déplacer le curseur
                new_x = min(max(mouse_x - self.cursor_width // 2, self.slider_x), self.slider_x + self.slider_width - self.cursor_width)
                SOUND[slider["Element"]] = (new_x - self.slider_x) / (self.slider_width - self.cursor_width)
                print(self.gestionnaire)
                self.gestionnaire.gestionSoundFond.Update()
                
        # cross close interface
        if event.type == pygame.MOUSEMOTION:
            local_pos = GetLocalPos(event, self.interfaceSurface, (320, 180))
            if local_pos:
                # cross close interface
                self.isCrossCloseHover = self.rectCloseCross.collidepoint(local_pos)
