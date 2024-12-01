from settings import *

class MiniMap:
    def __init__(self, main_map, map_base, minimap_size, screen_size):
        """
        Initialise la minimap.

        :param main_map: Carte principale (non utilisée directement ici).
        :param map_base: Base de la carte (liste 2D décrivant le type de chaque case).
        :param minimap_size: Taille (en pixels) de la minimap (carrée).
        :param screen_size: Taille de l'écran principal.
        """
        self.main_map = main_map
        self.map_base = map_base
        self.minimap_size = minimap_size
        self.screen_size = screen_size

        # Surface de la minimap (là où on dessine)
        self.minimap_surface = pygame.Surface((minimap_size, minimap_size))

        # Position de la minimap sur l'écran
        self.minimap_pos = (screen_size[0] - minimap_size - 10, 10)  # Haut droite

        # Calcul de l'échelle (réduction entre la carte et la minimap)
        map_width, map_height = len(map_base[0]), len(map_base)
        self.scale = minimap_size / max(map_width, map_height)  # Chaque case sera réduite

        # Images ou couleurs associées aux types de cellules
        self.sprite_images = self.load_sprite_images()

    def load_sprite_images(self):
        """
        Charge les surfaces ou définit les couleurs pour représenter les types de cellules.
        """
        # Chaque cellule est associée à une couleur ou une image
        return {
            "O": (0, 255, 0),  # Vert (obstacles)
            "B": (128, 128, 128),  # Gris (bordures)
            "F": (255, 255, 0),  # Jaune (fleurs)
            "M": (139, 69, 19),  # Marron (boue)
            "R": (100, 100, 100),  # Gris foncé (rocher)
            " ": (0, 200, 0),  # Vert foncé (herbe)
        }

    def draw_minimap(self):
        """
        Dessine tous les éléments de la mini-carte sur la surface.
        """
        self.minimap_surface.fill((50, 50, 50))  # Fond gris foncé

        for y, row in enumerate(self.map_base):
            for x, cell in enumerate(row):
                if cell in self.sprite_images:
                    color = self.sprite_images[cell]

                    # Calcul des dimensions et position sur la minimap
                    cell_x = int(x * self.scale)
                    cell_y = int(y * self.scale)
                    cell_size = int(self.scale)

                    # Dessiner le rectangle correspondant à la cellule
                    pygame.draw.rect(
                        self.minimap_surface,
                        color,
                        (cell_x, cell_y, cell_size, cell_size)
                    )

    def draw_player_position(self, player_pos, CASEMAP):
        """
        Dessine la position du joueur sur la minimap.
        """
        # Calcul des coordonnées du joueur sur la minimap
        player_x = int(player_pos[0] / CASEMAP * self.scale)
        player_y = int(player_pos[1] / CASEMAP * self.scale)

        # Dessiner un cercle rouge pour représenter le joueur
        pygame.draw.circle(self.minimap_surface, (255, 0, 0), (player_x, player_y), 3)

    def Update(self, player_pos, CASEMAP, screen):
        """
        Met à jour et dessine la minimap sur l'écran.

        :param player_pos: Position actuelle du joueur (en pixels).
        :param CASEMAP: Taille d'une cellule dans la carte principale.
        :param screen: Surface principale où tout est affiché.
        """
        # Dessiner les cellules de la minimap
        self.draw_minimap()

        # Dessiner la position actuelle du joueur
        self.draw_player_position(player_pos, CASEMAP)

        # Afficher la minimap sur l'écran
        screen.blit(self.minimap_surface, self.minimap_pos)
