# import settings 
from SourcesFichiers.Ressources.PyMathsSources.sources.settingsPyMaths import *

class Poly2degNv(object):
    """ Class parent de l'exercice Polynôme du second degré. Contient des méthodes utilisées à plusieurs reprises par les deux class enfant. 
        Permet de gérer plus facilement des appels et la création des exercices.

        Input : 
            doc -> pdf latex
            a -> valeurs différentes de 0
            b -> valeurs différentes de 0
            c -> valeurs différentes de 0
        
        Output : / """
    
    def __init__(self, doc, a, b, c) -> None:
        """ Initialisation des attributs de la class de parent de l'exercice polynômes du second degré. """

        self.doc = doc # pdf latex

        self.a = a # coef a
        self.b = b # coef b
        self.c = c # coef c

    def __pgcd__(self, a, b) -> int:
        """ Méthode pgcd, permet de calculer le plus grand diviseur comment entre deux nombres. Utiliser pour créer des fractions iréductibles.
            Input : 
                a -> nombre entier 
                b -> nombre entier
            Output : a -> nombre entier """

        while b != 0:
            a,b=b,a%b
        return a # retour du pgcd
    
    def __WritePoly__(self, element = "x") -> None:
        """ Méthode permettant d'écrire le polynôme du second degré. s'adapte aux valeurs envoyés (0, alpha...) également.
            Input : element -> str ou int
            Output : /  """
        
        # bloc au centre de la page page : polynome
        self.doc.append(NoEscape("\\begin{align*}"))
        if self.b < 0 or self.c < 0: # permet de respecter l'affichage mathématique
            if self.b < 0 and self.c < 0:
                self.doc.append(NoEscape("\\ f(%s) =  %s%s^2  %s%s  %s \\\\" % (element, self.a, element, self.b, element, self.c)))
            elif self.b < 0:
                self.doc.append(NoEscape("\\ f(%s) =  %s%s^2  %s%s + %s \\\\" % (element, self.a, element, self.b, element, self.c)))
            else:
                self.doc.append(NoEscape("\\ f(%s) =  %s%s^2 + %s%s  %s \\\\" % (element, self.a, element, self.b, element, self.c)))
        else:
            self.doc.append(NoEscape("\\ f(%s) =  %s%s^2 + %s%s + %s \\\\" % (element, self.a, element, self.b, element, self.c)))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))


