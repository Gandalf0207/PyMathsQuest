#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

# import settings
from SourcesFichiers.Ressources.PyMathsSources.sources.settingsPyMaths import *

# import class exercice volumes
from SourcesFichiers.Ressources.PyMathsSources.sources.VolumesFolder.VolumesNv1 import ConsignesVolumesNv1, CorrectionVolumesNv1
from SourcesFichiers.Ressources.PyMathsSources.sources.VolumesFolder.VolumesNv2 import ConsignesVolumesNv2, CorrectionVolumesNv2

class Volumes(object):
    """ Class gestion pour préparer et corriger l'exercice sur les volumes
        Deux type de fonctionnement : 
            - Automatique : Tout est géré automatiquement, il suffit d'appeler la méthode GestionAllExoVolumes
            - Personnalisé : Vous sélectionnez ce que vous souhaitez comme exercice : consignes / corrections en appelant les méthode correspondante

        Input :  
            doc -> pdf latex
            i -> entier : correspondant au numéro de l'exercice 
            choixNiveau -> int : niveau de l'exo
            a -> int, valeur 5,25 
            b -> int, valeur 25,50 
            r -> int, valeur 4, 12 
            L -> int, valeur 8, 34
            l -> int, valeur 7, 23 
            h -> int, valrur 3, 45
        
        Output : / """
    
    def __init__(self, doc, i, choixNiveau, a, b, r, d, L, l, h) -> None:
        """ Initialisation des attributs de la class de gestion de l'exercice volumes. """

        self.doc = doc # pdf latex
        self.choixNiveau = choixNiveau # niveau difficulté
        self.i = i # numéro exo
        self.a = a # coef nb
        self.b = b # coef nb
        self.r = r # coef nb
        self.d = d # coef nb
        self.L = L # coef nb
        self.l = l # coef nb
        self.h = h # coef nb

        # on définit la taille de l'écriture pour le document
        self.doc.append(pylatex.Command('fontsize', arguments = ['12', '10']))
        self.doc.append(pylatex.Command('selectfont')) 

        self.consigneNv1 = ConsignesVolumesNv1(self.doc, self.i, self.a, self.b, self.r, self.d, self.L, self.l, self.h)
        self.correctionNv1 = CorrectionVolumesNv1(self.doc, self.i, self.a, self.b, self.r, self.d, self.L, self.l, self.h)

        self.consigneNv2 = ConsignesVolumesNv2(self.doc, self.i, self.a, self.b, self.r, self.h)
        self.correctionNv2 = CorrectionVolumesNv2(self.doc, self.i, self.a, self.b, self.r, self.h)


    def GestionAllExoVolumes(self) ->None:
        if self.choixNiveau == 1:
            # appel méthode pour créer toutes les consignes
            self.consigneNv1.VolumesTitreConsigne()
            self.consigneNv1.ConsigneVCube(1)
            self.consigneNv1.ConsigneVSphere(2)
            self.consigneNv1.ConsigneVCone(3)
            self.consigneNv1.ConsigneVCylindre(4)
            self.consigneNv1.ConsigneVPaveDroit(5)
            self.consigneNv1.ConsigneVPyramideBaseCarre(6)
            self.consigneNv1.ConsigneADisque(7)
            self.consigneNv1.ConsigneATriangleRectangle(8)
            self.consigneNv1.ConsigneARectangle(9)

            # ajout nouvelle page pour séparer la correction de l'exercice    
            self.doc.append(NewPage())

            # appel des méthodes pour créer toutes les corrections
            self.correctionNv1.VolumesTitreCorrection()
            self.correctionNv1.CorrectionVCube(1)
            self.correctionNv1.CorrectionVSphere(2)
            self.correctionNv1.CorrectionVCone(3)
            self.correctionNv1.CorrectionVCylindre(4)
            self.correctionNv1.CorrectionVPaveDroit(5)
            self.correctionNv1.CorrectionVPyramideBaseCarre(6)
            self.correctionNv1.CorrectionADisque(7)
            self.correctionNv1.CorrectionATriangleRectangle(8)
            self.correctionNv1.CorrectionARectangle(9)


            # ajout nouvelle page pour séparer la fin de la correction de l'exercice suivant
            self.doc.append(NewPage()) 

        elif self.choixNiveau == 2:

            # appel méthode pour créer toutes les consignes
            self.consigneNv2.VolumesNv2Consigne()

            # ajout nouvelle page pour séparer la correction de l'exercice    
            self.doc.append(NewPage())

            # appel des méthodes pour créer toutes les corrections
            self.correctionNv2.VolumesNv2Correction()

            # ajout nouvelle page pour séparer la fin de la correction de l'exercice suivant
            self.doc.append(NewPage())           



