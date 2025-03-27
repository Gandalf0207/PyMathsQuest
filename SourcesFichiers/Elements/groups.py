#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

from settings import *

class AllSprites(pygame.sprite.LayeredUpdates):
    def __init__(self) -> None:
        """Méhode d'initialisation d'un élement sans colision sur la map. Input / Output : None"""

        super().__init__()
        self.display_surface = pygame.display.get_surface() # surface générale
        self.offset = pygame.Vector2(0, 0)
        self.map_width = LONGUEUR * CASEMAP
        self.map_height = LARGEUR * CASEMAP + 160 #  +160 = hotbar y

    def create_fog(self, targetPos):
        vision_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        vision_surface.fill((0, 0, 0, 255))  # Couche totalement noire (gamma à 0)

        posHalo = self.get_target_screen_coords(targetPos)

        for i in range(250, 0, -2):  # Dégradé plus smooth avec plus d'étapes
            alpha = int((i / 250) * 255)
            pygame.draw.circle(vision_surface, (0, 0, 0, alpha), (posHalo), i)
        
        return vision_surface

    def get_target_screen_coords(self, target_pos: tuple) -> tuple:
        """Méthode pour obtenir les coordonnées de la cible par rapport à la fenêtre du jeu."""
        
        # Calcul de l'offset pour centrer la caméra sur le joueur
        camera_x = -(target_pos[0] - WINDOW_WIDTH / 2)
        camera_y = -(target_pos[1] - WINDOW_HEIGHT / 2)

        # Limiter la caméra pour ne pas montrer le vide
        camera_x = min(0, max(camera_x, WINDOW_WIDTH - self.map_width))
        camera_y = min(0, max(camera_y, WINDOW_HEIGHT - self.map_height))

        # Calcul des coordonnées de la cible par rapport à la fenêtre du jeu
        target_screen_x = target_pos[0] + camera_x
        target_screen_y = target_pos[1] + camera_y

        return (target_screen_x, target_screen_y)


    def draw(self, target_pos: tuple) -> None:
        """Méthode pour dessiner tout les éléments autour de la cible (lock cam). Input : tuple coords target, Output : None"""
        
        # aaptation de la lock cam en fonction de la taille de la map
        if INFOS["HideHotBar"]:
            if INFOS["DemiNiveau"]:
                if NIVEAU["Map"] == "NiveauMedievale":
                    self.map_width = 11 * CASEMAP
                    self.map_height = 11 * CASEMAP 
            else:
                self.map_width = LONGUEUR * CASEMAP
                self.map_height = LARGEUR * CASEMAP 
        else:
            if INFOS["DemiNiveau"]:
                if NIVEAU["Map"] == "NiveauMedievale":
                    self.map_width = 11 * CASEMAP
                    self.map_height = 11 * CASEMAP + 170 # hotbar
            else:
                self.map_width = LONGUEUR * CASEMAP
                self.map_height = LARGEUR * CASEMAP + 170 # hotbar

                
        # Calcul de l'offset pour centrer la caméra sur le joueur
        camera_x = -(target_pos[0] - WINDOW_WIDTH / 2)
        camera_y = -(target_pos[1] - WINDOW_HEIGHT / 2)

        # Limiter la caméra pour ne pas montrer le vide
        camera_x = min(0, max(camera_x, WINDOW_WIDTH - self.map_width))
        camera_y = min(0, max(camera_y, WINDOW_HEIGHT - self.map_height))

        # Affection offset
        self.offset.x = camera_x
        self.offset.y = camera_y

        # Séparer sol et objets
        ground_sprites = [sprite for sprite in self if hasattr(sprite, 'ground')]
        object_sprites = [sprite for sprite in self if not hasattr(sprite, 'ground')]

        # 1️⃣ Afficher le sol en premier (aucun tri nécessaire)
        for sprite in ground_sprites:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)

        # 2️⃣ Trier et afficher les objets en fonction de leur rect.bottom
        for sprite in sorted(object_sprites, key=lambda sprite: sprite.rect.bottom):
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)


        # Appliquer le masque de vision smooth
        if not INFOS["ReactorOn"] and NIVEAU["Map"] =="NiveauBaseFuturiste" and not INFOS["DemiNiveau"]:
            vision_surface = self.create_fog(target_pos)
            self.display_surface.blit(vision_surface, (0, 0))