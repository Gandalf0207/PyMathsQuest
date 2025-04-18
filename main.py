#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

from settings import *
from SourcesFichiers.Personnages.player import *
from SourcesFichiers.Elements.touche import *
from SourcesFichiers.Elements.interactions import *
from SourcesFichiers.Elements.groups import *
from SourcesFichiers.Map.loadMapGestion import *
from SourcesFichiers.Elements.hotbar import *
from SourcesFichiers.Personnages.pnj import *
from SourcesFichiers.Ressources.creationTexte import *
from SourcesFichiers.Elements.construire import *
from SourcesFichiers.Interface.Game.interfaceExo import *
from SourcesFichiers.Elements.sound import *
from SourcesFichiers.Interface.Game.gestionInterfaceGame import *
from SourcesFichiers.Elements.cinematique import *
from SourcesFichiers.Interface.Other.gestionInterfaceOther import *
from SourcesFichiers.Interface.Other.animationLancement import *
from SourcesFichiers.ExosCours.gestionCours import *


class Game(object):
    def __init__(self) -> None:
        """Méthode initialisation all settings du jeu en général (groupe, construction...)
        Input / Output : None"""

        # General setup
        pygame.init() # Initialisation de la fenetre pygame
        
        self.displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # taille fenetre
        self.displayCaption = pygame.display.set_caption(TEXTE["Elements"]["GameName"]) # titre fenetre
        self.running = True # stop de la fenetre
        self.clock = pygame.time.Clock() # dt

        # all groupes
        self.allSprites = AllSprites()
        self.collisionSprites = pygame.sprite.Group()
        self.allPNJ = pygame.sprite.Group()
        self.interactionsGroup = pygame.sprite.Group()
        
        # bool globaux : 
        self.demiNiveau = False
        self.ERROR_RELANCER = False
        self.checkLoadingDone = False
        self.checkCoursDone = False
 
        # clear json stockage value exos
        fichier = join("data", "exercicesValues.json")
        # Écrire un objet JSON vide
        with open(fichier, "w") as f:
            json.dump({}, f)

        #animation lancement
        self.animationLancement = AnimationLancementObj(self)
        threading.Thread(target=self.animationLancement.Update, daemon=True).start()
        self.animationLancementEnd = False

        self.gestionCours = GestionCours(self)

        # tool box
        self.GameTool = GameToolBox(self)
        self.GameTool.CreateFont()

        # interface home
        self.GestionInterfaceOther = GestionOtherInterface(self)



    # méthode de call de la class tool
    def ChargementEcran(self):
        """Chargement écran"""
        self.GameTool.ChargementEcran()

    def textScreen(self, text):
        """Texte sur l'écran"""
        self.GameTool.textScreen(text)

    def fondu_au_noir(self):
        """Fondu au noir screen"""
        self.GameTool.fondu_au_noir()

    def ouverture_du_noir(self, targetPos):
        """Ouverture au noir screen"""
        self.GameTool.ouverture_du_noir(targetPos)


    def SetupAllMap(self):
        """Méthode de création de tout les éléments pour le niveau / map
        Input / Output : None"""

        # Ssurface secondaire (hotbar)
        self.minimap_surface = pygame.Surface((300, 150), pygame.SRCALPHA)
        self.ideaTips_surface = pygame.Surface((514, 150), pygame.SRCALPHA)
        self.allSettings_surface = pygame.Surface((426, 150), pygame.SRCALPHA)

        # surface bg hotbar
        self.bgHotBar = pygame.Surface((WINDOW_WIDTH, 170))
        try :
            self.hotbarBcg = pygame.image.load(join("Image", "Interface", "Hotbar.png")).convert_alpha()
            self.bgHotBar.blit(self.hotbarBcg, (0,0))
        except:
            INFOS["ErrorLoadElement"] = True

        # boolean de check game
        self.followObject = None #ojn suivre
        self.followPlayer = False # bool 
        self.interface_exo = False
        self.cinematique = False # cinématique
        self.cinematiqueObject = None # obj de la cinematique 

        # timer outils waiting
        self.timer_begin = 0
        self.timer_delay = 3500  

        # placement du bool sur True
        self.ERROR_RELANCER = True
        while self.ERROR_RELANCER:
            #lancement création
            self.loadMapElement = LoadMapGestion(self.allSprites, self.collisionSprites, self.allPNJ, self.interactionsGroup)
            self.map, self.mapBase, self.ERROR_RELANCER = self.loadMapElement.Update() # mise à jour des variables


        # gestion des interface du jeu
        self.gameInterfaces = GestionGameInterfaces(self, self.GameTool.gestionSoundFond, self.gestionCours) 

        #pnj
        self.pnj = GestionPNJ(self.displaySurface, self.allPNJ, self.map, self, self.GameTool.gestionSoundDialogues, self.gameInterfaces)
        
        # Initialisation dans votre setup 
        self.minimap = MiniMap(self.mapBase, self.map, self.minimap_surface, self.interactionsGroup)
        self.ideaTips = InfosTips(self.ideaTips_surface)
        self.settingsAll = SettingsAll(self.allSettings_surface,self.GameTool.gestionSoundFond, self.gameInterfaces, self)

        # Interactions
        self.InteractionObject = Interactions(self, self.gameInterfaces)

        if not INFOS["DemiNiveau"] and NIVEAU["Map"] not in ["NiveauBaseFuturiste", "NiveauMordor"]:
            #construction
            self.buildElements = Construire(self)

        playerPosSpawn = LoadJsonMapValue("coordsMapObject", "Spawn")
        
        if NIVEAU["Map"] == "NiveauBaseFuturiste" and not INFOS["DemiNiveau"] :
            self.cinematique = True # player apparait par le portail
            INFOS["HidePlayer"] = True

        self.player = Houmous(((playerPosSpawn[0] + 1 )*CASEMAP,(playerPosSpawn[1] + 0.5 )*CASEMAP), self.allSprites, self.collisionSprites) 
        self.checkLoadingDone = True

        
    def SetupExo(self):
        """Méthode de création de l'exo : setup de la class
        Input / Output : None"""

        self.InterfaceExo = CreateExo(self)
        self.InterfaceExo.start()
        self.checkLoadingDone = True



    def StartMap(self):
        """Lance la création de map / cours / infos en fonction du niveau"""
        
        # Affichage initial de l'écran de chargement
        self.GameTool.SetInfosLevel()
        threading.Thread(target=self.SetupAllMap).start()

        if NIVEAU["Niveau"] == "Seconde":
            if NIVEAU["Map"] == "NiveauPlaineRiviere":
                self.checkCoursDone = False # passe en true dans le gestionCours
                threading.Thread(target=self.gestionCours.MakeCours, daemon=True).start()
            else:
                self.checkCoursDone = True # on ne génère ppas de cours 
        elif NIVEAU["Niveau"] == "Premiere":
            if NIVEAU["Map"] == "NiveauMedievale":
                self.checkCoursDone = False # passe en true dans le gestionCours
                threading.Thread(target=self.gestionCours.MakeCours, daemon=True).start()
            else:
                self.checkCoursDone = True # on ne génère ppas de cours 

        self.checkLoadingDone = False
        self.ChargementEcran()


    def run(self):
        """Méthode main, boucle du jeu"""

        while self.running: # update du jeu

            if INFOS["UpdateFont"]: # update font au changement
                self.GameTool.CreateFont()
            
            if INFOS["ErrorLoadElement"]: # error chargement fichiers ressources (ecran)
                self.displaySurface.fill("#000000")
                text = TEXTE["Elements"]["ErreurLoad"]
                self.textScreen(text)

                # element de gestions
                self.fondu_au_noir()
                text2 = TEXTE["Elements"]["CloseGame"]
                self.textScreen(text2)
                self.running = False


            # get event et mise à jours des éléments pour event spécifique (clicks...)
            dt = self.clock.tick(30) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                elif INFOS["GameStart"]: # dans le jeu

                    # rebinding keys fonctionnement
                    if INFOS["RebindingKey"]:
                        if event.type == pygame.KEYDOWN:
                            if not INFOS["RebindingKey"] =="echap" and event.key != pygame.K_ESCAPE: # verif
                                KEYSBIND[INFOS["RebindingKey"]] = event.key

                            INFOS["RebindingKey"] = False  # Fin du rebind
                            # Sauvegarde des nouvelles touches
                            pygame.event.clear([pygame.KEYDOWN, pygame.KEYUP])

                            with open(join("SourcesFichiers", "Ressources", "keybinds.json"), "w") as f:
                                json.dump(KEYSBIND, f)
                    
                    # s'il n'y a pas de cinématique en cours
                    elif not self.cinematique:

                        if event.type == pygame.KEYDOWN: 

                            self.gameInterfaces.GestionInterfaceGlobale(event)

                            # interaction avec les éléments de la map
                            if event.key == KEYSBIND["action"]:

                            # element d'interaction
                                self.InteractionObject.Interagir((self.allSprites, self.collisionSprites), self.interactionsGroup)

                                # si pas possible, on construit le pont si possible
                                if not INFOS["DemiNiveau"] and NIVEAU["Map"] in ["NiveauPlaineRiviere", "NiveauMedievale"] :
                                    if NIVEAU["Map"] in ["NiveauPlaineRiviere", "NiveauMedievale"] and not self.buildElements.getConstructionStatuePont():
                                        self.buildElements.BuildBridge(self.loadMapElement, self.player.rect.center)
                                    elif NIVEAU["Map"] == "NiveauMedievale" and not self.buildElements.getPlaceStatueBoat():
                                        self.buildElements.PlaceBoat(self.loadMapElement, self.player.rect.center)
                            
                            # affichge ou non de la hotbar
                            if event.key == KEYSBIND["hideHotBar"]:
                                INFOS["HideHotBar"] = True if not INFOS["HideHotBar"] else False
                                INFOS["Hover"] = False
                        

                        # open au clic des interfaces de la hotbar
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            self.settingsAll.OpenInterfaceElementClic(event)

                        if event.type == pygame.MOUSEMOTION:
                            self.settingsAll.HoverElement(event)

                        # update pnj
                        self.cinematique, self.cinematiqueObject, self.followPlayer, self.followObject = self.pnj.update(self.player.rect.center, event) # pnj update 
                
                
                elif INFOS["EndGame"]:
                    self.GestionInterfaceOther.Update(event, "End") # scroll (event)

                else:

                    # element interface game hompe menu (avant start)
                    if event.type == pygame.USEREVENT and event.animationLancement == "animation_finie":
                        self.animationLancementEnd = True
                    
                    # update dans la boucle pour scroll event
                    if self.animationLancementEnd:        
                        self.GestionInterfaceOther.Update(event, "Start")


            if INFOS["GameStart"]:            
                # update de tous les sprites de la map
                self.allSprites.update(dt, self.cinematique)
                self.displaySurface.fill("#000000")

                if self.followPlayer:
                    self.followObject.Update(self.player.rect.center, dt)


                # si pas de cinématique
                if not self.cinematique:
                    self.allSprites.draw(self.player.rect.center) # lockcam player
                else:
                    if NIVEAU["Map"] in ["NiveauBaseFuturiste", "NiveauMordor"]:
                        self.allSprites.draw(self.player.rect.center) # lockcam player
                    else:
                        self.allSprites.draw(self.cinematiqueObject.targetObject.rect.center) # pnj lockcam

                # Afficher la minimap sur l'écran principal + menu settings all
                if not self.cinematique :
                    if not self.demiNiveau: # pas besoin de la minimap
                        self.minimap.Update(self.player.rect.center, self.allPNJ, self.interactionsGroup)
                    self.ideaTips.Update()
                    self.settingsAll.Update()

                    if not INFOS["HideHotBar"]: # check hide bool
                        self.displaySurface.blit(self.bgHotBar, (0, WINDOW_HEIGHT-170)) # hotbar bg
                        if not self.demiNiveau : # pas besoin de la minimap dans les demi niveau
                            self.displaySurface.blit(self.minimap_surface, (10, WINDOW_HEIGHT-160))
                        self.displaySurface.blit(self.ideaTips_surface, COORDS_BOX_IDEAS_TIPS)# reste hotbar
                        self.displaySurface.blit(self.allSettings_surface, COORS_BOX_ALL_SETTINGS)# reste hotbar

                    
                    #pnj close
                    self.pnj.isClose(self.player.rect.center)
                    self.InteractionObject.Update(self.player, self.interactionsGroup) # interaction update
            
                elif self.cinematique and not INFOS["CinematiqueEndAct"] and NIVEAU["Map"] != "NiveauMordor": # si cinématique
                    if NIVEAU["Map"] != "NiveauBaseFuturiste":
                        self.cinematique, endCinematique = self.cinematiqueObject.Update(dt)
                    else:
                        current_time = pygame.time.get_ticks() #check timer (wait 2 s)
                        if current_time - self.timer_begin > self.timer_delay:
                            if self.cinematiqueObject == None :
                                INFOS["HidePlayer"] = False
                                coordsSpawn = LoadJsonMapValue("coordsMapObject", "Spawn")
                                goal = [coordsSpawn[0] + 8, coordsSpawn[1]]
                                pathAcces = [".","S", "P"]
                                self.cinematiqueObject = Cinematique(goal, self.player, self.map, pathAcces)
                            self.cinematique, endCinematique = self.cinematiqueObject.Update(dt)
                        else:
                            endCinematique = False
                    # fin cinématique + action 
                    if endCinematique:
                        if NIVEAU["Map"] != "NiveauBaseFuturiste":
                            self.pnj.EndCinematique() # finition cinématique
                        else:
                            self.player.EndCinematique()
                        self.cinematiqueObject.Replacement(self.allPNJ) # placement convenable du png
                        self.fondu_au_noir() # animation
                        
                        # action en fonction du niveau et des pnj
                        if NIVEAU["Map"] == "NiveauPlaineRiviere":
                            if  not PNJ["PNJ1"]:
                                # écran noir + text de fin cinématique
                                self.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["Cinematique1End"])
                            
                                # pont nb 1
                                allObj = LoadJsonMapValue("coordsMapObject", "ObjAPlacer")
                                for obj in allObj:
                                    if obj[3] == "ArbreBucheron":
                                        coords = [obj[0]+1, obj[1]]
                                self.loadMapElement.AddPont("Pont1", coords)
                            
                                # sup arbre
                                for object in self.collisionSprites:
                                    if (object.pos[0] // CASEMAP, object.pos[1] // CASEMAP) == self.cinematiqueObject.goal:
                                        object.kill()
                                
                                # reset valeue individuelle
                                PNJ["PNJ1"] = True

                                STATE_HELP_INFOS[0] = "LearnCrossBridge"

                            # reset values cinmatique
                            self.cinematique = False
                            self.cinematiqueObject = None
                            
                            self.ouverture_du_noir(object.pos)

                        if NIVEAU["Map"] == "NiveauMedievale":
                            if not PNJ["PNJ4"]:
                                self.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["Cinematique1End"])

                                for object in self.allSprites:
                                    if object.id == "Portal":
                                        object.kill()  

                                allObj = LoadJsonMapValue("coordsMapObject", "ObjAPlacer")
                                for obj in allObj:
                                    if obj[3] == "Portal":
                                        coords = [obj[0], obj[1]]
                                self.loadMapElement.AddCercle("CerclePortal", coords)

                                PNJ["PNJ4"] = True  

                                STATE_HELP_INFOS[0] = "OpenPortail"


                            # reset values cinmatique
                            self.cinematique = False
                            self.cinematiqueObject = None
                        
                        if NIVEAU["Map"] == "NiveauBaseFuturiste":
                            
                            # kill portal
                            for spriteElement in self.allSprites:
                                if spriteElement.id == "Portal":
                                    spriteElement.kill()

                            # reset values cinmatique
                            self.cinematique = False
                            self.cinematiqueObject = None
                        

                        self.allSprites.draw(self.player.rect.center)

                
                # update jusqu'a construction du pont / placement bateau
                if (PNJ["PNJ2"] and NIVEAU["Map"] == "NiveauPlaineRiviere") or (PNJ["PNJ1"] and NIVEAU["Map"] == "NiveauMedievale"):
                    if not self.buildElements.getConstructionStatuePont() or not self.buildElements.getPlaceStatueBoat() : # check
                        self.buildElements.Update(self.player.rect.center)

                # update des interfaces
                if not self.cinematique:
                    self.gameInterfaces.Update(event)


                if INFOS["Exo"]:
                    if not self.gameInterfaces.isInterfaceExoOpen:
                        self.gameInterfaces.CloseAllInterface() # VERIF Sécu

                        self.checkLoadingDone = False
                        # Affichage initial de l'écran de chargement
                        threading.Thread(target=self.SetupExo).start()
                        self.ChargementEcran()
                        # mise à jour de l'interface pour la méthode d'interface
                        self.gameInterfaces.MiseAJourInterfaceExo(self.InterfaceExo) 
                
                # si exo réussit    
                if INFOS["ExoPasse"]:
                    INFOS["ExoPasse"] = False
                    INFOS["HideHotBar"] = False
                    self.GameTool.ChangementNiveau() # changement niveau

                # si passage en demi niveau
                if INFOS["DemiNiveau"] and not self.demiNiveau:
                    self.demiNiveau = True # bool de verif
                    self.GameTool.ChangementDemiNiveau() # chargement du demi niveau

                if INFOS["ReloadCours"]:
                    INFOS["ReloadCours"] = False
                    self.gestionCours.Clear()
                    self.checkCoursDone = False
                    threading.Thread(target=self.gestionCours.MakeCours, daemon=True).start()
                    self.ChargementEcran()
                
                if INFOS["EndPhase"]:
                    INFOS["EndPhase"] = False
                    # check de si on affiche le menu de fin ou alors on passe au niveau sup
                    if NIVEAU["All"]:
                        if NIVEAU["Niveau"] == "Premiere":
                            self.GameTool.fondu_au_noir()
                            INFOS["GameStart"] = False # jouer la cinématique avant
                            INFOS["EndGame"] = True # de meme
                        else:
                            INFOS["ExoPasse"] = True
                    else:
                        self.GameTool.fondu_au_noir()
                        INFOS["GameStart"] = False # jouer la cinématique avant
                        INFOS["EndGame"] = True # de meme 

                if not INFOS["CinematiqueEndAct"] and INFOS["BoolDoubleCheck"]: # on arrete la cinématique 
                    self.cinematique = False
            
                # changement cursor
                ChangeCursor(INFOS["Hover"], "Hand")

            elif INFOS["EndGame"]:
                self.GestionInterfaceOther.Update(event, "End") # auto scroll (auto update)
            
                # changement cursor
                ChangeCursor(INFOS["Hover"], "Hand")

            # element de gestions
            if INFOS["CrashGame"]:
                self.fondu_au_noir()
                if INFOS["ReactorCrash"]:
                    text1 = TEXTE["Elements"][NIVEAU["Map"]]["ExplosionReacteur"]
                    self.textScreen(text1)

                text2 = TEXTE["Elements"]["CloseGame"]
                self.textScreen(text2)
                self.running = False


            
            # update toolBOX
            self.GameTool.Update()
            pygame.event.pump()  # 👈 Permet à Pygame de traiter les événements même sans interaction
            pygame.display.update()

        pygame.quit()


