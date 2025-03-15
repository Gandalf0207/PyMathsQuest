from settings import *

class CreditsInterfaceGame():
    def __init__(self, gestionnaire: any) ->None:
        """Méthode initialisation de l'interface de crédtis.
        Input : gestionnaire = self méthode d'appel"""
        
        # Initialisation
        self.gestionnaire = gestionnaire
        
        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT),  pygame.SRCALPHA)
        self.interfaceSurface.fill("#ffffff")

        # close interface cross
        self.surfaceCloseCross = pygame.Surface((24,24))
        self.isCrossCloseHover = False
        try :
            self.crossClose = pygame.image.load(join("Image", "Interface", "Croix", "x-mark.png")).convert_alpha()
            self.crossClose2 = pygame.image.load(join("Image", "Interface", "Croix", "x-mark2.png")).convert_alpha()
        except:
            INFOS["ErrorLoadElement"] = True


    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill("#ffffff")
        text = FONT["FONT36"].render(TEXTE["Elements"]["InterfaceCreditsGame"]["Title"], True, (0,0,0))
        self.interfaceSurface.blit(text, (10,10))

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
        self.displaySurface.blit(self.interfaceSurface, (0,0)) # pos topleft

        # cross close interface
        if event.type == pygame.MOUSEMOTION:
            # cross close interface
            check = False
            self.isCrossCloseHover = self.rectCloseCross.collidepoint(event.pos)
            if self.isCrossCloseHover:
                check = True
            INFOS["Hover"] = check   

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectCloseCross.collidepoint(event.pos):
                # fermeture interface
                self.gestionnaire.MiseAJourInterfaceCredits()