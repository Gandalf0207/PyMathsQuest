# import settings
from SourcesFichiers.Ressources.PyMathsSources.sources.settingsPyMaths import *

class Eqt1degNv1(object):
    """ Class parent de l'exercice équation du premier degré. Contient des méthodes utilisés globalement.
        Permet de gérer plus facilement des appels et la création des exercices.
        
        Input : 
            doc -> pdf latex
            nb1 -> int, valeurs > 2
            nb2 -> int, valeurs > 2
            nb3 -> int, valeurs > 2
            nb4 -> int, valeurs > 2

        Output : / """

    def __init__(self, doc, nb1, nb2, nb3, nb4) -> None:
        """ Initialisation des attributs de la class de parent de l'exercice équation du permier degré. """
        
        self.doc = doc # pdf latex
        self.nb1 = nb1 # coef nb 
        self.nb2 = nb2 # coef nb 
        self.nb3 = nb3 # coef nb 
        self.nb4 = nb4 # coef nb 

    def __pgcd__(self, a, b) -> int:
        """ Méthode pgcd, permet de calculer le plus grand diviseur comment entre deux nombres. Utiliser pour créer des fractions iréductibles.
            Input : 
                a -> nombre entier 
                b -> nombre entier
            Output : a -> nombre entier """
        
        while b != 0:
            a,b=b,a%b
        return a    # retour du pgcd 

class ConsignesEqt1degNv1(Eqt1degNv1):
    """ Class enfant contenant toutes la méthode pour pouvoir écrire les consignes.
        
        Input : 
            doc -> pdf latex
            i -> numéro de l'exercice
            nb1 -> int, valeurs > 2
            nb2 -> int, valeurs > 2
            nb3 -> int, valeurs > 2
            nb4 -> int, valeurs > 2
    
        Output : / """
    
    def __init__(self, doc, i, nb1, nb2, nb3, nb4) -> None:
        """ Initialisation des attributs de la class enfant consignes, de l'exercice équation du premier degré. """

        super().__init__(doc, nb1, nb2, nb3, nb4) # initialisation class parent 
        self.i = i # numéro exercice

    def Eqt1degNv1Consigne(self) -> None:
        """ Méthode d'écriture du titres des consignes, avec l'équation. 
        Input : /
        Output : / """

        with self.doc.create(Section(f'Exo Equation du premier degré n°{self.i + 1}', numbering = False)):
            self.doc.append(NoEscape("\\ \\text{Trouver la valeur de $x$ dans cette équation du premier degré :}\\\\ " % ()))
            self.doc.append(NoEscape("\\\\"))

            # Niveau 1 exo
            self.doc.append("Niveau 1 :")
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\  \\Leftrightarrow %sx - %s &= %s + %sx \\\\" % (self.nb1, self.nb2, self.nb3, self.nb4)))
            self.doc.append(NoEscape("\\end{align*}"))

class CorrectionEqt1degNv1(Eqt1degNv1):
    """ Class enfant contenant toutes la méthode pour pouvoir écrire la correction et calculer les valeurs. 
    
        Input : 
            doc -> pdf latex
            i -> numéro de l'exercice
            nb1 -> int, valeurs > 2
            nb2 -> int, valeurs > 2
            nb3 -> int, valeurs > 2
            nb4 -> int, valeurs > 2
    
        Output : / """
    
    def __init__(self, doc, i, nb1, nb2, nb3, nb4) -> None:
        """ Initialisation des attributs de la class enfant correction, de l'exercice équation du premier degré. """
        
        super().__init__(doc, nb1, nb2, nb3, nb4) # initialisation class parent
        self.i = i # numéro exercice

    def Eqt1degNv1Correction(self)  -> None:
        """ Méthode d'écriture du titre des corrections ainsi que toutes les étapes de correction (un seul élément). 
            Input : /
            Output : / """
        
        with self.doc.create(Section(f"Correction Exo n°{self.i+1}", numbering = False)):
        # niveau 1 correction
            self.doc.append("Niveau 1 :")

        self.doc.append(NoEscape("\\ \\text{L'équation à résoudre est : } " % ()))

        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  \\Leftrightarrow %sx - %s &= %s + %sx \\\\" % (self.nb1,self.nb2,self.nb3,self.nb4)))
        self.doc.append(NoEscape("\\end{align*}"))


        # etape 1
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 1} : Regroupons les termes contenant la variable x d’un côté de l’équation et les termes constants de l’autre côté. Retirons %sx des deux côtés et ajoutons %s des deux côtés également : }" % (self.nb4,self.nb2)))

        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  \\Leftrightarrow %sx - %s + %s -%sx &= %s + %sx -%sx +%s \\\\" % (self.nb1,self.nb2,self.nb3,self.nb4,self.nb3,self.nb4,self.nb4,self.nb2)))
        nb = self.nb3 + self.nb2
        nbx = self.nb1 - self.nb4

        if nbx != 1:
            self.doc.append(NoEscape("\\  \\Leftrightarrow %sx &= %s \\\\" % (nbx,nb)))
            self.doc.append(NoEscape("\\end{align*}"))
        else:
            self.doc.append(NoEscape("\\  \\Leftrightarrow x &= %s \\\\" % (nb)))
            self.doc.append(NoEscape("\\end{align*}"))


        # etape 2 
        #que si x != 0
        if nbx != 1:
            self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 2} : Divisons les deux côtés de l’équation par %s pour isoler x et simplifions: }" % (nbx)))

            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%sx}{%s} &= \\frac{%s}{%s} \\\\" % (nbx,nbx,nb,nbx)))
            pgcd_frac3 = super().__pgcd__(nb,nbx)
            nb = nb//pgcd_frac3
            nbx = nbx//pgcd_frac3
            
            if nbx !=1:
                self.doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s}{%s} \\\\" % (nb,nbx)))
                self.doc.append(NoEscape("\\end{align*}"))
            else:
                self.doc.append(NoEscape("\\  \\Leftrightarrow x &= %s \\\\" % (nb)))
                self.doc.append(NoEscape("\\end{align*}"))      