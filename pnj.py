from settings import *

class PNJ(pygame.sprite.Sprite):
    def __init__(self, pos, pathIMAGE, groups) -> None:
        super().__init__(groups)
        self.image = pygame.image.load(join("Images","PNJ", pathIMAGE[0], pathIMAGE[1])).convert_alpha() 
        self.rect = self.image.get_frect(center = pos)
        
        self.hitbox = self.rect.inflate(-60,0)
 
        # Centrer la hitbox par rapport à l'image
        self.hitbox.center = self.rect.center


