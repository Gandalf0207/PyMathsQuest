from settings import *


def LoadJsonValueSpecifiqueFolder(index1 :str, pathFolder) -> list:
    """Récupération des valeur stockées dans le fichier json pour les renvoyer quand nécéssaire à l'aide des indices données pour les récupérer"""
    
    # récupération des valeurs stocké dans le json
    with open(pathFolder, "r", encoding="utf-8") as f: # ouvrir le fichier json en mode e lecture
        loadElementJson = json.load(f) # chargement des valeurs
    return loadElementJson.get(index1, None) # on retourne les valeurs aux indices de liste quisont données



def LoadTexte():
    """Méthode de création du fichier de dialogue
    Input / Output : None"""
    DIALOGUEALL = {
        "Fr" : LoadJsonValueSpecifiqueFolder("DialoguesFr", join("data", "dialogueNPC.json")),
        "En" : LoadJsonValueSpecifiqueFolder("DialoguesEn", join("data", "dialogueNPC.json")),
        "Es" : LoadJsonValueSpecifiqueFolder("DialoguesEs", join("data", "dialogueNPC.json")), 
    }

    ELEMENTSALL = {
        "Fr" :  LoadJsonValueSpecifiqueFolder("ElementsFr", join("data", "text.json")),
        "En" :  LoadJsonValueSpecifiqueFolder("ElementsEn", join("data", "text.json")),
        "Es" :  LoadJsonValueSpecifiqueFolder("ElementsEs", join("data", "text.json")),  
    }

    COURS = {
        "Fr" : LoadJsonValueSpecifiqueFolder("CoursFr", join("data", "cours.json")),
        "En" : LoadJsonValueSpecifiqueFolder("CoursEn", join("data", "cours.json")),
        "Es" : LoadJsonValueSpecifiqueFolder("CoursEs", join("data", "cours.json")),
    }

    for keyLangue in DICOLANGUE:
        if DICOLANGUE[keyLangue]:
            TEXTE["Dialogues"] = DIALOGUEALL[keyLangue]
            TEXTE["Elements"] = ELEMENTSALL[keyLangue]
            TEXTE["Cours"] = COURS[keyLangue]

