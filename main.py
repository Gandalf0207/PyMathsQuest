from settings import *
from Sources.Elements.interactions import *
from Sources.Elements.groups import *
from Sources.Map.loadMap import *
from Sources.Elements.hotbar import *
from Sources.Personnages.pnj import *
from Sources.Ressources.Texte.creationTexte import *
from Sources.Elements.construirePont import *
from Sources.Exos.createExo import *


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
        
        # boolean de check 
        self.INTERFACE_OPEN = False # interface secondaire ouvert
        self.interface_exo = False
        self.cinematique = False # cinématique
        self.cinematiqueObject = None # obj de la cinematique 

        self.CreateFont()

        # surface bg hotbar
        self.bgHotBar = pygame.Surface((WINDOW_WIDTH, 160))
        self.bgHotBar.fill((150,150,150))

    def CreateFont(self):
        FONT20 = pygame.font.Font(None, 20)
        FONT22 = pygame.font.Font(None, 22)
        FONT24 = pygame.font.Font(None, 24)
        FONT30 = pygame.font.Font(None, 30)
        FONT36 = pygame.font.Font(None, 36)
        FONT36B = pygame.font.Font(None, 36)
        FONT36B.set_bold(True)

        FONT["FONT20"] = FONT20
        FONT["FONT22"] = FONT22
        FONT["FONT24"] = FONT24
        FONT["FONT30"] = FONT30
        FONT["FONT36"] = FONT36
        FONT["FONT36b"] = FONT36B



    def LoadJsonMapValue(self, index1 :str, index2 :str) -> list:
        """Récupération des valeur stockées dans le fichier json pour les renvoyer quand nécéssaire 
        à l'aide des indices données.
        Input : index1 / index2 = str   , Output : list"""
        
        with open(join("Sources","Ressources","AllMapValue.json"), "r") as f: # ouverture lecture
            loadElementJson = json.load(f) # chargement des valeurs
        return loadElementJson[index1].get(index2, None) # retour valeurs


    def SetupAllMap(self):
        self.player = Player((8*CASEMAP,2*CASEMAP), self.allSprites, self.collisionSprites) 


        if INFOS["Niveau"] ==0:
            self.loadMapElement = LoadMapPlaineRiviere(self.allSprites, self.collisionSprites, self.allPNJ, self.interactionsGroup)
            self.map, self.mapBase = self.loadMapElement.Update()
            self.pnj = GestionPNJ(self.displaySurface, self.allPNJ, self.INTERFACE_OPEN, self.map, self)
            # Initialisation dans votre setup
            
            self.minimap = MiniMap(self.mapBase, self.map, self.minimap_surface)
            self.ideaTips = InfosTips(self.ideaTips_surface)
            self.settingsAll = SettingsAll(self.allSettings_surface, self.INTERFACE_OPEN)

            # infos traverser
            self.InteractionObject = Interactions(self)
            self.buildPont = ConstruirePont(self)

        else : 
            pass

        self.checkLoadingDone = True

    def SetupExo(self):

        self.InterfaceExo = CreateExo(self)
        self.InterfaceExo.start()
        self.checkLoadingDone = True

    # Fonction pour dessiner l'écran de chargement
    def ChargementEcran(self):
        font = pygame.font.Font(None, 74)
        loading_step = 0
        while not self.checkLoadingDone:
            self.displaySurface.fill((0,0,0))  # Remplir avec une couleur grise

            # Animation de texte dynamique avec des points qui défilent
            loading_text = f"{TEXTE["Elements"]["Loading"]}{'.' * (loading_step % 4)}"
            loading_step += 1
            text = font.render(loading_text, True, (255, 255, 255))
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.displaySurface.blit(text, text_rect.topleft)

            pygame.display.flip()
            pygame.time.delay(200)  # Temps de mise à jour de l'écran de chargement


        self.fondu_au_noir()
        self.ouverture_du_noir(self.player.rect.center)

    def textScreen(self, text):

        font = pygame.font.Font(None, 50)

        self.displaySurface.fill((0,0,0))
        textElement = font.render(text, True, (255,255,255))
        text_rect = textElement.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.displaySurface.blit(textElement, text_rect.topleft)

        pygame.display.flip()
        pygame.time.delay(2000)  # Temps de mise à jour de l'écran de chargement

        self.fondu_au_noir()

    def fondu_au_noir(self):
        fade_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        fade_surface.fill((0, 0, 0))
        alpha = 0

        while alpha < 255:
            fade_surface.set_alpha(alpha)
            self.displaySurface.blit(fade_surface, (0, 0))
            alpha += 5
            pygame.display.flip()
            self.clock.tick(30)  # Limite de rafraîchissement

    def ouverture_du_noir(self, targetPos):
        # Crée une surface noire avec un canal alpha (transparence)
        fade_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        fade_surface.fill((0, 0, 0))

        # Alpha initial pour la surface noire (complètement opaque)
        alpha = 255

        while alpha > 0:
            self.allSprites.draw(targetPos)
            # Ici, ne redessinez pas le fond du jeu, car il est déjà chargé et affiché
            # simplement superposez la surface noire pour l'effet de transparence.

            # Appliquer la surface noire avec alpha dégressif
            fade_surface.set_alpha(alpha)
            self.displaySurface.blit(fade_surface, (0, 0))

            # Réduire progressivement l'opacité pour rendre la surface noire plus transparente
            alpha -= 5
            pygame.display.flip()
            self.clock.tick(30)  # Limite de rafraîchissement


    def run(self):
        
        # Affichage initial de l'écran de chargement
        threading.Thread(target=self.SetupAllMap).start()

        self.ChargementEcran()


        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # s'il n'y a pas de cinématique en cours
                if not self.cinematique:

                    if event.type == pygame.KEYDOWN: # TP : ne pas oublier de retirer
                        if event.key == pygame.K_t:
                            first_sprite = next(iter(self.allPNJ))  # Premier objet du groupe
                            self.player.rect.center = (first_sprite.pos[0]*CASEMAP, first_sprite.pos[1]*CASEMAP)
                            self.player.hitbox_rect.center = (first_sprite.pos[0]*CASEMAP, first_sprite.pos[1]*CASEMAP)

                            print(f"tp : {first_sprite.pos}")
                            print(self.player.rect.center)

                        if event.key == pygame.K_0:
                            self.player.rect.center = (130*CASEMAP, 50*CASEMAP)
                            self.player.hitbox_rect.center = (130*CASEMAP, 50*CASEMAP)
                    
                        if event.key == pygame.K_p or event.key == pygame.K_v or event.key == pygame.K_i or event.key == pygame.K_b:
                            self.INTERFACE_OPEN = self.settingsAll.OpenInterfaceElementClavier(event, self.INTERFACE_OPEN)
                        
                        if event.key == pygame.K_e:
                            # pnj interface
                            self.INTERFACE_OPEN = self.pnj.OpenInterfaceElementClavier(self.INTERFACE_OPEN)
                            # element d'interaction
                            self.InteractionObject.Interagir()
                            # si pas possible, on construit le pont si possible
                            self.buildPont.BuildBridge(self.loadMapElement, self.player.rect.center)

                        if event.key == pygame.K_ESCAPE and self.INTERFACE_OPEN: # Close général interface build
                            if self.InterfaceExo:
                                INFOS["Exo"] = False
                            self.INTERFACE_OPEN = False

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.INTERFACE_OPEN = self.settingsAll.OpenInterfaceElementClic(event, self.INTERFACE_OPEN)
                    




            self.allSprites.update(dt, self.cinematique)
            self.displaySurface.fill("#000000")


            if not self.cinematique:
                self.allSprites.draw(self.player.rect.center)
            else:
                self.allSprites.draw(self.cinematiqueObject.pnjObject.rect.center) # pos pnj lockcam 

            # Afficher la minimap sur l'écran principal + menu settings all
            if not self.cinematique:
                self.displaySurface.blit(self.bgHotBar, (0, WINDOW_HEIGHT-160))
                
                self.minimap.Update(self.player.rect.center, self.allPNJ, self.interactionsGroup)
                self.ideaTips.Update()
                self.settingsAll.Update(event)

                self.displaySurface.blit(self.minimap_surface, (10, WINDOW_HEIGHT-160))
                self.displaySurface.blit(self.ideaTips_surface, COORDS_BOX_IDEAS_TIPS)
                self.displaySurface.blit(self.allSettings_surface, COORS_BOX_ALL_SETTINGS)
            
            if not self.cinematique:
                self.INTERFACE_OPEN, self.cinematique, self.cinematiqueObject = self.pnj.update(self.player.rect.center, self.INTERFACE_OPEN, event)
                self.InteractionObject.Update(self.player, self.interactionsGroup)
            
            else:
                self.cinematique, endCinematique = self.cinematiqueObject.Update(dt)
                if endCinematique:
                    self.pnj.EndCinematique()
                    self.cinematiqueObject.Replacement()
                    self.fondu_au_noir()
                    
                    if INFOS["Niveau"] == 0:
                        if  not PNJ["PNJ1"]:
                            # écran noir + text de fin cinématique
                            self.textScreen(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["Cinematique1End"])
                           
                            # pont nb 1
                            coordPont1 = self.LoadJsonMapValue("coordsMapObject", "ArbreSpecial Coords")
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
                    self.allSprites.draw(self.player.rect.center)

            
            # update jusqu'a construction du pont
            if PNJ["PNJ2"] and INFOS["Niveau"] == 0:
                if not self.buildPont.getConstructionStatue():
                    self.buildPont.Update(self.player.rect.center)


            # update de l'exo 
            if INFOS["Exo"]:
                if not self.INTERFACE_OPEN:
                    self.INTERFACE_OPEN = True
                    self.interface_exo = True

                    self.checkLoadingDone = False
                    # Affichage initial de l'écran de chargement
                    threading.Thread(target=self.SetupExo).start()

                    self.ChargementEcran()

                else:
                    self.InterfaceExo.Update(event)

            if INFOS["ExoPasse"]:
                pass

                    



            if self.INTERFACE_OPEN is None: # vérification : sécurité
                self.INTERFACE_OPEN = False




            pygame.display.flip()

        pygame.quit()




if __name__ == "__main__":
    
    LoadTexte()

    game = Game()
    game.run()





 
#  https://youtu.be/8OMghdHP-zs?si=88F8KqF8ghjV2GNJ&t=20790