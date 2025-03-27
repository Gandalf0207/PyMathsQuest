#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

# import settings
from SourcesFichiers.Ressources.PyMathsSources.sources.settingsPyMaths import *

class VolumesNv1(object):
    """Class parent de l'exercice de calcul de volume. Contient des méthodes utilisés globalement.
    Permet de gérer plus facilement des apples et la création des exercices.
    
        Input : 
            doc -> pdf latex
            a -> int, valeur 5,25 
            b -> int, valeur 25,50 
            r -> int, valeur 4, 12 
            d -> int, valeur 6, 32
            L -> int, valeur 8, 34
            l -> int, valeur 7, 23 
            h -> int, valrur 3, 45

        Output : / """

    def __init__(self, doc, a, b, r, d, L, l, h) -> None:
        """Initialisation des attribbuts de la class parent de l'exercie Volumes"""

        self.doc = doc # pdf latex
        self.a = a # coef nb
        self.b = b # coef nb
        self.r = r # coef nb
        self.d = d # coef nb
        self.L = L # coef nb
        self.l = l # coef nb
        self.h = h # coef nb

    def __pgcd__(self, a, b) -> int:
        """ Méthode pgcd, permet de calculer le plus grand diviseur comment entre deux nombres. Utiliser pour créer des fractions iréductibles.
            Input : 
                a -> nombre entier 
                b -> nombre entier
            Output : a -> nombre entier """

        while b != 0:
            a,b=b,a%b
        return a # retour du pgcd


