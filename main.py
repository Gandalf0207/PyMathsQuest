from settings import *
from Sources.Elements.touche import *
from Sources.Elements.interactions import *
from Sources.Elements.groups import *
from Sources.Map.loadMap import *
from Sources.Elements.hotbar import *
from Sources.Personnages.pnj import *
from Sources.Ressources.Texte.creationTexte import *
from Sources.Elements.construire import *
from Sources.Interface.interfaceExo import *
from Sources.Elements.sound import *
from Sources.Interface.gestionInterface import *
from Sources.Elements.cinematique import *


class Game(object):
    def __init__(self) -> None:
        """Méthode initialisation all settings du jeu en général (groupe, construction...)
        Input / Output : None"""

        # general setup
        pygame.init() # Initialisation de la fenetre pygame
        
        self.displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # taille fenetre
        self.displayCaption = pygame.display.set_caption(TEXTE["Elements"]["GameName"]) # titre fenetre
        self.running = True # stop de la fenetre
        self.clock = pygame.time.Clock() # dt

        # bool de check chargement
        self.checkLoadingDone = False

        # all groupes
        self.allSprites = AllSprites()
        self.collisionSprites = pygame.sprite.Group()
        self.allPNJ = pygame.sprite.Group()
        self.interactionsGroup = pygame.sprite.Group()

        # all surface secondaire (hotbar)
        self.minimap_surface = pygame.Surface((300, 150))
        self.ideaTips_surface = pygame.Surface((514, 150))
        self.allSettings_surface = pygame.Surface((426, 150))
        
        # boolean de check game
        self.interface_exo = False
        self.cinematique = False # cinématique
        self.cinematiqueObject = None # obj de la cinematique 
        self.hideHotbar = False
        self.demiNiveau = False

        # bool check map : 
        self.ERROR_RELANCER = False

        self.GameTool = GameToolBox(self)
        self.GameTool.CreateFont()

        # surface bg hotbar
        self.bgHotBar = pygame.Surface((WINDOW_WIDTH, 160))
        self.bgHotBar.fill((150,150,150))


        # timer outils waiting
        self.timer_begin = 0
        self.timer_delay = 3500  


    # méthode de call de la class tool
    def ChargementEcran(self):
        self.GameTool.ChargementEcran()

    def textScreen(self, text):
        self.GameTool.textScreen(text)

    def fondu_au_noir(self):
        self.GameTool.fondu_au_noir()

    def ouverture_du_noir(self, targetPos):
        self.GameTool.ouverture_du_noir(targetPos)


    def SetupAllMap(self):
        """Méthode de création de tout les éléments pour le niveau / map
        Input / Output : None"""


        # placement du bool sur True
        self.ERROR_RELANCER = True
        while self.ERROR_RELANCER:
            #lancement création
            self.loadMapElement = LoadMap(self.allSprites, self.collisionSprites, self.allPNJ, self.interactionsGroup)
            self.map, self.mapBase, self.ERROR_RELANCER = self.loadMapElement.Update() # mise à jour des variables


        # gestion des interface du jeu
        self.gameInterfaces = GestionOtherInterfaces(self, self.GameTool.gestionSoundFond) 

        #pnj
        self.pnj = GestionPNJ(self.displaySurface, self.allPNJ, self.map, self, self.GameTool.gestionSoundDialogues, self.gameInterfaces)
        
        # Initialisation dans votre setup 
        self.minimap = MiniMap(self.mapBase, self.map, self.minimap_surface)
        self.ideaTips = InfosTips(self.ideaTips_surface)
        self.settingsAll = SettingsAll(self.allSettings_surface,self.GameTool.gestionSoundFond, self.gameInterfaces, self)

        # Interactions
        self.InteractionObject = Interactions(self, self.gameInterfaces)

        if not INFOS["DemiNiveau"] and NIVEAU["Map"] != "NiveauBaseFuturiste":
            #construction
            self.buildElements = Construire(self)

        getPlayerPosSpawn = LoadJsonMapValue("coordsMapObject", "Spawn")
        playerPosSpawn = getPlayerPosSpawn[0] 
            
        if NIVEAU["Map"] == "NiveauBaseFuturiste":
            self.cinematique = True # player apparait par le portail
            INFOS["HidePlayer"] = True

        self.player = Player(((playerPosSpawn[0] + 1 )*CASEMAP,(playerPosSpawn[1] + 0.5 )*CASEMAP), self.allSprites, self.collisionSprites) 
        self.checkLoadingDone = True

        
    def SetupExo(self):
        """Méthode de création de l'exo : setup de la class
        Input / Output : None"""

        self.InterfaceExo = CreateExo(self)
        self.InterfaceExo.start()
        self.checkLoadingDone = True



    def StartMap(self):

        # Affichage initial de l'écran de chargement
        threading.Thread(target=self.SetupAllMap).start()

        self.ChargementEcran()


    def run(self):
        self.StartMap()

        while self.running:

            if INFOS["CrashGame"]:
                self.fondu_au_noir()
                if NIVEAU["Map"] == "NiveauBaseFuturiste":
                    text1 = "Vous avez envoyé trop de puissance dans le réacteur provoquant son explosion."
                    text2 = "Fermeture du jeu."
                self.textScreen(text1)
                self.textScreen(text2)

                self.running = False
            
            # si exo réussit
            if INFOS["ExoPasse"]:
                INFOS["ExoPasse"] = False
                self.hideHotbar = False
                self.GameTool.ChangementNiveau() # changement niveau

            # si passage en demi niveau
            if INFOS["DemiNiveau"] and not self.demiNiveau:
               self.demiNiveau = True # bool de verif
               self.GameTool.ChangementDemiNiveau() # chargement du demi niveau



            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # rebinding keys fonctionneemnt
                if INFOS["RebindingKey"]:
                    if event.type == pygame.KEYDOWN:
                        if not INFOS["RebindingKey"] =="echap" and event.key != pygame.K_ESCAPE: # verif
                            KEYSBIND[INFOS["RebindingKey"]] = event.key

                        INFOS["RebindingKey"] = False  # Fin du rebind
                        # Sauvegarde des nouvelles touches
                        pygame.event.clear([pygame.KEYDOWN, pygame.KEYUP])

                        with open("keybinds.json", "w") as f:
                            json.dump(KEYSBIND, f)
                
                # s'il n'y a pas de cinématique en cours
                elif not self.cinematique:

                    if event.type == pygame.KEYDOWN: # TP : ne pas oublier de retirer
                        if event.key == pygame.K_t:
                            first_sprite = next(iter(self.allPNJ))  # Premier objet du groupe
                            self.player.rect.center = (first_sprite.pos[0]*CASEMAP, first_sprite.pos[1]*CASEMAP)
                            self.player.hitbox_rect.center = (first_sprite.pos[0]*CASEMAP, first_sprite.pos[1]*CASEMAP)

                            print(f"tp : {first_sprite.pos}")
                            print(self.player.rect.center)

                        if event.key == pygame.K_0:
                            self.player.rect.center = (130*CASEMAP, 25*CASEMAP)
                            self.player.hitbox_rect.center = (130*CASEMAP, 25*CASEMAP)

                        self.gameInterfaces.GestionInterfaceGlobale(event)

                        # interaction avec les éléments de la map
                        if event.key == KEYSBIND["action"]:

                           # element d'interaction
                            self.InteractionObject.Interagir((self.allSprites, self.collisionSprites), self.interactionsGroup)

                            # si pas possible, on construit le pont si possible
                            if NIVEAU["Map"] in ["NiveauPlaineRiviere", "NiveauMedievale"] and not self.buildElements.getConstructionStatuePont():
                                self.buildElements.BuildBridge(self.loadMapElement, self.player.rect.center)
                            elif NIVEAU["Map"] == "NiveauMedievale" and not self.buildElements.getPlaceStatueBoat():
                                self.buildElements.PlaceBoat(self.loadMapElement, self.player.rect.center)
                        
                        # affichge ou non de la hotbar
                        if event.key == KEYSBIND["hideHotBar"]:
                            self.hideHotbar = True if not self.hideHotbar else False
                    
                    # open au clic des interface de la hotbar
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.settingsAll.OpenInterfaceElementClic(event)

                    # update pnj
                    self.cinematique, self.cinematiqueObject = self.pnj.update(self.player.rect.center, event) # pnj update 
            
            

                    
            # update de tous les sprites de la map
            self.allSprites.update(dt, self.cinematique)
            self.displaySurface.fill("#000000")


            # si pas de cinématique
            if not self.cinematique:
                self.allSprites.draw(self.player.rect.center, self.hideHotbar) # lockcam player
            else:
                if NIVEAU["Map"] == "NiveauBaseFuturiste":
                    self.allSprites.draw(self.player.rect.center, self.hideHotbar) # lockcam player
                else:
                    self.allSprites.draw(self.cinematiqueObject.pnjObject.rect.center, self.hideHotbar) # pnj lockcam

            # Afficher la minimap sur l'écran principal + menu settings all
            if not self.cinematique :
                if not self.demiNiveau: # pas besoin de la minimap
                    self.minimap.Update(self.player.rect.center, self.allPNJ, self.interactionsGroup)
                self.ideaTips.Update()
                self.settingsAll.Update()

                if not self.hideHotbar: # check hide bool
                    self.displaySurface.blit(self.bgHotBar, (0, WINDOW_HEIGHT-160)) # hotbar bg
                    if not self.demiNiveau : # pas besoin de la minimap dans les demi niveau
                        self.displaySurface.blit(self.minimap_surface, (10, WINDOW_HEIGHT-160))
                    self.displaySurface.blit(self.ideaTips_surface, COORDS_BOX_IDEAS_TIPS)# reste hotbar
                    self.displaySurface.blit(self.allSettings_surface, COORS_BOX_ALL_SETTINGS)# reste hotbar

                
                #pnj close
                self.pnj.isClose(self.player.rect.center)
                self.InteractionObject.Update(self.player, self.interactionsGroup) # interaction update
        
            else: # si cinématique 
                if NIVEAU["Map"] != "NiveauBaseFuturiste":
                    self.cinematique, endCinematique = self.cinematiqueObject.Update(dt)
                else:
                    current_time = pygame.time.get_ticks() #check timer (wait 2 s)
                    if current_time - self.timer_begin > self.timer_delay:
                        if self.cinematiqueObject == None :
                            INFOS["HidePlayer"] = False
                            coordsSpawn = LoadJsonMapValue("coordsMapObject", "Spawn")
                            goal = [coordsSpawn[0][0] + 8, coordsSpawn[0][1]]
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
                            coordPont1 = LoadJsonMapValue("coordsMapObject", "ArbreSpecial Coords")
                            coords = ((coordPont1[0] + 1)*CASEMAP, coordPont1[1]*CASEMAP) # on ajoute 1 pour etre sur la rivière
                            self.loadMapElement.AddPont("pont1", coords)
                        
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

                            for object in self.collisionSprites:
                                if (object.pos[0] // CASEMAP, object.pos[1] // CASEMAP) == self.cinematiqueObject.goal:
                                    object.kill()  

                            portal = LoadJsonMapValue("coordsMapObject", "Exit")
                            coords = ((portal[0])*CASEMAP, portal[1]*CASEMAP) # on ajoute 1 pour etre sur la rivière
                            self.loadMapElement.AddCerclePortal("CerclePortal", coords)

                            PNJ["PNJ4"] = True  

                            STATE_HELP_INFOS[0] = "OpenPortail"


                        # reset values cinmatique
                        self.cinematique = False
                        self.cinematiqueObject = None
                    
                    if NIVEAU["Map"] == "NiveauBaseFuturiste":
                        
                        # kill portal

                        # reset values cinmatique
                        self.cinematique = False
                        self.cinematiqueObject = None
                    

                    self.allSprites.draw(self.player.rect.center, self.hideHotbar)

            
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

            # update toolBOX
            self.GameTool.Update()


            pygame.display.flip()

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
        
        # création
        FONT20 = pygame.font.Font(None, 20)
        FONT22 = pygame.font.Font(None, 22)
        FONT24 = pygame.font.Font(None, 24)
        FONT30 = pygame.font.Font(None, 30)
        FONT36 = pygame.font.Font(None, 36)
        FONT36B = pygame.font.Font(None, 36)
        FONT36B.set_bold(True)
        FONT50 = pygame.font.Font(None, 50)
        FONT74 = pygame.font.Font(None, 74)

        # aplpication dans le dico setting
        FONT["FONT20"] = FONT20
        FONT["FONT22"] = FONT22
        FONT["FONT24"] = FONT24
        FONT["FONT30"] = FONT30
        FONT["FONT36"] = FONT36
        FONT["FONT36B"] = FONT36B
        FONT["FONT50"] = FONT50
        FONT["FONT74"] = FONT74


    def ChargementEcran(self):
        """Méthode pour dessiner l'écran de chargement"""

        loading_step = 0 # variable
        self.gestionnaire.checkLoadingDone = False
        while not self.gestionnaire.checkLoadingDone:
            self.gestionnaire.displaySurface.fill((0,0,0))  # Remplir avec une couleur grise

            # Animation de texte dynamique avec des points qui défilent
            loading_text = f"{TEXTE["Elements"]["Loading"]}{'.' * (loading_step % 4)}"
            loading_step += 1
            text = FONT["FONT74"].render(loading_text, True, (255, 255, 255))
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.gestionnaire.displaySurface.blit(text, text_rect.topleft)

            pygame.display.flip()
            pygame.time.delay(200)  # Temps de mise à jour de l'écran de chargement


        self.fondu_au_noir()
        self.ouverture_du_noir(self.gestionnaire.player.rect.center)

    def textScreen(self, text):
        """Méthode d'affichage du texte d'animation sur l'ecran"""
        compteur = 0
        while compteur < 2000:
            compteur += 1
            self.gestionnaire.displaySurface.fill((0,0,0))

            # get lines 
            max_width = 400
            wrapped_lines = wrap_text(text, FONT["FONT20"], max_width)  # Assurez-vous d'utiliser la même police

            # Affichage des lignes
            line_height = FONT["FONT50"].size("Tg")[1]  # Hauteur d'une ligne avec la bonne police
            y_offset = WINDOW_HEIGHT // 2 - (line_height * len(wrapped_lines) // 2)

            for i, line in enumerate(wrapped_lines):
                line_surface = FONT["FONT50"].render(line, True, (255, 255, 255))  # Couleur corrigée
                text_rect = line_surface.get_rect(center=(WINDOW_WIDTH // 2, y_offset + i * line_height))
                self.gestionnaire.displaySurface.blit(line_surface, text_rect)  # Utiliser text_rect directement


            pygame.display.flip()

        self.fondu_au_noir()

    def fondu_au_noir(self):
        "Méthode de fondu noir"

        fade_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        fade_surface.fill((0, 0, 0))
        alpha = 0

        while alpha < 255:
            fade_surface.set_alpha(alpha)
            self.gestionnaire.displaySurface.blit(fade_surface, (0, 0))
            alpha += 5
            pygame.display.flip()
            self.gestionnaire.clock.tick(30)  # Limite de rafraîchissement

    def ouverture_du_noir(self, targetPos):
        # Crée une surface noire avec un canal alpha (transparence)
        fade_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        fade_surface.fill((0, 0, 0))

        # Alpha initial pour la surface noire (complètement opaque)
        alpha = 255

        while alpha > 0:
            self.gestionnaire.allSprites.draw(targetPos, self.gestionnaire.hideHotbar)
            # Ici, ne redessinez pas le fond du jeu, car il est déjà chargé et affiché
            # simplement superposez la surface noire pour l'effet de transparence.

            # Appliquer la surface noire avec alpha dégressif
            fade_surface.set_alpha(alpha)
            self.gestionnaire.displaySurface.blit(fade_surface, (0, 0))

            # Réduire progressivement l'opacité pour rendre la surface noire plus transparente
            alpha -= 5
            pygame.display.flip()
            self.gestionnaire.clock.tick(30)  # Limite de rafraîchissement

        pygame.event.clear([pygame.KEYDOWN, pygame.KEYUP])
        self.gestionnaire.timer_begin = pygame.time.get_ticks() # timer update pour nv3
        
    def ResetValues(self):
        """En fonction du niveau, on passe au niveau supérieur"""

        match NIVEAU["Niveau"]:
            case "Seconde":

                match NIVEAU["Map"]:

                    case "NiveauPlaineRiviere":
                        if not INFOS["ChangementAnnee"]:
                            NIVEAU["Map"] = "NiveauMedievale"
                        else:
                            NIVEAU["Niveau"] = "Premiere"

                    case "NiveauMedievale":
                        NIVEAU["Map"] = "NiveauBaseFuturiste"

                    case "NiveauBaseFuturiste":
                        NIVEAU["Map"] = "NiveauPlaineRiviere"

            case "Premiere":
                pass
            case "Terminale" : 
                pass

        # reset valeurs
        PNJ["PNJ1"] = False
        PNJ["PNJ2"] = False
        PNJ["PNJ3"] = False
        PNJ["PNJ4"] = False
        PNJ["PNJ5"] = False

        # reset demi niveau (chateau)
        INFOS["DemiNiveau"] = False 
        self.demiNiveau = False


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
        self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["OpenChateau"])


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