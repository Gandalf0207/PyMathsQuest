from setting import *

# Ouvrir le fichier en mode écriture pour le vider
f = open("Value.json", "w")
f.write("{\n")


# Fonction de création de rivière en suivant les diagonales entre un point A et B avec déplacement haut bas gauche droite
def MastodonRiviere(start, goal):

    # Fonction pour connaitre la valeur du ratio (et agir en fonction)
    def checkValueRatio(ratio):
        if ratio > 0:
            return "Positif"
        else:
            "Negatif"

    # calcul du vector du point A ver b  / vector AB
    vector = [goal[0] - start[0], goal[1] - start[1]]
    
    # Vérification pour éviter la division par zéro
    if vector[0] == 0:
        ratio = float('inf')  # On peut aussi gérer ce cas différemment
    else:
        ratio = round(vector[1] / vector[0])

    # on passe la valeur en positif
    absoluteRatio = abs(ratio)

    # get des coords de pts référence de dépard
    compteurx = start[0]
    compteury = start[1]

    # Initialisation de la liste qui stock les déplacement à faire pour relier les pts entre eux
    POS = []
    
    # Gérer le cas où on se déplace uniquement verticalement
    if ratio == float('inf'):
        while compteury <= goal[1]:
            POS.append([compteury, compteurx])
            compteury += 1
        return POS

    # gros du travail deplacment
    while compteury + absoluteRatio <= goal[1]:
        POS.append([compteury, compteurx])
        for i in range(absoluteRatio):
            compteury += 1
            POS.append([compteury, compteurx])

        POS.append([compteury, compteurx])
        if ratio > 0:
            compteurx += 1
            POS.append([compteury, compteurx])
        elif ratio < 0:
            compteurx -= 1
            POS.append([compteury, compteurx])
    
    # finition
    if checkValueRatio(ratio) == "Positif":

        while compteury + 1 <= goal[1] or compteurx <= goal[0]:
            POS.append([compteury, compteurx])
            if compteury <= goal[1]:
                compteury += 1
                POS.append([compteury, compteurx])
                
            if compteurx <= goal[0]:
                POS.append([compteury, compteurx])    
                compteurx += 1
                POS.append([compteury, compteurx])
    else:
        while compteury + 1 <= goal[1] or compteurx >= goal[0]:
            POS.append([compteury, compteurx])
            if compteury <= goal[1]:
                compteury += 1
                POS.append([compteury, compteurx])
                
            if compteurx >= goal[0]:
                POS.append([compteury, compteurx])    
                compteurx -= 1
                POS.append([compteury, compteurx])
    return POS



# settings map
Longueur = 150
largeur = 75

# infos items
OBSTACLES = 200
OBSTACLES = 200
CASCADE = (0,10)

# placement pnj (ne tombre jamais sur les coords de la rivière)
PNJ = [[randint(5, largeur-5), randint(1+5,((Longueur//3) -5))], 
       [randint(5, largeur-5), randint(((Longueur//3)+5), (Longueur//3)*2 -5)], 
       [randint(5, largeur-5), randint(((Longueur//3)*2 +5), Longueur-5)]
    ]

# creation map base
Map = []
for i in range(largeur):
    mapTempo = []
    for j in range(Longueur):
        mapTempo.append("-")
    Map.append(mapTempo)



# création 2 rivières--------------------------------
for i in range(2):
    listeCheminRiviere = []
    listePointRepere = [] # initialisation de la list des pts repères

    # Point du haut (premier element)
    listePointRepere.append([randint(((i+1)*50 -4),((i+1)*50 +4)), 4])

    # Point du haut en bas
    for j in range(1, largeur//15):

        # Tout les autres pts de repère
        coords = [randint(((i+1)*50 -4),((i+1)*50 +4)), j*15]
        listePointRepere.append(coords)
    
    
    # Point du bas (dernier element)
    listePointRepere.append([randint(((i+1)*50 -4),((i+1)*50 +4)), largeur-4])

    # On ajoute les pts repère sur la map + les point spéciaux (haut et bas ) directement car collision avec montagne, donc il faut une ligne de 4 droite minimum
    for j in range(1,5):
        Map[4 -j][listePointRepere[0][0]] = "#"
        listeCheminRiviere.append([4 -j,listePointRepere[0][0]])

    for j in listePointRepere:
        Map[j[1]][j[0]] = "#"
        listeCheminRiviere.append([j[1],j[0]])

    for j in range(0,5):
        Map[largeur-5 +j][listePointRepere[-1][0]] = "#"
        listeCheminRiviere.append([largeur-5 +j,listePointRepere[-1][0]])


    
    # Pour tout les points repère, on lie des point A et B entre eux avec le script crée pour l'occasion
    for j in range(len(listePointRepere)-1):
        Map[listePointRepere[j][1]][listePointRepere[j][0]] = "#"
        start = [listePointRepere[j][0], listePointRepere[j][1]]
        goal = [listePointRepere[j+1][0], listePointRepere[j+1][1]]
        path = MastodonRiviere(start, goal)


        # On recup la list de déplcement et on ajoute la rivière à la map
        for coords in path:
            Map[coords[0]][coords[1]] = "#"
            listeCheminRiviere.append([coords[0],coords[1]])



    # Ajouter la rivière dans les données
    donnees = listeCheminRiviere
    # Sauvegarder les données dans le fichier JSON     
    f.write(f""" "Riviere{i}" : {donnees}, \n""")
        


# placement des pnj sur la map 
for i in PNJ:
    Map[i[0]][i[1]] = "P"
f.write(f""" "PNJ Coords" : {PNJ}, \n """)

# On affiche la map pour verif
for i in range(len(Map)):
    print(*Map[i], sep=" ")




# arbre à couper / pont tronc d'abre 

# pont
# herbe (alt 1 2 3)
# obstacles
# montagnes 
# cascade
# passage niveau suivant (cailloux)

f.write(f""""EndValue" : null""")

f.write("\n}")
