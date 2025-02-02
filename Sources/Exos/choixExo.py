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

        self.a = randint(5,25 )
        self.b = randint(25,50) 
        self.r = randint(4, 12) 
        self.d = randint(6, 32)
        self.L = randint(8, 34)
        self.l = randint(7, 23) 
        self.h = randint(3, 45)
        self.e = sqrt((self.r**2)+(self.h**2)) # check valeurs correct (nb chiffres après la virgule exo volume nv2)


        self.nb1 = randint(2,50)
        self.nb2 = randint(2,50)
        self.nb3 = randint(2,50)
        self.nb4 = randint(2,50)
        self.nb5 = randint(2,50)
        self.nb6 = randint(2,50)
        self.nb7 = randint(2,50)
        self.nb8 = randint(2,50)
        self.nb9 = randint(2,50)
        self.nb10 = randint(2,50)
        self.nb11 = randint(2,50)
        self.nb12 = randint(2,50)
        
    
        liste = [self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6, 
                 self.nb7, self.nb8, self.nb9, self.nb10, self.nb11, self.nb12]


        while not checkUniqueValuesList(liste):
            self.a = randint(5,25 )
            self.b = randint(25,50) 
            self.r = randint(4, 12) 
            self.d = randint(6, 32)
            self.L = randint(8, 34)
            self.l = randint(7, 23) 
            self.h = randint(3, 45)
            self.e = sqrt((self.r**2)+(self.h**2)) # check valeurs correct (nb chiffres après la virgule exo volume nv2)


            self.nb1 = randint(2,50)
            self.nb2 = randint(2,50)
            self.nb3 = randint(2,50)
            self.nb4 = randint(2,50)
            self.nb5 = randint(2,50)
            self.nb6 = randint(2,50)
            self.nb7 = randint(2,50)
            self.nb8 = randint(2,50)
            self.nb9 = randint(2,50)
            self.nb10 = randint(2,50)
            self.nb11 = randint(2,50)
            self.nb12 = randint(2,50)
            
        
            liste = [self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6, 
                    self.nb7, self.nb8, self.nb9, self.nb10, self.nb11, self.nb12]


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
        
        def arrondir(valeur):
            """Arrondit à 3 chiffres après la virgule uniquement si le nombre a plus de 3 chiffres après la virgule."""
            if isinstance(valeur, float):
                # Multiplie la valeur par 1000, prend la partie entière, puis compare
                if int(valeur * 1000) != valeur * 1000:
                    return round(valeur, 3)
            return valeur  # Si pas un float ou pas plus de 3 chiffres après la virgule
        
        self.c = self.b/4
        self.d = self.a + 3
        self.f = self.r - 1.5

        

        if not INFOS["Difficulte"]: # facile
            self.VCube = arrondir(self.a**3)
            self.VSphere = arrondir(4/3 * pi * self.r**3)
            self.VCone = arrondir(1/3 * self.h * pi * (self.d/2)**2)

            resultat = (f"VCube : {round(self.VCube)}; VSphere : {round(self.VSphere)}; VCone : {round(self.VCone)}")
            resultat2 = (f"VCube : {round(self.VCube*self.a)}; VSphere : {round(self.VSphere*(4/3))}; VCone : {round(self.VCone/self.h)}")
            resultat3 = (f"VCube : {round(self.VCube *pi)}; VSphere : {round(self.VSphere/pi)}; VCone : {round(self.VCone/((self.d/2)**2))}")
            
            self.listeConstruction = [(self.a, self.r, self.h, self.d), resultat, resultat2, resultat3]
                                      
        else:
            self.baseCylindre = arrondir(self.r**2 * pi)
            self.volumeCylindre1 = arrondir(self.r**2 * pi * self.a)
            self.volumeCylindre2 = arrondir(self.r**2 * pi * self.b)
            self.volumeGrandPaveDroit = self.b * self.f * self.a
            self.volumePetitPaveDroit = self.c * self.f * (self.d - self.a)
            self.volumeCone = arrondir((self.r**2 * pi * self.h) /3)
            self.volumeTotalChateau = self.volumeCone*2 + self.volumeCylindre1 + self.volumeCylindre2 + self.volumePetitPaveDroit + self.volumePetitPaveDroit

            resultat = f"VChateau : {round(self.volumeTotalChateau)}"
            resultat2 = f"VChateau : {round(self.volumeTotalChateau - self.volumeCone)}"
            resultat3 = f"VChateau : {round(self.volumeCone*3 + self.volumeCylindre2 - self.volumePetitPaveDroit)}" 

            self.listeConstruction = [(self.a, self.b, self.c, self.d, round(self.e, 3), self.f, self.r), resultat, resultat2, resultat3]



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
