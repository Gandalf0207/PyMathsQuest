from Sources.Texte.dialogues import *
from Sources.Texte.elements import *

def LoadTexte():
    """Méthode de création du fichier de dialogue
    Input / Output : None"""

    TEXTE["Dialogues"] = DialoguesFr if INFOS["Langue"] == "Fr" else DialoguesEn
    TEXTE["Elements"] = ElementsFr if INFOS["Langue"] == "Fr" else ElementsEn
