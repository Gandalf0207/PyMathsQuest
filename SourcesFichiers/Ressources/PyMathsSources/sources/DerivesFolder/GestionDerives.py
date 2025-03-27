#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

# import settings
from SourcesFichiers.Ressources.PyMathsSources.sources.settingsPyMaths import *
# import class de l'exercice eqt1deg
from SourcesFichiers.Ressources.PyMathsSources.sources.DerivesFolder.DerivesNv1 import ConsignesDerivesNv1, CorrectionsDerivesNv1

class Derives(object):
    """ Class gestion pour préparer et corriger l'exercice sur les dérives.
        Deux type de fonctionnement : 
            - Automatique : Tout est géré automatiquement, il suffit d'appeler la méthode GestionAllExoDerives
            - Personnalisé : Vous sélectionnez ce que vous souhaitez comme exercice : consignes / corrections en appelant les méthode correspondante"""
    
    def __init__(self, doc, i, choixNiveau, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9, nb10, ListeFonction :list = None , ListeAllCoef :list = None) -> None:
        """ Initialisation des attributs de la class de gestion de l'exercice des dérivés. """

        self.doc = doc # pdf latex
        self.choixNiveau = choixNiveau # niveau difficulté
        self.i = i # numéro exo 
        self.allNumber = [nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9, nb10]
        self.listeFonction, self.listeCoef, self.listeFonctionLatex = self.__CreateListeFonction__(ListeFonction, ListeAllCoef) # si une fonction est déjà faites pour la correction
        
        # on définit la taille de l'écriture pour le document
        self.doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
        self.doc.append(pylatex.Command('selectfont')) 

        self.consigneNv1 = ConsignesDerivesNv1(self.doc, self.i, self.listeFonction, self.listeCoef, self.listeFonctionLatex)
        self.correctionNv1 = CorrectionsDerivesNv1(self.doc, self.i, self.listeFonction, self.listeCoef, self.listeFonctionLatex)
        
    def __CreateListeFonction__(self, ListeFonction, ListeAllCoef):

        # on récupère s'il y a déjà des valeurs
        if ListeFonction == None:
            listeElement = ["Xcarre", "XexposantN", "racinecarreX", "X", "C", "expX"]
            allFonctionType = choices(listeElement, k=9)
            allFonctionLatex = []
            allListeCoef = []
        else:
            allFonctionType = ListeFonction
            allListeCoef = ListeAllCoef
            allFonctionLatex = []

        # on génère toutes les fonctions en latexs
        for i, element in enumerate(allFonctionType):
            if element == "Xcarre":
                if ListeAllCoef == None:
                    coef = choice(self.allNumber)
                    allListeCoef.append(coef)
                else :
                    coef = allListeCoef[i]
                allFonctionLatex.append(r" %sx^2 " % (coef))

            elif element == "XexposantN":
                if ListeAllCoef == None:
                    coef = (choice(self.allNumber), choice(self.allNumber))
                    allListeCoef.append(coef)
                else :
                    coef = [allListeCoef[i], allListeCoef[i+1]]
                allFonctionLatex.append(r" %sx^{%s} " % (coef[0], coef[1]))

            elif element == "racinecarreX":
                if ListeAllCoef == None:
                    coef = choice(self.allNumber)
                    allListeCoef.append(coef)
                else :
                    coef = allListeCoef[i]
                allFonctionLatex.append(r" %s \sqrt{x} " % (coef))

            elif element == "X":
                if ListeAllCoef == None:
                    coef = choice(self.allNumber)
                    allListeCoef.append(coef)
                else :
                    coef = allListeCoef[i]
                allFonctionLatex.append(r" %sx " %(coef))

            elif element == "C":
                if ListeAllCoef == None:
                    coef = choice(self.allNumber)
                    allListeCoef.append(coef)
                else :
                    coef = allListeCoef[i]
                allFonctionLatex.append(r"  %s " %(coef))

            elif element == "expX":
                if ListeAllCoef == None:
                    coef = choice(self.allNumber)
                    allListeCoef.append(coef)
                else :
                    coef = allListeCoef[i]
                allFonctionLatex.append(r" e^{%sx} " % (coef))

            return allFonctionType, allListeCoef, allFonctionLatex


    def GestionAllExoDerives(self) -> None:

        # appel méthode pour créer toutes les consignes
        self.consigneNv1.DerivesTitreConsigne()
        self.consigneNv1.ConsigneCalculDerives(1)
        self.consigneNv1.ConsigneTangente(2)
        self.consigneNv1.ConsignesDerives()
        # ajout nouvelle page pour séparer la correction de l'exercice    
        self.doc.append(NewPage())

        # appel des méthodes pour créer toutes les corrections
        self.correctionNv1.DerivesTitreCorrection()
        self.correctionNv1.CorrectionDerives()
        self.correctionNv1.CorrectionCalculDerives()
        self.correctionNv1.CorrectionTangente()

        # ajout nouvelle page pour séparer la fin de la correction de l'exercice suivant
        self.doc.append(NewPage())           



    def AddTitreConsigneNv1(self) -> None:
        """ Méthode personnalisé, choix de la consigne : titre des consignes. 
            Input : /
            Output : / """  
              
        self.consigneNv1.DerivesTitreConsigne()

    def AddConsigneCalculDerives(self, numEtape):
        self.consigneNv1.ConsigneCalculDerives(numEtape)

    def AddConsigneTangente(self, numEtape):
        self.consigneNv1.ConsigneTangente(numEtape)

    def AddConsignesDerives(self):
        self.consigneNv1.ConsignesDerives()

    def AddTitreCorrectionNv1(self) -> None:
        """ Méthode personnalisé, choix de la correction : titres et corrections. 
            Input : /
            Output : / """
        
        self.correctionNv1.DerivesTitreCorrection()

    def AddCorrectionDerives(self):
        self.correctionNv1.CorrectionDerives()

    def AddCorrectionCalculDerives(self):
        self.correctionNv1.CorrectionCalculDerives()

    def AddCorrectionTangente(self):
        self.correctionNv1.CorrectionTangente()