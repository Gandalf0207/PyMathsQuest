import heapq

# Fonction heuristique : on utilise la distance de Manhattan
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Fonction principale de l'algorithme A*
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_list:
        current = heapq.heappop(open_list)[1]
        
        # Si le but est atteint
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Chemin de start vers goal
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 4 directions (haut, bas, gauche, droite)
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Vérifier que le voisin est dans les limites et n'est pas un obstacle
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1
                
                # Si on trouve un meilleur chemin pour atteindre le voisin
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None  # Pas de chemin trouvé

# Exemple de grille
# 0 = cellule traversable, 1 = obstacle
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)  # point de départ
goal = (4, 4)   # point d'arrivée

# Exécution de l'algorithme
path = astar(grid, start, goal)
if path:
    print("Chemin trouvé :", path)
else:
    print("Aucun chemin trouvé.")
