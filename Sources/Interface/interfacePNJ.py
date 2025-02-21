from settings import *
from Sources.Personnages.pnj import *

class PNJInterface(object):

    def __init__(self, gestionnaire : any) -> None:
        """Méthode initialisation de l'interface de discussion avec les pnj.
        Input : gestionnaire (self class d'appel), Output : None."""

        # Initialisation
        self.gestionnaire = gestionnaire
        
        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale

        # Surface pour le fond transparent
        self.backgroundSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.backgroundSurface.fill((50, 50, 50, 200))  # Fond gris avec alpha (200)

        # Surface principale pour les éléments de l'interface
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.interfaceSurface.fill((0, 0, 0, 0))  # Transparent par défaut

        # Position du PNJ
        self.pnj_position = (100, 100)  # Position du PNJ (à gauche)

        # Variables pour le texte du pnj
        self.pnj_text = None
        self.pnj_displayed_text = ""  # Texte affiché du PNJ
        self.pnj_index = 0  # Index pour le texte du PNJ
        self.compteurDialogue = 1
        self.nombreDialogue = len(TEXTE["Dialogues"][NIVEAU["Map"]][self.gestionnaire.pnjActuel]["Principal"]) if not self.gestionnaire.pnjObj.discussion else len(TEXTE["Dialogues"][NIVEAU["Map"]][self.gestionnaire.pnjActuel]["Alternatif"])

        # timer click skip
        self.last_click_time = 0
        self.click_delay = 500    

        # chargement des éléments autre
        self.loadPNG()

        if self.gestionnaire.pnjObj.QuestionDone and not self.gestionnaire.pnjObj.discussion: # add 1 : skp dialogue question
            self.loadText(1)
        else:
            self.loadText()
        


    def loadText(self, skipDialogueQuestion = 0 ) -> None:
        """Méthode de chargement des dialogues en fontion du pnj et du niveau et de l'avancement de discussion. 
        Input / Output : None"""

        # variables de base
        self.pnj_displayed_text = ""
        self.pnj_index = 0

        # chargement au dialogue suivant si on a dejé faitune qustions
        self.compteurDialogue += skipDialogueQuestion

        # check déjà discuter avec pnj
        if not self.gestionnaire.pnjObj.discussion:
            # chargement du texte
            if self.compteurDialogue <= self.nombreDialogue:
                self.pnj_text = TEXTE["Dialogues"][NIVEAU["Map"]][self.gestionnaire.pnjActuel]["Principal"][f"Dialogue{self.compteurDialogue}"]
                self.gestionnaire.gestionSound.Dialogue(self.compteurDialogue)
                self.compteurDialogue += 1 # passage au dialogue suivant
            else:
                # gestion son
                self.gestionnaire.gestionSound.StopDialogue()

                self.gestionnaire.Vu() # bool de check passage
                self.CloseInterface() # fermeture interface

                # action après discussions
                if NIVEAU["Map"] == "NiveauPlaineRiviere":
                    if self.gestionnaire.pnjActuel == "PNJ1":
                        INVENTORY["OldAxe"] += 1
                        self.gestionnaire.CinematiqueBuild() # préparation au lancement cinematique
                    elif self.gestionnaire.pnjActuel == "PNJ2":
                        INVENTORY["Planks"] += 1
                        PNJ["PNJ2"] = True
                        STATE_HELP_INFOS[0] = "BuildBridge"
                    elif self.gestionnaire.pnjActuel == "PNJ3":
                        INVENTORY["Pickaxe"] += 1
                        PNJ["PNJ3"] = True
                        STATE_HELP_INFOS[0] = "MineRock"

                if NIVEAU["Map"] == "NiveauMedievale": 
                    if self.gestionnaire.pnjActuel == "PNJ1":
                        PNJ["PNJ1"] = True
                        INVENTORY["Showel"] += 1
                        STATE_HELP_INFOS[0] = "BuildBridge"
                    elif self.gestionnaire.pnjActuel == "PNJ2":
                        PNJ["PNJ2"] = True
                        STATE_HELP_INFOS[0] = "FindWell"
                    elif self.gestionnaire.pnjActuel == "PNJ3":
                        PNJ["PNJ3"] = True
                        INVENTORY["Key"] += 1
                        STATE_HELP_INFOS[0] = "OpenDoor"
                    elif self.gestionnaire.pnjActuel == "PNJ4":
                        self.gestionnaire.CinematiqueBuild() # préparation au lancement cinematique

                if NIVEAU["Map"] == "NiveauBaseFuturiste":
                    if self.gestionnaire.pnjActuel == "PNJ1":
                        PNJ["PNJ1"] = True

                    elif self.gestionnaire.pnjActuel == "PNJ2":
                        PNJ["PNJ2"] = True

                    elif self.gestionnaire.pnjActuel == "PNJ3":
                        PNJ["PNJ3"] = True
                        # tp pnj 
                        self.gestionnaire.gestionnaire.fondu_au_noir()
                        self.gestionnaire.gestionnaire.textScreen("")
                        allPNJCoords =  LoadJsonMapValue("coordsMapObject", "PNJ Coords")
                        pnjPiloteCoords = allPNJCoords[4]
                        pos = (pnjPiloteCoords[0]*CASEMAP + 64, pnjPiloteCoords[1]*CASEMAP + 64) # calcul coords pygame
                        self.gestionnaire.pnjObj.kill()
                        PNJOBJ(pos, "PNJ5", (self.gestionnaire.gestionnaire.allSprites, self.gestionnaire.gestionnaire.collisionSprites, self.gestionnaire.allPNJ))
                        self.gestionnaire.gestionnaire.ouverture_du_noir(self.gestionnaire.gestionnaire.player.rect.center)


                    elif self.gestionnaire.pnjActuel == "PNJ4":
                        PNJ["PNJ4"] = True

                    elif self.gestionnaire.pnjActuel == "PNJ5":
                        PNJ["PNJ5"] = True



        else:
            # get dialogue deja vu
            if self.compteurDialogue <= self.nombreDialogue:
                self.pnj_text = TEXTE["Dialogues"][NIVEAU["Map"]][self.gestionnaire.pnjActuel]["Alternatif"][f"Dialogue{self.compteurDialogue}"]
                self.gestionnaire.gestionSound.Dialogue(self.compteurDialogue)
                self.compteurDialogue += 1 # passage au dialogue suivant
            else:
                # gestion son
                self.gestionnaire.gestionSound.StopDialogue()
                self.CloseInterface() # fermeture interface


    def loadPNG(self) -> None:
        """Méthode de chargement des images.
        Input / Output : None"""
        
        self.pnjImage = pygame.image.load(join("Images", "PNJ", "Discussion", f"Grand{self.gestionnaire.pnjActuel}.png")).convert_alpha()
        self.playerImage = pygame.image.load(join("Images", "Player", "Discussion", "GrandPlayer.png")).convert_alpha()


    def BuildInterface(self) -> None:
        """Méthode de création des éléments de l'interface de discussion avec le pnj. 
        Input / Output : None"""
        self.interfaceSurface.fill((0, 0, 0, 0))  # Réinitialiser la surface avec une transparence complète

        # load element png
        self.interfaceSurface.blit(self.pnjImage, (50,360))
        self.interfaceSurface.blit(self.playerImage, (WINDOW_WIDTH-178, 360))

        # load nom pnj + creation text du nom
        self.pnjName = TEXTE["Dialogues"][NIVEAU["Map"]][self.gestionnaire.pnjActuel]["Nom"]
        pnjName = FONT["FONT36B"].render(self.pnjName, True, (255,255,255))
        self.interfaceSurface.blit(pnjName, (200, 400))

        # box petite question
        if self.gestionnaire.pnjActuel == "PNJ3" and NIVEAU["Map"] == "NiveauMedievale" and not self.gestionnaire.pnjObj.QuestionDone:
            self.surfaceBtnOui = pygame.Surface((75,50))
            self.surfaceBtnNon = pygame.Surface((75,50))

            self.rectBtnOui = pygame.Rect(800, 600, 75, 50)
            self.rectBtnNon = pygame.Rect(1000, 600, 75, 50)

            self.textO = TEXTE["Elements"]["InterfacePNJ"]["Oui"]
            self.textN = TEXTE["Elements"]["InterfacePNJ"]["Non"]

            self.textOui = FONT["FONT36"].render(self.textO, True, (10,10,10))
            self.textNon = FONT["FONT36"].render(self.textN, True, (10,10,10))

            self.surfaceBtnOui.blit(self.textOui, (0,0))
            self.surfaceBtnNon.blit(self.textNon, (0,0))

            self.interfaceSurface.blit(self.surfaceBtnOui, (self.rectBtnOui.x, self.rectBtnOui.y))
            self.interfaceSurface.blit(self.surfaceBtnNon, (self.rectBtnNon.x, self.rectBtnNon.y))


        else:

            # load btn skip / lancer
            self.surfaceBtnSkip = pygame.Surface((100,50))
            self.btnRectSkip = pygame.Rect(750,600,100,50)
            self.surfaceBtnSkip.fill((255,255,255))
            self.textS = TEXTE["Elements"]["InterfacePNJ"]["SkipButton"]
            self.textSkip = FONT["FONT36"].render(self.textS, True, (10,10,10))
            self.surfaceBtnSkip.blit(self.textSkip, (0,0))
            self.interfaceSurface.blit(self.surfaceBtnSkip, (self.btnRectSkip.x, self.btnRectSkip.y))


        # bloc gestion texte 
        if self.pnj_index < len(self.pnj_text):
            self.pnj_index += 1
        # Mettre à jour le texte affiché
        self.pnj_displayed_text = self.pnj_text[:self.pnj_index]


        # Largeur maximale de la boîte de texte
        max_width = 500
        wrapped_lines = wrap_text(self.pnj_displayed_text,FONT["FONT36"], max_width)

        # Affichage des lignes
        y_offset = 420  # Position Y de départ
        line_height = FONT["FONT36"].size("Tg")[1]  # Hauteur d'une ligne
        for i, line in enumerate(wrapped_lines):
            line_surface = FONT["FONT36"].render(line, True, (255, 255, 255))
            self.interfaceSurface.blit(line_surface, (200, y_offset + i * line_height))

    def CloseInterface(self):
        self.gestionnaire.gameInterfaces.CloseAllInterface()

    def Update(self, event : any) -> None:
        """Méthode d'update de l'interface de discussion.
        Input : event = (element pygame), Output : None"""

        # Dessiner le fond transparent
        self.displaySurface.blit(self.backgroundSurface, (0, 0))

        # Construire et afficher l'interface avec le texte
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (0, 0))

        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()


        # Vérifie si l'événement est un clic de souris (bouton skip)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time

                if self.gestionnaire.pnjActuel == "PNJ3" and NIVEAU["Map"] == "NiveauMedievale" and not self.gestionnaire.pnjObj.QuestionDone:
                    if self.rectBtnOui.collidepoint(event.pos):
                        self.gestionnaire.pnjObj.QuestionDone =True
                        self.loadText() # pasage au dialogue suivant
                        self.BuildInterface() # build des éléments
                    
                    if self.rectBtnNon.collidepoint(event.pos):
                        self.CloseInterface()
                else:
                    # Vérifiez si le clic est dans le rectangle du bouton
                    if self.btnRectSkip.collidepoint(event.pos):
                        self.loadText() # pasage au dialogue suivant
                        self.BuildInterface() # build des éléments


        # touche espace skip des dialogues
        if keys[KEYSBIND["skip"]] : 
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time

                # pnj question avant interaction
                if  self.gestionnaire.pnjActuel == "PNJ3" and NIVEAU["Map"] == "NiveauMedievale":
                    if self.gestionnaire.pnjObj.QuestionDone: # condition spécifique
                        self.loadText()
                        self.BuildInterface()   
                else:
                    self.loadText()
                    self.BuildInterface()   