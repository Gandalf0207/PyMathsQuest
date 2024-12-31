from settings import *
from Sources.Elements.traverser import *
from Sources.Elements.groups import *
from Sources.Map.loadMap import *
from Sources.Elements.hotbar import *
from Sources.Personnages.pnj import *
from Sources.Texte.creationTexte import *


class Game(object):
    def __init__(self) -> None:
        """Méthode initialisation all settings du jeu en général (groupe, construction...)
        Input / Output : None"""

        # general setup
        pygame.init() # Initialisation de la fenetre pygame
        self.displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # taille fenetre
        self.displayCaption = pygame.display.set_caption("PyMathsQuest") # titre fenetre
        self.running = True # stop de la fenetre
        self.clock = pygame.time.Clock() # dt

        # bool de check chargement
        self.checkLoadingDone = False

        # niveau
        self.niveau = 0

        # all groupes
        self.allSprites = AllSprites()
        self.collisionSprites = pygame.sprite.Group()
        self.allPNJ = pygame.sprite.Group()
        self.allpont = pygame.sprite.Group()

        # all surface secondaire (hotbar)
        self.minimap_surface = pygame.Surface((300, 150))
        self.allSettings_surface = pygame.Surface((426, 150))

        # boolean de check 
        self.INTERFACE_OPEN = False # interface secondaire ouvert
        self.cinematique = False # cinématique
        self.cinematiqueObject = None # obj de la cinematique 


        # info pnj
        self.PNJ1 = False
        self.PNJ2 = False
        self.PNJ3 = False

        # infos traverser
        self.traverserObject = Traverser(self)


    def SetupAllMap(self):
        self.player = Player((8*CASEMAP,2*CASEMAP), self.allSprites, self.collisionSprites) 


        if self.niveau ==0:
            self.loadMapElement = LoadMapPlaineRiviere(self.niveau, self.allSprites, self.collisionSprites, self.allPNJ)
            self.map, self.mapBase = self.loadMapElement.Update()
            self.pnj = GestionPNJ(self.displaySurface, self.niveau, self.allPNJ, self.INTERFACE_OPEN, self.map)
            # Initialisation dans votre setup
            
            self.minimap = MiniMap(self.mapBase, self.map, self.minimap_surface)
            self.settingsAll = SettingsAll(self.allSettings_surface, self.INTERFACE_OPEN)
        else : 
            pass

        self.checkLoadingDone = True


    # Fonction pour dessiner l'écran de chargement
    def ChargementEcran(self):
        font = pygame.font.Font(None, 74)
        loading_step = 0
        while not self.checkLoadingDone:
            self.displaySurface.fill((0,0,0))  # Remplir avec une couleur grise

            # Animation de texte dynamique avec des points qui défilent
            loading_text = f"Chargement{'.' * (loading_step % 4)}"
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
        # self.checkLoadingDone = True

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
                    

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.INTERFACE_OPEN = self.settingsAll.OpenInterfaceElementClic(event, self.INTERFACE_OPEN)
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p or event.key == pygame.K_v or event.key == pygame.K_i or event.key == pygame.K_b:
                            self.INTERFACE_OPEN = self.settingsAll.OpenInterfaceElementClavier(event, self.INTERFACE_OPEN)
                        
                        if event.key == pygame.K_e:
                            self.INTERFACE_OPEN = self.pnj.OpenInterfaceElementClavier(self.INTERFACE_OPEN)

                        if event.key == pygame.K_ESCAPE and self.INTERFACE_OPEN: # Close général interface build
                            self.INTERFACE_OPEN = False

                        if event.key == pygame.K_m:
                            if self.PNJ1:
                                self.traverserObject.MakeTraverser()
                
            

            self.allSprites.update(dt, self.cinematique)
            self.displaySurface.fill("#000000")


            if not self.cinematique:
                self.allSprites.draw(self.player.rect.center)
            else:
                self.allSprites.draw(self.cinematiqueObject.pnjObject.rect.center) # pos pnj lockcam 

            # Afficher la minimap sur l'écran principal + menu settings all
            if not self.cinematique:
                self.minimap.Update(self.player.rect.center, self.allPNJ)
                self.settingsAll.Update()

                self.displaySurface.blit(self.minimap_surface, (10, WINDOW_HEIGHT-160))
                self.displaySurface.blit(self.allSettings_surface, COORS_BOX_ALL_SETTINGS)
            
            if not self.cinematique:
                self.INTERFACE_OPEN, self.cinematique, self.cinematiqueObject = self.pnj.update(self.player.rect.center, self.INTERFACE_OPEN, event)
                self.traverserObject.Update(self.player, self.allpont)
            
            else:
                self.cinematique, endCinematique = self.cinematiqueObject.Update(dt)
                if endCinematique:
                    self.pnj.EndCinematique()
                    self.cinematiqueObject.Replacement()
                    self.fondu_au_noir()
                    
                    if self.niveau == 0:
                        if  not self.PNJ1:
                            # écran noir + text de fin cinématique
                            self.textScreen("Le bûcheron a coupé l'arbre, vous pouvez traverser la rivière !")
                            self.loadMapElement.AddPont(self.allpont, "pont1")
                        
                            # sup arbre
                            for object in self.collisionSprites:
                                if (object.pos[0] // CASEMAP, object.pos[1] // CASEMAP) == self.cinematiqueObject.goal:
                                    object.kill()
                            
                            # reset valeue individuelle
                            self.PNJ1 = True

                    # reset values cinmatique
                    self.cinematique = False
                    self.cinematiqueObject = None
                    
                 
                    
                    self.ouverture_du_noir(object.pos)
                    self.allSprites.draw(self.player.rect.center)



                    



            if self.INTERFACE_OPEN is None: # vérification : sécurité
                self.INTERFACE_OPEN = False




            pygame.display.flip()

        pygame.quit()




if __name__ == "__main__":
    
    LoadTexte()

    game = Game()
    game.run()





 
#  https://youtu.be/8OMghdHP-zs?si=88F8KqF8ghjV2GNJ&t=20790