class ConsignesPoly2degNv(Poly2degNv):
    """ Class enfant contenant toutes les méthodes pour pouvoir écrire les consignes.
        
        Input : 
            doc -> pdf latex
            i -> numéro de l'exercice
            a -> valeurs différentes de 0
            b -> valeurs différentes de 0
            c -> valeurs différentes de 0
    
        Output : / """
    
    def __init__(self, doc, i, a, b, c) -> None:
        """ Initialisation des attributs de la class enfant consignes, de l'exercice polynômes du second degré. """

        super().__init__(doc, a, b, c) # initialisation class parent 
        self.i = i # numéro exercice

    def Poly2DegTitreConsigne(self) -> None :
        """ Méthode d'écriture du titres des consignes. 
            Input : /
            Output : / """
        
        with self.doc.create(Section(f" Exo Polynôme du second degré n°{self.i+1}", numbering = False)): # titre exercice
            self.doc.append(NoEscape("\\ \\text{A l'aide de cette fonction polynôme du second degré, répondez aux questions suivantes :}\\\\ ")) # consigne générale
            self.doc.append(NoEscape("\\\\"))

            super().__WritePoly__() # affichage du polynome pour l'exercice
    
    def ConsigneAlpha(self, numEtape) -> None :
        """ Méthode d'écriture de la consigne pour : calculer alpha.
            Input : numéro de l'étape
            Output : / """

        self.doc.append(NoEscape("\\ %s. Donner la valeur de α \\\\" % (numEtape)))      
        self.doc.append(NoEscape("\\\\"))

    def ConsigneBeta(self, numEtape) -> None :
        """ Méthode d'écriture de la consigne pour : calculer beta.
            Input : numéro de l'étape
            Output : / """

        self.doc.append(NoEscape("\\ %s. Déduire la valeur de  β \\\\" % (numEtape)))            
        self.doc.append(NoEscape("\\\\"))          

    def ConsigneDelta(self, numEtape) -> None :
        """ Méthode d'écriture de la consigne pour : calculer delta.
            Input : numéro de l'étape
            Output : / """

        self.doc.append(NoEscape("\\ %s. Calculer la valeur de Δ \\\\" % (numEtape)))            
        self.doc.append(NoEscape("\\\\"))

    def ConsigneSolutionsDelta(self, numEtape) -> None :
        """ Méthode d'écriture de la consigne pour : calculer la/les solution(s) de delta. 
            Input : numéro de l'étape
            Output : / """

        self.doc.append(NoEscape("\\ %s. Trouver la/les solution(s) possible de Δ \\\\" % (numEtape)))            
        self.doc.append(NoEscape("\\\\"))
    
    def ConsigneFormeCanonique(self, numEtape) -> None :
        """ Méthode d'écriture de la consigne pour : écrire la forme canonique.
            Input : numéro de l'étape
            Output : / """

        self.doc.append(NoEscape("\\ %s. Déterminer la forme canonique \\\\" % (numEtape)))            
        self.doc.append(NoEscape("\\\\"))
    
    def ConsigneSommetS(self, numEtape) -> None :
        """ Méthode d'écriture de la consigne pour : calculer le sommet S.
            Input : numéro de l'étape
            Output : / """

        self.doc.append(NoEscape("\\ %s. Déterminer le Sommet S \\\\" % (numEtape)))            
        self.doc.append(NoEscape("\\\\"))
    
    def ConsignePointA(self, numEtape) -> None :
        """ Méthode d'écriture de la consigne pour : calculer le point A.
            Input : numéro de l'étape
            Output : / """

        self.doc.append(NoEscape("\\ %s. Déterminer le point A ayant pour abscisse 0 \\\\" % (numEtape)))            
        self.doc.append(NoEscape("\\\\"))
    
    def ConsigneAllureCourbe(self, numEtape) -> None :
        """ Méthode d'écriture de la consigne pour : représenter l'allure de la courbe.
            Input : numéro de l'étape
            Output : / """

        self.doc.append(NoEscape("\\ %s. Représenter l'allure de la coube avec les deux points demandés \\\\" % (numEtape)))            
        self.doc.append(NoEscape("\\\\"))

    def ConsigneTableauSignes(self, numEtape) -> None :
        """ Méthode d'écriture de la consigne pour : créer le tableau de signes.
            Input : numéro de l'étape
            Output : / """

        self.doc.append(NoEscape("\\ %s. Dresser le tableau de signes de f(x) \\\\" % (numEtape)))            
        self.doc.append(NoEscape("\\\\"))
    
    def ConsigneTableauVariations(self, numEtape) -> None :
        """ Méthode d'écriture de la consigne pour : créer le tableau de variations.
            Input : numéro de l'étape
            Output : / """

        self.doc.append(NoEscape("\\ %s. Dresser le tableau de variations de f(x) \\\\" % (numEtape)))            
        self.doc.append(NoEscape("\\\\"))


