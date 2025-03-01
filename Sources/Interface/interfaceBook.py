import pygame.locals
from settings import * 

class BookInterface(object):

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
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH/0.5, WINDOW_HEIGHT/0.5),  pygame.SRCALPHA)

        # book bcg
        self.bookBcg = pygame.image.load(join("Images", "Interface", "Book.png")).convert_alpha()
        self.interfaceSurface.blit(self.bookBcg, (0,0))


    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.blit(self.bookBcg, (0,0))
        text = FONT["FONT36"].render(TEXTE["Elements"]["HotBar"]["Book"]["Title"], True, (0,0,0))
        self.interfaceSurface.blit(text, (10,10))

    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()
        
        self.displaySurface.blit(self.backgroundSurface, (0,0))
        self.displaySurface.blit(self.interfaceSurface, (160, 90)) # pos topleft


