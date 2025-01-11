from settings import *
from Sources.Exos.choixExo import *
from Sources.Exos.renderLatex import *

class CreateExo:
    def __init__(self, gestionnaire):

        self.gestionnaire = gestionnaire

        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceExoSurface = pygame.Surface((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),  pygame.SRCALPHA)
        self.interfaceExoSurface.fill("#ffffff")

        self.ObjRender = RenderLatex()
        self.ObjExoChoix = GetExo()

        self.latexSurface = None

        self.font = pygame.font.Font(None, 30)
        self.font2 = pygame.font.Font(None, 22)

        self.last_click_time = 0
        self.click_delay = 300

        self.indexTexte = 0

        self.CreateRectButton()

    def CreateRectButton(self):
        self.surfaceButton1 = pygame.Surface((100,100))
        self.surfaceButton2 = pygame.Surface((100,100))
        self.surfaceButton3 = pygame.Surface((100,100))

         # Positions des boutons, 
        self.ButtonRect1 =pygame.Rect(68, WINDOW_HEIGHT/2 - 120, 100, 100) 
        self.ButtonRect2 = pygame.Rect(236, WINDOW_HEIGHT/2 - 120, 100, 100)
        self.ButtonRect3 = pygame.Rect(404, WINDOW_HEIGHT/2 -120, 100, 100)

    def BuildInterface(self):
        self.interfaceExoSurface.fill("#ffffff")

        # titre
        textTitre = self.font.render(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["ExoTexte"]["Title"], True, (0, 0, 0))
        self.interfaceExoSurface.blit(textTitre, (10, 10))

        # consigne
        self.textConsigne = TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["ExoTexte"][f"Difficulte{INFOS["Difficulte"]}"]["Consigne"]

        if self.indexTexte < len(self.textConsigne):
            self.indexTexte += 1
        # Mettre à jour le texte affiché
        self.displayed_text = self.textConsigne[:self.indexTexte]

        # Fonction simple pour découper le texte
        def wrap_text(text, font, max_width):
            words = text.split(' ')
            lines = []
            current_line = ''

            for word in words:
                test_line = f"{current_line} {word}".strip()
                if font.size(test_line)[0] <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word
            if current_line:
                lines.append(current_line)
            return lines

        max_width = 650
        wrapped_lines = wrap_text(self.displayed_text, self.font, max_width)

        # Affichage des lignes
        y_offset =  60 # Position Y de départ
        line_height = self.font2.size("Tg")[1]  # Hauteur d'une ligne
        for i, line in enumerate(wrapped_lines):
            line_surface = self.font2.render(line, True, (0,0,0))
            self.interfaceExoSurface.blit(line_surface, (20, y_offset + i * line_height))
        

        # équation
        self.interfaceExoSurface.blit(self.latexSurface, (10, 100))

        # réponse titre
        self.textQCM = self.font2.render(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["ExoTexte"]["DifficulteTrue"]["QCM"], True, (0, 0, 0))
        self.interfaceExoSurface.blit(self.textQCM, (10, WINDOW_HEIGHT/2 - 150))


        self.textR1 = self.font2.render(str(self.listeReponse[0]), True, (0,0,0))
        self.textR2 = self.font2.render(str(self.listeReponse[1]), True, (0,0,0))
        self.textR3 = self.font2.render(str(self.listeReponse[2]), True, (0,0,0))

        self.surfaceButton1.fill((200,205,205))
        self.surfaceButton2.fill((200,205,205))
        self.surfaceButton3.fill((200,205,205))

        self.surfaceButton1.blit(self.textR1, (0,0))
        self.surfaceButton2.blit(self.textR2, (0,0))
        self.surfaceButton3.blit(self.textR3, (0,0))

        self.interfaceExoSurface.blit(self.surfaceButton1, (self.ButtonRect1.x, self.ButtonRect1.y))
        self.interfaceExoSurface.blit(self.surfaceButton2, (self.ButtonRect2.x, self.ButtonRect2.y))
        self.interfaceExoSurface.blit(self.surfaceButton3, (self.ButtonRect3.x, self.ButtonRect3.y))


    def start(self):
        self.infosBuild = self.ObjExoChoix.Choix()
        self.latexSurface = self.ObjRender.GetElement(self.infosBuild[0]) # on donne l'eqt

        # réponse element 
        self.bonneReponsePlace= randint(0,2)
        self.listeReponse = [self.infosBuild[2], self.infosBuild[3]]
        self.listeReponse.insert(self.bonneReponsePlace, self.infosBuild[1]) # ajout à la place déterminé


    def Win(self):
        INFOS["ExoPasse"] = True

    def Loose(self):
        INFOS["ExoPasse"] = False

    def CloseInterface(self) -> None:
        """Méthode de fermeture de l'interface. Input / Output : None"""

        # changement des boolean de check
        self.gestionnaire.INTERFACE_OPEN = False
        self.gestionnaire.interface_exo = False
        INFOS["Exo"] = False


    def Update(self, event):
        #fermeture interface dans main
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
