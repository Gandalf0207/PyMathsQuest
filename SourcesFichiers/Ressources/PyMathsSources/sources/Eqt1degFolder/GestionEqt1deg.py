#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

# import settings
from SourcesFichiers.Ressources.PyMathsSources.sources.settingsPyMaths import *
# import class des exercices eqt1deg
from SourcesFichiers.Ressources.PyMathsSources.sources.Eqt1degFolder.Eqt1degNv1 import ConsignesEqt1degNv1, CorrectionEqt1degNv1
from SourcesFichiers.Ressources.PyMathsSources.sources.Eqt1degFolder.Eqt1degNv2 import ConsignesEqt1degNv2, CorrectionEqt1degNv2

class Eqt1deg(object):
    """ Class gestion pour préparer et corriger l'exercice sur les équations du premier degré.
        Deux type de fonctionnement : 
            - Automatique : Tout est géré automatiquement, il suffit d'appeler la méthode GestionAllExoEqt1deg
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
        """ Initialisation des attributs de la class de gestion de l'exercice équation du premier degré. """

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

        # on instancie les class consignes et correction de l'exercice
        self.consigneNv1 = ConsignesEqt1degNv1(self.doc, self.i, self.nb1, self.nb2, self.nb3, self.nb4)
        self.consigneNv2 = ConsignesEqt1degNv2(self.doc, self.i, self.nb1, self.nb2, self.nb3, self.nb4,self.nb5, self.nb6)
        self.correctionNv1 = CorrectionEqt1degNv1(self.doc, self.i, self.nb1, self.nb2, self.nb3, self.nb4)
        self.correctionNv2 = CorrectionEqt1degNv2(self.doc, self.i, self.nb1, self.nb2, self.nb3, self.nb4,self.nb5, self.nb6)

    def GestionAllExoEqt1deg(self) -> None:
        """ Méthode automatique, permet de créer un pdf avec un exercice complet (consignes + corrections). 
            Input : /
            Output : / """
        if self.choixNiveau == 1:
             # appel méthode pour créer toutes les consignes
            self.consigneNv1.Eqt1degNv1Consigne()

            # ajout nouvelle page pour séparer la correction de l'exercice    
            self.doc.append(NewPage())

            # appel des méthodes pour créer toutes les corrections
            self.correctionNv1.Eqt1degNv1Correction()

            # ajout nouvelle page pour séparer la fin de la correction de l'exercice suivant
            self.doc.append(NewPage())

        elif self.choixNiveau == 2:
             # appel méthode pour créer toutes les consignes
            self.consigneNv2.Eqt1degNv2Consigne()

            # ajout nouvelle page pour séparer la correction de l'exercice    
            self.doc.append(NewPage())

             # appel des méthodes pour créer toutes les corrections
            self.correctionNv2.Eqt1degNv2Correction()

            # ajout nouvelle page pour séparer la fin de la correction de l'exercice suivant
            self.doc.append(NewPage())

        
    def AddTitreConsigneNv1(self) -> None:
        """ Méthode personnalisé, choix de la consigne : titre des consignes. 
            Input : /
            Output : / """  
              
        self.consigneNv1.Eqt1degNv1Consigne()

    def AddTitreCorrectionNv1(self) -> None:
        """ Méthode personnalisé, choix de la correction : titres et corrections. 
            Input : /
            Output : / """
        
        self.correctionNv1.Eqt1degNv1Correction()

    def AddTitreConsigneNv2(self) -> None:
        """ Méthode personnalisé, choix de la consigne : titre des consignes. 
            Input : /
            Output : / """
        
        self.consigneNv2.Eqt1degNv2Consigne()

    def AddTitreCorrectionNv2(self) -> None:
        """ Méthode personnalisé, choix de la correction : titres et corrections. 
            Input : /
            Output : / """
        
        self.correctionNv2.Eqt1degNv2Correction()