import heapq
import math


# Fonction principale de l'algorithme A* avec déplacements en diagonale
def astar(grid, start, goal):
    vector = [goal[0] - start[0], goal[1] - start[1]]
    print(vector)
    ratio = round(vector[1] / vector[0])
    print(ratio)

    absoluteRatio = abs(ratio)

    compteurx = start[0]
    compteury = start[1]

    POS = []
    while compteury + absoluteRatio <= vector[1]:
        for i in range(2):
            compteury+= 1
            POS.append([compteury, compteurx])
            
        compteurx+=1
        POS.append([compteury, compteurx])

    return POS

            
# Exemple de grille
# 0 = cellule traversable, 1 = obstacle
grid = [
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
]

start =[0,0]  # point de départ
goal = [3,5]  # point d'arrivée

# Exécution de l'algorithme
path = astar(grid, start, goal)
if path:
    for i in path:
        grid[i[0]][i[1]] = "#"

    for i in range(len(grid)):
        print(*grid[i], sep=" ")

else:
    print("Aucun chemin trouvé.")
