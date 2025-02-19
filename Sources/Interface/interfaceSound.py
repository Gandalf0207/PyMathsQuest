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

    def CloseInterface(self) -> None:
        """Méthode de fermeture de l'interface. Input / Output : None"""
        # changement des boolean de check
        self.gestionnaire.CloseInterface()

    def Update(self, event) -> None:
        """Mise à jour de l'interface et gestion des interactions."""
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (320,180))

        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()
        if keys[KEYSBIND["echap"]]:  # Fermer avec ESC
            self.CloseInterface()

        # Coordonnées globales de l'événement
        global_pos = pygame.mouse.get_pos()

        # Convertir les coordonnées globales en locales
        surface_rect = pygame.Rect(320, 180, self.interfaceSurface.get_width(), self.interfaceSurface.get_height())

        if surface_rect.collidepoint(global_pos):
            local_pos = (global_pos[0] - surface_rect.x, global_pos[1] - surface_rect.y)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = local_pos
                for i, slider in enumerate(self.sliders):
                    if self.slider_x <= mouse_x <= self.slider_x + self.slider_width and \
                       slider["y"] - 5 <= mouse_y <= slider["y"] + self.slider_height + 5:
                        self.dragging = i  # On stocke l'index du slider actif

            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = None  # On arrête le glissement

            elif event.type == pygame.MOUSEMOTION and self.dragging is not None:
                mouse_x, _ = local_pos
                slider = self.sliders[self.dragging]

                # Déplacer le curseur
                new_x = min(max(mouse_x - self.cursor_width // 2, self.slider_x), self.slider_x + self.slider_width - self.cursor_width)
                SOUND[slider["Element"]] = (new_x - self.slider_x) / (self.slider_width - self.cursor_width)
                self.gestionnaire.gestionSound.Update()

