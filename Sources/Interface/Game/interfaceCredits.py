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

        self.interfaceCredit = None


    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill("#ffffff")
        text = FONT["FONT36"].render(TEXTE["Elements"]["InterfaceCreditsGame"]["Title"], True, (0,0,0))
        self.interfaceSurface.blit(text, (10,10))


    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (0,0)) # pos topleft