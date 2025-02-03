from settings import *
from math import atan2, degrees

class Sprites(pygame.sprite.Sprite):

    def __init__(self,pos : tuple, surf : any, groups : any) -> None:
        """Méthode initialisation class object sprite game sans collision.
        Input : pos = tuple, surf / groups = element pygame ; Output = None """

        # element de base
        super().__init__(groups)
        self.pos = pos
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.ground = True # bool dessins des sprites



class CollisionSprites(pygame.sprite.Sprite):
    
    def __init__(self,pos : tuple, surf : any,typeCollision : str, groups : any, InfoExo : bool = False ) -> None:
        """Méthode initialisation de sprites avec une collision.
        pos : tuple, surf / groups : element pygame, typeCollision : str , InfoExo : bool ; Output : None"""    

        # element de base
        super().__init__(groups)
        self.image = surf # img
        self.pos = pos # pos 
        self.id = typeCollision # id element
        self.InfoExo = InfoExo # si element exercice ou non (bool)

        if typeCollision == "Arbre"  or typeCollision == "Arbre2":
            self.rect = self.image.get_frect(topleft=(pos[0], pos[1]-68))
        elif typeCollision == "pont1" or typeCollision == "pont2":
            self.rect = self.image.get_frect(topleft=(pos[0]-33, pos[1]))
        elif typeCollision == "pont3":
            self.rect = self.image.get_frect(topleft=(pos[0], pos[1]-20))
        else:
            self.rect = self.image.get_frect(topleft=pos)

        # collision en fonction de l'élément # Créer une hitbox plus petite (réduire la largeur et la hauteur)
        match typeCollision:
            case "BorderTop":
                self.hitbox = self.rect.inflate(0,-90)
            case "BorderBottom":
                self.hitbox = self.rect.inflate(0,0)
            case "Souche":
                self.hitbox = self.rect.inflate(-120,-110)
            case "Souche2":
                self.hitbox = self.rect.inflate(-120,-110)
            case "HugeRock":
                self.hitbox = self.rect.inflate(-90,-100)
            case "campFire":
                self.hitbox = self.rect.inflate(-70,-70)
            case "banc":
                self.hitbox = self.rect.inflate(-70,-70)
            case "pont1" :
                self.hitbox = self.rect.inflate(-100,0)
            case "pont2":
                self.hitbox = self.rect.inflate(-100,0)
            case "pont3":
                self.hitbox = self.rect.inflate(0, -100)
            case "ExitRock":
                self.hitbox = self.rect.inflate(-60, -20)
            case "Champs":
                self.hitbox = self.rect.inflate(0,0)
            case "Murailles":
                self.hitbox = self.rect.inflate(0,-40)
            case "House":
                self.hitbox = self.rect.inflate(-20,-60)
            case "Well":
                self.hitbox = self.rect.inflate(-20,-60)
            case "Chateau":
                self.hitbox = self.rect.inflate(-20,-60)
            case "TableCraft":
                self.hitbox = self.rect.inflate(0,0)
            case "Boat":
                self.hitbox = self.rect.inflate(0,0)
            case "Mur":
                self.hitbox = self.rect.inflate(0,-40)
            case "Pilier":
                self.hitbox = self.rect.inflate(0,-20)
            case "Door":
                self.hitbox = self.rect.inflate(0,-60)
            case "CerclePortal":
                self.hitbox = self.rect.inflate(-128,-128)

            case _:  # par défaut
                self.hitbox = self.rect.inflate(-70,-140)

        # Centrer la hitbox par rapport à l'image
        self.hitbox.center = self.rect.center


class River(pygame.sprite.Sprite):

    def __init__(self, pos : tuple, groups : any, stateFormat : str) -> None:
        """Méthode initialisation sprite collision spécifique (rivière).
        Input : pos : tuple, groups  : element pygame, stateFormat : str (infos type de rivière). Output : None"""
        
        # Initialisation elements
        super().__init__(groups)
        self.state, self.frame_index = stateFormat, 0
        self.pos = pos

        # load all images sprites
        self.LoadImages()
        
        # Images et pos (rect)
        self.image = pygame.image.load(join("Images","Sol","Riviere", "RiverStraightN-Sx128", "0.gif")).convert_alpha() # Image initiale
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)
        self.hitbox.center = self.rect.center
        
        # information sur animation
        self.current_frame = 0
        self.animation_speed = 0.3  # Vitesse de l'animation
        self.time_last_update = pygame.time.get_ticks()


    def LoadImages(self) -> None:
        """Méthode de chargement de toutes les frames de rivière
        Input / Output : None"""

        self.frames = {
            "RiverAngularE-Sx128": [],
            "RiverAngularN-Ex128": [],
            "RiverAngularN-Wx128": [],
            "RiverAngularW-Sx128": [],
            "RiverStraightN-Sx128": [],
            "RiverStraightW-Ex128": [],
            "RiverMontainConflictx128": [],
            "RiverTN-SEx128" : [],
            "RiverTWN-Sx128" : [],
            "RiverTWN-Ex128" : [],
            "RiverTW-SEx128" : [],

        }

        # parcours dossier et get images / patch
        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join("Images","Sol", "Riviere", state)):
                if file_names:
                    # modification du dico de stockage
                    for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)


    def update(self, *args) -> None:
        """Méthode d'update des sprite de la rivière pour l'animation.
        Input : *args : tout autre args,  Output : None"""

        # Animation des frames
        current_time = pygame.time.get_ticks()
        if current_time - self.time_last_update > 300:  # Changer de frame toutes les 100 ms
            self.current_frame = (self.current_frame + 1) % len(self.frames["RiverStraightN-Sx128"])
            self.image = self.frames[self.state][self.current_frame]
            self.time_last_update = current_time
