from setting import *

# Fonction heuristique : on utilise la distance de Manhattan
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

        if ratio > 0:    
            compteurx+=1
        else:
            compteurx-=1
        POS.append([compteury, compteurx])

    return POS


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
        coords = [randint(((i+1)*50 -4),((i+1)*50 +4)), j*15]
        listePointRepere.append(coords)
    
    # Point du bas (dernier element)
    listePointRepere.append([randint(((i+1)*50 -4),((i+1)*50 +4)), l-1])

    print(listePointRepere)    
    
    for i in range(len(listePointRepere)-1):
        start = [listePointRepere[i][0], listePointRepere[i][1]]
        goal = [listePointRepere[i+1][0], listePointRepere[i+1][1]]
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
