from settings import *

class MiniMap:
    def __init__(self, main_map, map_base):
        """
        Initialise la minimap.
        """
        self.main_map = main_map
        self.map_base = map_base

        self.offset = pygame.Vector2(0, 0)
        self.minimap_size = 200  # Taille de la minimap
        self.minimap_surface = pygame.Surface((200, 100))  # Surface de la minimap

        self.minimap_pos = (10, 10)  # Position de la minimap sur l'écran

        # Calcul de l'échelle de réduction de la carte vers la minimap
        map_width, map_height = len(self.map_base[0]) /5, len(self.map_base) /5
        self.scale = self.minimap_size / max(map_width, map_height)

        # Chargement des sprites
        self.sprite_images = self.load_sprite_images()

        # Zone de verrouillage de la minimap
        self.lock_margin = self.minimap_size // 4  # Zone où la minimap est verrouillée (1/4 de la taille)

    def load_sprite_images(self):
        """
        Charge les surfaces ou définit les couleurs pour représenter les types de cellules.
        """
        return {
            "O": (0, 255, 0),  # Vert (obstacles)
            "B": (128, 128, 128),  # Gris (bordures)
            "F": (255, 255, 0),  # Jaune (fleurs)
            "M": (139, 69, 19),  # Marron (boue)
            "R": (100, 100, 100),  # Gris foncé (rocher)
            "-": (0, 200, 0),  # Vert foncé (herbe)
            "P": (0, 255, 255),  # Bleu
            "S": (0, 0, 0),  # Noir
            "#": (0, 255, 255),  # Cyan
        }

    def draw_minimap(self, player_pos):
        """
        Dessine la carte sur la minimap avec un déplacement lié à l'offset.
        """
        self.minimap_surface.fill((50, 50, 50))  # Fond gris foncé

        # Si la minimap est verrouillée (proche du joueur), on garde la caméra centrée sur lui
        if self.is_locked(player_pos):
            camera_x = -(player_pos[0] - self.minimap_size / 2)
            camera_y = -(player_pos[1] - self.minimap_size / 2)
        else:
            # Sinon on déverrouille la caméra et on permet un déplacement libre
            camera_x = -(self.offset.x)
            camera_y = -(self.offset.y)

        # Limiter l'offset pour ne pas dépasser la taille de la carte
        camera_x = min(0, max(camera_x, self.minimap_size - len(self.map_base[0]) * self.scale)) 
        camera_y = min(0, max(camera_y, self.minimap_size - len(self.map_base) * self.scale))

        self.offset.x = camera_x
        self.offset.y = camera_y

        # Dessiner les éléments de la carte
        for y, row in enumerate(self.map_base):
            for x, cell in enumerate(row):
                if cell in self.sprite_images:
                    color = self.sprite_images[cell]

                    # Calcul des dimensions et position de la cellule sur la minimap
                    cell_x = int(x * self.scale) - int(self.offset.x)
                    cell_y = int(y * self.scale) - int(self.offset.y)
                    cell_size = int(self.scale)

                    # Dessiner la cellule sur la minimap
                    pygame.draw.rect(self.minimap_surface, color, (cell_x, cell_y, cell_size, cell_size))

    def draw_player_position(self, player_pos):
        """
        Dessine la position du joueur sur la minimap.
        """
        player_x = int(player_pos[0] * self.scale) - self.offset.x
        player_y = int(player_pos[1] * self.scale) - self.offset.y
        pygame.draw.circle(self.minimap_surface, (255, 0, 0), (player_x, player_y), 3)

    def is_locked(self, player_pos):
        """
        Détermine si la minimap est verrouillée autour du joueur.
        """
        # Calcul de la zone de verrouillage
        player_x, player_y = player_pos
        map_width, map_height = len(self.map_base[0]), len(self.map_base)

        # Vérifie si le joueur est suffisamment loin des bords
        if player_x > self.lock_margin and player_x < map_width - self.lock_margin and player_y > self.lock_margin and player_y < map_height - self.lock_margin:
            return True
        else:
            return False

    def Update(self, player_pos, screen):
        """
        Met à jour et dessine la minimap sur l'écran.
        """
        # Dessiner les cellules de la minimap
        self.draw_minimap(player_pos)

        # Dessiner la position du joueur sur la minimap
        self.draw_player_position(player_pos)

        # Afficher la minimap sur l'écran
        screen.blit(self.minimap_surface, self.minimap_pos)

