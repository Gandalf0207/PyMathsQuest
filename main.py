from settings import *
from Sources.Elements.groups import *
from Sources.Map.loadMap import *
from Sources.Elements.hotbar import *
from Sources.Personnages.pnj import *
from Sources.Personnages.creationDialogues import *


class Game(object):
    def __init__(self) -> None:
        # general setup
        pygame.init() # Initialisation de la fenetre pygame
        self.displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # taille fenetre
        self.displayCaption = pygame.display.set_caption("PyMathsQuest") # titre fenetre
        self.running = True # stop de la fenetre
        self.clock = pygame.time.Clock() # dt

        self.checkLoadingDone = False

        # niveau
        self.niveau = 0


        self.allSprites = AllSprites()
        self.collisionSprites = pygame.sprite.Group()
        self.allPNJ = pygame.sprite.Group()

        self.minimap_surface = pygame.Surface((300, 150))
        self.allSettings_surface = pygame.Surface((426, 150))

        self.INTERFACE_OPEN = False
        

    def SetupAllMap(self):
        self.player = Player((8*CASEMAP,2*CASEMAP), self.allSprites, self.collisionSprites) 


        if self.niveau ==0:
            self.map, self.mapBase = LoadMapPlaineRiviere(self.niveau, self.allSprites, self.collisionSprites, self.allPNJ).Update()
            self.pnj = GestionPNJ(self.displaySurface, self.niveau, self.allPNJ, self.INTERFACE_OPEN)
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
        self.ouverture_du_noir()

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

    def ouverture_du_noir(self):
        # Crée une surface noire avec un canal alpha (transparence)
        fade_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        fade_surface.fill((0, 0, 0))

        # Alpha initial pour la surface noire (complètement opaque)
        alpha = 255

        while alpha > 0:
            self.allSprites.draw(self.player.rect.center)
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
            

            self.allSprites.update(dt)
            self.displaySurface.fill("#000000")
            self.allSprites.draw(self.player.rect.center)

            # Afficher la minimap sur l'écran principal
            self.minimap.Update(self.player.rect.center)

            self.settingsAll.Update()

            
            
            self.displaySurface.blit(self.minimap_surface, (10, WINDOW_HEIGHT-160))
            self.displaySurface.blit(self.allSettings_surface, COORS_BOX_ALL_SETTINGS)

            self.INTERFACE_OPEN = self.pnj.update(self.player.rect.center, self.INTERFACE_OPEN, event)

            if self.INTERFACE_OPEN is None: # vérification : sécurité
                self.INTERFACE_OPEN = False




            pygame.display.flip()

        pygame.quit()




if __name__ == "__main__":
    
    creationDialogues = createDialogues()

    game = Game()
    game.run()





 
#  https://youtu.be/8OMghdHP-zs?si=88F8KqF8ghjV2GNJ&t=20790