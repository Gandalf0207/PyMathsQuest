from settings import *
from Sources.Exos.choixExo import *
from Sources.Exos.renderLatex import *

class CreateExo:
    def __init__(self, gestionnaire : any) -> None:
        """Méthode d'initialisation des valeur pour la class de crétion des exercices
        Input : gestionnaire (self main class)
        Output : None"""

        self.gestionnaire = gestionnaire # self main

        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceExoSurface = pygame.Surface((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),  pygame.SRCALPHA)
        self.interfaceExoSurface.fill("#ffffff")

        # création obj pour la création d'exercice
        self.ObjRender = RenderLatex()
        self.ObjExoChoix = GetExo()

        # infos + variable utiles
        self.latexSurface = None
        self.last_click_time = 0
        self.click_delay = 300
        self.indexTexte = 0

        # création element button
        self.CreateRectButton()

    def CreateRectButton(self) -> None:
        """Mthode création des éléments pour les bouttons de réponse
        Inpur / Output : None"""

        # surface
        self.surfaceButton1 = pygame.Surface((100,100))
        self.surfaceButton2 = pygame.Surface((100,100))
        self.surfaceButton3 = pygame.Surface((100,100))

         # Positions des boutons : element collision rect 
        self.ButtonRect1 =pygame.Rect(68, WINDOW_HEIGHT/2 - 120, 100, 100) 
        self.ButtonRect2 = pygame.Rect(236, WINDOW_HEIGHT/2 - 120, 100, 100)
        self.ButtonRect3 = pygame.Rect(404, WINDOW_HEIGHT/2 -120, 100, 100)

    def BuildInterface(self) -> None:
        """Méthode ce construction de l'interface à chque rafraichissement
        Intput / Oupur : None"""

        # clear
        self.interfaceExoSurface.fill("#ffffff")

        # titre
        textTitre = FONT["FONT30"].render(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["ExoTexte"]["Title"], True, (0, 0, 0))
        self.interfaceExoSurface.blit(textTitre, (10, 10))

        # consigne
        self.textConsigne = TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["ExoTexte"][f"Difficulte{INFOS["Difficulte"]}"]["Consigne"]

        # Mettre à jour le texte affiché si nécessaire
        if self.indexTexte < len(self.textConsigne):
            self.indexTexte += 1
        self.displayed_text = self.textConsigne[:self.indexTexte]

        # Fonction simple pour découper le text
        max_width = 650
        wrapped_lines = wrap_text(self.displayed_text, FONT["FONT30"], max_width)

        # Affichage des lignes
        y_offset =  60 # Position Y de départ
        line_height = FONT["FONT22"].size("Tg")[1]  # Hauteur d'une ligne
        for i, line in enumerate(wrapped_lines):
            line_surface = FONT["FONT22"].render(line, True, (0,0,0))
            self.interfaceExoSurface.blit(line_surface, (20, y_offset + i * line_height))
        

        # équation affichage
        self.interfaceExoSurface.blit(self.latexSurface, (10, 100))

        # réponse titre
        self.textQCM = FONT["FONT22"].render(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["ExoTexte"]["DifficulteTrue"]["QCM"], True, (0, 0, 0))
        self.interfaceExoSurface.blit(self.textQCM, (10, WINDOW_HEIGHT/2 - 150))

        # réponse button
        self.textR1 = FONT["FONT22"].render(str(self.listeReponse[0]), True, (0,0,0))
        self.textR2 = FONT["FONT22"].render(str(self.listeReponse[1]), True, (0,0,0))
        self.textR3 = FONT["FONT22"].render(str(self.listeReponse[2]), True, (0,0,0))

        self.surfaceButton1.fill((200,205,205))
        self.surfaceButton2.fill((200,205,205))
        self.surfaceButton3.fill((200,205,205))

        self.surfaceButton1.blit(self.textR1, (0,0))
        self.surfaceButton2.blit(self.textR2, (0,0))
        self.surfaceButton3.blit(self.textR3, (0,0))

        self.interfaceExoSurface.blit(self.surfaceButton1, (self.ButtonRect1.x, self.ButtonRect1.y))
        self.interfaceExoSurface.blit(self.surfaceButton2, (self.ButtonRect2.x, self.ButtonRect2.y))
        self.interfaceExoSurface.blit(self.surfaceButton3, (self.ButtonRect3.x, self.ButtonRect3.y))


    def start(self) -> None:
        """Méthode de lancement de création de l'exercice. Appel unique par exo
        Input / Output : None"""
        
        # création exo -> liste de construction
        self.infosBuild = self.ObjExoChoix.Choix()
        # surface latex -> avec eqt
        self.latexSurface = self.ObjRender.GetElement(self.infosBuild[0]) # on donne l'eqt

        # réponse element placés aléatoirement
        self.bonneReponsePlace= randint(0,2)
        self.listeReponse = [self.infosBuild[2], self.infosBuild[3]]
        self.listeReponse.insert(self.bonneReponsePlace, self.infosBuild[1]) # ajout à la place déterminé


    def Win(self) -> None:
        """Méthode d'action si la réponse est juste
        Input / Output : None"""

        INFOS["ExoPasse"] = True

    def Loose(self) -> None:
        """Méthode d'action si la réponse est FAUSE
        Input / Output : None"""

        INFOS["ExoPasse"] = False

    def CloseInterface(self) -> None:
        """Méthode de fermeture de l'interface. Input / Output : None"""

        # changement des boolean de check
        self.gestionnaire.INTERFACE_OPEN = False
        self.gestionnaire.interface_exo = False
        INFOS["Exo"] = False


    def Update(self, event : any) -> None:
        """Méthode d'update général pour l'exercice interface, et de gestion de réponse (clic)
        Input : event (pygame
        Output : None)"""

        #setup de l'interface
        self.interfaceExoSurface.fill("#ffffff")
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceExoSurface, (320,180))

        # Gestion des clics de souris
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time

                # Coordonnées globales de l'événement
                global_pos = event.pos  # Coordonnées globales dans la fenêtre

                # Rect global de la surface de l'interface
                surface_rect = pygame.Rect(320, 180, self.interfaceExoSurface.get_width(), self.interfaceExoSurface.get_height())

                # Vérifiez si le clic est sur l'interface
                if surface_rect.collidepoint(global_pos):
                    # Convertissez en coordonnées locales
                    local_pos = (global_pos[0] - surface_rect.x, global_pos[1] - surface_rect.y)

                    # Vérifiez si le clic est sur un btn
                    if self.ButtonRect1.collidepoint(local_pos):
                        if self.bonneReponsePlace== 0:
                            self.Win()
                        else:
                            self.Loose()
                        self.CloseInterface()

                    elif self.ButtonRect2.collidepoint(local_pos):
                        if self.bonneReponsePlace== 1:
                            self.Win()
                        else:
                            self.Loose()
                        self.CloseInterface()

                    
                    elif self.ButtonRect3.collidepoint(local_pos):
                        if self.bonneReponsePlace== 2:
                            self.Win()
                        else:
                            self.Loose()
                        self.CloseInterface()