class ConsignesVolumesNv1(VolumesNv1):
    """Class enfant contenant toutes la méthode pour pouvoir écrire les consignes
    
        Input : 
            doc -> pdf latex
            i -> int numéro de l'exercice
            a -> int, valeur 5,25 
            b -> int, valeur 25,50 
            r -> int, valeur 4, 12 
            d -> int, valeur 6, 32
            L -> int, valeur 8, 34
            l -> int, valeur 7, 23 
            h -> int, valrur 3, 45

        Output : / """
    

    def __init__(self, doc, i, a, b, r, d, L, l, h) -> None:
        """Initialisation des attributs de la class enfant consignes, de l'exerccie volumes."""

        super().__init__(doc, a, b, r, d, L, l, h)
        self.i = i # nunméro de l'exercice

    def VolumesTitreConsigne(self) -> None:
        """Méthode d'écriture du titre des consignes
        Input  : /    
        Output : /"""

        with self.doc.create(Section(f"Exo Volumes n°{self.i+1}", numbering=False)): #titre de l'exo
            self.doc.append(NoEscape("Niveau 1 :\\\\"))
            self.doc.append(NoEscape("\\ \\parbox{ 450pt }{ A l'aide des valeurs données, veuillez calculer l'aire ou le volume demandé. Une valeur exacte et arrondie au millième vous est demandée.}  \\\\")) # consigne générale
            self.doc.append(NoEscape("\\\\"))

    def ConsigneVCube(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer le volume d'un cube.
        Input : numéro de l'étape
        Output : /"""

        self.doc.append(NoEscape("\\ %s. Calculer le volume d'un cube de côté : c = %sm \\\\" % (numEtape, self.a)))
        self.doc.append(NoEscape("\\\\"))

    def ConsigneVSphere(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer le volume d'une sphère.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer le volume d'une sphère de rayon : r = %sm \\\\" % (numEtape, self.r)))
        self.doc.append(NoEscape("\\\\"))

    def ConsigneVCone(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer le volume d'un cône.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer le volume d'un cône de hauteur et de diametre de base: h = %sm ; d = %sm \\\\" % (numEtape, self.h, self.d)))
        self.doc.append(NoEscape("\\\\"))

    def ConsigneVCylindre(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer le volume d'un cylindre.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer le volume d'un cylindre de hauteur et de rayon de base: h = %sm ; r = %sm \\\\" % (numEtape, self.h, self.r)))
        self.doc.append(NoEscape("\\\\"))   

    def ConsigneVPaveDroit(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer le volume d'un pavé droit.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer le volume d'un pavé droit de Longueur, largeur et hauteur : L = %sm ; l = %sm ; h = %sm \\\\" % (numEtape, self.L, self.l, self.h)))
        self.doc.append(NoEscape("\\\\"))   

    def ConsigneVPyramideBaseCarre(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer le volume d'une pyramide à base carré.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer le volume d'une pyramide à base carré de côté de base et hauter: c = %sm ; h = %sm \\\\" % (numEtape, self.b, self.h)))
        self.doc.append(NoEscape("\\\\"))  

    def ConsigneADisque(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer l'aire d'un disque.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer l'aire d'un disque de diametre:  d = %sm \\\\" % (numEtape, self.d)))
        self.doc.append(NoEscape("\\\\"))

    def ConsigneATriangleRectangle(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer l'aire triangle rectangle.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer l'aire d'un triangle rectangle (ABC) en A de côté : AB = %sm; AC = %sm \\\\" % (numEtape, self.a, self.b)))
        self.doc.append(NoEscape("\\\\"))   

    def ConsigneARectangle(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer l'aire d'un rectangle.
        Input : numéro de l'étape
        Output : /""" 

        self.doc.append(NoEscape("\\ %s. Calculer l'aire d'un rectangle : L = %sm; l = %sm \\\\" % (numEtape, self.L, self.l)))
        self.doc.append(NoEscape("\\\\"))


class CorrectionVolumesNv1(VolumesNv1):
    """Class enfant contentant toutes les méthodes pour pouvoir écrire les corrections et calculer les valeurs
    
      Input : 
        doc -> pdf latex
        i -> int numéro de l'exercice
        a -> int, valeur 5,25 
        b -> int, valeur 25,50 
        r -> int, valeur 4, 12 
        L -> int, valeur 8, 34
        l -> int, valeur 7, 23 
        h -> int, valrur 3, 45

    Output : / """
    

    def __init__(self, doc, i, a, b, r, d, L, l, h) -> None:
        """Initialisation des attributs de la class enfant correction, de l'exercice volumes"""
        
        super().__init__(doc, a, b, r, d, L, l, h)
        self.i = i # numéro exo

        self.VCube = None
        self.VSphere = None
        self.VCone = None
        self.VCylindre = None
        self.VPaveDroit = None
        self.VPyramideBaseCarre = None
        self.ADisque = None
        self.ATriangleRectangle = None
        self.ARectangle = None

        self.__AllCalculs__()

    def arrondir(self, valeur):
        """Arrondit à 3 chiffres après la virgule uniquement si le nombre a plus de 3 chiffres après la virgule."""
        if isinstance(valeur, float):
            # Multiplie la valeur par 1000, prend la partie entière, puis compare
            if int(valeur * 1000) != valeur * 1000:
                return round(valeur, 3)
        return valeur  # Si pas un float ou pas plus de 3 chiffres après la virgule

    def __AllCalculs__(self) -> None:
        """Méthode de calcculs afin de pouvoirs écrire toutes les corrections.
        Input : /
        Output : / """

        # arrondie à 10^-3
        self.VCube = self.arrondir(self.a**3)
        self.VSphere = self.arrondir(4/3 * pi * self.r**3)
        self.VCone = self.arrondir(1/3 * self.h * pi * (self.d/2)**2)
        self.VCylindre = self.arrondir(pi * self.h * self.r**2)
        self.VPaveDroit = self.arrondir(self.L * self.l * self.h)
        self.VPyramideBaseCarre = self.arrondir((self.b**2 * self.h) / 3)
        self.ADisque = self.arrondir(pi * (self.d / 2)**2)
        self.ATriangleRectangle = self.arrondir((self.a * self.b) / 2)
        self.ARectangle = self.arrondir(self.L * self.l)


    def VolumesTitreCorrection(self) -> None:
        """Méthode d'écriture du titre des corrections
        Input : / 
        Output : / """

        with self.doc.create(Section(f"Correction Exo Volumes n°{self.i + 1}", numbering=False)): # titre exp correction
            self.doc.append(NoEscape("Niveau 1 :\\\\"))
            self.doc.append(NoEscape("\\  \\\\"))

    def CorrectionVCube(self, numEtape) -> None:
        """Méthode d'écriture de la correction pour : calculer le volume d'un cube
            Input : numéro de l'étape
            Output : / """ 

        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape %s : Calculer le volume d'un cube} \\\\ La formule pour calculer le volume d'un cube de côte c est :}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ Vcube = c^3 \\\\"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))    
        
        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $c$ par %s: }}" % (self.a)))
        self.doc.append(NoEscape("\\begin{align*}"))  
        self.doc.append(NoEscape("\\ Vcube &= %s^3 \\\\" % (self.a)))
        self.doc.append(NoEscape("\\ Vcube &\\approx %s m^3 \\\\" % (self.VCube)))
        self.doc.append(NoEscape("\\\\"))

        self.doc.append(NoEscape("\\end{align*}"))

    def CorrectionVSphere(self, numEtape) -> None:
        """Méthode d'écriture de la correction pour : calculer le volume d'une sphere
            Input : numéro de l'étape
            Output : / """ 
        
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape %s : Calculer le volume d'une sphere} \\\\ La formule pour calculer le volume d'une sphere de rayon r est :}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ VSphere = \\frac{4}{3} \\cdot \\pi \\cdot r^3 \\\\"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))    
        
        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $r$ par %s: }}" % (self.r)))
        self.doc.append(NoEscape("\\begin{align*}"))  
        self.doc.append(NoEscape("\\ VSphere &= \\frac{4}{3} \\cdot \\pi \\cdot %s^3  \\\\" % (self.r)))
        self.doc.append(NoEscape("\\ VSphere &\\approx %s m^3 \\\\" % (self.VSphere)))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))

    def CorrectionVCone(self, numEtape) -> None: 
        """Méthode d'écriture de la correction pour : calculer le volume d'un cône
        Input : numéro de l'étape
        Output : / """ 
        
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape %s : Calculer le volume d'un cone} \\\\ La formule pour calculer le volume d'un cone de hauteur h et de diametre de base $d$ est :}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ VCone = \\frac{1}{3} \\cdot \\pi \\cdot r^2 \\cdot h \\\\"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))    
        
        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $h$ par %s; $r$ par $\\frac{%s}{2}$ : }}" % (self.h, self.d)))
        self.doc.append(NoEscape("\\begin{align*}"))  
        self.doc.append(NoEscape("\\ VCone &= \\frac{1}{3} \\cdot \\pi \\cdot %s^2 \\cdot %s  \\\\" % (self.d/2, self.h )))
        self.doc.append(NoEscape("\\ VCone &\\approx %s m^3 \\\\" % (self.VCone)))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}")) 

    def CorrectionVCylindre(self, numEtape) -> None: 
        """Méthode d'écriture de la correction pour : calculer le volume d'un cylindre
        Input : numéro de l'étape
        Output : / """ 
        
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape %s : Calculer le volume d'un cylindre} \\\\ La formule pour calculer le volume d'un cylindre de rayon de base r et de hauteur h est :}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ VCylindre = \\pi \\cdot r^2 \\cdot h \\\\"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))    
        
        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $h$ par %s; $r$ par %s : }}" % (self.h, self.r)))
        self.doc.append(NoEscape("\\begin{align*}"))  
        self.doc.append(NoEscape("\\ VCylindre &= \\pi \\cdot %s^2 \\cdot %s \\\\" % (self.r, self.h )))
        self.doc.append(NoEscape("\\ VCylindre &\\approx %s m^3 \\\\" % (self.VCylindre)))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}")) 

    def CorrectionVPaveDroit(self, numEtape) -> None: 
        """Méthode d'écriture de la correction pour : calculer le volume d'un pavé droit
        Input : numéro de l'étape
        Output : / """ 
        
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape %s : Calculer le volume d'un pavé droit} \\\\ La formule pour calculer le volume d'un pavé droit de longeur L, de largeur l et de hauteur h est :}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ VPaveDroit = L \\cdot l \\cdot h \\\\"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))    
        
        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $h$ par %s; $L$ par %s ; $l$ = %s: }}" % (self.h, self.L, self.l)))
        self.doc.append(NoEscape("\\begin{align*}"))  
        self.doc.append(NoEscape("\\ VPaveDroit &= %s \\cdot  %s \\cdot %s \\\\" % (self.L, self.l, self.h)))
        self.doc.append(NoEscape("\\ VPaveDroit &= %s m^3 \\\\" % (self.VPaveDroit)))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}")) 

    def CorrectionVPyramideBaseCarre(self, numEtape) -> None: 
        """Méthode d'écriture de la correction pour : calculer le volume d'une piramide à base carré
        Input : numéro de l'étape
        Output : / """ 
        
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape %s : Calculer le volume d'une pyramide à base carré} \\\\ La formule pour calculer le volume d'une pyramide à base carré de côté de base c et de hauteur h est :}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ VPyramideBaseCarre = \\frac{c^2 \\cdot h}{3} \\\\"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))    
        
        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $h$ par %s; $c$ par %s}}" % (self.h, self.b)))
        self.doc.append(NoEscape("\\begin{align*}"))  
        self.doc.append(NoEscape("\\ VPyramideBaseCarre &= \\frac{%s^2 \\cdot %s}{3} \\\\" % (self.b, self.h)))
        self.doc.append(NoEscape("\\ VPyramideBaseCarre &\\approx %s m^3 \\\\" % (self.VPyramideBaseCarre)))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}")) 

    def CorrectionADisque(self, numEtape) -> None: 
        """Méthode d'écriture de la correction pour : calculer l'aire d'un dique
        Input : numéro de l'étape
        Output : / """ 
        
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape %s : Calculer l'aire d'un disque} \\\\ La formule pour calculer l'aire d'un disque de diametre d est :}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ ADisque = \\pi \\cdot r^2 \\\\"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))    
        
        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $r$ par $\\frac{%s}{2}$ }}" % (self.d)))
        self.doc.append(NoEscape("\\begin{align*}"))  
        self.doc.append(NoEscape("\\ ADisque &=  \\pi \\cdot %s^2 \\\\" % (self.d /2)))
        self.doc.append(NoEscape("\\ ADisque &\\approx%s m^2 \\\\" % (self.ADisque)))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}")) 

    def CorrectionATriangleRectangle(self, numEtape) -> None: 
        """Méthode d'écriture de la correction pour : calculer l'aire d'un triangle rectangle
        Input : numéro de l'étape
        Output : / """ 
        
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape %s : Calculer l'aire d'un triangle rectangle} \\\\ La formule pour calculer l'aire d'un triangle ABC rectangle en A de côté AB et AC est :}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ ATriangleRectangle = \\frac{AB \\cdot AC}{2} \\\\"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))    
        
        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant AB par %s ; AC par %s }}" % (self.a, self.b)))
        self.doc.append(NoEscape("\\begin{align*}"))  
        self.doc.append(NoEscape("\\ ADisque &=  \\frac{%s \\cdot %s}{2} \\\\" % (self.a, self.b)))
        self.doc.append(NoEscape("\\ ADisque &\\approx %s m^2 \\\\" % (self.ATriangleRectangle)))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}")) 


    def CorrectionARectangle(self, numEtape) -> None: 
        """Méthode d'écriture de la correction pour : calculer l'aire d'un rectangle
        Input : numéro de l'étape
        Output : / """ 
        
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape %s : Calculer l'aire d'un rectangle} \\\\ La formule pour calculer l'aire d'un  rectangle de longueur et largeur L et l est :}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ ATriangleRectangle = L \\cdot l \\\\"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))    
        
        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $L$ par %s ; $l$ par %s }}" % (self.L, self.l)))
        self.doc.append(NoEscape("\\begin{align*}"))  
        self.doc.append(NoEscape("\\ ADisque &=  %s \\cdot %s \\\\" % (self.L, self.l)))
        self.doc.append(NoEscape("\\ ADisque &\\approx %s m^2 \\\\" % (self.ARectangle)))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}")) 