class CorrectionsPoly2degNv(Poly2degNv):
    """ Class enfant contenant toutes les méthodes pour pouvoir écrire les corrections et calculer les valeurs. 
    
        Input : 
            doc -> pdf latex
            i -> numéro de l'exercice
            a -> valeurs différentes de 0
            b -> valeurs différentes de 0
            c -> valeurs différentes de 0
    
        Output : / """
    
    def __init__(self, doc, i, a, b, c) -> None:
        """ Initialisation des attributs de la class enfant correction, de l'exercice polynômes du second degré. """

        super().__init__(doc, a, b, c) # initialisation class parent
        self.i = i # numéro exercice
        self.alpha = None # création variables 
        self.beta = None # création variables 
        self.delta = None # création variables 
        self.deltaRacine = None # création variables 
        self.Scoords = None # création variables 
        self.Acoords = None # création variables 
        self.__AllCalculs__() # méthode de calcul pour toutes les valeurs nécessaires à l'exercice 

    def __AllCalculs__(self) -> None:
        """ Méthode effectuant tout les calculs afin de pouvoir écrire toutes les corrections.
            Input : /
            Output : / """
        
        #Calcul Alpha -> tuple
        numAlpha = -self.b
        denAlpha = 2*self.a
        divisionAlphaValue = super().__pgcd__(numAlpha, denAlpha)
        numAlpha = numAlpha // divisionAlphaValue
        denAlpha = denAlpha // divisionAlphaValue
        self.alpha = (numAlpha, denAlpha) # mise à jour de la valeur alpha

       # Calcul beta -> tuple
        numBeta = self.c * 4*self.a - self.b**2  
        denBeta = 4*self.a
        divisionBetaValue = super().__pgcd__(numBeta, denBeta)
        numBeta = numBeta // divisionBetaValue
        denBeta = denBeta // divisionBetaValue
        self.beta = (numBeta, denBeta)  # mise à jour de la valeur beta

        # Calcul delta : 
        self.delta = self.b**2 - 4*self.a*self.c # mise à jour de la valeur delta

        #solutions delta :
        if self.delta >0: 
            #calcul x1
            numx1, denx1 = self.__SimplificationDeltaRacines__(-self.b - sqrt(self.delta), 2 * self.a)
            #calcul x2
            numx2, denx2 = self.__SimplificationDeltaRacines__(-self.b + sqrt(self.delta), 2 * self.a)
            self.deltaRacine = ((numx1, denx1),(numx2, denx2)) # mise à jour des racines de delta

        elif self.delta == 0: 
            self.deltaRacine = (numAlpha, denAlpha) # mise à jour des racines de delta

        elif self.delta < 0:
            self.deltaRacine = None # mise à jour des racines de delta

        # Calculs des coordonnés des deux points
        self.Scoords = (round(self.alpha[0]/self.alpha[1], 2), round(self.beta[0]/self.beta[1], 2)) # mise à jours du sommet S
        self.Acoords = (0, self.c) # mise à jour du point A

    def __SimplificationDeltaRacines__(self, num, den) -> Union[int, float]:
        """ Méthode de pgcd légèrement différente, ne fonctionne qu'avec des entier pour le calculs des racines de delta > 0
        
        Input : 
            num -> int , float
            den -> int , float
            
        Output : 
            num -> int , float
            den -> int , float """
        
        num = num
        den = den

        if isinstance(num, int) and isinstance(den, int):
            # trouver le plus grand commun diviseur (PGCD)
            facteur_commun = super().__pgcd__(int(num), den)
            num //= facteur_commun
            den //= facteur_commun
    
        # retour des valeurs pour la fraction irréductible
        return num, den

    def Poly2DegTitreCorrection(self) -> None:
        """ Méthode d'écriture du titre des corrections. 
            Input : /
            Output : / """
        
        with self.doc.create(Section(f'Correction Exo Polynome du second degré n°{self.i + 1}', numbering = False)): # titre exercice
            self.doc.append(NoEscape("\\ \\text{Le polynome étudié} \\\\"))
            self.doc.append(NoEscape("\\\\"))

            super().__WritePoly__() # afffichage rappel du polynôme
    
    def CorrectionAlpha(self, numEtape) -> None:
        """ Méthode d'écriture de la correction pour : calculer alpha.
            Input : numéro de l'étape
            Output : / """
        
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape %s : Donner la valeur de α } \\\\ La valeur de α est calculée avec cette formule :}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ α = - \\frac{ b }{ 2 \\cdot a } \\\\"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))  

        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{En remplaçant : }}"))
        self.doc.append(NoEscape("\\begin{align*}"))  
        self.doc.append(NoEscape("\\ α &=  \\frac{- (%s)}{2 \\cdot (%s)} \\\\" % (self.b, self.a)))

        if self.alpha[1] == 1:
            self.doc.append(NoEscape("\\ α &= %s \\\\"%(self.alpha[0])))
        else:
            self.doc.append(NoEscape("\\ α &= \\frac{%s}{%s} \\\\" % (self.alpha[0], self.alpha[1])))

        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))  

    def CorrectionBeta(self, numEtape):
        """ Méthode d'écriture de la correction pour : calculer beta.
            Input : numéro de l'étape
            Output : / """ 
        
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape %s : Donner la valeur de β } \\\\ La valeur de β est calculée avec cette formule :}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ β = f(α)  \\\\"))
        self.doc.append(NoEscape("\\end{align*}"))
        super().__WritePoly__("α")


        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{Calculons : }}"))
        self.doc.append(NoEscape("\\begin{align*}"))
        if self.alpha[1] == 1:
            if self.b < 0 or self.c < 0:
                if self.b < 0 and self.c < 0:
                    self.doc.append(NoEscape("\\ β =  %s \\cdot (%s)^2  %s \\cdot (%s)  %s \\\\" % (self.a, self.alpha[0], self.b, self.alpha[0], self.c)))
                    self.doc.append(NoEscape("\\\\"))
                elif self.b < 0:
                    self.doc.append(NoEscape("\\ β =  %s \\cdot (%s)^2  %s \\cdot (%s) + %s \\\\" % (self.a, self.alpha[0], self.b, self.alpha[0], self.c)))
                    self.doc.append(NoEscape("\\\\"))
                else:
                    self.doc.append(NoEscape("\\ β =  %s \\cdot (%s)^2 + %s \\cdot (%s)  %s \\\\" % (self.a, self.alpha[0], self.b, self.alpha[0], self.c)))
                    self.doc.append(NoEscape("\\\\"))
            else:
                self.doc.append(NoEscape("\\ β =  %s \\cdot (%s)^2 + %s \\cdot (%s) + %s \\\\" % (self.a, self.alpha[0], self.b, self.alpha[0], self.c)))
                self.doc.append(NoEscape("\\\\"))
        else:
            if self.b < 0 or self.c < 0:
                if self.b < 0 and self.c < 0:
                    self.doc.append(NoEscape("\\ β =  %s \\cdot (\\frac{%s}{%s})^2  %s \\cdot (\\frac{%s}{%s})  %s \\\\" % (self.a, self.alpha[0], self.alpha[1], self.b, self.alpha[0], self.alpha[1], self.c)))
                    self.doc.append(NoEscape("\\\\"))
                elif self.b < 0:
                    self.doc.append(NoEscape("\\ β =  %s \\cdot (\\frac{%s}{%s})^2  %s \\cdot (\\frac{%s}{%s}) + %s \\\\" % (self.a, self.alpha[0], self.alpha[1], self.b, self.alpha[0], self.alpha[1], self.c)))
                    self.doc.append(NoEscape("\\\\"))
                else:
                    self.doc.append(NoEscape("\\ β =  %s \\cdot (\\frac{%s}{%s})^2 + %s \\cdot (\\frac{%s}{%s})  %s \\\\" % (self.a, self.alpha[0], self.alpha[1], self.b, self.alpha[0], self.alpha[1], self.c)))
                    self.doc.append(NoEscape("\\\\"))
            else:
                self.doc.append(NoEscape("\\ β =  %s \\cdot (\\frac{%s}{%s})^2 + %s \\cdot (\\frac{%s}{%s}) + %s \\\\" % (self.a, self.alpha[0], self.alpha[1], self.b, self.alpha[0], self.alpha[1], self.c)))
                self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))       


        self.doc.append(NoEscape("\\begin{align*}"))
        if self.beta[1] ==1 : 
            self.doc.append(NoEscape("\\ β = %s \\\\" % (self.beta[1])))
        else:
            self.doc.append(NoEscape("\\ β = \\frac{%s}{%s}\\\\" % (self.beta[0], self.beta[1])))

        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))       

    def CorrectionDelta(self, numEtape):
        """ Méthode d'écriture de la correction pour : calculer delta.
            Input : numéro de l'étape
            Output : / """
        
        self.doc.append(NoEscape("\\  \\parbox{ 450pt }{ \\textbf{Etape %s : Valeur de Δ } \\\\ La formule du discriminant est :}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ Δ = b^2 - 4 \\cdot a \\cdot c \\\\"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))

        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{Ici $a$ = %s, $b$ = %s, $c$ = %s. Calculons : }}" % (self.a, self.b, self.c)))
        self.doc.append(NoEscape("\\begin{align*}"))
        self.doc.append(NoEscape("\\ Δ &= (%s)^2 - 4 \\cdot (%s) \\cdot (%s) \\\\" % (self.b, self.a, self.c)))
        self.doc.append(NoEscape("\\ Δ &= %s \\\\" % (self.delta)))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))

    def CorrectionSolutionsDelta(self, numEtape):
        """ Méthode d'écriture de la correction pour : calculer la/les solution(s) de delta. 
            Input : numéro de l'étape
            Output : / """ 
        
        self.doc.append(NoEscape("\\parbox{ 450pt }{\\textbf{Etape %s : Trouver la/les solution(s) possible(s) de Δ} \\\\ Les solutions dépendent de la valeur de Δ :}"% (numEtape)))
        self.doc.append(NoEscape("{\\renewcommand{\\labelitemi}{\\textbullet}"))
        self.doc.append(NoEscape("\\begin{itemize}"))
        self.doc.append(NoEscape("\\item $\\text{Si Δ > 0, il y a deux solutions réelles distinctes.}$"))
        self.doc.append(NoEscape("\\item $\\text{Si Δ = 0, il y a une solution réelle unique (racine double).}$"))
        self.doc.append(NoEscape("\\item $\\text{Si Δ < 0, il n'y a pas de solution réelle, mais deux solutions complexes.}$"))
        self.doc.append(NoEscape("\\end{itemize}"))
        self.doc.append(NoEscape("\\ }"))  # Ferme la redéfinition temporaire de labelitemi
        self.doc.append(NoEscape("  \\\\"))

        # terminer delta    
        if self.delta > 0:
            self.doc.append(NoEscape("\\ \\parbox{ 450pt }{Ici Δ > 0, donc il y a \\textbf{deux solutions réelles distinctes} données par : }"))
            self.doc.append(NoEscape("\\begin{align*}"))            
            self.doc.append(NoEscape("\\ x1 = \\frac{-b - \\sqrt{Δ} }{2 \\cdot a}  ,  x2 = \\frac{-b + \\sqrt{Δ} }{2 \\cdot a} \\\\ "))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))  
            
            self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\text{Calculons :}}"))
            self.doc.append(NoEscape("\\begin{align*}"))

            if self.deltaRacine[0][1] == 1:            
                self.doc.append(NoEscape("\\ x1 = \\frac{-(%s) - \\sqrt{%s} }{2 \\cdot %s}  &=  %s \\\\" % (self.b, self.delta, self.a, self.deltaRacine[0][0])))
            else: 
                self.doc.append(NoEscape("\\ x1 = \\frac{-(%s) - \\sqrt{%s} }{2 \\cdot %s}  &\\approx  \\frac{%s}{%s} \\\\" % (self.b, self.delta, self.a, round(float(self.deltaRacine[0][0]),2), round(float(self.deltaRacine[0][1]),2))))

            if self.deltaRacine[1][1] == 1:            
                self.doc.append(NoEscape("\\ x2 = \\frac{-(%s) + \\sqrt{%s} }{2 \\cdot %s}  &=  %s \\\\" % (self.b, self.delta, self.a, self.deltaRacine[1][0])))
            else: 
                self.doc.append(NoEscape("\\ x2 = \\frac{-(%s) + \\sqrt{%s} }{2 \\cdot %s}  &\\approx  \\frac{%s}{%s} \\\\" % (self.b, self.delta, self.a, round(float(self.deltaRacine[1][0]),2), round(float(self.deltaRacine[1][1]),2))))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))


        elif self.delta == 0:
            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ Ici Δ = 0, donc il y a \\textbf{une solution réelle unique (racine double)} données par : }"))

            self.doc.append(NoEscape("\\begin{align*}"))            
            self.doc.append(NoEscape("\\ x = \\frac{-b}{2 \\codt a} \\\\ "))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))  

            self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\text{Calculons :}}"))
            self.doc.append(NoEscape("\\begin{align*}"))

            if self.deltaRacine[1] == 1:            
                self.doc.append(NoEscape("\\ x = \\frac{-(%s)}{2 \\cdot %s}  &=  %s \\\\" % (self.b, self.a, self.deltaRacine[0])))
            else: 
                self.doc.append(NoEscape("\\ x = \\frac{-(%s) }{2 \\cdot %s}  &\\approx  \\frac{%s}{%s} \\\\" % (self.b, self.a, round(float(self.deltaRacine[0]),2), round(float(self.deltaRacine[1]),2))))


        else:
            self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ Ici Δ < 0, donc il n'y a \\textbf{aucune solution réelle}}"))

            self.doc.append(NoEscape("\\begin{align*}"))            
            self.doc.append(NoEscape("\\ x = \\emptyset \\\\ "))
            self.doc.append(NoEscape("\\\\"))
            self.doc.append(NoEscape("\\end{align*}"))

    def CorrectionFormeCanonique(self, numEtape):
        """ Méthode d'écriture de la correction pour : écrire la forme canonique.
            Input : numéro de l'étape
            Output : / """
        
        self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\textbf{Etape %s : Déterminer la forme canonique} \\\\ La forme canonique d’un polynôme est donnée par :}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))            
        self.doc.append(NoEscape("\\ f(x) = a(x - α)^2 + β \\\\"))
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))

        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{Ainsi, la forme canonique est :}}"))
        self.doc.append(NoEscape("\\begin{align*}"))
        if self.alpha[1] == 1 or self.beta[1] == 1:
            if self.alpha[1] == 1 and self.beta[1] == 1:
                self.doc.append(NoEscape("\\ f(x) = %s(x - (%s))^2 + (%s) \\\\" % (self.a, self.alpha[0], self.beta[0])))
            elif self.beta[1] == 1 :
                self.doc.append(NoEscape("\\ f(x) = %s(x - \\frac{%s}{%s})^2 + (%s) \\\\" % (self.a, self.alpha[0],self.alpha[1], self.beta[0])))
            elif self.alpha[1] == 1 :
                self.doc.append(NoEscape("\\ f(x) = %s(x - (%s))^2 + \\frac{%s}{%s} \\\\" % (self.a, self.alpha[0], self.beta[0], self.beta[1])))
        else:
            self.doc.append(NoEscape("\\ f(x) = %s(x - \\frac{%s}{%s})^2 + \\frac{%s}{%s} \\\\" % (self.a, self.alpha[0], self.alpha[1], self.beta[0], self.beta[1])))

        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}")) 

    def CorrectionSommetS(self, numEtape):
        """ Méthode d'écriture de la correction pour : calculer le sommet S.
            Input : numéro de l'étape
            Output : / """
        
        self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\textbf{Etape %s : Déterminer le sommet $S$} \\\\ Le sommet $S$ est donné par les coordonnées (α,β).}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))    
        if self.alpha[1] == 1 or self.beta[1] == 1:
            if self.alpha[1] == 1 and self.beta[1] == 1:
                self.doc.append(NoEscape("\\ S = (%s, %s) \\\\" % (self.alpha[0], self.beta[0])))
            elif self.beta[1] == 1 :
                self.doc.append(NoEscape("\\ S = (\\frac{%s}{%s}, %s) \\\\" % (self.alpha[0],self.alpha[1], self.beta[0])))
            elif self.alpha[1] == 1 :
                self.doc.append(NoEscape("\\ S = (%s, \\frac{%s}{%s}) \\\\" % (self.alpha[0], self.beta[0], self.beta[1])))
        else:
            self.doc.append(NoEscape("\\ S = (\\frac{%s}{%s}, \\frac{%s}{%s}) \\\\" % (self.alpha[0], self.alpha[1], self.beta[0], self.beta[1])))

        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))

    def CorrectionPointA(self, numEtape):
        """ Méthode d'écriture de la correction pour : calculer le point A.
            Input : numéro de l'étape
            Output : / """
        
        self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\textbf{Etape %s : Déterminer le spoint $A$ ayant pour abscisse 0} \\\\ Pour $x$ = 0, calculons $f(0)$.}" % (numEtape)))
        self.doc.append(NoEscape("\\begin{align*}"))
        if self.b < 0 or self.c < 0:
            if self.b < 0 and self.c < 0:
                self.doc.append(NoEscape("\\ f(0) &=  %s \\cdot 0^2  %s \\cdot 0  %s \\\\" % (self.a, self.b, self.c)))
            elif self.b < 0:
                self.doc.append(NoEscape("\\ f(0) &=  %s \\cdot 0^2  %s \\cdot 0 + %s \\\\" % (self.a, self.b, self.c)))
            else:
                self.doc.append(NoEscape("\\ f(0) &=  %s \\cdot 0^2 + %s \\cdot 0  %s \\\\" % (self.a, self.b, self.c)))
        else:
            self.doc.append(NoEscape("\\ f(0) &=  %s \\cdot 0^2 + %s \\cdot 0 + %s \\\\" % (self.a, self.b, self.c)))

        self.doc.append(NoEscape("\\ f(0) &= %s \\\\" %(self.c) )) # self.c car les autres éléments s'annulent en 0
        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\end{align*}"))
        self.doc.append(NoEscape("\\ \\parbox{ 450 pt}{ \\text{Ainsi, le point $A$ est (0,%s):}}"% (self.c)))
        self.doc.append(NoEscape("\\\\"))

    def CorrectionAllureCourbe(self, numEtape):
        """ Méthode d'écriture de la correction pour : représenter l'allure de la courbe.
            Input : numéro de l'étape
            Output : / """

        courbe = CourbeRepresentation(self.doc, self.a, self.b, self.c, self.Scoords, self.Acoords) # création objet
        courbe.generate_graph() # création graphe
        courbe.courbe_poly(numEtape, width=r'1\textwidth', dpi=300) # ajout du graphe sur la page

        # insérer une barrière pour garantir l'ordre du contenu
        self.doc.append(NoEscape("\\FloatBarrier"))

    def CorrectionTableauSignes(self, numEtape):
        """ Méthode d'écriture de la correction pour : créer le tableau de signes.
            Input : numéro de l'étape
            Output : / """
        
        # rappel + description
        if self.a > 0:
            if self.delta < 0 : 
                self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\textbf{Etape %s : Déterminer le tableau de signes de $f(x)$} \\\\ La valeur de $Δ$ est négative : $Δ$ = %s < 0. La droite réelle est donc divisdé en un seul est unique interval.\\\\ Pour $a$ positif : $a$ = %s > 0 \\\\}" % (numEtape, self.delta, self.a)))
            elif self.delta == 0 : 
                self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\textbf{Etape %s : Déterminer le tableau de signes de $f(x)$} \\\\ La valeur de $Δ$ est null : $Δ$ = %s. La droite réelle est donc divisdé en deux intervals.\\\\ Pour $a$ positif : $a$ = %s > 0 \\\\}" % (numEtape, self.delta, self.a)))
            elif self.delta > 0  :
                self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\textbf{Etape %s : Déterminer le tableau de signes de $f(x)$} \\\\ La valeur de $Δ$ est positive : $Δ$ = %s > 0. La droite réelle est donc divisdé en trois intervals.\\\\ Pour $a$ positif : $a$ = %s > 0 \\\\}" % (numEtape, self.delta, self.a)))

        elif self.a < 0:
            if self.delta < 0 : 
                self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\textbf{Etape %s : Déterminer le tableau de signes de $f(x)$} \\\\ La valeur de $Δ$ est négative : $Δ$ = %s < 0. La droite réelle est donc divisdé en un seul est unique interval.\\\\ Pour $a$ négatif : $a$ = %s < 0 \\\\}" % (numEtape, self.delta, self.a)))
            elif self.delta == 0 : 
                self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\textbf{Etape %s : Déterminer le tableau de signes de $f(x)$} \\\\ La valeur de $Δ$ est null : $Δ$ = %s. La droite réelle est donc divisdé en deux intervals.\\\\ Pour $a$ négatif : $a$ = %s < 0 \\\\}" % (numEtape, self.delta, self.a)))
            elif self.delta > 0  :
                self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\textbf{Etape %s : Déterminer le tableau de signes de $f(x)$} \\\\ La valeur de $Δ$ est positive : $Δ$ = %s > 0. La droite réelle est donc divisdé en trois intervals.\\\\ Pour $a$ négatif : $a$ = %s < 0 \\\\}" % (numEtape, self.delta, self.a)))


        # tableau 
        self.doc.append(NoEscape("\\begin{table}[htbp]"))  # début du flottant
        self.doc.append(NoEscape("\\centering"))          # centrage
        self.doc.append(NoEscape("\\begin{tikzpicture}")) # début du TikZ

        if self.a > 0:
            if self.delta < 0: 
                self.doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f(x)$ / 1}{$- \\infty$, $+ \\infty$}"))
                self.doc.append(NoEscape("\\tkzTabLine{, +}"))                
            elif self.delta == 0: 
                self.doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f(x)$ / 1}{$- \\infty$, $\\alpha$, $+ \\infty$}"))
                self.doc.append(NoEscape("\\tkzTabLine{, +, z, +}"))
            elif self.delta > 0:
                self.doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f(x)$ / 1}{$- \\infty$, $x_1$, $x_2$, $+ \\infty$}"))
                self.doc.append(NoEscape("\\tkzTabLine{, +, z, -, z, +, }"))
        elif self.a < 0:
            if self.delta < 0: 
                self.doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f(x)$ / 1}{$- \\infty$, $+ \\infty$}"))
                self.doc.append(NoEscape("\\tkzTabLine{, -}"))
            elif self.delta == 0: 
                self.doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f(x)$ / 1}{$- \\infty$, $\\alpha$, $+ \\infty$}"))
                self.doc.append(NoEscape("\\tkzTabLine{, -, z, -}"))
            elif self.delta > 0:
                self.doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f(x)$ / 1}{$- \\infty$, $x_1$, $x_2$, $+ \\infty$}"))
                self.doc.append(NoEscape("\\tkzTabLine{, -, z, +, z, -, }"))  

        self.doc.append(NoEscape("\\end{tikzpicture}"))   # fin TikZ
        self.doc.append(NoEscape("\\caption{Table de signes pour $f(x)$}")) # légende
        self.doc.append(NoEscape("\\label{tab:variations}"))  # référence
        self.doc.append(NoEscape("\\end{table}"))        # fin du flottant

        # insérer une barrière pour garantir l'ordre du contenu
        self.doc.append(NoEscape("\\FloatBarrier"))

    def CorrectionTableauVariations(self, numETape):
        """ Méthode d'écriture de la consigne pour : créer le tableau de variations.
            Input : numéro de l'étape
            Output : / """
        
        # rappel + description
        if self.a > 0:
            self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\textbf{Etape %s : Dresser le tableau de variations de $f(x)$} \\\\ Pour $a$ > 0, la parabole à une branche descendante et une branche montante avec un minimum au sommet $S$  \\\\}" % (numETape)))
        elif self.a < 0:
            self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\textbf{Etape %s : Dresser le tableau de variations de $f(x)$} \\\\ Pour $a$ < 0, la parabole à une branche montante et une branche descendante avec un maximum au sommet $S$  \\\\}" % (numETape)))

        # tableau 
        self.doc.append(NoEscape("\\begin{table}[htbp]"))  # début du flottant
        self.doc.append(NoEscape("\\centering"))          # centrage
        self.doc.append(NoEscape("\\begin{tikzpicture}")) # début du TikZ
        
        if self.a > 0:
            self.doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $α$, $+ ∞$}"))
            self.doc.append(NoEscape("\\tkzTabVar{+/, -/ $β$, +/}"))
        elif self.a < 0 : 
            self.doc.append(NoEscape("\\tkzTabInit{$x$ / 1, $f (x)$ / 1}{$- ∞$, $α$, $+ ∞$}"))
            self.doc.append(NoEscape("\\tkzTabVar{-/, +/ $β$, -/}"))

        self.doc.append(NoEscape("\\end{tikzpicture}"))   # fin TikZ
        self.doc.append(NoEscape("\\caption{Table de variations pour $f(x)$}")) # légende
        self.doc.append(NoEscape("\\label{tab:variations}"))  # référence
        self.doc.append(NoEscape("\\end{table}"))        # fin du flottant


        # insérer une barrière pour garantir l'ordre du contenu
        self.doc.append(NoEscape("\\FloatBarrier"))


