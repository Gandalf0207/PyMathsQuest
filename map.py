from setting import *
from jeuDeLaVie import *

import json
data = {
    "coordsMapBase" : {
        "Montagnes Coords": "null",
        "Riviere0 Coords" : "null",
        "Riviere1 Coords" : "null",
        "Flowers Coords" : "null",
        "AllMap" : "null"
    },

    "coordsMapObject" : {
        "Obstacles Coords" : "null",
        "PNJ Coords" : "null",
        "ArbreSpecial Coords" : "null"
    }
}

# Ouvrir le fichier en mode écriture pour le vider
with open("Value.json", "w") as valueFileJson:
    json.dump(data, valueFileJson, indent=4)


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
            POS.append([compteury,compteurx])
            compteury += 1
        return POS

    # gros du travail deplacment
    while compteury + absoluteRatio <= goal[1]:
        POS.append([compteury,compteurx])
        for i in range(absoluteRatio):
            compteury += 1
            POS.append([compteury,compteurx])

        POS.append([compteury,compteurx])
        if ratio > 0:
            compteurx += 1
            POS.append([compteury,compteurx])
        elif ratio < 0:
            compteurx -= 1
            POS.append([compteury,compteurx])
    
    # finition
    if checkValueRatio(ratio) == "Positif":

        while compteury + 1 <= goal[1] or compteurx <= goal[0]:
            POS.append([compteury, compteurx])
            if compteury <= goal[1]:
                compteury += 1
                POS.append([compteury,compteurx])
                
            if compteurx <= goal[0]:
                POS.append([compteury,compteurx])    
                compteurx += 1
                POS.append([compteury,compteurx])
    else:
        while compteury + 1 <= goal[1] or compteurx >= goal[0]:
            POS.append([compteury, compteurx])
            if compteury <= goal[1]:
                compteury += 1
                POS.append([compteury,compteurx])
                
            if compteurx >= goal[0]:
                POS.append([compteury,compteurx])    
                compteurx -= 1
                POS.append([compteury,compteurx])
    return POS

def PlacementSpeciauxRiviere(Map, index1, index2, element):
    def checkPos(indice):
        print(indice, " element list")
        listElementTerrain = ["-", "H"]
        if Map[indice[0]][indice[1]-1] in listElementTerrain:
            if ((Map[indice[0]][indice[1]-2] in listElementTerrain )and( Map[indice[0]][indice[1]+1] in listElementTerrain) and (indice[0] >=10) and (indice[0] <= 65)):
                return True
            else:
                return False
        else:
            return False
        
    with open("Value.json", "r") as f:
        loadElementJson = json.load(f)
    listeCoordsElement = loadElementJson[index1].get(index2, None)

    Go = True
    while Go:
        indice = randint(0, largeur-1)
        print(indice, " numéro")
        if checkPos(listeCoordsElement[indice]):
            Go = False
    itemCoords = listeCoordsElement[indice]
    Map[itemCoords[0]][itemCoords[1]-1] = element

    return [itemCoords[0],itemCoords[1]-1]



def writeJsonValue(liste, index1, index2):
        # Chargement des données JSON si elles existent, sinon crée un dictionnaire vide
    try:
        with open("Value.json", "r") as f:
            donnees = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        assert ValueError("Error load JSON file")

    # Ajouter la rivière dans les données
    donnees[f"{index1}"][f"{index2}"] = liste

    # Sauvegarder les données dans le fichier JSON avec une indentation pour un format lisible
    with open("Value.json", "w") as f:
        json.dump(donnees, f, indent=4)
 


# settings map
Longueur = 150
largeur = 75

# infos items
OBSTACLES = 200
OBSTACLES = 200
CASCADE = (0,10)


# creation map base
Map = []
for i in range(largeur):
    mapTempo = []
    for j in range(Longueur):
        mapTempo.append("-")
    Map.append(mapTempo)

# --------------------------Element map de base-----------------------------------------------# 

# positions des chaines de montagnes : 
listeMontagne = []
for i in range(2):
    for j in range(Longueur):
        Map[i*(largeur-1)][j] = "M"
        listeMontagne.append([i*(largeur-1), j])
    for j in range(largeur):
        Map[j][i*(Longueur-1)] = "M"
        listeMontagne.append([j, i*(Longueur-1)])

