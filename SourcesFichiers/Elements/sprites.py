from settings import *

class Sprites(pygame.sprite.Sprite):

    def __init__(self,pos : tuple, surf : any, idName, groups : any, layer= 0) -> None:
        """Méthode initialisation class object sprite game sans collision.
        Input : pos = tuple, surf / groups = element pygame ; Output = None """

        # element de base
        super().__init__(groups)
        self.pos = pos
        self.image = surf
        self.id = idName
        self.rect = self.image.get_frect(topleft = pos)
        self.ground = True # bool dessins des sprites

        # Vérifier si le groupe principal supporte les layers
        for group in groups:
            if isinstance(group, pygame.sprite.LayeredUpdates):
                group.change_layer(self, layer)

class CollisionSprites(pygame.sprite.Sprite):
    
    def __init__(self,pos : tuple, surf : any,typeCollision : str, groups : any, InfoExo : bool = False, layer = 0) -> None:
        """Méthode initialisation de sprites avec une collision.
        pos : tuple, surf / groups : element pygame, typeCollision : str , InfoExo : bool ; Output : None"""    

        # element de base
        super().__init__(groups)
        self.image = surf # img
        self.pos = pos # pos 
        self.id = typeCollision # id element
        self.InfoExo = InfoExo # si element exercice ou non (bool)

        # Vérifier si le groupe principal supporte les layers
        for group in groups:
            if isinstance(group, pygame.sprite.LayeredUpdates):
                group.change_layer(self, layer)

        if typeCollision == "Arbre"  or typeCollision == "Arbre1" or typeCollision == "ArbreBucheron":
            self.rect = self.image.get_frect(topleft=(pos[0], pos[1]-66))
        elif typeCollision == "Pont1" or typeCollision == "Pont2":
            self.rect = self.image.get_frect(topleft=(pos[0]-33, pos[1]))
        elif typeCollision in["WallAngularNE", "WallAngularNW"] and (not INFOS["DemiNiveau"]) and NIVEAU["Map"] == "NiveauMedievale":
            self.rect = self.image.get_frect(topleft=(pos[0], pos[1]-64))
        elif typeCollision == "Pilier":
            self.rect = self.image.get_frect(topleft=(pos[0], pos[1]-56))
        elif typeCollision[:5] == "WallB" and not INFOS["DemiNiveau"]:
            self.rect = self.image.get_frect(topleft=(pos[0], pos[1]+102))
        else:
            self.rect = self.image.get_frect(topleft=pos)




        # collision en fonction de l'élément # Créer une hitbox plus petite (réduire la largeur et la hauteur)
        match typeCollision:
            case "BorderTop":
                self.hitbox = self.rect.inflate(0,-90)
            case "BorderBottom":
                self.hitbox = self.rect.inflate(0,0)
            case "Souche":
                self.hitbox = self.rect.inflate(-100,-100)
            case "Souche1":
                self.hitbox = self.rect.inflate(-100,-100)
            case "Arbre":
                self.hitbox = self.rect.inflate(-100,-140)
            case "Arbre1":
                self.hitbox = self.rect.inflate(-100,-140)
            case "HugeRock":
                self.hitbox = self.rect.inflate(-90,-100)
            case "CampFire":
                self.hitbox = self.rect.inflate(-70,-70)
            case "Pont1" :
                self.hitbox = self.rect.inflate(-100,0)
            case "Pont2":
                self.hitbox = self.rect.inflate(-100,0)
            case "ExitRock":
                self.hitbox = self.rect.inflate(-60, -20)
            case "Champs":
                self.hitbox = self.rect.inflate(0,0)
            case "House":
                self.hitbox = self.rect.inflate(-20,-60)
            case "Well":
                self.hitbox = self.rect.inflate(-20,-60)
            case "Chateau":
                self.hitbox = self.rect.inflate(0, -30)
            case "TableCraft":
                self.hitbox = self.rect.inflate(0,0)
            case "Boat":
                self.hitbox = self.rect.inflate(0,0)
            case "Pilier":
                self.hitbox = self.rect.inflate(-40,-20)
            case "CerclePortal":
                self.hitbox = self.rect.inflate(-128,-128)
            case "DoorMuraille":
                self.hitbox = self.rect.inflate(0, -60)
            case "DoorChateau":
                self.hitbox = self.rect.inflate(0, -60)
            case "DoorChateauInterieur":
                self.hitbox = self.rect.inflate(0, -60)
            case "ReactorBloc":
                self.hitbox = self.rect.inflate(-128,-128)
            case "StructureCafet":
                self.hitbox = self.rect.inflate(0,0)
            case "StructureEssence":
                self.hitbox = self.rect.inflate(0,0)
            case "StructureLancement":
                self.hitbox = self.rect.inflate(0,0)
            case "DoorFuturisteClose":
                self.hitbox = self.rect.inflate(0, -60)
            case "Vitre":
                self.hitbox = self.rect.inflate(0,0)
            case "Caisse":
                self.hitbox = self.rect.inflate(-80, -80)
            case "ControlPanel": 
                self.hitbox = self.rect.inflate(0,0)
            case "DoorFuturisteVaisseau":
                self.hitbox = self.rect.inflate(0,-60)
            case "CrashVaisseau":
                self.hitbox = self.rect.inflate(-30,-30)
            case "Pot":
                self.hitbox = self.rect.inflate(-40, -40)
            case "DoorCellule":
                self.hitbox = self.rect.inflate(0,-60)
            case "DoorPrison":
                self.hitbox = self.rect.inflate(0,-60)
            case "Barreaux":
                self.hitbox = self.rect.inflate(0,0)
            case "VolcanStruc":
                self.hitbox = self.rect.inflate(-30,-30)
            case "DoorVolcan":
                self.hitbox = self.rect.inflate(0,-60)
            case "DoorVolcanEntree":
                self.hitbox = self.rect.inflate(-50,-60)
            case "Lave":
                self.hitbox = self.rect.inflate(0, -20)
                

            case _:  # par défaut
                self.hitbox = self.rect.inflate(0,0)

        if typeCollision[:4] == "Wall":
            if typeCollision == "WallWEHaut":
                self.hitbox = self.rect.inflate(0,-50)
            else:
                self.hitbox = self.rect.inflate(0,0)

        # Centrer la hitbox par rapport à l'image
        self.hitbox.center = self.rect.center



