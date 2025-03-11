from settings import *

class AnimationLancementObj():
    def __init__(self, gestionnaire) -> None:
        """Méthode initialisation de l'animation."""
        

        self.displaySurface = pygame.display.get_surface() # surface générale


        #song 
        pygame.mixer.init()
        self.canal4 = pygame.mixer.Channel(4)


        # Initialisation des variables
        self.frame_index = 0
        self.frames = 342
        self.path = join("Image", "AnimationLancementGame")
        self.gestionnaire = gestionnaire

        # Paramètres d'animation
        self.animation_speed = 41  # Temps en millisecondes entre chaque frame
        self.time_last_update = pygame.time.get_ticks()

        self.animationPlayed = False

        self.PlaySon()
    
    def PlaySon(self) -> None:
        SOUND["EffetSonore"] = 0.8
        self.songPath = join("Sound", "EffetSonore", "SonLancement.mp3")
        self.music = pygame.mixer.Sound(self.songPath)
        self.canal4.set_volume(SOUND["EffetSonore"])
        self.canal4.play(self.music)

    def Update(self) -> None:
        """Met à jour l'animation une seule fois jusqu'à la fin"""
        while not self.animationPlayed:
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
                    self.animationPlayed = True
                    SOUND["EffetSonore"] = 0.05
                    pygame.display.flip()

        # Mettre à jour le played de l'animation (main action)
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {"animationLancement": "animation_finie"}))




        