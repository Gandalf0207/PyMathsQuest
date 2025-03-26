# import settings
from SourcesFichiers.Ressources.PyMathsSources.sources.settingsPyMaths import *
# import class de l'exercice eqt1deg
from SourcesFichiers.Ressources.PyMathsSources.sources.Eqt2IncsFolder.Eqt2IncsNv1 import ConsignesEqt2IncsNv1, CorrectionEqt2IncsNv1
from SourcesFichiers.Ressources.PyMathsSources.sources.Eqt2IncsFolder.Eqt2IncsNv2 import ConsignesEqt2IncsNv2, CorrectionEqt2IncsNv2

class Eqt2Incs(object):
    """ Class gestion pour préparer et corriger l'exercice sur les équations à 2 incs.
        Deux type de fonctionnement : 
            - Automatique : Tout est géré automatiquement, il suffit d'appeler la méthode GestionAllExoEqt2Incs
            - Personnalisé : Vous sélectionnez ce que vous souhaitez comme exercice : consignes / corrections en appelant les méthode correspondante

        Input :  
            doc -> pdf latex
            i -> entier : correspondant au numéro de l'exercice 
            choixNiveau -> int : niveau de l'exo
            nb1 -> int, valeurs > 2
            nb2 -> int, valeurs > 2
            nb3 -> int, valeurs > 2
            nb4 -> int, valeurs > 2
            nb5 -> int, valeurs > 2
            nb6 -> int, valeurs > 2
        
        Output : / """
    
    def __init__(self, doc, i, choixNiveau, nb1, nb2, nb3, nb4, nb5, nb6) -> None:
        """ Initialisation des attributs de la class de gestion de l'exercice équation à 2 incs. """

        self.doc = doc # pdf latex
        self.choixNiveau = choixNiveau # niveau difficulté
        self.i = i # numéro exo 
        self.nb1 = nb1  # valeur nb
        self.nb2 = nb2  # valeur nb
        self.nb3 = nb3  # valeur nb
        self.nb4 = nb4  # valeur nb
        self.nb5 = nb5  # valeur nb
        self.nb6 = nb6  # valeur nb

        # on définit la taille de l'écriture pour le document
        self.doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
        self.doc.append(pylatex.Command('selectfont')) 

        self.consigneNv1 = ConsignesEqt2IncsNv1(self.doc, self.i, self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6)
        self.consigneNv2 = ConsignesEqt2IncsNv2(self.doc, self.i, self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6)
        self.correctionNv1 = CorrectionEqt2IncsNv1(self.doc, self.i, self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6)
        self.correctionNv2 = CorrectionEqt2IncsNv2(self.doc, self.i, self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6)
        
    def GestionAllExoEqt2Incs(self) -> None:
        if self.choixNiveau == 1:
             # appel méthode pour créer toutes les consignes
            self.consigneNv1.Eqt2IncsNv1Consigne()

            # ajout nouvelle page pour séparer la correction de l'exercice    
            self.doc.append(NewPage())

            # appel des méthodes pour créer toutes les corrections
            self.correctionNv1.Eqt2IncsNv1Correction()

            # ajout nouvelle page pour séparer la fin de la correction de l'exercice suivant
            self.doc.append(NewPage())           


        elif self.choixNiveau == 2:
            # appel méthode pour créer toutes les consignes
            self.consigneNv2.Eqt2IncsNv2Consigne()

            # ajout nouvelle page pour séparer la correction de l'exercice    
            self.doc.append(NewPage())

             # appel des méthodes pour créer toutes les corrections
            self.correctionNv2.Eqt2IncsNv2Correction()

            # ajout nouvelle page pour séparer la fin de la correction de l'exercice suivant
            self.doc.append(NewPage())   

    def AddTitreConsigneNv1(self) -> None:
        """ Méthode personnalisé, choix de la consigne : titre des consignes. 
            Input : /
            Output : / """  
              
        self.consigneNv1.Eqt2IncsNv1Consigne()

    def AddTitreCorrectionNv1(self) -> None:
        """ Méthode personnalisé, choix de la correction : titres et corrections. 
            Input : /
            Output : / """
        
        self.correctionNv1.Eqt2IncsNv1Correction()

    def AddTitreConsigneNv2(self) -> None:
        """ Méthode personnalisé, choix de la consigne : titre des consignes. 
            Input : /
            Output : / """
        
        self.consigneNv2.Eqt2IncsNv2Consigne()

    def AddTitreCorrectionNv2(self) -> None:
        """ Méthode personnalisé, choix de la correction : titres et corrections. 
            Input : /
            Output : / """
        
        self.correctionNv2.Eqt2IncsNv2Correction()

