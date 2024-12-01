from settings import *
from groups import *
from loadMap import *
from miniMap import *


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

        # groups
        self.allSprites = AllSprites()
        self.collisionSprites = pygame.sprite.Group()

    def SetupAllMap(self):
        self.player = Player((8*CASEMAP,2*CASEMAP), self.allSprites, self.collisionSprites) 


        if self.niveau ==0:
            self.map, self.mapBase = LoadMapPlaineRiviere(self.niveau, self.allSprites, self.collisionSprites).Update()
            # Initialisation dans votre setup
            self.miniMap = MiniMap(self.mapBase, self.displaySurface)
            self.miniMap.update(self.player.rect.center)
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
            
            self.allSprites.update(dt)
            self.displaySurface.fill("#000000")
            self.allSprites.draw(self.player.rect.center)

            
            self.miniMap.update(self.player.rect.center)


            pygame.display.update()

        pygame.quit()




if __name__ == "__main__":
    game = Game()
    game.run()




 
#  https://youtu.be/8OMghdHP-zs?si=88F8KqF8ghjV2GNJ&t=20790