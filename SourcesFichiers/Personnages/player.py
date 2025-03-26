from settings import *

class Houmous(pygame.sprite.Sprite):  # player : private joke

    def __init__(self, pos : tuple, groups : any, collision_sprites : any) -> None:
        """Méthode initialisation gestion player.
        Input : pos : tuple, groups / collision_sprites : element pygame ; Output : None"""

        # initialisation
        super().__init__(groups)
        self.collision_sprites = collision_sprites
        self.id = "Player"
        # sound
        pygame.mixer.init()
        self.canal2 = pygame.mixer.Channel(2)
        self.SoundFoot = True
        try :
            self.grass1 = join("Sound", "EffetSonore", "GrassWalk", "WalkGrass1.mp3")
            self.grass2 = join("Sound", "EffetSonore", "GrassWalk", "WalkGrass2.mp3")

            self.floor1 = join("Sound", "EffetSonore", "FloorWalk", "Floor1.mp3")
            self.floor2 = join("Sound", "EffetSonore", "FloorWalk", "Floor2.mp3")

            self.rock1 = join("Sound", "EffetSonore", "RockWalk", "Rock1.mp3")
            self.rock2 = join("Sound", "EffetSonore", "RockWalk", "Rock2.mp3")   
        except:
            INFOS["ErrorLoadElement"] = True

        # load image
        self.load_images()
        
        # création element base
        self.state, self.frame_index = "down", 0
        try:
            if INFOS["HidePlayer"]:
                self.image = self.hidePlayerPng
            else:
                self.image = pygame.image.load(join("Image","Player", "down", "0.png")).convert_alpha() # première image 
            self.rect = self.image.get_frect(center = pos)
            self.hitbox_rect = self.rect.inflate(-60,-30) # collision
        except:
            INFOS["ErrorLoadElement"] = True

        #movement
        self.direction = pygame.Vector2(0,0)
        self.speed = 500 # vitesse


    def load_images(self) -> None:
        """Méthode de chargement de toutes les images pour l'animation
        Input / Output : None"""
        try:
            self.hidePlayerPng = pygame.image.load(join("Image", "Player", "HidePlayer.png")).convert_alpha()

            # dico stockage images
            self.frames = {'left' : [],'right' : [],'up' : [],'down' : []}

            # parcours du folder et ajout de toutes les images
            for state in self.frames.keys():
                for folder_path, sub_folders, file_names in walk(join("Image","Player", state)):
                    if file_names:
                        for file_name in sorted(file_names, key= lambda name: int(name.split('.')[0])):
                            full_path = join(folder_path, file_name)
                            surf = pygame.image.load(full_path).convert_alpha()
                            self.frames[state].append(surf)
        except:
            INFOS["ErrorLoadElement"] = True

    def input(self) -> None:
        """Méthode détection input clavier -> modification vecteur déplacement
        Input / Output : None"""

        # Récupérer les touches pressées
        keys = pygame.key.get_pressed()

        # Modification du vecteur de déplacement avec vérification des touches
        self.direction.x = int(keys[KEYSBIND["right"]]) - int(keys[KEYSBIND["left"]])
        self.direction.y = int(keys[KEYSBIND["down"]]) - int(keys[KEYSBIND["up"]])
      
        # normalisation vecteur déplacement
        self.direction = self.direction.normalize() if self.direction else self.direction

        if NIVEAU["Map"] in ["NiveauPlaineRiviere", "NiveauMedievale"]:
            self.sound1 = self.grass1
            self.sound2 = self.grass2
        elif NIVEAU["Map"] == "NiveauBaseFuturiste" : 
            self.sound1 = self.floor1
            self.sound2 = self.floor2   
        elif NIVEAU["Map"] == "NiveauMordor" : 
            self.sound1 = self.rock1
            self.sound2 = self.rock2   

        

        try:
            if self.direction: # il y a un deplacement
                if self.SoundFoot:
                    self.SoundFoot = False
                    songCanal2 = pygame.mixer.Sound(self.sound1) 
                else:
                    self.SoundFoot = True
                    songCanal2 = pygame.mixer.Sound(self.sound2)

                if not self.canal2.get_busy():
                    self.canal2.set_volume(SOUND["EffetSonore"])
                    self.canal2.play(songCanal2)
        except:
            INFOS["ErrorLoadElement"] = True

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
        if not INFOS["NoClip"]:
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
        if INFOS["HidePlayer"]:
            self.image = self.hidePlayerPng
        else:
            self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])] # changement frame pour animation


    def update(self, dt : int, cinematique : bool) -> None:
        """Méthode d'update du player sur la map.
        Input : dt : int, cinematique : bool ,  Output : None"""
        if not cinematique:
            self.input() # get déplacements
        else:
            pygame.event.clear([pygame.KEYDOWN, pygame.KEYUP])

        self.move(dt) # effectuer les déplacements
        self.animate(dt) # appliquer les déplacements




    # cinematique elements
    def UpdateCinematique(self, dt : int, pointSuivant : tuple, pathDeplacement : list) -> any:
        """Méthode update du déplacement du pnj lors de la cinématique
        Input : int, tuple, list
        Ouput : tuple, list"""

        pointSuivant, pathDeplacement = self.Move(dt, pointSuivant, pathDeplacement) # déplacement
        # update deplacement
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.animate(dt)
        return pointSuivant, pathDeplacement
    

    def EndCinematique(self) -> None:
        """Met fin à la cinématique.
        Input / Output : None"""

        self.state, self.frame_index = "down", 0 # replacement correct
        if NIVEAU["Map"] == "NiveauBaseFuturiste":
            coordsSpawn = LoadJsonMapValue("coordsMapObject", "Spawn")
            pos = [(coordsSpawn[0] + 7)*CASEMAP + 64, coordsSpawn[1] * CASEMAP + 64]
        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect.inflate(-60,0) # collision
        self.direction = pygame.Vector2(0,0)

    def EndAnimation(self):
        self.state, self.frame_index = "down", 0  # Réinitialisation

        pos = self.rect.center
        self.rect = self.image.get_frect(center=pos)
        self.hitbox_rect = self.rect.inflate(-60, 0)  # Collision

        self.direction = pygame.Vector2(0, 0)  # ANNULER tout mouvement résiduel
        pygame.event.clear([pygame.KEYDOWN, pygame.KEYUP])  # Effacer les touches pressées


    def Move(self, dt: int, pointSuivant : tuple, pathDeplacement :list) -> any:
        """Déplace le PNJ vers le point cible selon les coordonnées données par la cinématique.d
        Input : dt : int (delta time), list de déplacment point (path)
        Output : any (deux éléments srvant aux calculs de directions)
        """

        if pointSuivant:  # Vérifie si un point cible existe

            # Extraire les coordonnées cibles
            target_x, target_y = pointSuivant

            # Calcul des différences entre la position actuelle et la cible
            dx = target_x - self.hitbox_rect.x
            dy = target_y - self.hitbox_rect.y

            # Distance totale au point cible
            distance = sqrt(dx**2 + dy**2)

            if dx > 0:
                self.direction.x += 0.001
            elif dx < 0:
                self.direction.x -= 0.001
            if dy > 0:
                self.direction.y += 0.001
            elif dy < 0:
                self.direction.y -=0.001

            if distance == 0:  # Si le PNJ est déjà sur la cible
                if pathDeplacement:  # Passer au point suivant si disponible
                    pointSuivant = pathDeplacement.pop(0)
                else:
                    pointSuivant = None  # Fin du chemin

            # Si la distance restante est inférieure au déplacement possible
            elif distance <= self.speed * dt:
                # Atteindre directement la cible
                self.hitbox_rect.topleft = (target_x, target_y)
                self.rect.topleft = self.hitbox_rect.topleft  # Synchroniser la rect
                if pathDeplacement:  # Passer au prochain point
                    pointSuivant = pathDeplacement.pop(0)
                else:
                    pointSuivant = None  # Fin du chemin
            else:
                # Calcul du déplacement proportionnel à la direction
                move_x = (self.speed * dt * dx) / distance
                move_y = (self.speed * dt * dy) / distance

                # Appliquer le déplacement
                self.hitbox_rect.x += move_x
                self.hitbox_rect.y += move_y
                self.rect.topleft = self.hitbox_rect.topleft  # Synchroniser la rect
                

        return pointSuivant, pathDeplacement