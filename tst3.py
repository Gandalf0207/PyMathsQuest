import heapq

def astar(grid, start, goal):
    def heuristic(a, b):
        # Calcul de la distance de Manhattan ou diagonale (selon les déplacements)
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(node):
        # Retourne les voisins possibles, en incluant les déplacements diagonaux
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            x, y = node[0] + dx, node[1] + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "-":
                neighbors.append((x, y))
        return neighbors

    # Initialisation des listes de priorités et des coûts
    open_list = []
    closed_list = set()
    g_costs = {start: 0}
    f_costs = {start: heuristic(start, goal)}
    came_from = {}

    # Utilisation d'une heap pour gérer le nœud avec le plus faible f
    heapq.heappush(open_list, (f_costs[start], start))

    while open_list:
        current_f, current = heapq.heappop(open_list)
        
        # Si on atteint le but, on reconstruit le chemin
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        closed_list.add(current)
        
        for neighbor in get_neighbors(current):
            if neighbor in closed_list:
                continue

            tentative_g = g_costs[current] + 1  # Coût pour aller vers un voisin
            
            if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                came_from[neighbor] = current
                g_costs[neighbor] = tentative_g
                f_costs[neighbor] = tentative_g + heuristic(neighbor, goal)
                if neighbor not in [i[1] for i in open_list]:
                    heapq.heappush(open_list, (f_costs[neighbor], neighbor))

    return None  # Aucun chemin trouvé

# Exemple de grille
grid = [
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
]

start = (0, 0)  # point de départ
goal = (3, 4)   # point d'arrivée

# Exécution de l'algorithme
path = astar(grid, start, goal)
if path:
    for i in path:
        grid[i[0]][i[1]] = "#"

    for i in range(len(grid)):
        print(*grid[i], sep=" ")

else:
    print("Aucun chemin trouvé.")
