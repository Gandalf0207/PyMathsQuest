#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

# import settings
from SourcesFichiers.Ressources.PyMathsSources.sources.settingsPyMaths import *

class Eqt2IncsNv1(object):
    """ Class parent de l'exercice équation à deux incs. Contient des méthodes utilisés globalement.
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
    
    def __init__(self, doc, nb1, nb2, nb3, nb4, nb5, nb6) -> None:
        """ Initialisation des attributs de la class de parent de l'exercice équation à deux incs. """

        self.doc = doc # pdf latex
        self.nb1 = nb1  # coef nb
        self.nb2 = nb2  # coef nb
        self.nb3 = nb3  # coef nb
        self.nb4 = nb4  # coef nb
        self.nb5 = nb5  # coef nb
        self.nb6 = nb6  # coef nb

    def __pgcd__(self, a, b) -> int:
        """ Méthode pgcd, permet de calculer le plus grand diviseur comment entre deux nombres. Utiliser pour créer des fractions iréductibles.
            Input : 
                a -> nombre entier 
                b -> nombre entier
            Output : a -> nombre entier """
        
        while b != 0:
            a,b=b,a%b
        return a # retour du pgcd 


class ConsignesEqt2IncsNv1(Eqt2IncsNv1):
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
        """ Initialisation des attributs de la class enfant consignes, de l'exercice equation à 2 incs. """

        super().__init__(doc, nb1, nb2, nb3, nb4, nb5, nb6) # initialisation class parent 
        self.i = i # numéro exercice

    def Eqt2IncsNv1Consigne(self) -> None:
        """ Méthode d'écriture du titres des consignes, avec l'équation. 
        Input : /
        Output : / """

        with self.doc.create(Section(f" Exo Équation à 2 inconnues n°{self.i+1}", numbering = False)):
            self.doc.append(NoEscape("\\ \\text{Pour chaque système d'équation ci-dessous; calculez la valeur (arrondie si nécéssaire) de $x$ et $y$}\\\\ " % ()))
            self.doc.append(NoEscape("\\\\"))

            # niveau 1 exo
            self.doc.append("Niveau 1 :")
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\begin{cases}"))
            self.doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (self.nb1, self.nb2, self.nb5)))
            self.doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (self.nb3, self.nb4, self.nb6)))
            self.doc.append(NoEscape("\\end{cases}"))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))

