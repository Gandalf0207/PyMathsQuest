### Script conçu avec IA 

from settings import *

class Astar(object):
    def __init__(self, start, goal, mapCalcul, pathAccessible, band_width = 0) -> None:
        # Initialisation des coordonnées (x, y) pour start et goal
        self.start = (start[0], start[1])
        self.goal = (goal[0], goal[1])
        self.mapCalcul = mapCalcul
        self.pathAccessible = pathAccessible
        self.band_width = band_width  # Largeur de la bande
        self.parents = {}  # Nouveau dictionnaire pour suivre les parents

    def __heuristic__(self, a, b):
        # Distance de Manhattan entre les points a et b
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def __is_band_accessible__(self, current, direction):
        # Vérifie que toute la bande est accessible dans la direction donnée
        dx, dy = direction
        for offset in range(-self.band_width, self.band_width + 1):
            if dx != 0:  # Déplacement horizontal
                neighbor = (current[0], current[1] + offset)
            else:  # Déplacement vertical
                neighbor = (current[0] + offset, current[1])
                
            if not (0 <= neighbor[1] < len(self.mapCalcul) and
                    0 <= neighbor[0] < len(self.mapCalcul[0]) and
                    self.mapCalcul[neighbor[1]][neighbor[0]] in self.pathAccessible):
                return False

        return True

    def a_star(self):
        import heapq

        open_list = []
        heapq.heappush(open_list, (0, self.start))  # Initialisation de la liste ouverte avec le point de départ
        g_score = {self.start: 0}  # Coût du chemin le plus court trouvé jusqu'à chaque point
        f_score = {self.start: self.__heuristic__(self.start, self.goal)}  # Coût total estimé (f = g + h)
        
        # Directions possibles (droite, bas, gauche, haut)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while open_list:
            # Choisir le noeud avec le coût le plus bas (f_score) dans la liste ouverte
            current = heapq.heappop(open_list)[1]

            # Si on atteint le but, on reconstruit le chemin
            if current == self.goal:
                path = []
                while current in self.parents:
                    path.append(current)
                    current = self.parents[current]
                path.append(self.start)
                
                # Ajout des coordonnées de la bande pour chaque point du chemin
                band_path = []
                for point in path:
                    for offset in range(-self.band_width, self.band_width + 1):
                        if (point[0] + offset, point[1]) not in band_path:
                            band_path.append((point[0] + offset, point[1]))
                        if (point[0], point[1] + offset) not in band_path:
                            band_path.append((point[0], point[1] + offset))
                return band_path[::-1]  # Retourne le chemin dans l'ordre du départ vers le but avec les coordonnées de la bande

            # Exploration des voisins du point courant
            for direction in directions:  # dx et dy sont utilisés directement ici
                neighbor = (current[0] + direction[0], current[1] + direction[1])  # Calcul du voisin (x, y)

                # Vérification que le voisin est dans les limites de la grille et accessible pour toute la bande
                if self.__is_band_accessible__(current, direction):
                    tentative_g_score = g_score[current] + 1  # Tentative de coût total (g + 1)

                    # Si ce chemin vers le voisin est meilleur, on le met à jour
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + self.__heuristic__(neighbor, self.goal)
                        heapq.heappush(open_list, (f_score[neighbor], neighbor))
                        
                        # Mise à jour du parent
                        self.parents[neighbor] = current

        # Si on n'a pas trouvé de chemin, retourner une liste vide
        return False
