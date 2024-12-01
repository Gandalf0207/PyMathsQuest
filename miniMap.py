from settings import *  # Assurez-vous que les constantes sont bien définies dans settings.py

class MiniMap:
    def __init__(self, game_map, screen, minimap_size=(200, 100)):
        """
        :param game_map: La carte principale (double liste).
        :param screen: L'écran Pygame sur lequel afficher la minimap.
        :param minimap_size: Taille de la minimap à afficher (en pixels).
        """
        self.game_map = game_map
        self.screen = screen
        self.minimap_size = minimap_size

        self.map_width = len(game_map[0])  # Largeur de la carte
        self.map_height = len(game_map)    # Hauteur de la carte

        # Calcul du facteur de réduction pour la minimap
        self.cell_width = self.minimap_size[0] // self.map_width
        self.cell_height = self.minimap_size[1] // self.map_height

        # Créer une surface pour la minimap complète
        self.minimap_surface = pygame.Surface(self.minimap_size)

        # Remplir la minimap avec les éléments de la carte
        self._generate_full_minimap()

    def _generate_full_minimap(self):
        """
        Génère toute la minimap en réduisant la carte complète.
        """
        for y in range(self.map_height):
            for x in range(self.map_width):
                # Calculer la couleur à partir de la case
                if self.game_map[y][x] == "O":
                    color = (0, 255, 0)  # Vert
                elif self.game_map[y][x] == "#":
                    color = (0, 0, 0)  # Noir
                else:
                    color = (200, 200, 200)  # Gris clair

                # Calculer la position sur la minimap
                minimap_x = x * self.cell_width
                minimap_y = y * self.cell_height

                # Dessiner la case sur la minimap
                pygame.draw.rect(self.minimap_surface, color, (minimap_x, minimap_y, self.cell_width, self.cell_height))

    def update(self, player_pos):
        """
        Déplace le focus de la minimap autour du joueur.
        """
        map_x, map_y = player_pos

        # Calculer les bords de la portion visible de la minimap (focus autour du joueur)
        focus_width = self.minimap_size[0] // 4  # Par exemple, afficher un quart de la minimap autour du joueur
        focus_height = self.minimap_size[1] // 4

        focus_x = (map_x - focus_width // 2) * self.cell_width
        focus_y = (map_y - focus_height // 2) * self.cell_height

        # Limiter le focus à l'intérieur de la minimap
        focus_x = max(0, min(focus_x, self.minimap_size[0] - focus_width))
        focus_y = max(0, min(focus_y, self.minimap_size[1] - focus_height))

        # Afficher la minimap
        self.screen.blit(self.minimap_surface, (10, 10))
        pygame.draw.rect(self.screen, (255, 0, 0), (10 + focus_x, 10 + focus_y, focus_width, focus_height), 2)  # Focus rouge
