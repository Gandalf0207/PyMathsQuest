import pygame.locals
from settings import *
from SourcesFichiers.Elements.sprites import *
from SourcesFichiers.Personnages.pnj import *

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
        elif self.gestionnaire.pnjActuel == "PNJ5" and NIVEAU["Map"] == "NiveauBaseFuturiste" and PNJ["PNJ4"] and not self.gestionnaire.pnjObj.discussion :
            self.loadText(1)
        elif self.gestionnaire.pnjActuel == "PNJ3" and PNJ["PNJ2"] and NIVEAU["Map"] == "NiveauMordor":
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
                self.gestionnaire.gestionSound.Dialogue(self.compteurDialogue, self.gestionnaire.pnjActuel)
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
                        INFOS["GetCours"] +=1
                        self.gestionnaire.CinematiqueBuild() # préparation au lancement cinematique
                    elif self.gestionnaire.pnjActuel == "PNJ2":
                        INVENTORY["Planks"] += 1
                        PNJ["PNJ2"] = True
                        INFOS["GetCours"] +=1
                        STATE_HELP_INFOS[0] = "BuildBridge"
                    elif self.gestionnaire.pnjActuel == "PNJ3":
                        INVENTORY["Pickaxe"] += 1
                        PNJ["PNJ3"] = True
                        INFOS["GetCours"] +=1
                        STATE_HELP_INFOS[0] = "MineRock"

                if NIVEAU["Map"] == "NiveauMedievale": 
                    if self.gestionnaire.pnjActuel == "PNJ1":
                        PNJ["PNJ1"] = True
                        INFOS["GetCours"] +=1
                        STATE_HELP_INFOS[0] = "BuildBridge"
                    elif self.gestionnaire.pnjActuel == "PNJ2":
                        PNJ["PNJ2"] = True
                        STATE_HELP_INFOS[0] = "FindWell"
                    elif self.gestionnaire.pnjActuel == "PNJ3":
                        PNJ["PNJ3"] = True
                        INVENTORY["Key"] += 1
                        INFOS["GetCours"] +=1
                        STATE_HELP_INFOS[0] = "OpenDoor"
                    elif self.gestionnaire.pnjActuel == "PNJ4":
                        INFOS["GetCours"] +=1
                        self.gestionnaire.CinematiqueBuild() # préparation au lancement cinematique

                if NIVEAU["Map"] == "NiveauBaseFuturiste":
                    if self.gestionnaire.pnjActuel == "PNJ1":
                        PNJ["PNJ1"] = True
                        INFOS["GetCours"] +=1
                        STATE_HELP_INFOS[0] = "UseVent"

                    elif self.gestionnaire.pnjActuel == "PNJ2":
                        PNJ["PNJ2"] = True
                        STATE_HELP_INFOS[0] = "Electricity"

                    elif self.gestionnaire.pnjActuel == "PNJ3":
                        INFOS["GetCours"] +=1
                        PNJ["PNJ3"] = True
                        
                        if PNJ["PNJ4"]:
                            STATE_HELP_INFOS[0] = "SeePNJ4"
                        else:
                            STATE_HELP_INFOS[0] = "SeePNJ3"

                        # tp pnj 
                        self.gestionnaire.gestionnaire.fondu_au_noir()
                        self.gestionnaire.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["PiloteMoveCafet"])
                        allPNJCoords =  LoadJsonMapValue("coordsMapObject", "PNJ Coords")
                        pnjPiloteCoords = allPNJCoords[4]
                        pos = (pnjPiloteCoords[0]*CASEMAP + 64, pnjPiloteCoords[1]*CASEMAP + 64) # calcul coords pygame
                        self.gestionnaire.pnjObj.kill()
                        PNJOBJ(pos, "PNJ5", (self.gestionnaire.gestionnaire.allSprites, self.gestionnaire.gestionnaire.collisionSprites, self.gestionnaire.allPNJ))
                        self.gestionnaire.gestionnaire.ouverture_du_noir(self.gestionnaire.gestionnaire.player.rect.center)


                    elif self.gestionnaire.pnjActuel == "PNJ4":
                        PNJ["PNJ4"] = True
                        INFOS["GetCours"] +=1
                        if PNJ["PNJ3"]:
                            STATE_HELP_INFOS[0] = "SeePNJ4"
                        else:
                            STATE_HELP_INFOS[0] = "SeePNJ3"    


                    elif self.gestionnaire.pnjActuel == "PNJ5":
                        PNJ["PNJ5"] = True
                        INFOS["DemiNiveau"] = True      
                        STATE_HELP_INFOS[0] = "SeePNJ5"    

                    elif self.gestionnaire.pnjActuel == "PNJ6":
                            PNJ["PNJ6"] = True
                            self.gestionnaire.gestionnaire.fondu_au_noir()
                            self.gestionnaire.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["CrashVaisseau"])

                            # clear inventaire
                            INVENTORY["Pickaxe"] = 0
                            INVENTORY["OldAxe"] = 0
                            INVENTORY["Showel"] = 0


                            # remplacement des textures 
                            allSolModif = []
                            VitreSprite = None
                            PanelControlBloc = None
                            allSpritesEspace = []
                            for sprite in self.gestionnaire.gestionnaire.allSprites:
                                if sprite.id == "Vitre":
                                    VitreSprite = sprite
                                elif sprite.id == "ControlPanel":
                                    PanelControlBloc = sprite
                                elif sprite.id in ["Sol", "Sol2", "Sol3", "Sol4"]:
                                    allSpritesEspace.append(sprite)
                                elif sprite.id == "Sol1":
                                    allSolModif.append(sprite)

                            solModif = sample(allSolModif, (len(allSolModif)//randint(2,3)))

                            try :
                                vitre  = pygame.image.load(join("Image", "Obstacle", "VitreBroken.png")).convert_alpha()
                                sol = pygame.image.load(join("Image", "Sol", "SolMordor.png")).convert_alpha()
                                sol2 = pygame.image.load(join("Image", "Sol", "MordorSol2.png")).convert_alpha()
                                sol3 = pygame.image.load(join("Image", "Sol", "MordorSol3.png")).convert_alpha()

                                solV2 = pygame.image.load(join("Image", "Sol", "SolMordorV2.png")).convert_alpha()
                                sol2V2 = pygame.image.load(join("Image", "Sol", "MordorSol2V2.png")).convert_alpha()
                                sol3V2= pygame.image.load(join("Image", "Sol", "MordorSol3V2.png")).convert_alpha()
                                obstacle = pygame.image.load(join("Image", "Obstacle", "HugeRock.png")).convert_alpha()
                                solVaisseau = pygame.image.load(join("Image", "Sol", "FloorVaisseauBroken.png"))

                                # sol vaisseau
                                for sprite in solModif:
                                    pos = sprite.pos
                                    sprite.kill()
                                    Sprites(pos, solVaisseau, "Sol1", self.gestionnaire.gestionnaire.allSprites, layer=0)
                                
                                # vitre
                                sprite = VitreSprite
                                pos = sprite.pos
                                sprite.kill()
                                CollisionSprites(pos, vitre, "Vitre", ((self.gestionnaire.gestionnaire.allSprites, self.gestionnaire.gestionnaire.collisionSprites)))

                                # panel bloc
                                sprite = PanelControlBloc
                                pos = sprite.pos
                                sprite.kill()
                                path = join("Image", "Obstacle", "VaisseauControlPanelBroken")
                                AnimatedCollisionSprites(pos,path, "TableauDeBord",  (self.gestionnaire.gestionnaire.allSprites, self.gestionnaire.gestionnaire.collisionSprites), layer=2)

                                # sol
                                for sprite in allSpritesEspace:
                                    pos = sprite.pos
                                    sprite.kill()
                                    if randint(1, 2) == 1:
                                        x = randint(1, 100)
                                        if x < 70 :
                                            Sprites(pos, sol, "Sol", self.gestionnaire.gestionnaire.allSprites, layer=0)
                                        elif x < 90:
                                            Sprites(pos, sol2, "Sol2", self.gestionnaire.gestionnaire.allSprites, layer=0)
                                        else:
                                            Sprites(pos, sol3, "Sol3", self.gestionnaire.gestionnaire.allSprites, layer=0)
                                    else:
                                        x = randint(1, 100)
                                        if x < 70 :
                                            Sprites(pos, solV2, "Sol", self.gestionnaire.gestionnaire.allSprites, layer=0)
                                        elif x < 90:
                                            Sprites(pos, sol2V2, "Sol2", self.gestionnaire.gestionnaire.allSprites, layer=0)
                                        else:
                                            Sprites(pos, sol3V2, "Sol3", self.gestionnaire.gestionnaire.allSprites, layer=0)
                                    
                                    if randint(1, 100) < 25:
                                        CollisionSprites(pos, obstacle, "HugeRock", ((self.gestionnaire.gestionnaire.allSprites, self.gestionnaire.gestionnaire.collisionSprites)), layer=1)


                            
                            except:
                                INFOS["ErrorLoadElement"] = True

                            # remplacement du pnj
                            allPNJ = self.gestionnaire.allPNJ
                            for ObjPNJ in allPNJ:
                                pos = ObjPNJ.pos
                                pos = (pos[0]*CASEMAP + 64, pos[1]*CASEMAP + 64) # calcul coords pygame
                                ObjPNJ.kill()
                                PNJOBJ(pos, "PNJ7", (self.gestionnaire.allPNJ, self.gestionnaire.gestionnaire.allSprites, self.gestionnaire.gestionnaire.collisionSprites) )

                            self.gestionnaire.gestionnaire.ouverture_du_noir(self.gestionnaire.gestionnaire.player.rect.center)
                            STATE_HELP_INFOS[0] = "SeePNJ6"
                            

                    elif self.gestionnaire.pnjActuel == "PNJ7":
                        INFOS["GetCours"] +=1
                        PNJ["PNJ7"] = True
                        STATE_HELP_INFOS[0] = "EscapeVaisseau"

                if NIVEAU["Map"] == "NiveauMordor":
                    if self.gestionnaire.pnjActuel == "PNJ1":
                        INFOS["GetCours"] +=1
                        PNJ["PNJ1"] = True
                        
                        #animation 
                        self.gestionnaire.gestionnaire.fondu_au_noir()
                        self.gestionnaire.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["GoPrison"])

                        player = self.gestionnaire.gestionnaire.player
                        # deplacement player
                        player.hitbox_rect.center = (71*CASEMAP + 64, 1*CASEMAP + 64) # +64 center case à coté
                        player.rect.center = player.hitbox_rect.center

                        self.gestionnaire.gestionnaire.ouverture_du_noir(player.rect.center)

                        STATE_HELP_INFOS[0] = "PotParchemin"
                    
                    if self.gestionnaire.pnjActuel == "PNJ2":
                        INFOS["GetCours"] +=1
                        PNJ["PNJ2"] = True
                        STATE_HELP_INFOS[0] = "SeePNJ2avant" # update tips player

                        self.gestionnaire.FollowBuild() # préparation au follow du pnj

                    if self.gestionnaire.pnjActuel == "PNJ3":
                        INFOS["GetCours"] +=1
                        PNJ["PNJ3"] = True # update
                        self.gestionnaire.gestionnaire.fondu_au_noir()
                        self.gestionnaire.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["KillPNJ3"])
                        self.gestionnaire.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["LeavePNJ2"])
                        STATE_HELP_INFOS[0] = "OpenDoorPrison" # update tips player

                        self.gestionnaire.pnjObj.kill()

                        # kill pnj + stop follow
                        for pnjObj in self.gestionnaire.allPNJ:
                            if pnjObj.numPNJ == "PNJ2":
                                self.gestionnaire.EndFollow()
                                pnjObj.kill()

                    if self.gestionnaire.pnjActuel == "PNJ4":
                        INFOS["GetCours"] +=1
                        PNJ["PNJ4"] = True
                        STATE_HELP_INFOS[0] = "OpenVolcan" # update tips player
                    
                    if self.gestionnaire.pnjActuel == "PNJ5":
                        PNJ["PNJ5"] = True

                        INFOS["Exo"] = True # lancement exo dans main (changement variable)
                        self.gestionnaire.gestionnaire.fondu_au_noir()
                        self.gestionnaire.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["MakeExo"]) # text animation
                        



        else:
            try :
                # get dialogue deja vu
                if self.compteurDialogue <= self.nombreDialogue:
                    self.pnj_text = TEXTE["Dialogues"][NIVEAU["Map"]][self.gestionnaire.pnjActuel]["Alternatif"][f"Dialogue{self.compteurDialogue}"]
                    self.gestionnaire.gestionSound.Dialogue(self.compteurDialogue,self.gestionnaire.pnjActuel)
                    self.compteurDialogue += 1 # passage au dialogue suivant
                else:
                    # gestion son
                    self.gestionnaire.gestionSound.StopDialogue()
                    self.CloseInterface() # fermeture interface

                    # ouverture automatique interface
                    if NIVEAU["Map"] == "NiveauMordor" and INFOS["DemiNiveau"]:
                        INFOS["Exo"] = True # lancement exo dans main (changement variable)
                        self.gestionnaire.gestionnaire.fondu_au_noir()
                        self.gestionnaire.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["MakeExo"]) # text animation
                    
                    if NIVEAU["Map"] == "NiveauMordor" and self.gestionnaire.pnjActuel == "PNJ1": # remise en place du tp si nécessaire
                        #animation 
                        self.gestionnaire.gestionnaire.fondu_au_noir()
                        self.gestionnaire.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["GoPrison"])

                        player = self.gestionnaire.gestionnaire.player
                        # deplacement player
                        player.hitbox_rect.center = (71*CASEMAP + 64, 1*CASEMAP + 64) # +64 center case à coté
                        player.rect.center = player.hitbox_rect.center

                        self.gestionnaire.gestionnaire.ouverture_du_noir(player.rect.center)




            except:
                self.CloseInterface() # fermeture interface # sécurité
    def loadPNG(self) -> None:
        """Méthode de chargement des images.
        Input / Output : None"""
        try :
            self.pnjImage = pygame.image.load(join("Image", "NPC", NIVEAU["Map"], self.gestionnaire.pnjActuel, f"Grand{self.gestionnaire.pnjActuel}.png")).convert_alpha()
            self.playerImage = pygame.image.load(join("Image", "Player", "GrandPlayer.png")).convert_alpha()
        except:
            INFOS["ErrorLoadElement"] = True

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

        # box petite question
        if self.gestionnaire.pnjActuel == "PNJ3" and NIVEAU["Map"] == "NiveauMedievale" and not self.gestionnaire.pnjObj.QuestionDone:
            self.surfaceBtnOui = pygame.Surface((128,50))
            self.surfaceBtnNon = pygame.Surface((128,50))
            self.surfaceBtnOui.fill("#ffffff")
            self.surfaceBtnNon.fill("#ffffff")

            self.rectBtnOui = pygame.Rect(WINDOW_WIDTH-178, 575, 128, 50)
            self.rectBtnNon = pygame.Rect(WINDOW_WIDTH-178, 650, 128, 50)

            self.textO = TEXTE["Elements"]["InterfacePNJ"]["Oui"]
            self.textN = TEXTE["Elements"]["InterfacePNJ"]["Non"]

            self.textOui = FONT["FONT36"].render(self.textO, True, (10,10,10))
            self.textNon = FONT["FONT36"].render(self.textN, True, (10,10,10))

            self.surfaceBtnOui.blit(self.textOui, self.textOui.get_rect(center=(self.surfaceBtnOui.get_width()//2, self.surfaceBtnOui.get_height()//2)))
            self.surfaceBtnNon.blit(self.textNon, self.textNon.get_rect(center=(self.surfaceBtnNon.get_width()//2, self.surfaceBtnNon.get_height()//2)))

            self.interfaceSurface.blit(self.surfaceBtnOui, (self.rectBtnOui.x, self.rectBtnOui.y))
            self.interfaceSurface.blit(self.surfaceBtnNon, (self.rectBtnNon.x, self.rectBtnNon.y))

        else:

            # load btn skip / lancer
            self.surfaceBtnSkip = pygame.Surface((128,50))
            self.btnRectSkip = pygame.Rect(WINDOW_WIDTH-178,600,128,50)
            self.surfaceBtnSkip.fill((255,255,255))
            self.textS = TEXTE["Elements"]["InterfacePNJ"]["SkipButton"]
            self.textSkip = FONT["FONT36"].render(self.textS, True, (10,10,10))
            self.surfaceBtnSkip.blit(self.textSkip, self.textSkip.get_rect(center=(self.surfaceBtnSkip.get_width()//2, self.surfaceBtnSkip.get_height()//2)))
            self.interfaceSurface.blit(self.surfaceBtnSkip, (self.btnRectSkip.x, self.btnRectSkip.y))



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
                
                elif self.gestionnaire.pnjActuel == "PNJ5" and NIVEAU["Map"] == "NiveauBaseFuturiste" and not PNJ["PNJ4"]:
                    self.CloseInterface()
                    STATE_HELP_INFOS[0] = "SeePNJ"    


                elif self.gestionnaire.pnjActuel == "PNJ3" and not PNJ["PNJ2"] and NIVEAU["Map"] == "NiveauMordor":
                    self.CloseInterface()
                    STATE_HELP_INFOS[0] = "SeePNJ2avant" # update tips player


                else:
                    # Vérifiez si le clic est dans le rectangle du bouton
                    if self.btnRectSkip.collidepoint(event.pos):
                        self.loadText() # pasage au dialogue suivant
                        self.BuildInterface() # build des éléments

        if event.type == pygame.MOUSEMOTION:
            if self.gestionnaire.pnjActuel == "PNJ3" and NIVEAU["Map"] == "NiveauMedievale" and not self.gestionnaire.pnjObj.QuestionDone:
                if self.rectBtnNon.collidepoint(event.pos) or self.rectBtnOui.collidepoint(event.pos):
                    INFOS["Hover"] = True 
                else:
                    INFOS["Hover"] = False
            else:
                if self.btnRectSkip.collidepoint(event.pos):
                    INFOS["Hover"] = True 
                else:
                    INFOS["Hover"] = False


                


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
                elif self.gestionnaire.pnjActuel == "PNJ5" and NIVEAU["Map"] == "NiveauBaseFuturiste" and not PNJ["PNJ4"]:
                    self.CloseInterface()
                    STATE_HELP_INFOS[0] = "SeePNJ"    

                elif self.gestionnaire.pnjActuel == "PNJ3" and not PNJ["PNJ2"] and NIVEAU["Map"] == "NiveauMordor":
                    self.CloseInterface()
                    STATE_HELP_INFOS[0] = "SeePNJ2avant" # update tips player


                else:
                    self.loadText()
                    self.BuildInterface()   