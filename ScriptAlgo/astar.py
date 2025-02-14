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
        heapq.heappush(open_list, (0, self.start))
        g_score = {self.start: 0}
        f_score = {self.start: self.__heuristic__(self.start, self.goal)}

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while open_list:
            current = heapq.heappop(open_list)[1]

            if current == self.goal:
                path = []
                while current in self.parents:
                    path.append(current)
                    current = self.parents[current]
                path.append(self.start)
                path.reverse()

                # Construction précise de la bande
                band_path = set()
                for i in range(len(path) - 1):
                    start = path[i]
                    end = path[i + 1]

                    # Ajout des points sur l'axe principal
                    band_path.add(start)

                    # Ajout de la bande sur le segment entre start et end
                    if start[0] == end[0]:  # Mouvement vertical
                        for offset in range(-self.band_width, self.band_width + 1):
                            band_path.add((start[0] + offset, start[1]))
                    elif start[1] == end[1]:  # Mouvement horizontal
                        for offset in range(-self.band_width, self.band_width + 1):
                            band_path.add((start[0], start[1] + offset))

                # Ajout du dernier point
                band_path.add(path[-1])
                return list(band_path)

            for direction in directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])

                if self.__is_band_accessible__(neighbor, direction):
                    tentative_g_score = g_score[current] + 1

                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_g_score + self.__heuristic__(neighbor, self.goal)
                        heapq.heappush(open_list, (f_score[neighbor], neighbor))
                        self.parents[neighbor] = current

        return False