class AnimatedSprites(pygame.sprite.Sprite):
    def __init__(self, pos : tuple, groups : any, Id, path, layer = 0) -> None:
        """Méthode initialisation sprite collision spécifique (rivière).
        Input : pos : tuple, groups  : element pygame, stateFormat : str (infos type de rivière). Output : None"""
        
        # Initialisation elements
        super().__init__(groups)
        self.frame_index =  0
        self.pos = pos
        self.id = Id


        # Vérifier si le groupe principal supporte les layers
        for group in groups:
            if isinstance(group, pygame.sprite.LayeredUpdates):
                group.change_layer(self, layer)

        # Images et pos (rect)
        self.path = path
        try :
            self.image = pygame.image.load(join(path, "0.gif")).convert_alpha() # Image initiale
            self.rect = self.image.get_rect(topleft=pos)
        except:
            INFOS["ErrorLoadElement"] = True
        self.ground = True # bool dessins des sprites

        
        # load all images sprites
        self.LoadImages()

        # information sur animation
        self.current_frame = 0
        self.animation_speed = 0.3  # Vitesse de l'animation
        self.time_last_update = pygame.time.get_ticks()


    def LoadImages(self) -> None:
        """Méthode de chargement de toutes les frames de rivière
        Input / Output : None"""

        self.frames = []

        # parcours dossier et get images / patch
        for folder_path, sub_folders, file_names in walk(self.path):
            if file_names:
                # modification du dico de stockage
                for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                    full_path = join(folder_path, file_name)
                    try :
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames.append(surf)
                    except:
                        INFOS["ErrorLoadElement"] = True


    def update(self, *args) -> None:
        """Méthode d'update des sprite de la rivière pour l'animation.
        Input : *args : tout autre args,  Output : None"""

        # Animation des frames
        current_time = pygame.time.get_ticks()
        if current_time - self.time_last_update > 300:  # Changer de frame toutes les 100 ms
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.time_last_update = current_time



