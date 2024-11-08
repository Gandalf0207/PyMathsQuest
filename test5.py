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
with open("Value2.json", "w") as valueFileJson:
    json.dump(data, valueFileJson, indent=4)



def writeJsonValue(liste, index1, index2):
        # Chargement des données JSON si elles existent, sinon crée un dictionnaire vide
    try:
        with open("Value2.json", "r") as f:
            donnees = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        assert ValueError("Error load JSON file")

    # Ajouter la rivière dans les données
    # liste_str = json.dumps(liste)
    donnees[f"{index1}"][f"{index2}"] = liste
    # Sauvegarder les données dans le fichier JSON avec une indentation pour un format lisible
    with open("Value2.json", "w") as f:
        json.dump(donnees, f, indent=4)
 

# settings map
Longueur = 15
largeur = 15

# creation map base
Map = []
for i in range(largeur):
    mapTempo = []
    for j in range(Longueur):
        mapTempo.append("-")
    Map.append(mapTempo)

writeJsonValue(Map, "coordsMapBase", "AllMap")