class CorrectionEqt2IncsNv1(Eqt2IncsNv1):
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
        """ Initialisation des attributs de la class enfant correction, de l'exercice équation à 2 incs. """

        super().__init__(doc, nb1, nb2, nb3, nb4, nb5, nb6) # initialisation class parent
        self.i = i # numéro exercice

    def Eqt2IncsNv1Correction(self) -> None:
        """ Méthode d'écriture du titre des corrections ainsi que toutes les étapes de correction (un seul élément). 
            Input : /
            Output : / """
        
        with self.doc.create(Section(f"Correction Exo n°{self.i+1}", numbering = False)):
            # niveau 1 correction
            self.doc.append("Niveau 1 :")
        # on redonne l'exercice
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\begin{cases}"))
        self.doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (self.nb1, self.nb2, self.nb5)))
        self.doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (self.nb3, self.nb4, self.nb6)))
        self.doc.append(NoEscape("\\end{cases}"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))

        #puis on développe chaque étape avec un commentaire de ce que l'on fait
        # etape 1 
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 1} : Multiplier chaque équation pour aligner les coefficients d'une variable. Pour aligner les coefficients de x, nous pouvons multiplier les deux équations pour obtenir le même coefficient de x. Par exemple, nous pouvons multiplier l'équation 1 par %s et l'équation 2 par %s: }" % (self.nb3,self.nb1)))

        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  %s \\times (%sx + %sy) &= %s \\times %s \\\\" % (self.nb3, self.nb1, self.nb2, self.nb5, self.nb3)))
        self.doc.append(NoEscape("\\  %s \\times (%sx + %sy) &= %s \\times %s \\\\" % (self.nb1, self.nb3, self.nb4, self.nb6, self.nb1)))
        self.doc.append(NoEscape("\\end{align*}"))

        newNb1 = self.nb3*self.nb1
        newNb2 = self.nb3*self.nb2
        newNb5 = self.nb3*self.nb5
        newNb3 = self.nb1*self.nb3
        newNb4 = self.nb1*self.nb4
        newNb6 = self.nb1*self.nb6
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (newNb1, newNb2, newNb5)))
        self.doc.append(NoEscape("\\  %sx + %sy &= %s \\\\" % (newNb3, newNb4, newNb6)))
        self.doc.append(NoEscape("\\end{align*}"))

        # etape 2 
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 2} : Soustraire les équations. En soustrayant l'équation 1 de l'équation 2, nous éliminons la variable x:}"))

        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ \\Leftrightarrow  (%sx + %sy) - (%sx + %sy) &= %s - %s\\\\" % (newNb1, newNb2, newNb3, newNb4, newNb5, newNb6)))
        newY = newNb2 - newNb4
        newValue = newNb5 - newNb6
        self.doc.append(NoEscape("\\ \\Leftrightarrow  %sy &= %s\\\\" % (newY, newValue)))
        self.doc.append(NoEscape("\\end{align*}"))

        # etape 3 
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 3} : Résoudre pour y}"))
        division = super().__pgcd__(newValue, newY)
        newValue = newValue// division
        newY = newY // division

        self.doc.append(NoEscape("\\begin{align*}"))
        if newY ==1:
            self.doc.append(NoEscape("\\ \\Leftrightarrow  y  &= %s\\\\" % (newValue)))
        else:
            self.doc.append(NoEscape("\\ \\Leftrightarrow  y  &= \\frac{%s}{%s} \\\\" % (newValue, newY)))
        self.doc.append(NoEscape("\\end{align*}"))
        
        
        # etape 4
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape 4} : Substituer y dans l'une des équations d'origine pour résoudre pour x}"))

        self.doc.append(NoEscape("\\begin{align*}"))
        if newY ==1 : 
            self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx + %s &= %s\\\\" % (self.nb1, self.nb2, self.nb5)))
            self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx &= %s - %s\\\\" % (self.nb1, self.nb5, self.nb2)))
            newValue2 = self.nb5 - self.nb2
            self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s \\\\" % (self.nb1, newValue2)))
            division = super().__pgcd__(self.nb1, newValue2)
            newX = self.nb1 // division
            newValue2 = newValue2 // division

            if newX ==1:
                self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= %s \\\\" % (newValue2)))
            else:
                self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\\\" % (newValue2, newX)))
        else:
            self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx + %s \\times \\frac{%s}{%s} &= %s\\\\" % (self.nb1, self.nb2, newValue, newY, self.nb5)))
            newValue_ = self.nb2*newValue
            division = super().__pgcd__(newValue_, newY)
            newValue_ = newValue_// division
            newY_ = newY // division
            if newY_ ==1:
                self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx + %s &= %s\\\\" % (self.nb1, newValue_, self.nb5)))
                self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx &= %s - %s\\\\" % (self.nb1, self.nb5, newValue_)))
                newValue2 = self.nb5 - newValue_
                self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s \\\\" % (self.nb1, newValue2)))
                division = super().__pgcd__(self.nb1, newValue2)
                newX = self.nb1 // division
                newValue2 = newValue2 // division

                if newX ==1:
                    self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= %s \\\\" % (newValue2)))
                else:
                    self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\\\" % (newValue2, newX)))
            else:
                self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx + \\frac{%s}{%s}  &= %s\\\\" % (self.nb1, newValue_, newY_, self.nb5)))
                self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s - \\frac{%s}{%s}\\\\" % (self.nb1, self.nb5, newValue_, newY_)))
                newValue2 = newValue_ - self.nb5*newY_  
                division = super().__pgcd__(newValue2, newY_)
                newValue2 = newValue2// division
                newY_ = newY_ // division

                if newY_ ==1:
                    self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= %s \\\\" % (self.nb1, newValue2)))
                    division = super().__pgcd__(self.nb1, newValue2)
                    newX = self.nb1 // division
                    newValue2 = newValue2 // division

                    if newX ==1:
                        self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= %s \\\\" % (newValue2)))
                    else:
                        self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\\\" % (newValue2, newX)))
                else:
                    self.doc.append(NoEscape("\\ \\Leftrightarrow  %sx  &= \\frac{%s}{%s} \\\\" % (self.nb1, newValue2, newY_)))
                    self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\times \\frac{1}{%s} \\\\" % (newValue2, newY_, self.nb1)))
                    newX = newY_*self.nb1
                    division = super().__pgcd__(newValue2, newX)
                    newValue2 = newValue2// division
                    newX = newX // division

                    if newX ==1:
                        self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= %s \\\\" % (newValue2)))
                    else:
                        self.doc.append(NoEscape("\\ \\Leftrightarrow  x  &= \\frac{%s}{%s} \\\\" % (newValue2, newX))) 
        
        self.doc.append(NoEscape("\\end{align*}"))  
