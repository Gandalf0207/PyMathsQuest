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
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH*(3/4), WINDOW_HEIGHT*(3/4)),  pygame.SRCALPHA)

        # close interface cross
        self.surfaceCloseCross = pygame.Surface((24,24), pygame.SRCALPHA)
        self.isCrossCloseHover = False
        self.crossClose = pygame.image.load(join("Image","Interface", "Croix", "x-mark.png")).convert_alpha()
        self.crossClose2 = pygame.image.load(join("Image","Interface", "Croix", "x-mark2.png")).convert_alpha()

        # book bcg
        self.bookBcg = pygame.image.load(join("Image", "Interface", "Book.png")).convert_alpha()
        self.interfaceSurface.blit(self.bookBcg, (0,0))


    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.blit(self.bookBcg, (0,0))

        # close element
        self.surfaceCloseCross.fill((0,0,0,0))
        self.rectCloseCross = pygame.Rect(self.interfaceSurface.get_width() - 39, 5, 24, 24)
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
        self.displaySurface.blit(self.interfaceSurface, (160, 90)) # pos topleft


        if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):

            local_pos = GetLocalPos(event, self.interfaceSurface, (160, 90))
            if local_pos:
                if event.type == pygame.MOUSEMOTION:
                    # cross close interface
                    self.isCrossCloseHover = self.rectCloseCross.collidepoint(local_pos)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rectCloseCross.collidepoint(local_pos):
                        # fermeture interface
                        self.gestionnaire.CloseAllInterface()
