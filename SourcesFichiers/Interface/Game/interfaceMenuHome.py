from settings import * 

class HomeMenuInterface(object):

    def __init__(self, gestionnaire: any) ->None:
        """Méthode initialisation de l'interface de book.
        Input : gestionnaire = self méthode d'appel"""
        
        # Initialisation
        self.gestionnaire = gestionnaire

        # Surface pour le fond transparent
        self.backgroundSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.backgroundSurface.fill((50, 50, 50, 200))  # Fond gris avec alpha (200)
        
        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),  pygame.SRCALPHA)
        self.interfaceSurface.fill((0,0,0,0))

        self.isHoverBtnQuitter = False
        self.isHoverBtnCredits = False

        self.btnTexture = pygame.image.load(join("Images", "Element", "Start.png")).convert_alpha()
        self.btnTextureHover = pygame.image.load(join("Images", "Element", "StartHover.png")).convert_alpha()

        # timer click
        self.last_click_time = 0
        self.click_delay = 500   

    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill((0,0,0,0))

        # btn crédits
        self.surfaceBtnCredits = pygame.Surface((350, 100))
        self.btnRectCredits = pygame.Rect(((WINDOW_WIDTH//4) - self.surfaceBtnCredits.get_width() //2), 65, 350, 100)
        if self.isHoverBtnCredits:
            self.surfaceBtnCredits.blit(self.btnTextureHover, (0,0))
        else:
            self.surfaceBtnCredits.blit(self.btnTexture, (0,0))

        self.textC = TEXTE["Elements"]["InterfaceHomeMenu"]["Credits"]
        self.textCredits = FONT["FONT50"].render(self.textC, True, (10,10,10))
        self.surfaceBtnCredits.blit(self.textCredits, self.textCredits.get_rect(center=(self.surfaceBtnCredits.get_width()//2, self.surfaceBtnCredits.get_height()//2)))
        self.interfaceSurface.blit(self.surfaceBtnCredits, (self.btnRectCredits.x, self.btnRectCredits.y))

        # btn leave
        self.surfaceBtnQuitter = pygame.Surface((350, 100))
        self.btnRectQuitter = pygame.Rect(((WINDOW_WIDTH//4) - self.surfaceBtnQuitter.get_width() //2), 195, 350, 100)
        if self.isHoverBtnQuitter:
            self.surfaceBtnQuitter.blit(self.btnTextureHover, (0,0))
        else:
            self.surfaceBtnQuitter.blit(self.btnTexture, (0,0))

        self.textQ = TEXTE["Elements"]["InterfaceHomeMenu"]["Quitter"]
        self.textQuitter = FONT["FONT50"].render(self.textQ, True, (10,10,10))
        self.surfaceBtnQuitter.blit(self.textQuitter, self.textQuitter.get_rect(center=(self.surfaceBtnQuitter.get_width()//2, self.surfaceBtnQuitter.get_height()//2)))
        self.interfaceSurface.blit(self.surfaceBtnQuitter, (self.btnRectQuitter.x, self.btnRectQuitter.y))





    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()
        self.displaySurface.blit(self.backgroundSurface, (0,0))
        self.displaySurface.blit(self.interfaceSurface, (320,180)) # pos topleft


        if event.type == pygame.MOUSEBUTTONDOWN:
            # delay de click
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time
            
                local_pos = GetLocalPos(event, self.interfaceSurface, (320, 180))
                if local_pos:

                    if self.btnRectCredits.collidepoint(local_pos):
                        self.gestionnaire.MiseAJourInterfaceCredits()
                    if self.btnRectQuitter.collidepoint(local_pos):
                        INFOS["CrashGame"] = True

        if event.type == pygame.MOUSEMOTION:
            # Obtenir la position locale de la souris dans l'interface
            local_pos = GetLocalPos(event, self.interfaceSurface, (320, 180))
            
            if local_pos:
                hovered_btn = None

                if self.btnRectCredits.collidepoint(local_pos):
                    hovered_btn = "Credits"
                elif self.btnRectQuitter.collidepoint(local_pos):
                    hovered_btn = "Quitter"

                # Mise à jour des états des boutons
                self.isHoverBtnCredits = (hovered_btn == "Credits")
                self.isHoverBtnQuitter = (hovered_btn == "Quitter")

                # Modifier le curseur si sur un bouton, sinon le réinitialiser
                INFOS["Hover"] = bool(hovered_btn)