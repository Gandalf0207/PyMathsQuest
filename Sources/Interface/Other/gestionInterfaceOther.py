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

        # bool check
        self.isConditionAccept = False
        self.isHorverText = False
        self.isHoverBtnLancer = False

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

        # element licence
        if self.isHorverText:
            textCondition = FONT["FONT20U"].render(TEXTE["Elements"]["HomeInterface"]["TexteConditions"], True, (0,0,0))
        else:
            textCondition = FONT["FONT20"].render(TEXTE["Elements"]["HomeInterface"]["TexteConditions"], True, (0,0,0))

        self.text_rect = textCondition.get_rect(center=(WINDOW_WIDTH // 2, 400))
        self.interfaceSurface.blit(textCondition, self.text_rect)

        self.checkbox_rect = pygame.Rect(self.text_rect.x- 25, 400 - 10, 20, 20)
        
        pygame.draw.rect(self.interfaceSurface, BLACK, self.checkbox_rect, 2) # Dessiner la case (cochée ou non)
        if self.isConditionAccept:
            pygame.draw.rect(self.interfaceSurface, GREEN, self.checkbox_rect.inflate(-4, -4))  # Case remplie si cochée

        # btn lancer game
        self.surfaceBtnLancer = pygame.Surface((350, 100))
        self.btnRectLancer = pygame.Rect(((WINDOW_WIDTH//2) - self.surfaceBtnLancer.get_width() //2), 450, 350, 140)
        if self.isConditionAccept:
            if self.isHoverBtnLancer:
                self.surfaceBtnLancer.fill((143, 235, 233))
            else:
                self.surfaceBtnLancer.fill((141, 201, 200))
        else:
            self.surfaceBtnLancer.fill((144, 158, 148))
        self.textL = TEXTE["Elements"]["HomeInterface"]["Lancer"]
        self.textLancer = FONT["FONT50"].render(self.textL, True, (10,10,10))
        self.surfaceBtnLancer.blit(self.textLancer, self.textLancer.get_rect(center=(self.surfaceBtnLancer.get_width()//2, self.surfaceBtnLancer.get_height()//2)))
        self.interfaceSurface.blit(self.surfaceBtnLancer, (self.btnRectLancer.x, self.btnRectLancer.y))



    def Update(self, event) -> None:
        """Gestion des événements et mise à jour de l'interface."""

        # Mettre à jour l'affichage
        self.BuildInterface()

        self.interfaceSurface.blit(self.niveauSurface, (80, 100))
        self.interfaceSurface.blit(self.difficulteSurface, (480, 100))
        self.interfaceSurface.blit(self.langueSurface, (880, 100))
        self.displaySurface.blit(self.interfaceSurface, (0, 0))

        if event.type == pygame.KEYDOWN:
            if event.key == KEYSBIND["echap"] and self.isInterfaceConditionsUtilisationOPEN:
                self.isInterfaceConditionsUtilisationOPEN = False
                self.interfaceUpdate = None

        if not self.isInterfaceConditionsUtilisationOPEN: # éviter les interaction si les conditions sont ouvertess
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.checkbox_rect.collidepoint(event.pos) and not self.isConditionAccept:  # Clic sur la case
                    self.isConditionAccept = True
                elif self.checkbox_rect.collidepoint(event.pos) and self.isConditionAccept:
                    self.isConditionAccept = False
                elif self.text_rect.collidepoint(event.pos):  # Clic sur le texte
                    self.isInterfaceConditionsUtilisationOPEN = True
                    self.interfaceUpdate = self.keepInterfacConditionsUtilisationObj
            elif event.type == pygame.MOUSEMOTION:
                self.isHorverText = self.text_rect.collidepoint(event.pos)  # Vérifie si la souris est sur le texte
                self.isHoverBtnLancer = self.btnRectLancer.collidepoint(event.pos)

        if self.isInterfaceConditionsUtilisationOPEN:
            self.interfaceUpdate.Update(event)
