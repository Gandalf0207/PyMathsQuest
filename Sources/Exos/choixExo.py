from settings import *

class GetExo:

    def __init__(self) -> None:
        """Méthode initialisation des valeur de création des différents exercices
        Input / Ouput : None"""

        self.CreateValues() # valeurs aléatoires
        self.listeConstruction = [] # list return valeurs constructions (resultats, nombres...)


    def CreateValues(self) -> None:
        """Méthode de créations des valeur aléatoires (sous conditions et vérification)
        Input / Output : None"""

        def checkUniqueValuesList(liste):
            return len(liste) == len(set(liste)) # check de si toutes les valeurs sont uniques

        liste = []
        self.a = randint(-25,25)
        self.c = randint(-25,25)
        self.b = randint(-25,25)
        self.nb1 = randint(2,50)
        self.nb2 = randint(2,50)
        self.nb3 = randint(2,50)
        self.nb4 = randint(2,50)
        self.nb5 = randint(2,50)
        self.nb6 = randint(2,50)
        self.nb7 = randint(2,50)
        self.nb8 = randint(2,50)
        self.nb9 = randint(2,50)
        self.nb12 = randint(2,50)
        self.nb10 = randint(2,50)
        self.nb11 = randint(2,50)

        while not checkUniqueValuesList(liste) or self.a ==0 or self.b == 0 or self.c==0:
            self.CreateValues() # création des valeurs 


    def pgcd(self, a: int, b : int) -> int:
        # calcul de pgcd 
        while b != 0:
            a,b=b,a%b
        return a
    

    def ExoNv0(self) -> list:
        """Méthode de création de l'exo 1 : deux niveaux de difficulté : eqt du premier degré
        Input : None
        Output : list"""

        if not INFOS["Difficulte"]: # facile
            eqt = r"$ \Leftrightarrow %sx - %s = %s + %sx $" %(self.nb1, self.nb2, self.nb3, self.nb4)

            # résolution de pymaths
            nb = self.nb3 + self.nb2
            nbx = self.nb1 - self.nb4

            if nbx != 1:
                pgcd_frac = self.pgcd(nb,nbx)
                nb = nb//pgcd_frac
                nbx = nbx//pgcd_frac
                if nbx!=1:
                    resultat = round(nb/nbx, 3)
                else:
                    resultat = nb
            else:
                resultat = nb

            # formatage resultats
            resultat2 = nbx
            resultat3 = nb * nbx
            self.listeConstruction = [eqt, resultat, resultat2, resultat3]
        
        else: # difficile
            eqt = r"$ \Leftrightarrow \frac{%s}{%s}x + %s = \frac{%s}{%s} - %sx $" % (self.nb1,self.nb2,self.nb3,self.nb4,self.nb5,self.nb6)
            
            # résolution de pymaths
                # etape 1 : Simplification des fractions et dénominateur commun
            den_common = self.nb2 * self.nb5  # dénominateur commun

            num1 = self.nb1 * self.nb5  # ajustement des numérateurs pour dénominateur commun
            num2 = self.nb4 * self.nb2

            num3 = self.nb3 * den_common  # multiplication des termes constants
            num6 = self.nb6 * den_common

            # etape 2 : Regroupement des termes
                # calcul des coefficients
            numx = num1 + num6
            num_const = num2 - num3

            # etape 3 : Isolation de x
            gcd = self.pgcd(num_const, numx)
            num_const //= gcd
            numx //= gcd

            if numx == 1:
                resultat = num_const
            else:
                resultat = round(num_const/numx, 3)

            # formatage résultats
            resultat2 = numx
            resultat3 = num6
            self.listeConstruction = [eqt, resultat, resultat2, resultat3]

    def ExoNv1(self) -> None:
        """Méthode de création de l'exo 2 : deux niveaux de difficulté
        Input / Output : None"""
        pass

    def ExoNv2(self) -> None:
        """Méthode de création de l'exo 3 : deux niveaux de difficulté
        Input / Output : None"""
        pass

    def ExoNv3(self) -> None:
        """Méthode de création de l'exo 4 : deux niveaux de difficulté
        Input / Output : None"""
        pass

    def ExoNv4(self) -> None:
        """Méthode de création de l'exo 5 : deux niveaux de difficulté
        Input / Output : None"""
        pass

    def ExoNv5(self) -> None:
        """Méthode de création de l'exo 6 : deux niveaux de difficulté
        Input / Output : None"""
        pass

    def ExoNv6(self) -> None:
        """Méthode de création de l'exo 7 : deux niveaux de difficulté
        Input / Output : None"""
        pass

    def ExoNv7(self) -> None:
        """Méthode de création de l'exo 8 : deux niveaux de difficulté
        Input / Output : None"""
        pass

    def ExoNv8(self) -> None:
        """Méthode de création de l'exo 9 : deux niveaux de difficulté
        Input / Output : None"""
        pass

    def ExoNv9(self) -> None:
        """Méthode de création de l'exo 10 : deux niveaux de difficulté
        Input / Output : None"""
        pass

    def ExoNv10(self) -> None:
        """Méthode de création de l'exo 11 : deux niveaux de difficulté
        Input / Output : None"""
        pass

    def ExoNv11(self) -> None:
        """Méthode de création de l'exo 12 : deux niveaux de difficulté
        Input / Output : None"""
        pass

    def ExoNv12(self) -> None:
        """Méthode de création de l'exo 13 : deux niveaux de difficulté
        Input / Output : None"""
        pass

    def ExoNv13(self) -> None:
        """Méthode de création de l'exo 14 : deux niveaux de difficulté
        Input / Output : None"""
        pass

    def ExoNv14(self) -> None:
        """Méthode de création de l'exo 15 : deux niveaux de difficulté
        Input / Output : None"""
        pass


    def Choix(self) -> list:
        """Méthode choix de création de l'exo en fonction du niveau
        Input : None
        Ouput : list"""
        
        if NIVEAU["Niveau"] == "Seconde": # appel de la bonne méthode
            if NIVEAU["Map"] == "NiveauPlaineRiviere":
                if NIVEAU["Numero"] == 0:
                    self.ExoNv0()
            elif NIVEAU["Map"] == "NiveauMedievale":
                if NIVEAU["Numero"] == 0:
                    self.ExoNv1()

            # case 2:
            #     self.ExoNv2()
            # case 3:
            #     self.ExoNv3()
            # case 4:
            #     self.ExoNv4()
            # case 5:
            #     self.ExoNv5()
            # case 6:
            #     self.ExoNv6()
            # case 7:
            #     self.ExoNv7()
            # case 8:
            #     self.ExoNv8()
            # case 9:
            #     self.ExoNv9()
            # case 10:
            #     self.ExoNv10()
            # case 11:
            #     self.ExoNv11()
            # case 12:
            #     self.ExoNv12()
            # case 13:
            #     self.ExoNv13()
            # case 14:
            #     self.ExoNv14()

        return self.listeConstruction
