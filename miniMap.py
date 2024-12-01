from settings import *
from sprites import *


class MiniMap():
    def __init__(self, map, mapBase, minimap_size, screen_size, allSprites):

        self.allSprites = allSprites    
        self.main_map = map
        self.base_map = mapBase
        self.minimap_size = minimap_size
        self.screen_size = screen_size
        self.minimap_surface = pygame.Surface((minimap_size, minimap_size))
        self.scale = minimap_size / max(len(mapBase[0]), len(mapBase))  # Échelle de réduction
        self.minimap_pos = (screen_size[0] - minimap_size - 10, 10)  # Position en haut à droite

    def MakeMinimap(self):

        self.minimap_surface.fill((50, 50, 50))  # Fond de la minimap (gris foncé)

        # Dessiner chaque case de la minimap
        for y, row in enumerate(self.base_map):
            for x, cell in enumerate(row):
                color = self.get_cell_color(cell)
                if color:
                    rect = pygame.Rect(x * self.scale, y * self.scale, self.scale, self.scale)
                    Sprites()
                    pygame.draw.rect(self.minimap_surface, color, rect)

        # Dessiner la position actuelle du joueur sur la minimap
        player_cell_x = int(player_pos[0] // CASEMAP * self.scale)
        player_cell_y = int(player_pos[1] // CASEMAP * self.scale)
        pygame.draw.circle(self.minimap_surface, (255, 0, 0), (player_cell_x, player_cell_y), 3)  # Cercle rouge

        # Afficher la minimap sur l'écran principal
        screen.blit(self.minimap_surface, self.minimap_pos)

    def get_cell_color(self, cell_type):
        """
        Renvoie la couleur associée au type de cellule.

        :param cell_type: Le type de cellule (exemple : "O", "#", etc.).
        :return: La couleur (tuple RGB) ou None si le type est inconnu.
        """
        color_map = {
            "O": (0, 255, 0),  # Vert (obstacles)
            "#": (0, 0, 255),  # Bleu (rivière)
            "B": (128, 128, 128),  # Gris (bordures)
            "F": (255, 255, 0),  # Jaune (fleurs)
            "M": (139, 69, 19),  # Marron (boue)
            "R": (100, 100, 100),  # Gris foncé (rocher)
            " ": (0, 200, 0),  # Vert foncé (herbe)
        }
        return color_map.get(cell_type, None)
