#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

# import settings
from SourcesFichiers.Ressources.PyMathsSources.sources.settingsPyMaths import *

class VolumesNv2(object):
    """Class parent de l'exercice de calcul de volume. Contient des méthodes utilisés globalement.
    Permet de gérer plus facilement des apples et la création des exercices.
    
        Input : 
            doc -> pdf latex
            a -> int, valeur 5,25 
            b -> int, valeur 25,50 
            r -> int, valeur 4, 12 
            h -> int, valrur 3, 45

        Output : / """
    
    def __init__(self, doc, a, b, r, h) -> None:
        """Initialisation des attributs de la class parent de l'exercie Volumes"""

        self.doc = doc # pdf latex
        self.a = a # coef nb
        self.b = b # coef nb
        self.c = b/4
        self.d = a + 3
        self.f = r - 1.5
        self.r = r # coef nb
        self.h = h # coef nb

        self.e = sqrt((self.r**2) + (self.h**2))  # hypothénuse

    def __pgcd__(self, a, b) -> int:
        """ Méthode pgcd, permet de calculer le plus grand diviseur comment entre deux nombres. Utiliser pour créer des fractions iréductibles.
            Input : 
                a -> nombre entier 
                b -> nombre entier
            Output : a -> nombre entier """

        while b != 0:
            a,b=b,a%b
        return a # retour du pgcd



