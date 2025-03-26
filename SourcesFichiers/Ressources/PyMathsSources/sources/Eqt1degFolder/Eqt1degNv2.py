from SourcesFichiers.Ressources.PyMathsSources.sources.settingsPyMaths import *

class Eqt1degNv2(object):
    """ Class parent de l'exercice équation du premier degré. Contient des méthodes utilisés globalement.
        Permet de gérer plus facilement des appels et la création des exercices.
        
        Input : 
            doc -> pdf latex
            nb1 -> int, valeurs > 2
            nb2 -> int, valeurs > 2
            nb3 -> int, valeurs > 2
            nb4 -> int, valeurs > 2
            nb5 -> int, valeurs > 2
            nb6 -> int, valeurs > 2

        Output : / """
    
    def __init__(self, doc, nb1, nb2, nb3, nb4,nb5, nb6) -> None:
        """ Initialisation des attributs de la class de parent de l'exercice équation du permier degré. """
      
        self.doc = doc # pdf latex
        self.nb1 = nb1 # coef nb  
        self.nb2 = nb2 # coef nb  
        self.nb3 = nb3 # coef nb  
        self.nb4 = nb4 # coef nb  
        self.nb5 = nb5 # coef nb 
        self.nb6 = nb6 # coef nb 

    def __pgcd__(self, a,b) -> int:
        """ Méthode pgcd, permet de calculer le plus grand diviseur comment entre deux nombres. Utiliser pour créer des fractions iréductibles.
            Input : 
                a -> nombre entier 
                b -> nombre entier
            Output : a -> nombre entier """
        
        while b != 0:
            a,b=b,a%b
        return a # retour du pgcd 

class ConsignesEqt1degNv2(Eqt1degNv2):
    """ Class enfant contenant toutes la méthode pour pouvoir écrire les consignes.
        
        Input : 
            doc -> pdf latex
            i -> numéro de l'exercice
            nb1 -> int, valeurs > 2
            nb2 -> int, valeurs > 2
            nb3 -> int, valeurs > 2
            nb4 -> int, valeurs > 2
            nb5 -> int, valeurs > 2
            nb6 -> int, valeurs > 2

        Output : / """

    def __init__(self, doc, i, nb1, nb2, nb3, nb4, nb5, nb6) -> None:
        """ Initialisation des attributs de la class enfant consignes, de l'exercice équation du premier degré. """

        super().__init__(doc, nb1, nb2, nb3, nb4, nb5, nb6) # initialisation class parent
        self.i = i # numéro exercice

    def Eqt1degNv2Consigne(self) ->None:
        """ Méthode d'écriture du titres des consignes, avec l'équation. 
        Input : /
        Output : / """

        with self.doc.create(Section(f'Exo Equation du premier degré n°{self.i + 1}', numbering = False)):
            self.doc.append(NoEscape("\\ \\text{Trouver la valeur de $x$ dans cette équation du premier degré :}\\\\ " % ()))
            self.doc.append(NoEscape("\\\\"))

        # viveau 2 exo
        self.doc.append("Niveau 2 :")
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx \\\\" % (self.nb1,self.nb2,self.nb3,self.nb4,self.nb5,self.nb6)))
        self.doc.append(NoEscape("\\end{align*}"))

class CorrectionEqt1degNv2(Eqt1degNv2):
    """ Class enfant contenant toutes la méthode pour pouvoir écrire la correction et calculer les valeurs. 
    
        Input : 
            doc -> pdf latex
            i -> numéro de l'exercice
            nb1 -> int, valeurs > 2
            nb2 -> int, valeurs > 2
            nb3 -> int, valeurs > 2
            nb4 -> int, valeurs > 2
            nb5 -> int, valeurs > 2
            nb6 -> int, valeurs > 2
    
        Output : / """
    
    def __init__(self, doc, i, nb1, nb2, nb3, nb4, nb5, nb6) -> None:
        """ Initialisation des attributs de la class enfant correction, de l'exercice équation du premier degré. """

        super().__init__(doc, nb1, nb2, nb3, nb4, nb5, nb6) # initialisation class parent
        self.i = i # numéro exercice

    def Eqt1degNv2Correction(self) ->None :
        """ Méthode d'écriture du titre des corrections ainsi que toutes les étapes de correction (un seul élément). 
            Input : /
            Output : / """
        
        with self.doc.create(Section(f"Correction Exo n°{self.i + 1}", numbering=False)):
            self.doc.append("Niveau 2 :")

            self.doc.append(NoEscape("\\text{L'équation donnée est : }"))
            
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\  \\Leftrightarrow \\frac{%s}{%s}x + %s &= \\frac{%s}{%s} - %sx \\\\" % (self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6)))
            self.doc.append(NoEscape("\\end{align*}"))

        # etape 1 : Simplification des fractions et dénominateur commun
        self.doc.append(NoEscape("\\textbf{Étape 1 : Simplification des fractions et mise au même dénominateur.}\\\\"))
        den_common = self.nb2 * self.nb5  # dénominateur commun

        # fractions simplifiées si nécessaire
        num1 = self.nb1 * self.nb5  # ajustement des numérateurs pour dénominateur commun
        num2 = self.nb4 * self.nb2
        self.doc.append(NoEscape("\\text{Nous multiplions chaque terme par le dénominateur commun } %s \\text{ :}" % den_common))

        # nouvelle équation après mise au dénominateur commun
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  \\Leftrightarrow %sx + %s \\cdot %s &= %s - %s \\cdot %sx \\\\" % (num1, self.nb3, den_common, num2, self.nb6, den_common)))
        num3 = self.nb3 * den_common  # multiplication des termes constants
        num6 = self.nb6 * den_common
        self.doc.append(NoEscape("\\  \\Leftrightarrow %sx + %s &= %s - %sx \\\\" % (num1, num3, num2, num6)))
        self.doc.append(NoEscape("\\end{align*}"))

        # etape 2 : Regroupement des termes
        self.doc.append(NoEscape("\\textbf{Étape 2 : Regroupement des termes en } x \\text{ d’un côté et les constantes de l’autre côté.}\\\\"))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  \\Leftrightarrow %sx + %sx &= %s - %s \\\\" % (num1, num6, num2, num3)))

        # calcul des coefficients
        numx = num1 + num6
        num_const = num2 - num3
        self.doc.append(NoEscape("\\  \\Leftrightarrow %sx &= %s \\\\" % (numx, num_const)))
        self.doc.append(NoEscape("\\end{align*}"))

        # etape 3 : Isolation de x
        self.doc.append(NoEscape("\\textbf{Étape 3 : Isolation de } x \\text{ en divisant par le coefficient.}\\\\"))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s}{%s} \\\\" % (num_const, numx)))

        # simplification finale de la fraction
        gcd = super().__pgcd__(num_const, numx)
        num_const //= gcd
        numx //= gcd
        if numx == 1:
            self.doc.append(NoEscape("\\  \\Leftrightarrow x &= %s \\\\" % num_const))
        else:
            self.doc.append(NoEscape("\\  \\Leftrightarrow x &= \\frac{%s}{%s} \\\\" % (num_const, numx)))
        self.doc.append(NoEscape("\\end{align*}"))