class CourbeRepresentation(object):
    """ Class spécial de génération de graphe (fonction f(x) avec les deux points calculés).
    
        Input : 
            doc -> pdf latex
            a -> valeurs différentes de 0
            b -> valeurs différentes de 0
            c -> valeurs différentes de 0
            Scoords -> tuple de coordonnées
            Acoords -> tuple de coordonnées 
            
        Output : / """
    
    def __init__(self, doc, a, b, c, Scoords, Acoords) -> None:
        """ Initialisation des attributs de la class de génération de courbe, correction, de l'exercice polynômes du second degré. """

        self.doc = doc
        self.a = a
        self.b = b
        self.c = c
        self.Scoords = Scoords
        self.Acoords = Acoords

    def courbe_poly(self, numEtape, width, dpi=300) -> None:
        """ Ajout de la représentation graphique de la fonction avec description dans le document latex / pdf."""      

        self.doc.append(NoEscape("\\\\"))
        self.doc.append(NoEscape("\\ \\parbox{ 450pt }{\\textbf{Étape %s : Représenter l’allure de la courbe avec les deux points demandés.} \\\\ On représente la parabole $f(x)$ avec les points $S$ (sommet) et $A$.}" % (numEtape)))
        self.doc.append(NoEscape("\\\\"))

        # Ajout du graphique
        with self.doc.create(Figure(position='htbp')) as plot:
            plot.add_plot(width=NoEscape(width), dpi=dpi)

    def plot(self, func) -> None:
        """ Création du graphique avec matplotlib. """
        plt.clf() # clear figure précédente
        plt.axvline(x=0, color='r')
        plt.axhline(y=0, color='r')
        axes = plt.gca()
        axes.set_xlabel('x : abscisse')
        axes.set_ylabel('f(x) : ordonnée')

        # Coordonnées des points
        x_point_S = self.Scoords[0]
        y_point_S = self.Scoords[1]
        x_point_A = self.Acoords[0]
        y_point_A = self.Acoords[1]

        # Tracé de la courbe
        x = np.linspace(-x_point_S * 5, x_point_S * 5, 100)
        y = func(x)
        plt.plot(x, y, label="f(x)")

        # ajout des points sur la courbe
        plt.scatter(x_point_S, y_point_S, color='g', label=f'S({x_point_S}; {y_point_S})')
        plt.scatter(x_point_A, y_point_A, color='black', label=f'A({x_point_A}; {y_point_A})')

        # légende
        plt.legend(loc=0, fontsize=10)

    def generate_graph(self) -> None:
        """ Génère et affiche le graphique à partir des coefficients donnés. """
        func = lambda x: (self.a * x**2) + (self.b * x) + self.c
        self.plot(func)
