from settings import *
from SourcesFichiers.Elements.sprites import *
from SourcesFichiers.ExosCours.choixExo import *
from SourcesFichiers.ExosCours.renderLatex import *

class CreateExo:
    def __init__(self, gestionnaire : any) -> None:
        """Méthode d'initialisation des valeur pour la class de crétion des exercices
        Input : gestionnaire (self main class)
        Output : None"""

        self.gestionnaire = gestionnaire # self main

        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceExoSurface = pygame.Surface((WINDOW_WIDTH*(3/4), WINDOW_HEIGHT*(3/4)),  pygame.SRCALPHA)
        self.interfaceExoSurface.fill("#ffffff")

        # Surface pour le fond transparent
        self.backgroundSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.backgroundSurface.fill((50, 50, 50, 200))  # Fond gris avec alpha (200)

        # création obj pour la création d'exercice
        self.ObjRender = RenderLatex()
        self.ObjExoChoix = GetExo()

        # infos + variable utiles
        self.latexSurface = None
        self.last_click_time = 0
        self.click_delay = 300
        self.indexTexte = 0

        # hauteur x element 
        self.hauteurAct = 0

        # close interface cross
        self.surfaceCloseCross = pygame.Surface((24,24))
        self.isCrossCloseHover = False
        try :
            self.crossClose = pygame.image.load(join("Image", "Interface","Croix", "x-mark.png")).convert_alpha()
            self.crossClose2 = pygame.image.load(join("Image","Interface", "Croix", "x-mark2.png")).convert_alpha()
            self.btnTexture = pygame.image.load(join("Image","Interface", "Button", "Exo", "NonHover.png")).convert_alpha()
            self.btnTextureHover = pygame.image.load(join("Image","Interface", "Button", "Exo", "Hover.png")).convert_alpha()
        except:
            INFOS["ErrorLoadElement"] = True

        self.isBtn1Hover = False
        self.isBtn2Hover = False
        self.isBtn3Hover = False
        
        # création element button
        self.CreateRectButton()

    def CreateRectButton(self) -> None:
        """Mthode création des éléments pour les bouttons de réponse
        Inpur / Output : None"""

        # surface
        longueur, largeur = 253, 100

        self.surfaceButton1 = pygame.Surface((longueur, largeur))
        self.surfaceButton2 = pygame.Surface((longueur, largeur))
        self.surfaceButton3 = pygame.Surface((longueur, largeur))

         # Positions des boutons : element collision rect 
        self.ButtonRect1 = pygame.Rect(50, self.interfaceExoSurface.get_height() -125, longueur, largeur) 
        self.ButtonRect2 = pygame.Rect(353, self.interfaceExoSurface.get_height() -125, longueur, largeur)
        self.ButtonRect3 = pygame.Rect(656, self.interfaceExoSurface.get_height() -125, longueur, largeur)

    def BuildInterface(self) -> None:
        """Méthode ce construction de l'interface à chque rafraichissement
        Intput / Oupur : None"""
        self.hauteurAct = 0 # reset car update interface

        # clear
        self.interfaceExoSurface.fill("#ffffff")

        # titre
        textT = TEXTE["Elements"][NIVEAU["Map"]]["ExoTexte"][NIVEAU["Niveau"]]["Title"] if NIVEAU["Map"] != "NiveauMordor" else TEXTE["Elements"][NIVEAU["Map"]]["ExoTexte"][NIVEAU["Niveau"]][f"DemiNiveau{INFOS["DemiNiveau"]}"]["Title"]
        textTitre = FONT["FONT30"].render(textT, True, (0, 0, 0))
        self.interfaceExoSurface.blit(textTitre, (10, 10))
            # update hauteur
        heightText = FONT["FONT30"].size("TG")[1]
        self.hauteurAct += heightText + 10

        # consigne
        self.textConsigne = TEXTE["Elements"][NIVEAU["Map"]]["ExoTexte"][NIVEAU["Niveau"]][f"Difficulte{INFOS["Difficulte"]}"]["Consigne"] if NIVEAU["Map"] != "NiveauMordor" else TEXTE["Elements"][NIVEAU["Map"]]["ExoTexte"][NIVEAU["Niveau"]][f"DemiNiveau{INFOS["DemiNiveau"]}"][f"Difficulte{INFOS["Difficulte"]}"]["Consigne"]
        
        # Mettre à jour le texte affiché si nécessaire
        if self.indexTexte < len(self.textConsigne):
            self.indexTexte += 1
        self.displayed_text = self.textConsigne[:self.indexTexte]

        # Fonction simple pour découper le text
        max_width = self.interfaceExoSurface.get_width() - 50
        wrapped_lines = wrap_text(self.displayed_text, FONT["FONT22"], max_width)

        # Affichage des lignes
        self.hauteurAct +=  20 # Position Y de départ
        line_height = FONT["FONT22"].size("Tg")[1]  # Hauteur d'une ligne
        for i, line in enumerate(wrapped_lines):
            line_surface = FONT["FONT22"].render(line, True, (0,0,0))
            self.interfaceExoSurface.blit(line_surface, (20, self.hauteurAct))
            self.hauteurAct += line_height
        

        # équation affichage
        if NIVEAU["Niveau"] == "Seconde": # appel de la bonne méthode
            if NIVEAU["Map"] in ["NiveauPlaineRiviere", "NiveauMordor"]:
                if not INFOS["DemiNiveau"]:
                    self.hauteurAct += 120
                    self.interfaceExoSurface.blit(self.latexSurface, (self.latexSurface.get_rect(center = (self.interfaceExoSurface.get_width()//2, self.hauteurAct))))
                else:
                    self.hauteurAct += 20
                    textInfo = f"a : {self.infosBuild[0][2][4]} ; b :{self.infosBuild[0][2][5]} ; A : {self.infosBuild[0][2][0]}; B : {self.infosBuild[0][2][1]}, C : {self.infosBuild[0][2][2]} , D : {self.infosBuild[0][2][3]}"
                    text = FONT["FONT20"].render(textInfo, True, (0,0,0))
                    self.interfaceExoSurface.blit(text, (20, self.hauteurAct))

                    self.hauteurAct += 100
                    try :
                        self.exoBoss1Image = pygame.image.load(join("Image", "Exo", "ExoBoss1.png")).convert_alpha()
                        self.interfaceExoSurface.blit(self.exoBoss1Image, self.exoBoss1Image.get_rect(center = (self.interfaceExoSurface.get_width()//2, self.hauteurAct)))
                    except:
                        INFOS["ErrorLoadElement"] = True


            elif NIVEAU["Map"] == "NiveauMedievale":
                if not INFOS["Difficulte"]: # facile
                    self.hauteurAct += 20
                    textInfo = f"c : {self.infosBuild[0][0]} ; r :{self.infosBuild[0][1]} ; h : {self.infosBuild[0][2]}; d : {self.infosBuild[0][3]}"
                    text = FONT["FONT20"].render(textInfo, True, (0,0,0))
                    self.interfaceExoSurface.blit(text, (20, self.hauteurAct))

                    self.hauteurAct += 100
                    try :
                        self.volumeSimpleImg = pygame.image.load(join("Image", "Exo", "ExoVolumeSimple.png")).convert_alpha()
                        self.interfaceExoSurface.blit(self.volumeSimpleImg, self.volumeSimpleImg.get_rect(center = (self.interfaceExoSurface.get_width()//2, self.hauteurAct)))
                    except:
                        INFOS["ErrorLoadElement"] = True
                else:
                    self.hauteurAct += 20
                    textInfo = f"a = {self.infosBuild[0][0]} ; b = {self.infosBuild[0][1]} ; c = {self.infosBuild[0][2]} ; d = {self.infosBuild[0][3]} ; e = {self.infosBuild[0][4]} ; f = {self.infosBuild[0][5]} ; r = {self.infosBuild[0][6]}"
                    text = FONT["FONT20"].render(textInfo, True, (0,0,0))
                    self.interfaceExoSurface.blit(text, (20, self.hauteurAct))

                    self.hauteurAct += 100 
                    try :
                        self.volumeDifficileImg = pygame.image.load(join("Image", "Exo", "ExoVolumeDifficile.png")).convert_alpha()
                        self.interfaceExoSurface.blit(self.volumeDifficileImg, self.volumeDifficileImg.get_rect(center = (self.interfaceExoSurface.get_width()//2, self.hauteurAct)))
                    except:
                        INFOS["ErrorLoadElement"] = True    
            elif NIVEAU["Map"] == "NiveauBaseFuturiste":
                self.hauteurAct += 20
                textInfo = f"A : {self.infosBuild[0][1][0]} ; B :{self.infosBuild[0][1][1]} ; C : {self.infosBuild[0][1][2]}; D : {self.infosBuild[0][1][3]}"
                text = FONT["FONT20"].render(textInfo, True, (0,0,0))
                self.interfaceExoSurface.blit(text, (20, self.hauteurAct))
                self.hauteurAct += 150

                self.interfaceExoSurface.blit(self.infosBuild[0][0], self.infosBuild[0][0].get_rect(center = (self.interfaceExoSurface.get_width()//2, self.hauteurAct)))

        elif NIVEAU["Niveau"] == "Premiere":
            if NIVEAU["Map"] in ["NiveauMedievale", "NiveauBaseFuturiste"]:
                self.hauteurAct += 120
                self.interfaceExoSurface.blit(self.latexSurface, (self.latexSurface.get_rect(center = (self.interfaceExoSurface.get_width()//2, self.hauteurAct))))

        # réponse titre
        textQ = TEXTE["Elements"][NIVEAU["Map"]]["ExoTexte"][NIVEAU["Niveau"]][f"Difficulte{INFOS["Difficulte"]}"]["QCM"] if NIVEAU["Map"] != "NiveauMordor" else TEXTE["Elements"][NIVEAU["Map"]]["ExoTexte"][NIVEAU["Niveau"]][f"DemiNiveau{INFOS["DemiNiveau"]}"][f"Difficulte{INFOS["Difficulte"]}"]["QCM"]
        self.textQCM = FONT["FONT24"].render(textQ, True, (0, 0, 0))
        self.interfaceExoSurface.blit(self.textQCM, self.textQCM.get_rect(center=(self.interfaceExoSurface.get_width()//2, self.interfaceExoSurface.get_height()-150)))

        # réponse button
        self.surfaceButton1.fill((200,205,205))
        self.surfaceButton2.fill((200,205,205))
        self.surfaceButton3.fill((200,205,205))

        self.allReponseTexte = [str(self.listeReponse[0]),str(self.listeReponse[1]),str(self.listeReponse[2])]

        for textIndice in range(len(self.allReponseTexte)):
            
            #bcg btn
            if textIndice == 0:
                if self.isBtn1Hover:
                    self.surfaceButton1.blit(self.btnTextureHover, (0,0))
                else:
                    self.surfaceButton1.blit(self.btnTexture, (0,0))
            elif textIndice == 1:
                if self.isBtn2Hover:
                    self.surfaceButton2.blit(self.btnTextureHover, (0,0))
                else:
                    self.surfaceButton2.blit(self.btnTexture, (0,0))
            elif textIndice == 2:
                if self.isBtn3Hover:
                    self.surfaceButton3.blit(self.btnTextureHover, (0,0))
                else:
                    self.surfaceButton3.blit(self.btnTexture, (0,0))



            # Largeur et hauteur du bouton
            button_width = self.surfaceButton1.get_width()
            button_height = self.surfaceButton1.get_height()

            # Largeur max du texte à ne pas dépasser
            max_width = button_width - 10  # On enlève une marge de 5 pixels de chaque côté

            # Fonction simple pour découper le text
            wrapped_lines = wrap_text(self.allReponseTexte[textIndice], FONT["FONT24"], max_width)

            # Hauteur totale du texte
            line_height = FONT["FONT24"].size("Tg")[1]
            total_text_height = len(wrapped_lines) * line_height

            # Y de départ pour centrer verticalement
            y_offset = (button_height - total_text_height) // 2

            for i, line in enumerate(wrapped_lines):
                line_surface = FONT["FONT24"].render(line, True, (0,0,0))

                # X pour centrer horizontalement
                x = (button_width - line_surface.get_width()) // 2
                            
                if textIndice == 0:
                    self.surfaceButton1.blit(line_surface, (x, y_offset + i * line_height))
                elif textIndice == 1:
                    self.surfaceButton2.blit(line_surface, (x, y_offset + i * line_height))
                elif textIndice == 2:
                    self.surfaceButton3.blit(line_surface, (x, y_offset + i * line_height))

        self.interfaceExoSurface.blit(self.surfaceButton1, (self.ButtonRect1.x, self.ButtonRect1.y))
        self.interfaceExoSurface.blit(self.surfaceButton2, (self.ButtonRect2.x, self.ButtonRect2.y))
        self.interfaceExoSurface.blit(self.surfaceButton3, (self.ButtonRect3.x, self.ButtonRect3.y))



        # close element
        self.surfaceCloseCross.fill("#ffffff")
        self.rectCloseCross = pygame.Rect(self.interfaceExoSurface.get_width() - 34, 10, 24, 24)
        if self.isCrossCloseHover:
            self.surfaceCloseCross.blit(self.crossClose2, (0,0))
        else:
            self.surfaceCloseCross.blit(self.crossClose, (0,0))
        self.interfaceExoSurface.blit(self.surfaceCloseCross, (self.rectCloseCross.x, self.rectCloseCross.y))



    def start(self) -> None:
        """Méthode de lancement de création de l'exercice. Appel unique par exo
        Input / Output : None"""
        
        # création exo -> liste de construction
        self.infosBuild = self.ObjExoChoix.Choix()
        # surface latex -> avec eqt
        if NIVEAU["Niveau"] == "Seconde":
            if (NIVEAU["Map"] == "NiveauPlaineRiviere") or ( NIVEAU["Map"] == "NiveauMordor" and not INFOS["DemiNiveau"]):
                self.latexSurface = self.ObjRender.GetElement(self.infosBuild[0], 30) # on donne l'eqt

        elif NIVEAU["Niveau"] == "Premiere":
            if NIVEAU["Map"] in ["NiveauMedievale", "NiveauBaseFuturiste"]:
                self.latexSurface = self.ObjRender.GetElement(self.infosBuild[0], 30) # on donne l'eqt
            

        # réponse element placés aléatoirement
        self.bonneReponsePlace= randint(0,2)
        self.listeReponse = [self.infosBuild[2], self.infosBuild[3]]
        self.listeReponse.insert(self.bonneReponsePlace, self.infosBuild[1]) # ajout à la place déterminé


    def Win(self) -> None:
        """Méthode d'action si la réponse est juste
        Input / Output : None"""
        if (NIVEAU["Map"] != "NiveauMordor" and INFOS["DemiNiveau"]) or (NIVEAU["Map"] == "NiveauPlaineRiviere"):
            INFOS["ExoPasse"] = True
        elif NIVEAU["Map"] == "NiveauMordor" and not INFOS["DemiNiveau"]:
            INFOS["DemiNiveau"] = True
            INFOS["ExoPasse"] = False # on ne veux pas changer de niveau
            STATE_HELP_INFOS[0] = "SeePNJ" # update tips player
        else: # interaction pnj roi nv mrodor
            pygame.event.clear([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])  # Nettoyer les événements
            INFOS["CinematiqueEndAct"] = True # on lance la cinématique de fin (aucune action du player)

            self.gestionnaire.fondu_au_noir()
            text = TEXTE["Elements"][NIVEAU["Map"]]["KillRoi"]
            self.gestionnaire.textScreen(text)
            self.gestionnaire.cinematique = True

            for pnj in self.gestionnaire.allPNJ:
                if pnj.numPNJ == "PNJ5":
                    pos = (pnj.pos[0]*CASEMAP, pnj.pos[1]*CASEMAP)
                    pnj.kill()
                    path = join("Image", "AnimationKillRoi")
                    AnimatedSpritesUnique(pos, self.gestionnaire.allSprites, "KillRoi", path, layer = 1)
            INFOS["ExoPasse"] = False

        # add du total exo dans la gestion des interface (close)
        INFOS["ExoReussit"] += 1 


    def Loose(self) -> None:
        """Méthode d'action si la réponse est FAUSE
        Input / Output : None"""

        INFOS["ExoPasse"] = False

        pygame.event.clear([pygame.KEYDOWN, pygame.KEYUP])  # Nettoyer les événements


    def Update(self, event : any) -> None:
        """Méthode d'update général pour l'exercice interface, et de gestion de réponse (clic)
        Input : event (pygame
        Output : None)"""

        #setup de l'interface
        self.interfaceExoSurface.fill("#ffffff")
        self.BuildInterface()
        self.displaySurface.blit(self.backgroundSurface, (0,0))
        self.displaySurface.blit(self.interfaceExoSurface, (160,90))

        # Gestion des clics de souris
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time
                
                local_pos = GetLocalPos(event, self.interfaceExoSurface, (160, 90))
                if local_pos:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Vérifiez si le clic est sur un btn
                        if self.ButtonRect1.collidepoint(local_pos):
                            if self.bonneReponsePlace== 0:
                                self.Win()
                            else:
                                self.Loose()
                            self.gestionnaire.gameInterfaces.CloseAllInterface()

                        elif self.ButtonRect2.collidepoint(local_pos):
                            if self.bonneReponsePlace== 1:
                                self.Win()
                            else:
                                self.Loose()
                            self.gestionnaire.gameInterfaces.CloseAllInterface()

                        
                        elif self.ButtonRect3.collidepoint(local_pos):
                            if self.bonneReponsePlace== 2:
                                self.Win()
                            else:
                                self.Loose()
                            self.gestionnaire.gameInterfaces.CloseAllInterface()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.rectCloseCross.collidepoint(local_pos):
                                # fermeture interface
                                self.Loose()
                                self.gestionnaire.gameInterfaces.CloseAllInterface()

        if event.type == pygame.MOUSEMOTION:
            local_pos = GetLocalPos(event, self.interfaceExoSurface, (160, 90))
            if local_pos:
                # cross close interface
                if event.type == pygame.MOUSEMOTION:
                    check = False
                    self.isCrossCloseHover = self.rectCloseCross.collidepoint(local_pos)
                    self.isBtn1Hover = self.ButtonRect1.collidepoint(local_pos)
                    self.isBtn2Hover = self.ButtonRect2.collidepoint(local_pos)
                    self.isBtn3Hover = self.ButtonRect3.collidepoint(local_pos)

                    if self.isCrossCloseHover or self.isBtn1Hover or self.isBtn2Hover or self.isBtn3Hover:
                        check = True
                    INFOS["Hover"] = check   