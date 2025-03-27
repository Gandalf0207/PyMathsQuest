#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

from SourcesFichiers.Ressources.PyMathsSources.sources.Eqt2IncsFolder.GestionEqt2Incs import *
from SourcesFichiers.Ressources.PyMathsSources.sources.Eqt1degFolder.GestionEqt1deg import *
from SourcesFichiers.Ressources.PyMathsSources.sources.Poly2defFolder.GestionPoly2deg import *
from SourcesFichiers.Ressources.PyMathsSources.sources.VolumesFolder.GestionVolumes import *
from SourcesFichiers.Ressources.PyMathsSources.sources.DerivesFolder.GestionDerives import *

# Importation des scripts de mise en age et de gestions autre
from SourcesFichiers.Ressources.PyMathsSources.sources.basePDF import *
from SourcesFichiers.Ressources.PyMathsSources.sources.aModule_Gestion import Contenue_Page_1

from SourcesFichiers.Ressources.PyMathsSources.sources.settingsPyMaths import *


class Generation(object):
    def __init__(self) -> None:
        # Initialisation des paramètres du PDF
        geometry_options = {"head": "40pt", "margin": "5mm", "bottom": "0.6cm", "includeheadfoot": True}
        self.doc = Document(geometry_options=geometry_options)

        # Ajout des paquets nécessaires
        self.doc.preamble.append(pylatex.Command('usepackage', 'newunicodechar'))
        self.doc.packages.append(NoEscape("\\usepackage{tkz-tab}"))
        self.doc.packages.append(NoEscape("\\usepackage{placeins}"))
        self.doc.packages.append(NoEscape("\\usepackage{amsmath}"))
        self.doc.packages.append(NoEscape("\\usepackage[utf8]{inputenc}"))
        self.doc.packages.append(NoEscape("\\usepackage{enumitem}"))
        self.doc.packages.append(NoEscape("\\usepackage{array}"))
        self.doc.packages.append(NoEscape("\\usepackage{tabularx}"))

        self.doc.packages.append(NoEscape("\\usepackage{amssymb}"))
        self.doc.packages.append(NoEscape("\\usepackage{geometry}"))

        self.doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{∞}{\ensuremath{\infty}}'))
        self.doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{Δ}{\ensuremath{\Delta}}'))
        self.doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{α}{\ensuremath{\alpha}}'))
        self.doc.preamble.append(pylatex.NoEscape(r'\newunicodechar{β}{\ensuremath{\beta}}'))

    def GetDoc(self):
        return self.doc

    def FirstPage(self, title):
         # Ajout de l'en-tête et du contenu de la première page
        hp = HeaderFooter(self.doc, title)
        hp.HeaderFooterPage()

        Contenue_Page_1.generate_contenue_p1(self.doc)
        self.doc.append(NewPage())

    def GetValues(self):
        liste = []

        def checkUniqueValuesList(liste):
            return len(liste) == len(set(liste)) # check de si toutes les valeurs sont uniques
        
        self.a = random.randint(5,25 )
        self.b = random.randint(25,50) 
        self.r = random.randint(4, 12) 
        self.d = random.randint(6, 32)
        self.L = random.randint(8, 34)
        self.l = random.randint(7, 23) 
        self.h = random.randint(3, 45)
        self.e = sqrt((self.r**2)+(self.h**2)) # check valeurs correct (nb chiffres après la virgule exo volume nv2)


        self.nb1 = random.randint(2,50)
        self.nb2 = random.randint(2,50)
        self.nb3 = random.randint(2,50)
        self.nb4 = random.randint(2,50)
        self.nb5 = random.randint(2,50)
        self.nb6 = random.randint(2,50)
        self.nb7 = random.randint(2,50)
        self.nb8 = random.randint(2,50)
        self.nb9 = random.randint(2,50)
        self.nb12 = random.randint(2,50)
        self.nb10 = random.randint(2,50)
        self.nb11 = random.randint(2,50)
    
        liste = [self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6, self.nb7, self.nb8, self.nb9, self.nb10, self.nb11, self.nb12]

        while not checkUniqueValuesList(liste) or e != round(e,3):
            liste= []
            self.a = random.randint(5,25 )
            self.b = random.randint(25,50) 
            self.r = random.randint(4, 12) 
            self.d = random.randint(6, 32)
            self.L = random.randint(8, 34)
            self.l = random.randint(7, 23) 
            self.h = random.randint(3, 45)
            self.e = sqrt((self.r**2)+(self.h**2)) # check valeurs correct (nb chiffres après la virgule exo volume nv2)

            self.nb1 = random.randint(2,50)
            self.nb2 = random.randint(2,50)
            self.nb3 = random.randint(2,50)
            self.nb4 = random.randint(2,50)
            self.nb5 = random.randint(2,50)
            self.nb6 = random.randint(2,50)
            self.nb7 = random.randint(2,50)
            self.nb8 = random.randint(2,50)
            self.nb9 = random.randint(2,50)
            self.nb12 = random.randint(2,50)
            self.nb10 = random.randint(2,50)
            self.nb11 = random.randint(2,50)
            liste = [self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6, self.nb7, self.nb8, self.nb9, self.nb10, self.nb11, self.nb12]

            self.nb_1 = random.randint(3, 8)
            self.nb_2 = random.randint(3, 8)
            self.nb_3 = random.randint(3, 8)
            self.nb_4 = random.randint(3, 8)
            self.nb_5 = random.randint(3, 8)
            self.nb_6 = random.randint(3, 8)
            self.nb_7 = random.randint(3, 8)
            self.nb_8 = random.randint(3, 8)
            self.nb_9 = random.randint(3, 8)
            self.nb_10 = random.randint(3, 8)

    def BuildPdf(self, title, filePath):
        """Méthode pour générer le pdf depuis"""
        output_path = filePath.replace(f"{title}.pdf", "")
        self.doc.generate_pdf(output_path, clean_tex=True, compiler="pdfLaTex")
        
        final_pdf_path = output_path + ".pdf"
        webbrowser.open(f"file://{os.path.abspath(final_pdf_path)}")


# Generation instance

# Build pdf avec l'appel des méthodes
# Génération des valeurs
# Firts page
# méthodes des exos
# genrate pdf méthode