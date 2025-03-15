from settings import *


class ConditionsUtilisationInterface(object):

    def __init__(self, gestionnaire: any) ->None:
        """Méthode initialisation de l'interface de conditions utilisation.
        Input : gestionnaire = self méthode d'appel"""
        
        # Initialisation
        self.gestionnaire = gestionnaire
        
        # Surface pour le fond transparent
        self.backgroundSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.backgroundSurface.fill((50, 50, 50, 200))  # Fond gris avec alpha (200)

        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH//2, WINDOW_HEIGHT//2),  pygame.SRCALPHA)

        # close interface cross
        self.surfaceCloseCross = pygame.Surface((24,24))
        self.isCrossCloseHover = False
        try :
            self.crossClose = pygame.image.load(join("Image","Interface", "Croix", "x-mark.png")).convert_alpha()
            self.crossClose2 = pygame.image.load(join("Image","Interface", "Croix", "x-mark2.png")).convert_alpha()
        except:
            INFOS["ErrorLoadElement"] = True

        self.CreateBoxConditionsElements()


    def CreateBoxConditionsElements(self) -> None:
        """Création de la boîte des conditions d'utilisation."""
        # Box conditions d'utilisation
        self.box_width = (WINDOW_WIDTH//2) - 40
        self.box_height =( WINDOW_HEIGHT//2) - 70
        self.box_x = (WINDOW_WIDTH // 2 - self.box_width) // 2 
        self.box_y = 50
        
        self.textConditionsSurface = pygame.Surface((self.box_width, 900), pygame.SRCALPHA)

        self.textConditionsSurface.fill((255, 255, 255))
           
        textConditions = TEXTE["Elements"]["HomeInterface"]["InterfaceCondition"]["ConditionsUtilisation"]
        max_width = self.box_width - 60  # Marge de 40px de chaque côté

        wrapped_lines = wrap_text_2(textConditions, FONT["FONT20"], max_width)

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
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill((255, 255, 255))
        text = FONT["FONT36"].render(TEXTE["Elements"]["HomeInterface"]["InterfaceCondition"]["Title"], True, (0,0,0))
        self.interfaceSurface.blit(text, (10,10))

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
    
        # close element
        self.surfaceCloseCross.fill("#ffffff")
        self.rectCloseCross = pygame.Rect(self.interfaceSurface.get_width() - 34, 10, 24, 24)
        if self.isCrossCloseHover:
            self.surfaceCloseCross.blit(self.crossClose2, (0,0))
        else:
            self.surfaceCloseCross.blit(self.crossClose, (0,0))
        self.interfaceSurface.blit(self.surfaceCloseCross, (self.rectCloseCross.x, self.rectCloseCross.y))


    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()
        self.displaySurface.blit(self.backgroundSurface, (0,0))
        self.displaySurface.blit(self.interfaceSurface, (320, 180))  # pos topleft


        if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
            
            local_pos = GetLocalPos(event, self.interfaceSurface, (320,180))
            if local_pos:

                local_x, local_y = local_pos  # Extraction des coordonnées locales

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:  # Molette haut
                        self.scroll_y = max(self.scroll_y - 30, 0)
                    if event.button == 5:  # Molette bas
                        self.scroll_y = min(self.scroll_y + 30, self.max_scroll)

                    # Vérification clic sur scrollbar avec les coordonnées locales
                    if self.scrollbar_x <= local_x <= self.scrollbar_x + self.scrollbar_width and \
                            self.scrollbar_y <= local_y <= self.scrollbar_y + self.scrollbar_height:
                        self.scrolling = True

                    if self.rectCloseCross.collidepoint(local_pos):
                        # fermeture interface
                        self.gestionnaire.isInterfaceConditionsUtilisationOPEN = False

                if event.type == pygame.MOUSEBUTTONUP:
                    self.scrolling = False


        if event.type == pygame.MOUSEMOTION : 
            local_pos = GetLocalPos(event, self.interfaceSurface, (320, 180))
            if local_pos:
                # cross close interface
                if event.type == pygame.MOUSEMOTION:
                    self.isCrossCloseHover = self.rectCloseCross.collidepoint(local_pos)

                if event.type == pygame.MOUSEMOTION and self.scrolling:
                    rel_y = event.rel[1]
                    new_scroll_y = self.scroll_y + (rel_y * self.max_scroll / (self.box_height - self.scrollbar_height))
                    self.scroll_y = min(max(new_scroll_y, 0), self.max_scroll)