from SourcesFichiers.Ressources.Texte.dialogues import *
from SourcesFichiers.Ressources.Texte.elements import *

def LoadTexte():
    """Méthode de création du fichier de dialogue
    Input / Output : None"""
    DIALOGUEALL = {
        "Fr" : DialoguesFr,
        "En" : DialoguesEn,
        "Es" : DialoguesEs, 
    }

    ELEMENTSALL = {
        "Fr" : ElementsFr,
        "En" : ElementsEn,
        "Es" : ElementsEs,  
    }


    for keyLangue in DICOLANGUE:
        if DICOLANGUE[keyLangue]:
            TEXTE["Dialogues"] = DIALOGUEALL[keyLangue]
            TEXTE["Elements"] = ELEMENTSALL[keyLangue]

