from settings import *

class GetExo:

    def __init__(self):
        self.CreateValues()
        self.listeConstruction = []


    def CreateValues(self):

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
            self.CreateValues()


    def pgcd(self, a, b):
        # eqt simple
        while b != 0:
            a,b=b,a%b
        return a
    

    def ExoNv0(self):
        if not INFOS["Difficulte"]:
            eqt = r"$ \Leftrightarrow %sx - %s = %s + %sx $" %(self.nb1, self.nb2, self.nb3, self.nb4)

            # résolution de pymaths
            nb = self.nb3 + self.nb2
            nbx = self.nb1 - self.nb4

            if nbx != 1:
                pgcd_frac = self.pgcd(nb,nbx)
                nb = nb//pgcd_frac
                nbx = nbx//pgcd_frac
                if nbx!=1:
                    resultat = nb/nbx
                else:
                    resultat = nb
            else:
                resultat = nb

            self.listeConstruction = [eqt, resultat, self.nb1, self.nb2, self.nb3, self.nb4]
        
        else:
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
                resultat = [num_const, numx]

            self.listeConstruction = [eqt, resultat, self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6]

    def ExoNv1(self):
        pass

    def ExoNv2(self):
        pass

    def ExoNv3(self):
        pass

    def ExoNv4(self):
        pass

    def ExoNv5(self):
        pass

    def ExoNv6(self):
        pass

    def ExoNv7(self):
        pass

    def ExoNv8(self):
        pass

    def ExoNv9(self):
        pass

    def ExoNv10(self):
        pass

    def ExoNv11(self):
        pass

    def ExoNv12(self):
        pass

    def ExoNv13(self):
        pass

    def ExoNv14(self):
        pass


    def Choix(self):
        if INFOS["Niveau"] == 0:
            self.ExoNv0()
        
        return self.listeConstruction