class AnimatedCollisionSprites(pygame.sprite.Sprite):
    def __init__(self,pos,  path ,typeCollision : str, groups : any, layer = 0, InfoExo = False) -> None:
        """Méthode initialisation de sprites avec une collision.
        pos : tuple, surf / groups : element pygame, typeCollision : str , InfoExo : bool ; Output : None"""    

        # element de base
        super().__init__(groups)
        self.pos = pos # pos 
        self.frame_index =  0
        self.id = typeCollision # id element
        
        self.InfoExo = InfoExo # si element exercice ou non (bool)
        
        
        # Images et pos (rect)
        self.path = path
        try :
            self.image = pygame.image.load(join(path, "0.gif")).convert_alpha() # Image initiale
            self.rect = self.image.get_rect(topleft=pos)
        except:
            INFOS["ErrorLoadElement"] = True
        self.ground = True # bool dessins des sprites

        # Vérifier si le groupe principal supporte les layers
        for group in groups:
            if isinstance(group, pygame.sprite.LayeredUpdates):
                group.change_layer(self, layer)

        if typeCollision in ["Pont3", "Pont5"]:
            self.rect = self.image.get_frect(topleft=(pos[0]-32, pos[1]))   
        elif typeCollision == "Pont4":
            self.rect = self.image.get_frect(topleft=(pos[0], pos[1]-32))   
        elif typeCollision == "Chandelier":
            self.rect = self.image.get_frect(topleft=(pos[0], pos[1]-56))   
        else:
            self.rect = self.image.get_frect(topleft=pos)

        # collision en fonction de l'élément # Créer une hitbox plus petite (réduire la largeur et la hauteur)
        match typeCollision:
            case "Pont3":
                self.hitbox = self.rect.inflate(0, -100)
            case "Pont4":
                self.hitbox = self.rect.inflate(-100, 0)
            case "Pont 5":
                self.hitbox = self.rect.inflate(0, -100)
            case "Chandelier":
                self.hitbox = self.rect.inflate(0, -60)
            case "StructureReactor":
                self.hitbox = self.rect.inflate(0, 0)
            case "River":
                self.hitbox = self.rect.inflate(0,0)
            
            case _:  # par défaut
                self.hitbox = self.rect.inflate(0, 0)

        # Centrer la hitbox par rapport à l'image
        self.hitbox.center = self.rect.center


        # load all images sprites
        self.LoadImages()

        # information sur animation
        self.current_frame = 0
        self.animation_speed = 0.3  # Vitesse de l'animation
        self.time_last_update = pygame.time.get_ticks()


    def LoadImages(self) -> None:
        """Méthode de chargement de toutes les frames de rivière
        Input / Output : None"""

        self.frames = []

        # parcours dossier et get images / patch
        for folder_path, sub_folders, file_names in walk(self.path):
            if file_names:
                # modification du dico de stockage
                for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                    full_path = join(folder_path, file_name)
                    try :
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames.append(surf)
                    except:
                        INFOS["ErrorLoadElement"] = True

    def update(self, *args) -> None:
        """Méthode d'update des sprite de la rivière pour l'animation.
        Input : *args : tout autre args,  Output : None"""

        # Animation des frames
        current_time = pygame.time.get_ticks()
        if current_time - self.time_last_update > 300:  # Changer de frame toutes les 100 ms
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.time_last_update = current_time


class AnimatedSpritesUnique(pygame.sprite.Sprite):
    def __init__(self, pos : tuple, groups : any, Id, path, layer = 0) -> None:
        """Méthode initialisation sprite collision spécifique (rivière).
        Input : pos : tuple, groups  : element pygame, stateFormat : str (infos type de rivière). Output : None"""
        
        # Initialisation elements
        super().__init__(groups)
        self.frame_index =  0
        self.pos = pos
        self.id = Id


        # Vérifier si le groupe principal supporte les layers
        for group in groups:
            if isinstance(group, pygame.sprite.LayeredUpdates):
                group.change_layer(self, layer)

        # Images et pos (rect)
        self.path = path
        try :
            self.image = pygame.image.load(join(path, "0.gif")).convert_alpha() # Image initiale
            self.rect = self.image.get_rect(topleft=pos)
        except:
            INFOS["ErrorLoadElement"] = True
        self.ground = True # bool dessins des sprites

        
        # load all images sprites
        self.LoadImages()

        # information sur animation
        self.current_frame = 0
        self.animation_speed = 0.3  # Vitesse de l'animation
        self.time_last_update = pygame.time.get_ticks()


    def LoadImages(self) -> None:
        """Méthode de chargement de toutes les frames de rivière
        Input / Output : None"""

        self.frames = []

        # parcours dossier et get images / patch
        for folder_path, sub_folders, file_names in walk(self.path):
            if file_names:
                # modification du dico de stockage
                for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                    full_path = join(folder_path, file_name)
                    try :
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames.append(surf)
                    except:
                        INFOS["ErrorLoadElement"] = True


    def update(self, *args) -> None:
        """Méthode d'update des sprite de la rivière pour l'animation.
        Input : *args : tout autre args,  Output : None"""

        # Animation des frames
        current_time = pygame.time.get_ticks()
        if current_time - self.time_last_update > 300:  # Changer de frame toutes les 100 ms

            if self.current_frame +1 > len(self.frames)-1: # passage à la suite
                if NIVEAU["Map"] == "NiveauMordor" and INFOS["DemiNiveau"]:
                    INFOS["EndPhase"] = True
 
            else: #animation classique
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.image = self.frames[self.current_frame]
                self.time_last_update = current_time

