from settings import *
from Sources.Interface.Other.conditionsUtiilisationInterface import *

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

        # variables stockage infos
        self.keepInterfacConditionsUtilisationObj = ConditionsUtilisationInterface(self)
        self.isInterfaceConditionsUtilisationOPEN = False
        self.interfaceUpdate = None

        # Chargement des images et des éléments
        self.LoadImage()

    def LoadImage(self) -> None:
        """Chargement des images."""
        pass

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


    def Update(self, event) -> None:
        """Gestion des événements et mise à jour de l'interface."""

        # Mettre à jour l'affichage
        self.BuildInterface()

        self.interfaceSurface.blit(self.niveauSurface, (80, 100))
        self.interfaceSurface.blit(self.difficulteSurface, (480, 100))
        self.interfaceSurface.blit(self.langueSurface, (880, 100))
        self.displaySurface.blit(self.interfaceSurface, (0, 0))

        if event.type == pygame.KEYDOWN:
            if event.key == KEYSBIND["echap"] and not self.isInterfaceConditionsUtilisationOPEN:
                self.isInterfaceConditionsUtilisationOPEN = True
                self.interfaceUpdate = self.keepInterfacConditionsUtilisationObj
            elif event.key == KEYSBIND["echap"] and self.isInterfaceConditionsUtilisationOPEN:
                self.isInterfaceConditionsUtilisationOPEN = False
                self.interfaceUpdate = None


        if self.isInterfaceConditionsUtilisationOPEN:
            self.interfaceUpdate.Update(event)
