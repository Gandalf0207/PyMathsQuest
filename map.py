from setting import *
import heapq
import math

# Fonction heuristique : on utilise la distance de Manhattan
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Fonction principale de l'algorithme A* avec déplacements en diagonale
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    # Directions : 8 directions (haut, bas, gauche, droite, et diagonales)
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # Haut, Bas, Gauche, Droite
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonales
    ]

    while open_list:
        current = heapq.heappop(open_list)[1]
        
        # Si le but est atteint
        if current == goal:
            path = []
            while current in came_from:
                path.append(list(current))  # Conversion tuple -> liste
                current = came_from[current]
            path.append(list(start))  # Conversion tuple -> liste pour le départ
            return path[::-1]  # Chemin de start vers goal sous forme de liste de listes
        
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Vérifier que le voisin est dans les limites et n'est pas un obstacle
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == "-":
                # Calcul du coût pour le mouvement (1 pour horizontal/vertical, 1.41 pour diagonal)
                move_cost = 1 if dx == 0 or dy == 0 else math.sqrt(2)
                tentative_g_score = g_score[current] + move_cost
                
                # Si on trouve un meilleur chemin pour atteindre le voisin
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None  # Pas de chemin trouvé



L = 150
l = 75

PNJ = [[randint(0+3, l-3), randint(1+5,((L//3) -5))], 
       [randint(0+3, l-3), randint(((L//3)+5), (L//3)*2 -5)], 
       [randint(0+3, l-3), randint(((L//3)*2 +5), L)]
    ]


OBSTACLES = 200
OBSTACLES = 200
CASCADE = (0,10)
Map = []


for i in range(l):
    m = []
    for j in range(L):
        m.append("-")
    Map.append(m)


# Place de la rivière
# ligne avec pts de reference tout les 15pts
# couloir de 9 point

for i in range(2):
    listePointRepere = []
    for j in range(l//15):
 
        # Tout les autres pts de repère
        coords = [j*15, randint(((i+1)*50 -4),((i+1)*50 +4))]
        listePointRepere.append(coords)
    
    # Point du bas (dernier element)
    listePointRepere.append([l-1, randint(((i+1)*50 -4),((i+1)*50 +4))])

    print(listePointRepere)    
    
    for i in range(len(listePointRepere)-1):
        start = (listePointRepere[i][0], listePointRepere[i][1])
        goal = (listePointRepere[i+1][0], listePointRepere[i+1][1])
        path = astar(Map, start, goal)
    
        if path:
            for i in path:
                Map[i[0]][i[1]] = "#"

for i in range(len(Map)):
    print(*Map[i], sep=" ")


# Script A* à reprendre 




# Place des pnj
for i in PNJ:
    Map[i[0]][i[1]] = "P"


# for i in range(len(Map)):
#         print(*Map[i], sep=" ")

# pnj 
# arbre à couper / pont tronc d'abre 
# rivière
# pont
# herbe (alt 1 2 3)
# obstacles
# montagnes 
# cascade
# passage niveau suivant (cailloux)