class ConsignesVolumesNv2(VolumesNv2):
    """Class enfant contenant toutes la méthode pour pouvoir écrire les consignes
    
        Input : 
            doc -> pdf latex
            i -> int numéro de l'exercice
            a -> int, valeur 5,25 
            b -> int, valeur 25,50 
            r -> int, valeur 4, 12 
            h -> int, valrur 3, 45

        Output : / """
    
    def __init__(self, doc, i, a, b, r, h) -> None:
        """Initialisation des attributs de la class enfant consignes, de l'exercice volumes."""

        super().__init__(doc, a, b, r, h)
        self.i = i # nunméro de l'exercice

    def VolumesNv2Consigne(self) -> None:
        """Méthode d'écriture du titre des consignes
        Input  : /    
        Output : /"""
        image_path = "Images/VolumesImages/volume.png"


        with self.doc.create(Section(f"Exo Volumes n°{self.i+1}", numbering=False)): #titre de l'exo
            self.doc.append(NoEscape("Niveau 2 :\\\\"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\ \\parbox{ 450pt }{ A l'aide des valeurs données, veuillez calculer le volume total de la figure représentée ci-dessous. a = %sm ; b = %sm ; c = %sm ; d = %sm ; e = %sm ; f = %sm ; r = %sm}  \\\\" % (self.a, self.b, self.c, self.d, self.e, self.f, self.r))) # consigne générale
            self.doc.append(NoEscape("\\\\"))

            # Ajouter une image
            with self.doc.create(Figure(position='h!')) as figure:
                figure.add_image(image_path, width=NoEscape(r'0.8\textwidth'))  # Spécifiez le chemin et la largeur
                figure.add_caption("Figure représentant la géométrie de l'exercice.")


class CorrectionVolumesNv2(VolumesNv2):
    """Class enfant contenant toutes la méthode pour pouvoir écrire les corrections
    
        Input : 
            doc -> pdf latex
            i -> int numéro de l'exercice
            a -> int, valeur 5,25 
            b -> int, valeur 25,50 
            r -> int, valeur 4, 12 
            h -> int, valrur 3, 45

        Output : / """
    
    def __init__(self, doc, i, a, b, r, h) -> None:
        """Initialisation des attributs de la class enfant correction, de l'exercice volumes."""

        super().__init__(doc, a, b, r, h)
        self.i = i # nunméro de l'exercice

        self.__AllCalculs__()


    def arrondir(self, valeur):
        """Arrondit à 3 chiffres après la virgule uniquement si le nombre a plus de 3 chiffres après la virgule."""
        if isinstance(valeur, float):
            # Multiplie la valeur par 1000, prend la partie entière, puis compare
            if int(valeur * 1000) != valeur * 1000:
                return round(valeur, 3)
        return valeur  # Si pas un float ou pas plus de 3 chiffres après la virgule
    
    def __AllCalculs__(self):
        self.baseCylindre = self.arrondir(self.r**2 * pi)
        self.volumeCylindre1 = self.arrondir(self.r**2 * pi * self.a)
        self.volumeCylindre2 = self.arrondir(self.r**2 * pi * self.b)
        self.volumeGrandPaveDroit = self.b * self.f * self.a
        self.volumePetitPaveDroit = self.c * self.f * (self.d - self.a)
        self.volumeCone = self.arrondir((self.r**2 * pi * self.h) /3)

        self.volumeTotalChateau = self.volumeCone*2 + self.volumeCylindre1 + self.volumeCylindre2 + self.volumePetitPaveDroit + self.volumePetitPaveDroit

    def VolumesNv2Correction(self) -> None:
        """Méthode d'écriture du titre des corrections
        Input  : /    
        Output : /"""

        with self.doc.create(Section(f'Correction Exo Volume n°{self.i + 1}', numbering = False)): # titre exercice
            self.doc.append(NoEscape("Niveau 2 :\\\\"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\ \\parbox{ 450pt }{ \\text{Pour le calcul total du volume de ce chateau, il fallait trouver la hauteur du cône grace au theoreme de pythagore } (base et hypothénuse). \\\\ Cela permettait de trouver la valeur du côté adjacent (hauteur) } \\\\" )) # correction générale
            self.doc.append(NoEscape("\\\\"))            
            self.doc.append(NoEscape("\\\\"))


        
            # étape 1 : base cylindre 
            self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 1 : Calculer l'aire du disque du cylindre / cône (base) } \\\\ La formule pour calculer l'aire d'un disque de rayon r est :}"))
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\ ADisque = \\pi \\cdot r^2 \\\\"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}")) 

            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $r$ par %s }}" % (self.r)))
            self.doc.append(NoEscape("\\begin{align*}"))  
            self.doc.append(NoEscape("\\ ADisque &=  \\pi \\cdot %s^2 \\\\" % (self.r )))
            self.doc.append(NoEscape("\\ ADisque &\\approx %s m^2 \\\\" % (self.baseCylindre)))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}")) 

            # étape 2 : volume cylindre 1
            self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 2 : Calculer le volume du cylindre de gauche  } \\\\ La formule pour calculer le volume d'un cylindre avec une base $r^2 \\cdot \\pi$ et de hauteur h est :}"))
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\ VCylindre = r^2 \\cdot \\pi \\cdot h \\\\"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))    

            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $h$ par %s; $r$ par %s : }}" % (self.a, self.r)))
            self.doc.append(NoEscape("\\begin{align*}"))  
            self.doc.append(NoEscape("\\ VCylindre &= %s \\cdot %s^2 \\cdot \\pi \\\\" % (self.a, self.r)))
            self.doc.append(NoEscape("\\ VCylindre &\\approx %s m^3 \\\\" % (self.volumeCylindre1)))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}")) 

            # étape 3 : volume cylindre 2
            self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 3 : Calculer le volume du cylindre de droite  } \\\\ La formule pour calculer le volume d'un cylindre avec une base $r^2 \\cdot \\pi$ et de hauteur h est :}"))
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\ VCylindre = r^2 \\cdot \\pi \\cdot h \\\\"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))    

            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $h$ par %s; $r$ par %s : }}" % (self.b, self.r)))
            self.doc.append(NoEscape("\\begin{align*}"))  
            self.doc.append(NoEscape("\\ VCylindre &= %s \\cdot %s^2 \\cdot \\pi \\\\" % (self.b, self.r)))
            self.doc.append(NoEscape("\\ VCylindre &\\approx %s m^3 \\\\" % (self.volumeCylindre2)))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}")) 

            # étape 4 : volume gros pavé droit
            self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 4 : Calculer le volume du grand pavé droit  } \\\\ La formule pour calculer le volume d'un pavé droit de longeur L, de largeur l et de hauteur h est :}"))
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\ VPaveDroit = L \\cdot l \\cdot h \\\\"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))   

            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $h$ par %s; $L$ par %s ; $l$ = %s: }}" % (self.a, self.b, self.f)))
            self.doc.append(NoEscape("\\begin{align*}"))  
            self.doc.append(NoEscape("\\ VPaveDroit &= %s \\cdot  %s \\cdot %s \\\\" % (self.a, self.b, self.f)))
            self.doc.append(NoEscape("\\ VPaveDroit &= %s m^3 \\\\" % (self.volumeGrandPaveDroit)))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))      

            # étape 5 : volume grand pavé droit
            self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 5 : Calculer le volume du petit pavé droit  } \\\\ La formule pour calculer le volume d'un pavé droit de longeur L, de largeur l et de hauteur h est :}"))
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\ VPaveDroit = L \\cdot l \\cdot h \\\\"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))   

            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $h$ par %s; $L$ par %s ; $l$ = %s: }}" % ((self.d-self.a), self.c, self.f)))
            self.doc.append(NoEscape("\\begin{align*}"))  
            self.doc.append(NoEscape("\\ VPaveDroit &= %s \\cdot  %s \\cdot %s \\\\" % ((self.d-self.a), self.c, self.f)))
            self.doc.append(NoEscape("\\ VPaveDroit &= %s m^3 \\\\" % (self.volumePetitPaveDroit)))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))  

            
            # volume cone
            self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 6 : Calculer le volume du cône } \\\\ La formule pour calculer le volume d'un cône de hauteur $h$ et de base $r^2 \\cdot \\pi$  :}"))
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\ VCone = \\frac{1}{3} \\cdot r^2 \\cdot \\pi \\cdot h \\\\"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))  

                # calcul hauteur h
            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{Il faut calculer la hauteur $h$ à l'aide du rayon $r$ de la base et de la longueur $e$ en utilisant le théorème de pythagore.} \\\\ On utilise donc ce théorème  pour trouver la valeur de $h$ }" ))
            self.doc.append(NoEscape("\\begin{align*}"))  
            self.doc.append(NoEscape("\\ e^2 &= h^2 + r^2 \\\\" ))
            self.doc.append(NoEscape("\\ h^2 &= e^2 - r^2 \\\\" ))
            self.doc.append(NoEscape("\\ h &= \\sqrt{e^2 - r^2} \\\\" ))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))

            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant $e$ par %s; $r$ par %s : }}" % (self.e, self.r)))
            self.doc.append(NoEscape("\\begin{align*}"))  
            self.doc.append(NoEscape("\\ h &= \\sqrt{%s^2 - %s^2} \\\\" % (self.e, self.r)))
            self.doc.append(NoEscape("\\ h &= %s \\\\" % (self.h)))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}")) 

                #calcul volume cone
            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{Une fois la hauteur $h$ calculé, on remplace $h$ par %s; r par %s }}" % (self.h, self.r)))
            self.doc.append(NoEscape("\\begin{align*}"))  
            self.doc.append(NoEscape("\\ VCone &= \\frac{1}{3} \\cdot %s \\cdot %s^2 \\cdot \\pi \\\\" % (self.h, self.r)))
            self.doc.append(NoEscape("\\ VCone &= %s \\\\" % (self.volumeCone)))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))     

            # volume total 
            self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 7 : Calculer de la somme des volumes  } \\\\ Il suffit d'additionner tout les volumes entre eux : } \\\\"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\ VChâteau &\\approx %s m^3 \\\\" % (self.volumeTotalChateau)))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))   



