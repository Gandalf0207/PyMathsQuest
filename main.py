from settings import *
from CreationMap import *
from sprites import *
from player import *
from groups import *


class Game(object):
    def __init__(self) -> None:
        # general setup
        pygame.init() # Initialisation de la fenetre pygame
        self.displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # taille fenetre
        self.displayCaption = pygame.display.set_caption("PyMathsQuest") # titre fenetre
        self.running = True # stop de la fenetre
        self.clock = pygame.time.Clock() # dt

        self.checkLoadingDone = False
        self.LoadImages()

        # groups
        self.allSprites = AllSprites()
        self.collisionSprites = pygame.sprite.Group()

    def LoadImages(self):
        self.grass = pygame.image.load(join("Images", "Sol", "Grass", "Grass.png")).convert_alpha()
        self.flowers = pygame.image.load(join("Images", "Sol", "Flower", "Flower.png")).convert_alpha()
        self.tree = pygame.image.load(join("Images", "Obstacle", "Arbre.png")).convert_alpha()
        self.tree2 = pygame.image.load(join("Images", "Obstacle", "Arbre2.png")).convert_alpha()
        self.rock = pygame.image.load(join("Images", "Sol","Rock", "Rock.png")).convert_alpha()
        self.mud = pygame.image.load(join("Images", "Sol","Mud", "Mud.png")).convert_alpha()
        self.montainWE = pygame.image.load(join("Images", "Border","Mountain", "MountainStraighW-Ex128.png")).convert_alpha()
        self.montainWE1 = pygame.image.load(join("Images", "Border","Mountain", "MountainStraighW-Ealt1x128.png")).convert_alpha()

    def Setup(self):
        self.map, self.mapBase = NiveauPlaineRiviere(LONGUEUR, LARGEUR, 650,200,300).Update()

        for ordonnees in range(len(self.mapBase)):
            for abscisses in range(len(self.mapBase[ordonnees])):
                pos = (abscisses * CASEMAP, ordonnees * CASEMAP)  # Coordonnées de la case sur la carte
                if self.map[ordonnees][abscisses] == "O":
                    if randint(0,3) > 2:
                        CollisionSprites(pos, self.tree2, (self.allSprites, self.collisionSprites))
                    else:
                        CollisionSprites(pos, self.tree, (self.allSprites, self.collisionSprites))

                elif self.mapBase[ordonnees][abscisses] == "#":   # pos rivière à revoire
                    stateFormat = ""
                    if  ordonnees not in [0, LARGEUR-1] and abscisses not in [0,149]:
                        if self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                            stateFormat = "RiverAngularN-Ex128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees+1][abscisses] =="#":
                            stateFormat = "RiverAngularE-Sx128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                            stateFormat = "RiverAngularN-Wx128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees+1][abscisses] =="#":
                            stateFormat = "RiverAngularW-Sx128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees][abscisses-1] =="#":
                            stateFormat = "RiverStraightW-Ex128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif self.mapBase[ordonnees+1][abscisses] =="#" and self.mapBase[ordonnees-1][abscisses] =="#": 
                            stateFormat = "RiverStraightN-Sx128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                    else:
                        if ordonnees in [0, LARGEUR-1]: 
                            stateFormat = "RiverMontainConflictx128"
                            River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif abscisses ==0:
                            if self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                                stateFormat = "RiverAngularN-Ex128"
                                River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                            elif self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees+1][abscisses] =="#":
                                stateFormat = "RiverAngularE-Sx128"
                                River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                            elif self.mapBase[ordonnees+1][abscisses] =="#" and self.mapBase[ordonnees-1][abscisses] =="#": 
                                stateFormat = "RiverStraightN-Sx128"
                                River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        elif abscisses == LARGEUR-1:
                            if self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                                stateFormat = "RiverAngularN-Wx128"
                                River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                            elif self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees+1][abscisses] =="#":
                                stateFormat = "RiverAngularW-Sx128"
                                River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                            elif self.mapBase[ordonnees+1][abscisses] =="#" and self.mapBase[ordonnees-1][abscisses] =="#": 
                                stateFormat = "RiverStraightN-Sx128"
                                River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                
                elif self.mapBase[ordonnees][abscisses] == "B":
                    if (ordonnees == 0 or ordonnees == (LARGEUR-1) ):
                        if choice([True, False]):
                            CollisionSprites(pos, self.montainWE, (self.allSprites, self.collisionSprites))
                        else:
                            CollisionSprites(pos, self.montainWE1, (self.allSprites, self.collisionSprites))


                if self.mapBase[ordonnees][abscisses] == "F":
                    Sprites(pos, self.flowers, self.allSprites)
                elif self.mapBase[ordonnees][abscisses] == "M":
                    Sprites(pos, self.mud, self.allSprites) 
                elif self.mapBase[ordonnees][abscisses] == "R":
                    Sprites(pos, self.rock, self.allSprites) 
                else:
                    Sprites(pos, self.grass, self.allSprites) 


        self.player = Player((8*CASEMAP,2*CASEMAP), self.allSprites, self.collisionSprites) 

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
        
        threading.Thread(target=self.Setup).start()
        self.ChargementEcran()

        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.allSprites.update(dt)

            self.displaySurface.fill("#000000")
            self.allSprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()




 
#  https://youtu.be/8OMghdHP-zs?si=88F8KqF8ghjV2GNJ&t=20790