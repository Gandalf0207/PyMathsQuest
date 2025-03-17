from settings import *


def LoadJsonMapValueSpecifiqueFolder(index1 :str, pathFolder) -> list:
    """Récupération des valeur stockées dans le fichier json pour les renvoyer quand nécéssaire à l'aide des indices données pour les récupérer"""
    
    # récupération des valeurs stocké dans le json
    with open(pathFolder, "r", encoding="utf-8") as f: # ouvrir le fichier json en mode e lecture
        loadElementJson = json.load(f) # chargement des valeurs
    return loadElementJson.get(index1, None) # on retourne les valeurs aux indices de liste quisont données



def LoadTexte():
    """Méthode de création du fichier de dialogue
    Input / Output : None"""
    DIALOGUEALL = {
        "Fr" : LoadJsonMapValueSpecifiqueFolder("DialoguesFr", join("data", "dialogueNPC.json")),
        "En" : LoadJsonMapValueSpecifiqueFolder("DialoguesEn", join("data", "dialogueNPC.json")),
        "Es" : LoadJsonMapValueSpecifiqueFolder("DialoguesEs", join("data", "dialogueNPC.json")), 
    }

    ELEMENTSALL = {
        "Fr" :  LoadJsonMapValueSpecifiqueFolder("ElementsFr", join("data", "text.json")),
        "En" :  LoadJsonMapValueSpecifiqueFolder("ElementsEn", join("data", "text.json")),
        "Es" :  LoadJsonMapValueSpecifiqueFolder("ElementsEs", join("data", "text.json")),  
    }

    COURS = {
        "Fr" : LoadJsonMapValueSpecifiqueFolder("CoursFr", join("data", "cours.json")),
        "En" : LoadJsonMapValueSpecifiqueFolder("CoursEn", join("data", "cours.json")),
        "Es" : LoadJsonMapValueSpecifiqueFolder("CoursEs", join("data", "cours.json")),
    }

    for keyLangue in DICOLANGUE:
        if DICOLANGUE[keyLangue]:
            TEXTE["Dialogues"] = DIALOGUEALL[keyLangue]
            TEXTE["Elements"] = ELEMENTSALL[keyLangue]
            TEXTE["Cours"] = COURS[keyLangue]

