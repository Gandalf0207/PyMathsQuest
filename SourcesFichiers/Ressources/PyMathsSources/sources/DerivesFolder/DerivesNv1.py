#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

from SourcesFichiers.Ressources.PyMathsSources.sources.settingsPyMaths import *

class DerivesNV1(object):
    """ Class parent de l'exercice équation du premier degré. Contient des méthodes utilisés globalement.
    Permet de gérer plus facilement des appels et la création des exercices."""

    def __init__(self, doc, listeFonction, listeCoef, listeFonctionLatex) -> None:
        """ Initialisation des attributs de la class de parent de l'exercice équation du permier degré. """
        
        self.doc = doc
        self.listeFonction = listeFonction
        self.listeCoef = listeCoef
        self.listeFonctionLatex = listeFonctionLatex
        

class ConsignesDerivesNv1(DerivesNV1):
    """ Class enfant contenant toutes la méthode pour pouvoir écrire les consignes. """

    def __init__(self, doc, i, listeFonction, listeCoef, listeFonctionLatex) -> None:
        """ Initialisation des attributs de la class enfant consignes, de l'exercice dérivés. """

        super().__init__(doc, listeFonction, listeCoef, listeFonctionLatex) # initialisation class parent 
        self.i = i # numéro exercice

    def DerivesTitreConsigne(self) -> None:
        """Méthode d'écriture du titre des consignes."""
        with self.doc.create(Section(f"Exo Dérivés n°{self.i+1}", numbering=False)):  # titre exercice
            self.doc.append(NoEscape("\\text{Pour chaque dérivée donnée ci-dessous, répondez aux questions suivantes :}\\\\ "))

    def ConsigneCalculDerives(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer les dérivées"""
        self.doc.append(NoEscape(f"{numEtape}. Pour chaque fonction ci-dessous, calculez sa dérivée :\\\\ "))

    def ConsigneTangente(self, numEtape) -> None:
        """Méthode d'écriture de la consigne pour : calculer la tangente"""
        self.doc.append(NoEscape(f"{numEtape}. Pour chaque fonction ci-dessous, déterminez sa tangente au point d'abscisse 2 à l'aide de sa dérivée :\\\\ "))

    def ConsignesDerives(self):
        """Méthode pour afficher toutes les dérivées avec trois par ligne"""
        with self.doc.create(Section("Les fonctions :", numbering=False)):  # titre exercice
            # Calcul du nombre total de fonctions
            total_fonctions = len(self.listeFonctionLatex)
            
            self.doc.append(NoEscape("\\begin{align*}"))
            
            # Traitement des fonctions par groupe de trois
            for i in range(0, total_fonctions, 3):
                self.doc.append(NoEscape("\\begin{aligned}"))
                
                # Prendre jusqu'à trois fonctions à afficher
                for j in range(i, min(i+3, total_fonctions)):
                    # Utilisation de "&" pour aligner l'égalité de manière appropriée
                    self.doc.append(NoEscape(f"f(x) &= {self.listeFonctionLatex[j]} \\\\"))
                
                self.doc.append(NoEscape("\\end{aligned}"))
                
                # Ajouter un espacement horizontal entre les blocs
                if i + 3 < total_fonctions:
                    self.doc.append(NoEscape("\\quad"))  # Espace entre les groupes

            self.doc.append(NoEscape("\\end{align*}"))

    
    
class CorrectionsDerivesNv1(DerivesNV1):
    def __init__(self, doc, i, listeFonction, listeCoef, listeFonctionLatex):
        """ Initialisation des attributs de la class enfant corrections, de l'exercice dérivés. """

        super().__init__(doc, listeFonction, listeCoef, listeFonctionLatex) # initialisation class parent 
        self.i = i # numéro exercice

    def DerivesTitreCorrection(self) -> None:
        """Méthode d'écriture du titre des corrections."""
        with self.doc.create(Section(f"Correction Exo Dérivés n°{self.i+1}", numbering=False)):  # titre exercice
            self.doc.append(NoEscape("\\text{Pour chaque dérivée donnée il fallait donner sa dérivé et sa tengente pour x = 2 :}\\\\ "))


    def CorrectionDerives(self) -> None:
        """Méthode pour afficher toutes les dérivées avec trois par ligne"""
        with self.doc.create(Section("Rappel des fonctions :", numbering=False)):  # titre exercice
            # Calcul du nombre total de fonctions
            total_fonctions = len(self.listeFonctionLatex)
            
            self.doc.append(NoEscape("\\begin{align*}"))
            
            # Traitement des fonctions par groupe de trois
            for i in range(0, total_fonctions, 3):
                self.doc.append(NoEscape("\\begin{aligned}"))
                
                # Prendre jusqu'à trois fonctions à afficher
                for j in range(i, min(i+3, total_fonctions)):
                    # Utilisation de "&" pour aligner l'égalité de manière appropriée
                    self.doc.append(NoEscape(f"f(x) &= {self.listeFonctionLatex[j]} \\\\"))
                
                self.doc.append(NoEscape("\\end{aligned}"))
                
                # Ajouter un espacement horizontal entre les blocs
                if i + 3 < total_fonctions:
                    self.doc.append(NoEscape("\\quad"))  # Espace entre les groupes

            self.doc.append(NoEscape("\\end{align*}"))

    def CorrectionCalculDerives(self):
        """Affiche toutes les dérivées avec alignement propre et espacement."""
        with self.doc.create(Section("Les dérivées :", numbering=False)):  # Titre de la section
            total_fonctions = len(self.listeFonctionLatex)


            for j in range(total_fonctions):
                fonction = self.listeFonction[j]

                # Ajout de la règle
                regle = self.get_regle(fonction)
                self.doc.append(NoEscape(f"\\text{{{regle}}} \\\\ "))

                # Ajout de la fonction et de sa dérivée
                self.doc.append(NoEscape(f"\\ $ \\text{{Pour : }}  f(x) = {self.listeFonctionLatex[j]}, \\quad f'(x) = {self.PlacementDerive(fonction, j)} $\\\\"))
                
                self.doc.append(NoEscape("\\\\"))
                self.doc.append(NoEscape("\\\\"))
                self.doc.append(NoEscape("\\\\"))

    def get_regle(self, fonction):
        """Retourne la règle sous forme de texte avec math mode."""
        if "Xcarre" in fonction:
            return "Règle : La dérivée de $ax^2$ est $2ax$"
        elif "XexposantN" in fonction:
            return "Règle : La dérivée de $ax^n$ est $n \\cdot a \\cdot x^{n-1}$"
        elif "racinecarreX" in fonction:
            return "Règle : La dérivée de $\\sqrt{x}$ est $\\frac{1}{2\\sqrt{x}}$"
        elif "expX" in fonction:
            return "Règle : La dérivée de $e^{kx}$ est $k \\cdot e^{kx}$"
        elif "X" in fonction:
            return "Règle : La dérivée de $ax$ est simplement $a$"
        elif "C" in fonction:
            return "Règle : La dérivée d'une constante est $0$"
        return ""

    def PlacementDerive(self, fonction, j):
        """Retourne l'expression de la dérivée."""
        if "Xcarre" in fonction:
            return f"{self.listeCoef[j] * 2}x"
        elif "XexposantN" in fonction:
            coef, exposant = self.listeCoef[j]
            return f"{coef * exposant}x^{{{exposant - 1}}}"
        elif "racinecarreX" in fonction:
            return f"\\frac{{{self.listeCoef[j]}}}{{2 \\sqrt{{x}}}}"
        elif "expX" in fonction:
            return f"{self.listeCoef[j]}e^{{{self.listeCoef[j]}x}}"
        elif "X" in fonction:
            return f"{self.listeCoef[j]}"
        elif "C" in fonction:
            return "0"
        return ""


    def CorrectionTangente(self) -> None:
        """Affiche les calculs des tangentes au point x = 1 avec explications détaillées et équation finale."""
        with self.doc.create(Section("Les tangentes :", numbering=False)):  # Titre de la section
            # Explication introductive de la méthode
            self.doc.append(NoEscape("\\text{Pour trouver la tangente de $f(x)$ au point d'abscisse $x = 2$, nous utilisons la formule suivante :} \\\\"))
            self.doc.append(NoEscape("\\begin{align*}"))
            self.doc.append(NoEscape("\\ y = f'(a)(x-a) + f(a) \\\\ "))
            self.doc.append(NoEscape("\\ y = f'(2)(x-2) + f(2) \\\\ "))
            self.doc.append(NoEscape("\\end{align*}"))

            # Nombre total de fonctions
            total_fonctions = len(self.listeFonctionLatex)

            # Calcul et affichage des tangentes pour chaque fonction
            for j in range(total_fonctions):
                fonction = self.listeFonction[j]
                f1 = self.EvaluerFonction(fonction, j,  2)  # Calcul de f(1)
                f_prime1 = self.EvaluerDerivee(fonction, j, 2)  # Calcul de f'(1)

                self.doc.append(NoEscape("\\subsection*{Tangente pour : $f(x) = " + self.listeFonctionLatex[j] + "$}"))

                # Étape 1 : Calcul de f(1)
                self.doc.append(NoEscape("\\text{1. Calcul de } f(2): \\\\"))
                self.doc.append(NoEscape(f"f(2) = {f1} \\\\"))

                # Étape 2 : Calcul de f'(1)
                self.doc.append(NoEscape("\\text{2. Calcul de } f'(2): \\\\"))
                self.doc.append(NoEscape(f"f'(2) = {f_prime1} \\\\"))

                # Étape 3 : Équation finale de la tangente
                self.doc.append(NoEscape("\\text{3. Équation de la tangente :} \\\\"))
                self.doc.append(NoEscape(f"y = {f_prime1}(x - 2) + {f1} \\\\ "))

                if f1 - f_prime1 < 0:
                    self.doc.append(NoEscape(f"y = {f_prime1}x {f1 - 2 * f_prime1} \\\\")) # négatif
                else:
                    self.doc.append(NoEscape(f"y = {f_prime1}x + {f1 - 2 * f_prime1} \\\\"))


    def EvaluerFonction(self, fonction, j, x):
        """Évalue la fonction à un point donné (f(x))."""
        if "Xcarre" in fonction:
            return self.listeCoef[j] * (x ** 2)
        elif "XexposantN" in fonction:
            coef, exposant = self.listeCoef[j]
            return coef * (x ** exposant)
        elif "racinecarreX" in fonction:
            return round(self.listeCoef[j] * (x ** 0.5), 2)
        elif "expX" in fonction:
            return round(exp(self.listeCoef[j]*x),2) # Approximation de e
        elif "X" in fonction:
            return self.listeCoef[j] * x
        elif "C" in fonction:
            return self.listeCoef[j]
        return 0

    def EvaluerDerivee(self, fonction, j, x):
        """Évalue la dérivée de la fonction à un point donné (f'(x))."""
        if "Xcarre" in fonction:
            return 2 * self.listeCoef[j] * x
        elif "XexposantN" in fonction:
            coef, exposant = self.listeCoef[j]
            return round(coef * exposant * (x ** (exposant - 1)), 2)
        elif "racinecarreX" in fonction:
            return round(self.listeCoef[j] * (1 / (2 * (x ** 0.5))), 2)
        elif "expX" in fonction:
            return round((self.listeCoef[j] * (exp((self.listeCoef[j]-1)*x))), 2)
        elif "X" in fonction:
            return self.listeCoef[j]
        elif "C" in fonction:
            return 0
        return 0
