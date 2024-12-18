from settings import *
from math import atan2, degrees

class Sprites(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.ground = True

class CollisionSprites(pygame.sprite.Sprite):
    def __init__(self,pos, surf, groups) -> None:
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)

class River(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collisionSprites, stateFormat) -> None:
        super().__init__(groups)
        self.LoadImages()
        self.state, self.frame_index = stateFormat, 0
        self.image = pygame.image.load(join("Images","Sol","Riviere", "RiverStraightN-Sx128", "0.gif")).convert_alpha() # Image initiale
        self.rect = self.image.get_rect(topleft=pos)
        self.current_frame = 0
        self.animation_speed = 0.3  # Vitesse de l'animation
        self.collisionSprites = collisionSprites
        self.time_last_update = pygame.time.get_ticks()

    def LoadImages(self):
        self.frames = {
            "RiverAngularE-Sx128": [],
            "RiverAngularN-Ex128": [],
            "RiverAngularN-Wx128": [],
            "RiverAngularW-Sx128": [],
            "RiverStraightN-Sx128": [],
            "RiverStraightW-Ex128": [],
            "RiverMontainConflictx128": []
        }

        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join("Images","Sol", "Riviere", state)):
                if file_names:
                    for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)


    def update(self, dt):
        # Animation des frames
        current_time = pygame.time.get_ticks()
        if current_time - self.time_last_update > 300:  # Changer de frame toutes les 100 ms
            self.current_frame = (self.current_frame + 1) % len(self.frames["RiverStraightN-Sx128"])
            self.image = self.frames[self.state][self.current_frame]
            self.time_last_update = current_time
