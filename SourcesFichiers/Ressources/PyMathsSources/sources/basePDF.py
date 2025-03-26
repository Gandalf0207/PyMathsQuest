from pylatex import *
from pylatex.utils import *
from datetime import datetime

class HeaderFooter(object):
    def __init__(self, doc, typeExo) -> None:
        self.doc = doc
        self.typeExo = typeExo
        # Ajout d'un style de page personnalisé
        self.header = PageStyle("header")
        self.now = datetime.now()
        self.time = self.GetTime()

    def HeaderFooterPage(self):
        # Ajout de l'en-tête centré avec le type d'exercice
        with self.header.create(Head("C")):
            self.header.append(HugeText(bold(f"{self.typeExo}")))

        # Ajout de l'en-tête à droite avec la date et l'heure actuelles
        with self.header.create(Head("R")):
            self.header.append(italic(NoEscape(f"{self.time}")))

        # Ajout des crédits en bas à gauche
        with self.header.create(Foot("L")):
            self.header.append(italic("Théo LUBAN"))

        # Ajout du centre en bas pour les crédits supplémentaires
        with self.header.create(Foot("C")):
            self.header.append(italic("Py-Maths © Tous droits réservés"))

        # Ajout des crédits en bas à droite
        with self.header.create(Foot("R")):
            self.header.append(italic("Quentin PLADEAU"))

        # Ajout de l'en-tête et du pied de page à chaque page du document
        self.doc.preamble.append(self.header)
        self.doc.change_document_style("header")

    def GetTime(self):
        formatted_date = self.now.strftime("%Y-%m-%d")  # Format : Année-Mois-Jour
        formatted_time = self.now.strftime("%H:%M:%S")  # Format : Heure:Minute:Seconde
        return f"Le {formatted_date} à {formatted_time}"