# consigne nv1

    def AddVolumesTitreConsigne(self):
        """Méthode personnalisé, choix de la consigne : titre des consignes
        Input : /
        Output : / """
        
        self.consigneNv1.VolumesTitreConsigne()

    def AdConsigneVCube(self, numEtape):
        """Méthode personnalisé, choix de la consigne : Volume cube
        Input : /
        Output : / """
        
        self.consigneNv1.ConsigneVCube(numEtape)

    def AddConsigneVSphere(self, numEtape):
        """Méthode personnalisé, choix de la consigne : Volume sphere
        Input : /
        Output : / """
        
        self.consigneNv1.ConsigneVSphere(numEtape)

    def AddConsigneVCone(self, numEtape):
        """Méthode personnalisé, choix de la consigne : Volume cone
        Input : /
        Output : / """
        
        self.consigneNv1.ConsigneVCone(numEtape)

    def AddConsigneVCylindre(self, numEtape):
        """Méthode personnalisé, choix de la consigne : Volume cylindre
        Input : /
        Output : / """
        
        self.consigneNv1.ConsigneVCylindre(numEtape)

    def AddConsigneVPaveDroit(self, numEtape):
        """Méthode personnalisé, choix de la consigne : Volume pavé droit
        Input : /
        Output : / """
        
        self.consigneNv1.ConsigneVPaveDroit(numEtape)

    def AddConsigneVPyramideBaseCarre(self, numEtape):
        """Méthode personnalisé, choix de la consigne : Volume yramide base carré
        Input : /
        Output : / """
        
        self.consigneNv1.ConsigneVPyramideBaseCarre(numEtape)

    def AddConsigneADisque(self, numEtape):
        """Méthode personnalisé, choix de la consigne : Aire disque
        Input : /
        Output : / """
        
        self.consigneNv1.ConsigneADisque(numEtape)

    def AddConsigneATriangleRectangle(self, numEtape):
        """Méthode personnalisé, choix de la consigne : Aire triangle rectangle
        Input : /
        Output : / """
        
        self.consigneNv1.ConsigneATriangleRectangle(numEtape)

    def AddConsigneARectangle(self, numEtape):
        """Méthode personnalisé, choix de la consigne : Aire rectangle
        Input : /
        Output : / """
        
        self.consigneNv1.ConsigneARectangle(numEtape)

# correction nv1

    def AddVolumesTitreCorrection(self):
        """Méthode personnalisé, choix de la consigne : titre des consignes
        Input : /
        Output : / """
        
        self.consigneNv1.VolumesTitreConsigne()

    def AddCorrectionCube(self, numEtape):
        """Méthode personnalisé, choix de la correction : Volume cube
        Input : /
        Output : / """
        
        self.correctionNv1.CorrectionVCube(numEtape)

    def AddCorrectionVSphere(self, numEtape):
        """Méthode personnalisé, choix de la correction : Volume sphere
        Input : /
        Output : / """
        
        self.correctionNv1.CorrectionVSphere(numEtape)

    def AddCorrectionVCone(self, numEtape):
        """Méthode personnalisé, choix de la correction : Volume cone
        Input : /
        Output : / """
        
        self.correctionNv1.CorrectionVCone(numEtape)

    def AddCorrectionVCylindre(self, numEtape):
        """Méthode personnalisé, choix de la correction : Volume cylindre
        Input : /
        Output : / """
        
        self.correctionNv1.CorrectionVCylindre(numEtape)

    def AddCorrectionVPaveDroit(self, numEtape):
        """Méthode personnalisé, choix de la correction : Volume pavé droit
        Input : /
        Output : / """
        
        self.correctionNv1.CorrectionVPaveDroit(numEtape)

    def AddCorrectionVPyramideBaseCarre(self, numEtape):
        """Méthode personnalisé, choix de la correction : Volume yramide base carré
        Input : /
        Output : / """
        
        self.correctionNv1.CorrectionVPyramideBaseCarre(numEtape)

    def AddCorrectionADisque(self, numEtape):
        """Méthode personnalisé, choix de la correction : Aire disque
        Input : /
        Output : / """
        
        self.correctionNv1.CorrectionADisque(numEtape)

    def AddCorrectionATriangleRectangle(self, numEtape):
        """Méthode personnalisé, choix de la correction : Aire triangle rectangle
        Input : /
        Output : / """
        
        self.correctionNv1.CorrectionATriangleRectangle(numEtape)

    def AddCorrectionARectangle(self, numEtape):
        """Méthode personnalisé, choix de la correction : Aire rectangle
        Input : /
        Output : / """
        
        self.correctionNv1.CorrectionARectangle(numEtape)
