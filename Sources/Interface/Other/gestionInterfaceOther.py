from settings import *

class HomeInterface(object):

    def __init__(self, gestionnaire: any) -> None:
        """Initialisation de l'interface."""
        
        self.gestionnaire = gestionnaire
        
        # Création des surfaces
        self.displaySurface = pygame.display.get_surface()
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.interfaceSurface.fill((48, 155, 217))

        # Surfaces des éléments
        self.niveauSurface = pygame.Surface((320, 250), pygame.SRCALPHA)
        self.difficulteSurface = pygame.Surface((320, 250), pygame.SRCALPHA)
        self.langueSurface = pygame.Surface((320, 250), pygame.SRCALPHA)

        # Chargement des images et des éléments
        self.LoadImage()
        self.CreateBoxConditionsElements()

    def LoadImage(self) -> None:
        """Chargement des images."""
        pass

    def CreateBoxConditionsElements(self) -> None:
        """Création de la boîte des conditions d'utilisation."""
        # Box conditions d'utilisation
        self.box_width = 800 
        self.box_height = 200
        self.box_x = (WINDOW_WIDTH - self.box_width) // 2 
        self.box_y = ((WINDOW_HEIGHT - self.box_height) // 2) + 100
        
        self.textConditionsSurface = pygame.Surface((self.box_width - 40, 600), pygame.SRCALPHA)

        self.textConditionsSurface.fill((255, 255, 255))
           
        textConditions = TEXTE["Elements"]["HomeInterface"]["ConditionsUtilisation"]
        max_width = self.box_width - 60  # Marge de 30px de chaque côté

        wrapped_lines = wrap_text(textConditions, FONT["FONT20"], max_width)

        line_height = FONT["FONT20"].size("Tg")[1]  # Hauteur d'une ligne
        y_offset = 20  # Décalage du texte depuis le haut

        for i, line in enumerate(wrapped_lines):
            line_surface = FONT["FONT20"].render(line, True, (0, 0, 0))
            self.textConditionsSurface.blit(line_surface, (20, y_offset + i * line_height))

        # Scroll
        self.scroll_y = 0  
        self.max_scroll = max(0, self.textConditionsSurface.get_height() - (self.box_height - 40))

        # Scrollbar
        self.scrollbar_width = 8
        self.scrollbar_x = self.box_x + self.box_width - self.scrollbar_width - 5
        self.scrollbar_height = max(20, (self.box_height - 40) * (self.box_height - 40) / self.textConditionsSurface.get_height())
        self.scrollbar_y = self.box_y
        self.scrolling = False  

    def BuildInterface(self) -> None:
        """Construction de l'interface."""

        self.interfaceSurface.fill((48, 155, 217))

        # Titre du jeu
        text = FONT["FONT36"].render(TEXTE["Elements"]["GameName"], True, (0, 0, 0))
        self.interfaceSurface.blit(text, text.get_rect(center=(WINDOW_WIDTH // 2, 50)))

        # Box niveau
        self.niveauSurface.fill((255, 255, 255))
        titleTextNiveau = FONT["FONT24"].render(TEXTE["Elements"]["HomeInterface"]["Niveau"]["Title"], True, (0, 0, 0))
        self.niveauSurface.blit(titleTextNiveau, (10, 10))

        # Box difficulté
        self.difficulteSurface.fill((255, 255, 255))
        titleTextDifficulte = FONT["FONT24"].render(TEXTE["Elements"]["HomeInterface"]["Difficulte"]["Title"], True, (0, 0, 0))
        self.difficulteSurface.blit(titleTextDifficulte, (10, 10))

        # Box langue
        self.langueSurface.fill((255, 255, 255))
        titleTextLangue = FONT["FONT24"].render(TEXTE["Elements"]["HomeInterface"]["Langue"]["Title"], True, (0, 0, 0))
        self.langueSurface.blit(titleTextLangue, (10, 10))

        # Affichage des conditions d'utilisation avec scrolling
        self.interfaceSurface.blit(self.textConditionsSurface, (self.box_x + 20, self.box_y + 20), (0, self.scroll_y, self.box_width - 40, self.box_height - 40))

        # Scrollbar
        if self.max_scroll > 0:
            self.scrollbar_y = self.box_y + (self.scroll_y / self.max_scroll) * (self.box_height - self.scrollbar_height)
        else:
            self.scrollbar_y = self.box_y  

        # Couleur de la scrollbar
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        color = SCROLLBAR_HOVER if (self.scrollbar_x <= self.mouse_x <= self.scrollbar_x + self.scrollbar_width and
                                    self.scrollbar_y <= self.mouse_y <= self.scrollbar_y + self.scrollbar_height) else SCROLLBAR_COLOR

        pygame.draw.rect(self.interfaceSurface, color,
                         (self.scrollbar_x, self.scrollbar_y, self.scrollbar_width, self.scrollbar_height),
                         border_radius=4)

    def Update(self, event) -> None:
        """Gestion des événements et mise à jour de l'interface."""

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Molette haut
                self.scroll_y = max(self.scroll_y - 30, 0)
            if event.button == 5:  # Molette bas
                self.scroll_y = min(self.scroll_y + 30, self.max_scroll)

            # Vérification clic sur scrollbar
            if self.scrollbar_x <= self.mouse_x <= self.scrollbar_x + self.scrollbar_width and \
                    self.scrollbar_y <= self.mouse_y <= self.scrollbar_y + self.scrollbar_height:
                self.scrolling = True

        if event.type == pygame.MOUSEBUTTONUP:
            self.scrolling = False

        if event.type == pygame.MOUSEMOTION and self.scrolling:
            rel_y = event.rel[1]
            new_scroll_y = self.scroll_y + (rel_y * self.max_scroll / (self.box_height - self.scrollbar_height))
            self.scroll_y = min(max(new_scroll_y, 0), self.max_scroll)

        # Mettre à jour l'affichage
        self.BuildInterface()

        self.interfaceSurface.blit(self.niveauSurface, (80, 100))
        self.interfaceSurface.blit(self.difficulteSurface, (480, 100))
        self.interfaceSurface.blit(self.langueSurface, (880, 100))
        self.displaySurface.blit(self.interfaceSurface, (0, 0))