writeJsonValue(listeMontagne, "coordsMapBase", "Montagnes Coords")

# création 2 rivières--------------------------------
for i in range(2):
    listeCheminRiviere = []
    listePointRepere = [] # initialisation de la list des pts repères

    # Point du haut (premier element)
    listePointRepere.append([randint(((i+1)*50 -4),((i+1)*50 +4)),4])

    # Point du haut en bas
    nbPts = largeur // 15      
    verifLigne5 = randint(1,(nbPts-1)) # choix du lieu pour la ligne de 5 droite pour sécu 

    for j in range(1, nbPts):
        if verifLigne5 == j: # ajout du pts A et B pour une ligne de 5 toute droite pour sécu placement des pnj autour de la riviere
            pACoordsligne5 = [randint(((i+1)*50 -4),((i+1)*50 +4)),j*15]
            listePointRepere.append(pACoordsligne5)
            pBcoordsligne5 = [pACoordsligne5[0], j*15 + 5]
            listePointRepere.append(pBcoordsligne5)

        else:
            # Tout les autres pts de repère
            coords = [randint(((i+1)*50 -4),((i+1)*50 +4)),j*15]
            listePointRepere.append(coords)
    
    
    # Point du bas (dernier element)
    listePointRepere.append([randint(((i+1)*50 -4),((i+1)*50 +4)),largeur-4])

    # On ajoute les pts repère sur la map + les point spéciaux (haut et bas ) directement car collision avec montagne, donc il faut une ligne de 4 droite minimum
    for j in range(1,5):
        Map[5 -j][listePointRepere[0][0]] = "#"
        listeCheminRiviere.append([5-j,listePointRepere[0][0]])

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

    writeJsonValue(listeCheminRiviere, "coordsMapBase", f"Riviere{i} Coords")

# placement de l'herbe (Alt 1 et 2 et 3) avec jeu de la vie
jeuDeLaVie= JeuDeLaVie()
jeuDeLaVie.Base()
getPosFlower = jeuDeLaVie.Update()
listeFlowerCoords = []
for i in getPosFlower:
    if Map[i[0]][i[1]] =="-":
        Map[i[0]][i[1]] = "H"
        listeFlowerCoords.append([i[0], i[1]])

writeJsonValue(listeFlowerCoords, "coordsMapBase", "Flowers Coords")



writeJsonValue(Map, "coordsMapBase", "AllMap")

# --------------------------Element rajouté sur la map-----------------------------------------------# 

#placement des obstacle sur la map
listeObstacle = []
for i in range(OBSTACLES):
    pos = [randint(4, largeur-4), randint(4, Longueur-4)]
    while Map[pos[0]][pos[1]] != '-': # check de s'il y a déjà des éléments sur la map.
        pos = [randint(4, largeur-4), randint(4, Longueur-4)]
    Map[pos[0]][pos[1]] = "O"
    listeObstacle.append(pos)

writeJsonValue(listeObstacle, "coordsMapObject", "Obstacles Coords")



# placement pnj (ne tombre jamais sur les coords de la rivière)
PNJ = [[randint(5, largeur-5), randint(1+5,((Longueur//3) -5))], 
      None, #pnj à deplacer 
       [randint(5, largeur-5), randint(((Longueur//3)*2 +5), Longueur-5)]
    ]

# placement des pnj sur la map 
for i in PNJ:
    if i != None:
        Map[i[0]][i[1]] = "P"

PNJ[1] = PlacementSpeciauxRiviere(Map, "coordsMapBase", "Riviere1 Coords", "P") 
writeJsonValue(PNJ, "coordsMapObject", "PNJ Coords")

# placement arbre spécial 
arbreSpecial = PlacementSpeciauxRiviere(Map,"coordsMapBase", "Riviere0 Coords", "A") 
writeJsonValue(arbreSpecial, "coordsMapObject", "AbreSpecial Coords")










# passage niveau suivant (cailloux)


# set up fichier json basique
# modifier chaque variable quand nécessaire

# ==> avoir un fichier json clair et beau :sparkles:















































# On affiche la map pour verif
for i in range(len(Map)):
    print(*Map[i], sep=" ")