class GameToolBox(object):
    def __init__(self, gestionnaire):
        """Méthode initialisation variable de la tool box de la clas game"""
        self.gestionSoundFond = GestionSoundFond()
        threading.Thread(target=self.gestionSoundFond.BandeSon, daemon=True).start()

        self.gestionSoundDialogues = GestionSoundDialogues()
        self.gestionnaire = gestionnaire

        self.last_update_time = pygame.time.get_ticks()

    
    def CreateFont(self):
        """Méthode de création de toutes les fonts pour le jeu"""
        INFOS["UpdateFont"] = False

        typeFont = join("Font", "Roboto-Regular.ttf") if not POLICEECRITURE["Dyslexique"] else join("Font", "OpenDyslexic-Regular.otf")
        coefSize = 0.7 if not POLICEECRITURE["Dyslexique"] else 0.6


        # création
        try:
            FONT16  = pygame.font.Font(typeFont, int(16*coefSize))
            FONT18  = pygame.font.Font(typeFont, int(18*coefSize))
            FONT20 = pygame.font.Font(typeFont, int(20*coefSize))
            FONT20U = pygame.font.Font(typeFont, int(20*coefSize))
            FONT20U.set_underline(True)
            FONT22 = pygame.font.Font(typeFont, int(22*coefSize))
            FONT24 = pygame.font.Font(typeFont, int(24*coefSize))
            FONT30 = pygame.font.Font(typeFont, int(30*coefSize))
            FONT36 = pygame.font.Font(typeFont, int(36*coefSize))
            FONT36B = pygame.font.Font(typeFont, int(36*coefSize))
            FONT36B.set_bold(True)
            FONT50 = pygame.font.Font(typeFont, int(50*coefSize))
            FONT74 = pygame.font.Font(typeFont, int(74*coefSize))
        except:
            INFOS["ErrorLoadElement"] = True

        # aplpication dans le dico setting
        FONT["FONT16"] = FONT16
        FONT["FONT18"] = FONT18
        FONT["FONT20"] = FONT20
        FONT["FONT20U"] = FONT20U
        FONT["FONT22"] = FONT22
        FONT["FONT24"] = FONT24
        FONT["FONT30"] = FONT30
        FONT["FONT36"] = FONT36
        FONT["FONT36B"] = FONT36B
        FONT["FONT50"] = FONT50
        FONT["FONT74"] = FONT74


    def ChargementEcran(self):

        """Méthode fluide pour l'écran de chargement."""
        loading_step = 0  # Variable d'animation

        while not self.gestionnaire.checkLoadingDone or not self.gestionnaire.checkCoursDone:
            self.gestionnaire.displaySurface.fill((0, 0, 0))  # Fond noir

            # Texte de chargement animé
            loading_text = f"{TEXTE['Elements']['Loading']}{'.' * (loading_step % 4)}"
            loading_step += 1
            text = FONT["FONT74"].render(loading_text, True, (255, 255, 255))
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.gestionnaire.displaySurface.blit(text, text_rect.topleft)

            pygame.display.flip()
            self.gestionnaire.clock.tick(10)  # 10 FPS pour une animation fluide

            # Gérer les événements pour éviter freeze
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        self.fondu_au_noir()    
        self.ouverture_du_noir(self.gestionnaire.player.rect.center)

    def textScreen(self, text):
        """Méthode d'affichage optimisée du texte d'animation sur l'écran."""
        
        self.gestionnaire.displaySurface.fill((0, 0, 0))  # Remplir l'écran avec un fond noir

        # Découper le texte en plusieurs lignes pour l'affichage
        max_width = 1000  # Largeur maximale du texte
        wrapped_lines = wrap_text(text, FONT["FONT50"], max_width)  # Utilisation d'une fonction wrap_text pour gérer le retour à la ligne

        # Hauteur d'une ligne avec la bonne police
        line_height = FONT["FONT50"].size("Tg")[1]
        y_offset = WINDOW_HEIGHT // 2 - (line_height * len(wrapped_lines) // 2)  # Centrer verticalement le texte

        clock = pygame.time.Clock()  # Créer un objet Clock pour gérer le FPS

        # Affichage du texte ligne par ligne avec gestion des événements pour éviter les freezes
        for i, line in enumerate(wrapped_lines):
            line_surface = FONT["FONT50"].render(line, True, (255, 255, 255))  # Créer la surface de texte avec la police et la couleur
            text_rect = line_surface.get_rect(center=(WINDOW_WIDTH // 2, y_offset + i * line_height))  # Centrer chaque ligne

            self.gestionnaire.displaySurface.blit(line_surface, text_rect)  # Afficher le texte à l'écran
            pygame.display.flip()  # Mettre à jour l'écran

            clock.tick(30)  # Limiter à 60 FPS pour garantir que l'animation reste fluide

            # Gestion des événements pendant l'affichage du texte
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Quitter proprement si l'utilisateur ferme la fenêtre

        pygame.time.delay(2500)  # Affichage du texte complet pendant un moment supplémentaire
        self.fondu_au_noir()  # Transition avec fondu au noir après l'affichage du texte



    def fondu_au_noir(self):
        """Méthode de fondu au noir avec gestion de l'alpha et optimisation."""
        
        fade_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))  # Créer une surface de la taille de l'écran
        fade_surface.fill((0, 0, 0))  # Surface noire

        alpha = 0

        # Appliquer un fondu qui se fait progressivement
        while alpha < 255:
            # Appliquer le fondu sur la surface noire avec un alpha croissant
            fade_surface.set_alpha(alpha)
            self.gestionnaire.displaySurface.blit(fade_surface, (0, 0))

            alpha += 5  # Augmenter l'alpha à chaque itération pour créer l'effet de fondu
            pygame.display.flip()  # Mettre à jour l'écran
            self.gestionnaire.clock.tick(30)  # Limite de FPS pour rendre l'animation fluide

            # Gérer les événements pour éviter le freeze pendant l'animation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.event.clear([pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])  # Nettoyer les événements


    def ouverture_du_noir(self, targetPos):      
        """Méthode d'ouverture du noir avec gestion fluide."""
        fade_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        fade_surface.fill((0, 0, 0))

        alpha = 255

        while alpha > 0:
            self.gestionnaire.allSprites.draw(targetPos)
            fade_surface.set_alpha(alpha)
            self.gestionnaire.displaySurface.blit(fade_surface, (0, 0))
            
            alpha -= 5
            pygame.display.flip()
            self.gestionnaire.clock.tick(30)  # Limite FPS à 60

            # Gérer les événements pour éviter le freeze
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.event.clear([pygame.KEYDOWN, pygame.KEYUP])
        pygame.event.clear([pygame.KEYDOWN, pygame.KEYUP])
        self.gestionnaire.timer_begin = pygame.time.get_ticks()
        self.gestionnaire.player.EndAnimation()


    def SetInfosLevel(self):
        match NIVEAU["Map"]:
            case "NiveauPlaineRiviere":
                for key in INVENTORY:
                    INVENTORY[key] = 0

            case "NiveauMedievale":
                INVENTORY["Pickaxe"] = 1
                INVENTORY["OldAxe"] = 1
                INVENTORY["Showel"] = 1
     
    def ResetValues(self):
        """En fonction du niveau, on passe au niveau supérieur"""

        # changement map / niveau en fonction
        if not INFOS["AdminReset"]:
            match NIVEAU["Map"]:
                case "NiveauPlaineRiviere":
                    NIVEAU["Map"] = "NiveauMedievale"

                case "NiveauMedievale":
                    NIVEAU["Map"] = "NiveauBaseFuturiste"

                case "NiveauBaseFuturiste":
                    NIVEAU["Map"] = "NiveauMordor"

                case "NiveauMordor":
                    if NIVEAU["All"]:
                        match NIVEAU["Niveau"]:
                            case "Seconde":
                                NIVEAU["Niveau"] = "Premiere"
                                NIVEAU["Map"] = "NiveauMedievale"
                            case "Premiere":
                                pass


        # reset valeurs
        PNJ["PNJ1"] = False
        PNJ["PNJ2"] = False
        PNJ["PNJ3"] = False
        PNJ["PNJ4"] = False
        PNJ["PNJ5"] = False
        PNJ["PNJ6"] = False
        PNJ["PNJ7"] = False

        INFOS["AdminReset"] = False
        INFOS["EndPhase"] = False
        INFOS["BoolDoubleCheck"] = False
        INFOS["CinematiqueEndAct"] = False
        # reset demi niveau (chateau)
        INFOS["DemiNiveau"] = False 
        self.gestionnaire.demiNiveau = False


        # Réinitialiser les groupes
        self.gestionnaire.allSprites.empty()  # Vide le groupe, supprime les sprites.
        self.gestionnaire.collisionSprites.empty()
        self.gestionnaire.allPNJ.empty()
        self.gestionnaire.interactionsGroup.empty()

        self.gestionnaire.interface_exo = False
        self.gestionnaire.cinematique = False # cinématique
        self.gestionnaire.cinematiqueObject = None # obj de la cinematique 

        STATE_HELP_INFOS[0] = "SeePNJ"

    def ChangementNiveau(self):

        # texte
        self.fondu_au_noir()
        self.textScreen(TEXTE["Elements"]["LevelSup"])
        self.ResetValues()

        # call rebuild
        self.gestionnaire.StartMap()

    def ChangementDemiNiveau(self):
        self.fondu_au_noir()
        if NIVEAU["Map"] == "NiveauMedievale":
            self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["OpenChateau"])
        elif NIVEAU["Map"] == "BaseFuturiste" :
            self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["VaisseauSpacial"])
        elif NIVEAU["Map"] == "NiveauMordor":
            self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["EnterVolcan"])

        # Réinitialiser les groupes
        self.gestionnaire.allSprites.empty()  # Vide le groupe, supprime les sprites.
        self.gestionnaire.collisionSprites.empty()
        self.gestionnaire.allPNJ.empty()
        self.gestionnaire.interactionsGroup.empty()

        self.gestionnaire.interface_exo = False
        self.gestionnaire.cinematique = False # cinématique
        self.gestionnaire.cinematiqueObject = None # obj de la cinematique 

        # call rebuild
        self.gestionnaire.StartMap()

    def Update(self):
        updateSongFondTime = 150000 # 2min 30
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time >= updateSongFondTime:
            self.musiqueThread = threading.Thread(target=self.gestionSoundFond.BandeSon, daemon=True).start()
            self.last_update_time = current_time




















if __name__ == "__main__":
    
    LoadTexte()
    BindKey().Update()


    game = Game()
    game.run()





 
#  https://youtu.be/8OMghdHP-zs?si=88F8KqF8ghjV2GNJ&t=20790