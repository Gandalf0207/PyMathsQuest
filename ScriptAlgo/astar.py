import heapq

class Astar(object):
    def __init__(self, start, goal, mapCalcul, pathAccessible) -> None:
        # Initialisation des coordonnées (x, y) pour start et goal
        self.start = (start[0], start[1])
        self.goal = (goal[0], goal[1])
        self.mapCalcul = mapCalcul
        self.pathAccessible = pathAccessible

    def __heuristic__(self, a, b):
        # Distance de Manhattan entre les points a et b
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def a_star(self):
        open_list = []
        heapq.heappush(open_list, (0, self.start))  # Initialisation de la liste ouverte avec le point de départ
        g_score = {self.start: 0}  # Coût du chemin le plus court trouvé jusqu'à chaque point
        f_score = {self.start: self.__heuristic__(self.start, self.goal)}  # Coût total estimé (f = g + h)
        
        # Directions possibles (droite, bas, gauche, haut)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while open_list:
            # Choisir le noeud avec le coût le plus bas (f_score) dans la liste ouverte
            current = heapq.heappop(open_list)[1]

            # Si on atteint le but, on renvoie True
            if current == self.goal:
                return True

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

        # Si on n'a pas trouvé de chemin, retourner False
        return False
