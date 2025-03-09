from settings import *
from SourcesFichiers.Interface.Other.conditionsUtiilisationInterface import *
from SourcesFichiers.Ressources.Texte.creationTexte import *


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

        self.btnTexture = pygame.image.load(join("Images", "Element", "Start.png")).convert_alpha()
        self.btnTextureHover = pygame.image.load(join("Images", "Element", "StartHover.png")).convert_alpha()

        # bool radio button
        self.selectedOptionNiveau = 0  # choix 1 départ
        self.posRadioButtonNiveau = [(25, 50), (25, 100), (25, 150), (25, 200)]

        self.selectedOptionDifficulte = 0
        self.posRadioButtonDifficulte = [(25, 50), (25, 100)]

        self.selectedOptionLangue = 0
        self.posRadioButtonLangue = [(25, 50), (25, 100), (25, 150)]
        # Chargement des images et des éléments

        # timer click
        self.last_click_time = 0
        self.click_delay = 100  


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

        textAllNiveau = [TEXTE["Elements"]["HomeInterface"]["Niveau"]["Seconde"],
                         TEXTE["Elements"]["HomeInterface"]["Niveau"]["Premiere"],
                         TEXTE["Elements"]["HomeInterface"]["Niveau"]["Terminale"],
                         TEXTE["Elements"]["HomeInterface"]["Niveau"]["All"],]
        # Affichage des boutons radio
        for i, option in enumerate(textAllNiveau):
            pos = self.posRadioButtonNiveau[i]

            # Cercle externe (bouton radio)
            pygame.draw.circle(self.niveauSurface, BLACK, pos, 15, 2)

            # Si cette option est sélectionnée, on remplit le cercle
            if self.selectedOptionNiveau == i:
                pygame.draw.circle(self.niveauSurface, GREEN, pos, 10)  # Cercle interne rempli

            # Affichage du texte
            text_surface = FONT["FONT20"].render(option, True, BLACK)
            self.niveauSurface.blit(text_surface, (pos[0] + 30, pos[1] - 10))  # Décalage à droite
 


        # Box difficulté
        self.difficulteSurface.fill((255, 255, 255))
        titleTextDifficulte = FONT["FONT24"].render(TEXTE["Elements"]["HomeInterface"]["Difficulte"]["Title"], True, (0, 0, 0))
        self.difficulteSurface.blit(titleTextDifficulte, (10, 10))

        textAllDifficulte = [TEXTE["Elements"]["HomeInterface"]["Difficulte"]["Simple"],
                         TEXTE["Elements"]["HomeInterface"]["Difficulte"]["Difficile"],]

        # Affichage des boutons radio
        for i, option in enumerate(textAllDifficulte):
            pos = self.posRadioButtonNiveau[i]

            # Cercle externe (bouton radio)
            pygame.draw.circle(self.difficulteSurface, BLACK, pos, 15, 2)

            # Si cette option est sélectionnée, on remplit le cercle
            if self.selectedOptionDifficulte == i:
                pygame.draw.circle(self.difficulteSurface, GREEN, pos, 10)  # Cercle interne rempli

            # Affichage du texte
            text_surface = FONT["FONT20"].render(option, True, BLACK)
            self.difficulteSurface.blit(text_surface, (pos[0] + 30, pos[1] - 10))  # Décalage à droite
 

        # Box langue
        self.langueSurface.fill((255, 255, 255))
        titleTextLangue = FONT["FONT24"].render(TEXTE["Elements"]["HomeInterface"]["Langue"]["Title"], True, (0, 0, 0))
        self.langueSurface.blit(titleTextLangue, (10, 10))

        textAllLangue = [TEXTE["Elements"]["HomeInterface"]["Langue"]["Français"],
                            TEXTE["Elements"]["HomeInterface"]["Langue"]["Anglais"],
                            TEXTE["Elements"]["HomeInterface"]["Langue"]["Espagnol"],]

        # Affichage des boutons radio
        for i, option in enumerate(textAllLangue):
            pos = self.posRadioButtonNiveau[i]

            # Cercle externe (bouton radio)
            pygame.draw.circle(self.langueSurface, BLACK, pos, 15, 2)

            # Si cette option est sélectionnée, on remplit le cercle
            if self.selectedOptionLangue == i:
                pygame.draw.circle(self.langueSurface, GREEN, pos, 10)  # Cercle interne rempli

            # Affichage du texte
            text_surface = FONT["FONT20"].render(option, True, BLACK)
            self.langueSurface.blit(text_surface, (pos[0] + 30, pos[1] - 10))  # Décalage à droite
 


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
        self.btnRectLancer = pygame.Rect(((WINDOW_WIDTH//2) - self.surfaceBtnLancer.get_width() //2), 450, 350, 100)
        if self.isHoverBtnLancer and self.isConditionAccept:
            self.surfaceBtnLancer.blit(self.btnTextureHover, (0,0))
        else:
            self.surfaceBtnLancer.blit(self.btnTexture, (0,0))
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

                # delay de click
                current_time = pygame.time.get_ticks()
                if current_time - self.last_click_time > self.click_delay:
                    self.last_click_time = current_time


                    if self.checkbox_rect.collidepoint(event.pos) and not self.isConditionAccept:  # Clic sur la case
                        self.isConditionAccept = True
                    elif self.checkbox_rect.collidepoint(event.pos) and self.isConditionAccept:
                        self.isConditionAccept = False
                    elif self.text_rect.collidepoint(event.pos):  # Clic sur le texte
                        self.isInterfaceConditionsUtilisationOPEN = True
                        self.interfaceUpdate = self.keepInterfacConditionsUtilisationObj
                    elif self.isConditionAccept:
                        if self.btnRectLancer.collidepoint(event.pos):
                            INFOS["GameStart"] = True
                            ChangeCursor(False, "Hand")
                            self.gestionnaire.fondu_au_noir()
                            self.gestionnaire.StartMap()
                        

                # niveau
                for i, pos in enumerate(self.posRadioButtonNiveau):
                    global_pos = (pos[0] + 80, pos[1] + 100)  # Ajout du décalage de la surface niveauSurface
                    rect = pygame.Rect(global_pos[0] - 15, global_pos[1] - 15, 30, 30)

                    if rect.collidepoint(event.pos):
                        self.selectedOptionNiveau = i  # Met à jour le choix sélectionné

                        match self.selectedOptionNiveau:
                            case 0:
                                NIVEAU["Niveau"] = "Seconde"
                                NIVEAU["All"] = False
                            case 1:
                                NIVEAU["Niveau"] = "Premiere"
                                NIVEAU["All"] = False
                            case 2:
                                NIVEAU["Niveau"] = "Terminale"
                                NIVEAU["All"] = False
                            case 3:
                                NIVEAU["Niveau"] = "Seconde"
                                NIVEAU["All"] = True

                # difficulte
                for i, pos in enumerate(self.posRadioButtonDifficulte):
                    global_pos = (pos[0] + 480, pos[1] + 100)  # Ajout du décalage de la surface niveauSurface
                    rect = pygame.Rect(global_pos[0] - 15, global_pos[1] - 15, 30, 30)

                    if rect.collidepoint(event.pos):
                        self.selectedOptionDifficulte = i  # Met à jour le choix sélectionné

                        match self.selectedOptionDifficulte:
                            case 0:
                                INFOS["Difficulte"] = False
                            case 1:
                                INFOS["Difficulte"] = True

                # langue
                for i, pos in enumerate(self.posRadioButtonLangue):
                    global_pos = (pos[0] + 880, pos[1] + 100)  # Ajout du décalage de la surface niveauSurface
                    rect = pygame.Rect(global_pos[0] - 15, global_pos[1] - 15, 30, 30)

                    if rect.collidepoint(event.pos):
                        self.selectedOptionLangue = i  # Met à jour le choix sélectionné

                        match self.selectedOptionLangue:
                            case 0:
                                DICOLANGUE["Fr"] = True
                                DICOLANGUE["En"] = False
                                DICOLANGUE["Es"] = False
                            case 1 :
                                DICOLANGUE["Fr"] = False
                                DICOLANGUE["En"] = True
                                DICOLANGUE["Es"] = False
                            case 2 :
                                DICOLANGUE["Fr"] = False
                                DICOLANGUE["En"] = False
                                DICOLANGUE["Es"] = True
                        LoadTexte()

            elif event.type == pygame.MOUSEMOTION:
                self.isHorverText = self.text_rect.collidepoint(event.pos)  # Vérifie si la souris est sur le texte
                self.isHoverBtnLancer = self.btnRectLancer.collidepoint(event.pos)

                # check element licence
                if self.isConditionAccept and not self.isHorverText:
                    ChangeCursor(self.isHoverBtnLancer, "Hand")
                elif not self.isConditionAccept and not self.isHorverText:
                    ChangeCursor(self.isHoverBtnLancer, "Interdit")
                else:
                    ChangeCursor(self.isHorverText, "Hand")

                # check all radio button 
                allCoordsRadioButton = [self.posRadioButtonNiveau, self.posRadioButtonDifficulte, self.posRadioButtonLangue]
                for i, listCoords in enumerate(allCoordsRadioButton):
                    for coords in listCoords:
                        global_pos = (coords[0] + 80 + 400*i, coords[1] + 100)  # Ajout du décalage de la surface niveauSurface
                        rect = pygame.Rect(global_pos[0] - 15, global_pos[1] - 15, 30, 30)
                    
                        if rect.collidepoint(event.pos):
                            ChangeCursor(True, "Hand")


        if self.isInterfaceConditionsUtilisationOPEN:
            self.interfaceUpdate.Update(event)