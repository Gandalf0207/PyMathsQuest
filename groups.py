from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2(0, 0)
        self.map_width = LONGUEUR * CASEMAP
        self.map_height = LARGEUR * CASEMAP

    def draw(self, target_pos):
        # Calcul de l'offset pour centrer la caméra sur le joueur
        camera_x = -(target_pos[0] - WINDOW_WIDTH / 2)
        camera_y = -(target_pos[1] - WINDOW_HEIGHT / 2)

        # Limiter la caméra pour ne pas montrer le vide
        camera_x = min(0, max(camera_x, WINDOW_WIDTH - self.map_width))
        camera_y = min(0, max(camera_y, WINDOW_HEIGHT - self.map_height))

        self.offset.x = camera_x
        self.offset.y = camera_y

        # Dessiner les sprites
        ground_sprites = [sprite for sprite in self if hasattr(sprite, 'ground')]
        object_sprites = [sprite for sprite in self if not hasattr(sprite, 'ground')]

        for layer in [ground_sprites, object_sprites]:
            for sprite in sorted(layer, key=lambda sprite: sprite.rect.centery):
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)

class AllSpritesMiniMap(pygame.sprite.Group):
    def __init__(self, minimapSurf):
        super().__init__()
        self.display_surface = minimapSurf
        self.offset = pygame.Vector2(0, 0)
        self.map_width = LONGUEUR * 7 # px de chaque carre
        self.map_height = LARGEUR * 7 # px de chaque carre
        self.scale_x = self.display_surface.get_width() / self.map_width
        self.scale_y = self.display_surface.get_height() / self.map_height
        self.minimap_width  = 200
        self.minimap_height = 100

    def draw(self, target_pos):
        # Réduire la position cible à l'échelle de la minimap
        target_x = target_pos[0] * self.scale_x
        target_y = target_pos[1] * self.scale_y

        # Calculer l'offset pour centrer la caméra
        camera_x = -(target_x - self.minimap_width / 2)
        camera_y = -(target_y - self.minimap_height / 2)

        # Limiter la caméra pour ne pas sortir des bords
        camera_x = max(-(self.map_width * self.scale_x - self.minimap_width), min(0, camera_x))
        camera_y = max(-(self.map_height * self.scale_y - self.minimap_height), min(0, camera_y))

        self.offset.x = camera_x
        self.offset.y = camera_y

        # Dessiner les sprites
        ground_sprites = [sprite for sprite in self if hasattr(sprite, 'ground')]
        object_sprites = [sprite for sprite in self if not hasattr(sprite, 'ground')]

        for layer in [ground_sprites, object_sprites]:
            for sprite in sorted(layer, key=lambda sprite: sprite.rect.centery):
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)
