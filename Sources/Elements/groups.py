from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self) -> None:
        """Méhode d'initialisation d'un élement sans colision sur la map. Input / Output : None"""

        super().__init__()
        self.display_surface = pygame.display.get_surface() # surface générale
        self.offset = pygame.Vector2(0, 0)
        self.map_width = LONGUEUR * CASEMAP
        self.map_height = LARGEUR * CASEMAP + 160 #  +160 = hotbar y


    def draw(self, target_pos: tuple, hideHotbar) -> None:
        """Méthode pour dessiner tout les éléments autour de la cible (lock cam). Input : tuple coords target, Output : None"""
        if hideHotbar:
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
                    self.map_height = 11 * CASEMAP + 160 # hotbar
            else:
                self.map_width = LONGUEUR * CASEMAP
                self.map_height = LARGEUR * CASEMAP + 160 # hotbar

                
        # Calcul de l'offset pour centrer la caméra sur le joueur
        camera_x = -(target_pos[0] - WINDOW_WIDTH / 2)
        camera_y = -(target_pos[1] - WINDOW_HEIGHT / 2)

        # Limiter la caméra pour ne pas montrer le vide
        camera_x = min(0, max(camera_x, WINDOW_WIDTH - self.map_width))
        camera_y = min(0, max(camera_y, WINDOW_HEIGHT - self.map_height))

        # Affection offset
        self.offset.x = camera_x
        self.offset.y = camera_y

        # Dessiner les sprites
        ground_sprites = [sprite for sprite in self if hasattr(sprite, 'ground')]
        object_sprites = [sprite for sprite in self if not hasattr(sprite, 'ground')]

        for layer in [ground_sprites, object_sprites]:
            for sprite in sorted(layer, key=lambda sprite: sprite.rect.centery):
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)

