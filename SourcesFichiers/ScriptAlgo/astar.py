### Script conçu avec IA 

from settings import *


class Astar(object):
    def __init__(self, start, goal, mapCalcul, pathAccessible) -> None:
        # Initialisation des coordonnées (x, y) pour start et goal
        self.start = (start[0], start[1])
        self.goal = (goal[0], goal[1])
        self.mapCalcul = mapCalcul
        self.pathAccessible = pathAccessible
        self.parents = {}  # Nouveau dictionnaire pour suivre les parents

    def __heuristic__(self, a, b):
        # Distance de Manhattan entre les points a et b
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

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
                return path[::-1]  # Retourne le chemin dans l'ordre du départ vers le but

            # Exploration des voisins du point courant
            for dx, dy in directions:  # dx et dy sont utilisés directement ici
                neighbor = (current[0] + dx, current[1] + dy)  # Calcul du voisin (x, y)

                # Vérification que le voisin est dans les limites de la grille et accessible (valeur 0)
                if (0 <= neighbor[1] < len(self.mapCalcul) and
                    0 <= neighbor[0] < len(self.mapCalcul[0]) and
                    self.mapCalcul[neighbor[1]][neighbor[0]] in self.pathAccessible):  # 0 signifie accessible

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



class Astar2(object):
    def __init__(self, start, goal, mapCalcul, pathAccessible, band_width = 0) -> None:
        self.start = (start[0], start[1])
        self.goal = (goal[0], goal[1])
        self.mapCalcul = mapCalcul
        self.pathAccessible = pathAccessible
        self.band_width = band_width
        self.parents = {}

    def __heuristic__(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def __is_band_accessible__(self, current, direction):
        dx, dy = direction
        for offset in range(-self.band_width, self.band_width + 1):
            if dx != 0:
                neighbor = (current[0], current[1] + offset)
            else:
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

                band_path = set()
                for i in range(len(path) - 1):
                    start = path[i]
                    end = path[i + 1]

                    band_path.add(start)

                    if start[0] == end[0]:
                        for offset in range(-self.band_width, self.band_width + 1):
                            band_path.add((start[0] + offset, start[1]))
                    elif start[1] == end[1]:
                        for offset in range(-self.band_width, self.band_width + 1):
                            band_path.add((start[0], start[1] + offset))

                # Ajout du segment de bande pour le point start
                if len(path) > 1:
                    for offset in range(-self.band_width, self.band_width + 1):
                        if path[0][0] == path[1][0]:  # Mouvement vertical
                            band_path.add((self.start[0] + offset, self.start[1]))
                        elif path[0][1] == path[1][1]:  # Mouvement horizontal
                            band_path.add((self.start[0], self.start[1] + offset))

                # Ajout du dernier segment de bande pour le point goal
                if len(path) > 1:
                    for offset in range(-self.band_width, self.band_width + 1):
                        if path[-2][0] == self.goal[0]:  # Mouvement vertical
                            band_path.add((self.goal[0] + offset, self.goal[1]))
                        elif path[-2][1] == self.goal[1]:  # Mouvement horizontal
                            band_path.add((self.goal[0], self.goal[1] + offset))
                band_path.add(self.goal)
                
                # Remplacer les 'V' par des points accessibles
                corrected_path = []
                for point in band_path:
                    if self.mapCalcul[point[1]][point[0]] in self.pathAccessible:
                        corrected_path.append(point)
                
                return corrected_path

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

