# import settings 
from SourcesFichiers.Ressources.PyMathsSources.sources.settingsPyMaths import *
# import class de l'exercice poly2deg
from SourcesFichiers.Ressources.PyMathsSources.sources.Poly2defFolder.Poly2degNv import ConsignesPoly2degNv, CorrectionsPoly2degNv

class Poly2deg(object):
    """ Class gestion pour préparer et corriger l'exercice sur les polynômes du second degré.
        Deux type de fonctionnement : 
            - Automatique : Tout est géré automatiquement, il suffit d'appeler la méthode GestionAllExoPoly2deg
            - Personnalisé : Vous sélectionnez ce que vous souhaitez comme exercice : consignes / corrections en appelant les méthode correspondante

        Input :  
            doc -> pdf latex
            i -> entier correspondant au numéro de l'exercice 
            a -> valeurs différentes de 0
            b -> valeurs différentes de 0
            c -> valeurs différentes de 0
        
        Output : / """

    def __init__(self, doc, i, a, b, c) -> None:
        """ Initialisation des attributs de la class de gestion de l'exercice Les polynômes du second degré. """

        self.doc = doc # pdf latex
        self.i = i # numéro exercice
        self.a = a # coef a
        self.b = b # coef b
        self.c = c # coef c

        # on définit la taille de l'écriture pour le document
        self.doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
        self.doc.append(pylatex.Command('selectfont'))

        # on instancie les class consignes et correction de l'exercice
        self.consigne = ConsignesPoly2degNv(self.doc, self.i, self.a, self.b, self.c)
        self.correction = CorrectionsPoly2degNv(self.doc, self.i, self.a, self.b, self.c)

    # consignes + corrections automatiques
    def GestionAllExoPoly2deg(self) -> None:
        """ Méthode automatique, permet de créer un pdf avec un exercice complet (consignes + corrections). 
            Input : /
            Output : / """

        # appel des méthodes pour créer toutes les consignes
        self.consigne.Poly2DegTitreConsigne()
        self.consigne.ConsigneAlpha(1)
        self.consigne.ConsigneBeta(2)
        self.consigne.ConsigneDelta(3)
        self.consigne.ConsigneSolutionsDelta(4)
        self.consigne.ConsigneFormeCanonique(5)
        self.consigne.ConsigneSommetS(6)
        self.consigne.ConsignePointA(7)
        self.consigne.ConsigneAllureCourbe(8)
        self.consigne.ConsigneTableauSignes(9)
        self.consigne.ConsigneTableauVariations(10)

        # ajout nouvelle page pour séparer la correction de l'exercice    
        self.doc.append(NewPage())

        # appel des méthodes pour créer toutes les corrections
        self.correction.Poly2DegTitreCorrection()
        self.correction.CorrectionAlpha(1)
        self.correction.CorrectionBeta(2)
        self.correction.CorrectionDelta(3)
        self.correction.CorrectionSolutionsDelta(4)
        self.correction.CorrectionFormeCanonique(5)
        self.correction.CorrectionSommetS(6)
        self.correction.CorrectionPointA(7)
        self.correction.CorrectionAllureCourbe(8)
        self.correction.CorrectionTableauSignes(9)
        self.correction.CorrectionTableauVariations(10)

        # ajout nouvelle page pour séparer la fin de la correction de l'exercice suivant
        self.doc.append(NewPage())

    # consignes personnalisés
    def AddPoly2DegTitreConsigne(self) -> None:
        """ Méthode personnalisé, choix de la consigne : titre des consignes. 
            Input : /
            Output : / """
        
        self.consigne.Poly2DegTitreConsigne()

    def AddConsigneAlpha(self, numEtape) -> None:
        """ Méthode personnalisé, choix de la consigne : calcul de alpha. 
            Input : numéro de l'étape
            Output : / """
        
        self.consigne.ConsigneAlpha(numEtape) 

    def AddConsigneBeta(self, numEtape) -> None:
        """ Méthode personnalisé, choix de la consigne : calcul de beta. 
            Input : numéro de l'étape
            Output : / """
        
        self.consigne.ConsigneBeta(numEtape) 

    def AddConsigneDelta(self, numEtape) -> None:
        """ Méthode personnalisé, choix de la consigne : calcul de delta. 
            Input : numéro de l'étape
            Output : / """
        
        self.consigne.ConsigneDelta(numEtape)

    def AddConsigneSolutionsDelta(self, numEtape) -> None:
        """ Méthode personnalisé, choix de la consigne : calcul de(s) solution(s) de delta. 
            Input : numéro de l'étape
            Output : / """
        
        self.consigne.ConsigneSolutionsDelta(numEtape)

    def AddConsigneFormeCanonique(self, numEtape) -> None:
        """ Méthode personnalisé, choix de la consigne : écriture forme canonique. 
            Input : numéro de l'étape
            Output : / """
        
        self.consigne.ConsigneFormeCanonique(numEtape)

    def AddConsigneSommetS(self, numEtape) -> None:
        """ Méthode personnalisé, choix de la consigne : calcul sommet S. 
            Input : numéro de l'étape
            Output : / """
        
        self.consigne.ConsigneSommetS(numEtape)

    def AddConsignePointA(self, numEtape) -> None:
        """ Méthode personnalisé, choix de la consigne : calcul point A. 
            Input : numéro de l'étape
            Output : / """
        
        self.consigne.ConsignePointA(numEtape)

    def AddConsigneAllureCourbe(self, numEtape) -> None:
        """ Méthode personnalisé, choix de la consigne : représentation allure courbe. 
            Input : numéro de l'étape
            Output : / """
        
        self.consigne.ConsigneAllureCourbe(numEtape)

    def AddConsigneTableauSignes(self, numEtape) -> None:
        """ Méthode personnalisé, choix de la consigne : tableau de signes. 
            Input : numéro de l'étape
            Output : / """
        
        self.consigne.ConsigneTableauSignes(numEtape)

    def AddConsigneTableauVariations(self, numEtape) -> None:
        """ Méthode personnalisé, choix de la consigne : tableau de variations. 
            Input : numéro de l'étape
            Output : / """
        
        self.consigne.ConsigneTableauVariations(numEtape)


    # corrections personnalisés
    def AddPoly2DegTitreCorrection(self) -> None :
        """ Méthode personnalisé, choix de la correction : titres des corrections . 
            Input : /
            Output : /"""
        self.correction.Poly2DegTitreCorrection()

    def AddCorrectionAlpha(self, numEtape) -> None :
        """ Méthode personnalisé, choix de la correction : calcul alpha.
            Input : numéro de l'étape
            Output : / """
        
        self.correction.CorrectionAlpha(numEtape)

    def AddCorrectionBeta(self, numEtape) -> None :
        """ Méthode personnalisé, choix de la correction : calcul beta.
            Input : numéro de l'étape
            Output : / """
        
        self.correction.CorrectionBeta(numEtape)

    def AddCorrectionDelta(self, numEtape) -> None :
        """ Méthode personnalisé, choix de la correction : calcul delta.
            Input : numéro de l'étape
            Output : / """
        
        self.correction.CorrectionDelta(numEtape)

    def AddCorrectionSolutionsDelta(self, numEtape) -> None :
        """ Méthode personnalisé, choix de la correction :  calcul de(s) solution(s) de delta.
            Input : numéro de l'étape
            Output : / """
        
        self.correction.CorrectionSolutionsDelta(numEtape)

    def AddCorrectionFormeCanonique(self, numEtape) -> None :
        """ Méthode personnalisé, choix de la correction :  écriture forme canonique.
            Input : numéro de l'étape
            Output : / """
        
        self.correction.CorrectionFormeCanonique(numEtape)

    def AddCorrectionSommetS(self, numEtape) -> None :
        """ Méthode personnalisé, choix de la correction :  calcul sommet S.
            Input : numéro de l'étape
            Output : / """
        
        self.correction.CorrectionSommetS(numEtape)

    def AddCorrectionPointA(self, numEtape) -> None :
        """ Méthode personnalisé, choix de la correction :  calcul point A.
            Input : numéro de l'étape
            Output : / """
        
        self.correction.CorrectionPointA(numEtape)

    def AddCorrectionAllureCourbe(self, numEtape) -> None :
        """ Méthode personnalisé, choix de la correction :  représentation allure courbe. """
        self.correction.CorrectionAllureCourbe(numEtape)

    def AddCorrectionTableauSignes(self, numEtape) -> None :
        """ Méthode personnalisé, choix de la correction :  tableau de signes.
            Input : numéro de l'étape
            Output : / """
        
        self.correction.CorrectionTableauSignes(numEtape)

    def AddCorrectionTableauVariations(self, numEtape) -> None :
        """ Méthode personnalisé, choix de la correction :  tableau de variations.
            Input : numéro de l'étape
            Output : / """
        
        self.correction.CorrectionTableauVariations(numEtape)
