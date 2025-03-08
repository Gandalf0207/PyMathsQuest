from settings import *

class AnimationLancementObj():
    def __init__(self, gestionnaire) -> None:
        """Méthode initialisation de l'animation."""
        

        self.displaySurface = pygame.display.get_surface() # surface générale

        # Initialisation des variables
        self.frame_index = 0
        self.frames = 342
        self.path = join("Images", "AnimationLancementGame")
        self.gestionnaire = gestionnaire

        # Paramètres d'animation
        self.animation_speed = 41  # Temps en millisecondes entre chaque frame
        self.time_last_update = pygame.time.get_ticks()

    def LoadImages(self) -> None:
        """Méthode de chargement de toutes les frames"""


    def Update(self) -> None:
        """Met à jour l'animation une seule fois jusqu'à la fin"""
        while not self.gestionnaire.animationLancementIsDown:
            current_time = pygame.time.get_ticks()
            if current_time - self.time_last_update > self.animation_speed:
                self.time_last_update = current_time
                if self.frame_index < self.frames-2:
                    self.frame_index += 1
                    gc.collect() #☺ clear img
                    surf = pygame.image.load(join(self.path, f"{self.frame_index}.png")).convert()
                    self.displaySurface.blit(surf, (0,0))
                    pygame.display.flip()
                else:
                    self.gestionnaire.animationLancementIsDown = True
        