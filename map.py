from setting import *



# niveau rivière 

L = 150
l = 75

PNJ = [[randint(1,(l//3)-3), randint(1,L//3)], 
       [randint((l//3) +2, (l//3)*2 -2), randint(L//3, (L//3)*2)], 
       [randint((l//3)*2 +2, l), randint((L//3)*2+ 2, L)]
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
    for j in range(l//15):
        Map[j*15][randint((i+1)*50 -4,(i+1)*50 +4 )] = "R"


# Place des pnj
for i in PNJ:
    Map[i[0]][i[1]] = "P"


for i in range(len(Map)):
        print(*Map[i], sep=" ")

# pnj 
# arbre à couper / pont tronc d'abre 
# rivière
# pont
# herbe (alt 1 2 3)
# obstacles
# montagnes 
# cascade
# passage niveau suivant (cailloux)
