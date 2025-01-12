from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, pos : tuple, groups : any, collision_sprites : any) -> None:
        """Méthode initialisation gestion player.
        Input : pos : tuple, groups / collision_sprites : element pygame ; Output : None"""

        # initialisation
        super().__init__(groups)
        self.collision_sprites = collision_sprites
        
        # load image
        self.load_images()
        
        # création element base
        self.state, self.frame_index = "down", 0
        self.image = pygame.image.load(join("Images","Player", "down", "0.png")).convert_alpha() # première image 
        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect.inflate(-60,0) # collision

        #movement
        self.direction = pygame.Vector2(0,0)
        self.speed = 500 # vitesse


    def load_images(self) -> None:
        """Méthode de chargement de toutes les images pour l'animation
        Input / Output : None"""

        # dico stockage images
        self.frames = {'left' : [],'right' : [],'up' : [],'down' : []}

        # parcours du folder et ajout de toutes les images
        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join("Images","Player", state)):
                if file_names:
                    for file_name in sorted(file_names, key= lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)

    def input(self) -> None:
        """Méthode détection input clavier -> modification vecteur déplacement
        Input / Output : None"""

        # get touche clavier
        keys = pygame.key.get_pressed()

        # modification vecteur déplacement
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_q])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_z])
        
        # normalisation vecteur déplacement
        self.direction = self.direction.normalize() if self.direction else self.direction


    def move(self, dt : int) -> None:
        """Méthode déplacement du personnage joueur
        Input : dt : int, Output : None"""

        # déplacement box de collision et check collision
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')

        # placement de la box de collision au centre du joueur
        self.rect.center = self.hitbox_rect.center


    def collision(self, direction : tuple) -> None:
        """Méthode gestion de collision player et environnement.
        Input : direction : tuple, Output : None"""

        # check de collision avec tout les sprites
        for sprite in self.collision_sprites:
            if sprite.hitbox.colliderect(self.hitbox_rect):  # Utilisation hitbox
                if direction == 'horizontal': # axe x
                    if self.direction.x > 0: self.hitbox_rect.right = sprite.hitbox.left
                    if self.direction.x < 0: self.hitbox_rect.left = sprite.hitbox.right
                else: # axe y
                    if self.direction.y < 0: self.hitbox_rect.top = sprite.hitbox.bottom
                    if self.direction.y > 0: self.hitbox_rect.bottom = sprite.hitbox.top


    def animate(self, dt : int) -> None:
        """Méthode animation direction sprites player
        Intput : dt : int; Output : None"""

        # get state
        if self.direction.x != 0:
            self.state = "right" if self.direction.x > 0 else "left"
        if self.direction.y != 0:
            self.state = "down" if self.direction.y > 0 else "up"
            
        #animation
        self.frame_index = self.frame_index + 5*dt if self.direction else 0
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])] # changement frame pour animation


    def update(self, dt : int, cinematique : bool) -> None:
        """Méthode d'update du player sur la map.
        Input : dt : int, cinematique : bool ,  Output : None"""
        if not cinematique:
            self.input() # get déplacements
            self.move(dt) # effectuer les déplacements
            self.animate(dt) # appliquer les déplacements

