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

        # groups
        self.allSprites = AllSprites()
        self.collisionSprites = pygame.sprite.Group()

    def LoadImages(self):
        self.grass = pygame.image.load(join("Images", "Sol", "Grass", "Grass.png")).convert_alpha()
        # self.flowers = pygame.image.load(join("Images", "Sol", "Flower", "Flower.png")).convert_alpha()
        self.tree = pygame.image.load(join("Images", "Obstacle", "Arbre.png")).convert_alpha()

    def Setup(self):
        self.map, self.mapBase = NiveauPlaineRiviere(LONGUEUR, LARGEUR, 200).Update()

        for ordonnees in range(len(self.mapBase)):
            for abscisses in range(len(self.mapBase[ordonnees])):
                pos = (abscisses * CASEMAP, ordonnees * CASEMAP)  # Coordonnées de la case sur la carte
                if self.mapBase[ordonnees][abscisses] == "O":            
                    CollisionSprites(pos, self.tree, (self.allSprites, self.collisionSprites))
                elif self.mapBase[ordonnees][abscisses] == "#":   # pos rivière à revoire
                    stateFormat = ""
                    if self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                        stateFormat = "RiverAngularN-Ex128"
                        River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        print(1)
                    elif self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees+1][abscisses] =="#":
                        stateFormat = "RiverAngularE-Sx128"
                        River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        print(1)
                    elif self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                        stateFormat = "RiverAngularW-Sx128"
                        River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        print(1)
                    elif self.mapBase[ordonnees][abscisses-1] =="#" and self.mapBase[ordonnees-1][abscisses] =="#":
                        stateFormat = "RiverAngularN-Wx128"
                        River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        print(1)
                    elif self.mapBase[ordonnees][abscisses+1] =="#" and self.mapBase[ordonnees][abscisses-1] =="#":
                        stateFormat = "RiverStraightW-Ex128"
                        River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        print(1)
                    elif self.mapBase[ordonnees+1][abscisses] =="#" and self.mapBase[ordonnees-1][abscisses] =="#": 
                        stateFormat = "RiverStraightN-Sx128"
                        River(pos, (self.allSprites, self.collisionSprites), self.collisionSprites, stateFormat)
                        print(1)
                    
                
                Sprites(pos, self.grass, self.allSprites) 


        self.player = Player((0,0), self.allSprites, self.collisionSprites) 
        # self.gun = Gun(self.player, self.all_sprites)

    # Fonction pour dessiner l'écran de chargement
    def ChargementEcran(self):
        self.displaySurface.fill((50, 50, 50))  # Remplir avec une couleur grise
        font = pygame.font.Font(None, 74)
        text = font.render("Chargement...", True, (255, 255, 255))
        self.displaySurface.blit(text, (WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.flip()


    def run(self):
        # Affichage initial de l'écran de chargement
        self.ChargementEcran()
        self.LoadImages()
        self.Setup()

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