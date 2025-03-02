from settings import *

class GongInterface(object):
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        
        pygame.mixer.init()
        self.canal3 = pygame.mixer.Channel(3)


        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale

        # Surface pour le fond transparent
        self.backgroundSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.backgroundSurface.fill((50, 50, 50, 200))  # Fond gris avec alpha (200)

        # Surface principale pour les éléments de l'interface
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH /2, WINDOW_HEIGHT / 2), pygame.SRCALPHA)
        self.interfaceSurface.fill((0, 0, 0, 0))  # Transparent par défaut


        self.JordanPNG = pygame.image.load(join("Images", "PNJ", "Autre", "Jordanx128.png")).convert_alpha()
        self.gong = pygame.image.load(join("Images", "Interface", "Gong.png")).convert_alpha()
                # timer auto update   
        self.last_lower_time = pygame.time.get_ticks()  # Temps de la dernière baisse de température
        self.lower_interval = 5000  # Intervalle de secondes
        self.clicks = 0

        # timer click btn delays
        self.last_click_time = 0
        self.click_delay = 8000  

        self.gongSound = join("Sound", "EffetSonore", "Gong", "Gong.mp3")
        self.songSoleil = join("Sound", "EffetSonore", "Gong", "SongSoleilRouge.mp3")


    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""
        self.surfaceGong = pygame.Surface((640, 360))
        self.rectGong = pygame.Rect(0,0, 640,360)
        self.surfaceGong.blit(self.gong)

    def Update(self, event):
        # construction d'update
        self.BuildInterface()


        if event.type == pygame.MOUSEBUTTONDOWN:  # Si un clic souris est détecté
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time

                # Coordonnées globales de l'événement
                global_pos = event.pos  # Coordonnées globales dans la fenêtre

                # Rect global de la surface de l'interface
                surface_rect = pygame.Rect(320, 180, self.interfaceSurface.get_width(), self.interfaceSurface.get_height())

                # Vérifiez si le clic est sur l'interface
                if surface_rect.collidepoint(global_pos):
                    # Convertissez en coordonnées locales
                    local_pos = (global_pos[0] - surface_rect.x, global_pos[1] - surface_rect.y)
                    
                    if self.rectGong.collidepoint(local_pos):
                        self.clicks += 1
                        songCanal3 = pygame.mixer.Sound(self.gongSound)

                        if self.clicks > 3:
                            songCanal3 = pygame.mixer.Sound(self.songSoleil)
                            self.last_lower_time = current_time
                    
                    # play song
                    self.canal3.set_volume(SOUND["EffetSonore"])
                    self.canal3.play(songCanal3)
        if self.clicks <= 3:
            self.interfaceSurface.blit(self.surfaceGong, (self.rectGong.x, self.rectGong.y))
            self.displaySurface.blit(self.interfaceSurface, (320,180))
        else:
            self.displaySurface.blit(self.JordanPNG, (320, -50))

            text = FONT["FONT24"].render(TEXTE["Elements"]["Humour"], True, BLACK)
            self.displaySurface.blit(text, (25, 700))


            # fermeture interface
            current_time = pygame.time.get_ticks()
            if current_time - self.last_lower_time >= self.lower_interval:
                self.gestionnaire.CloseAllInterface()
                