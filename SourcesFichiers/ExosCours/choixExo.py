#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

from settings import *

class GetExo:

    def __init__(self) -> None:
        """Méthode initialisation des valeur de création des différents exercices
        Input / Ouput : None"""

        self.CreateValues() # valeurs aléatoires
        self.listeConstruction = [] # list return valeurs constructions (resultats, nombres...)
        self.ErrorGeneration = False

    def CreateValues(self) -> None:
        """Méthode de créations des valeur aléatoires (sous conditions et vérification)
        Input / Output : None"""
        if NIVEAU["Niveau"] == "Seconde":
            if NIVEAU["Map"] in ["NiveauPlaineRiviere", "NiveauMedievale", "NiveauMordor"]:
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
            elif NIVEAU["Map"] == "NiveauBaseFuturiste":
                XA = randint(-10,10)
                XB = randint(-10,10)
                XC = randint(-10,10)
                XD = randint(-10,10)

                YA = randint(-10,10)
                YB = randint(-10,10)
                YC = randint(-10,10)
                YD = randint(-10,10)

                #calculs avec conditon pour éviter les erreurs, et obtenir des valeurs correctes (meme principe que le script du fichier py_maths_boss)
                m1 = 0.01
                while m1 != round(m1,1):
                    XA = random.randint(-10,10)
                    XB = random.randint(-10,10)
                    YA = random.randint(-10,10)
                    YB = random.randint(-10,10)

                    A = (XA, YA) 
                    B = (XB, YB) 

                    if (XA != 0 and XB != 0 and YA != 0 and YB != 0) and (XB != XA and YB != YA):
                        m1 = (B[1]- A[1]) / (B[0] - A[0])
                    p1 = A[1] - (m1*A[0]) 

                #calculs avec conditon pour éviter les erreurs, et obtenir des valeurs correctes (meme principe que le script du fichier py_maths_boss)
                m2 = 0.01
                while m2 != round(m2,1):

                    XC = random.randint(-10,10)
                    XD = random.randint(-10,10)
                    YC = random.randint(-10,10)
                    YD = random.randint(-10,10)

                    C = (XC, YC)
                    D = (XD, YD)

                    if (XC != 0 and XD != 0 and YC != 0 and YD != 0) and (XD != XC and YD != YC):
                        m2 = (D[1]- C[1]) / (D[0] - C[0])
                    p2 = C[1] - (m2*C[0]) 
                
                self.valeurs = ([m1, round(p1,1), m2, round(p2,1), A, B, C, D]) # Retour des valeurs pour les équations réduites + coordonnées
        
        elif NIVEAU["Niveau"] == "Premiere" :   
            if NIVEAU["Map"] == "NiveauMedievale":
                self.a = randint(-7,7) # Génération aléatoire des valeurs
                self.b = randint(2,25)
                self.c = randint(2,10)

                while self.a ==0 or self.a ==-1 or self.a==1 or self.b == self.c: # on évite les valeurs non utilisables
                    self.a = random.randint(-15,15)
                    self.b = randint(2,25)
                    self.c = randint(2,10)


    def pgcd(self, a: int, b : int) -> int:
        # calcul de pgcd 
        while b != 0:
            a,b=b,a%b
        return a
    

    def ExoNv0(self) -> list:
        """Méthode de création de l'exo 1 : deux niveaux de difficulté : eqt du premier degré
        Input : None
        Output : list"""
        self.ErrorGeneration = False

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
                    self.ErrorGeneration = True
                else:
                    resultat = nb
            else:
                resultat = nb

            # formatage resultats
            resultat2 = (self.nb1 + nb)*random.choice([-1, 1])
            resultat3 = (nbx - nb)*random.choice([-1, 1])

            self.stockageValues = (self.nb1, self.nb2, self.nb3, self.nb4)
            self.listeConstruction = [eqt, resultat, resultat2, resultat3]
        
        else: # difficile
            eqt = r"$ \Leftrightarrow \frac{%s}{%s}x + %s = \frac{%s}{%s} - %sx $" % (self.nb1,self.nb2,self.nb3,self.nb4,self.nb5,self.nb6)
            

            # verif 
            if self.nb1 / self.nb2 == int( self.nb1 / self.nb2) or self.nb4 / self.nb5 == int( self.nb4 / self.nb5):
                self.ErrorGeneration = True

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
                self.ErrorGeneration = True

            # formatage résultats
            resultat2 = (numx)*random.choice([-1, 1])
            resultat3 = (num6)*random.choice([-1, 1])

            self.stockageValues = (self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6)
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

            choix = randint(1, 3)
            if choix == 1:
                resultat = (f"Volume du Cube : {round(self.VCube)}")
                resultat2 = (f"Volume de la Sphere : {round(self.VCone)}")
                resultat3 = (f"Volume du Cone : {round(self.VSphere)}")
            elif choix == 2:
                resultat = (f"Volume de la Sphere : {round(self.VSphere)}")
                resultat2 = (f"Volume du Cube : {round(self.VCone)}")
                resultat3 = (f"Volume du Cone : {round(self.VCube)}")
            else:
                resultat = (f"Volume du Cone : {round(self.VCone)}")
                resultat2 = (f"Volume de la Sphere : {round(self.VCube)}")
                resultat3 = (f"Volume du Cube : {round(self.VSphere)}")

            self.stockageValues = (self.a, self.b, self.r, self.d, self.L, self.l, self.h)
            self.listeConstruction = [(self.a, self.r, self.h, self.d), resultat, resultat2, resultat3]
                                      
        else:
            self.baseCylindre = arrondir(self.r**2 * pi)
            self.volumeCylindre1 = arrondir(self.r**2 * pi * self.a)
            self.volumeCylindre2 = arrondir(self.r**2 * pi * self.b)
            self.volumeGrandPaveDroit = self.b * self.f * self.a
            self.volumePetitPaveDroit = self.c * self.f * (self.d - self.a)
            self.volumeCone = arrondir((self.r**2 * pi * self.h) /3)
            self.volumeTotalChateau = self.volumeCone*2 + self.volumeCylindre1 + self.volumeCylindre2 + self.volumePetitPaveDroit + self.volumePetitPaveDroit

            resultat = f"Volume total du chateau Chateau : {round(self.volumeTotalChateau)}"
            resultat2 = f"Volume total du Chateau : {round(self.volumeTotalChateau - self.volumeCone + arrondir((self.r**2 * pi * self.e) /3) )}"
            resultat3 = f"Volume total du Chateau : {round(self.volumeTotalChateau - self.volumeCylindre1 + self.volumeCylindre2)}" 

            self.stockageValues = (self.a, self.b, self.r, self.d, self.L, self.l, self.h)
            self.listeConstruction = [(self.a, self.b, self.c, self.d, round(self.e, 3), self.f, self.r), resultat, resultat2, resultat3]

    def ExoNv2(self) -> None:
        """Méthode de création de l'exo 3 : deux niveaux de difficulté
        Input / Output : None"""
        # Formatage des résultats en chaînes de caractères
        resultat = f"Equation réduite de (AB) : {self.valeurs[0]}x + {self.valeurs[1]} \n Equation réduite de (CD) : {self.valeurs[2]}x + {self.valeurs[3]}"
        resultat2 =  f"Equation réduite de (AB) : {self.valeurs[1]}x + {self.valeurs[0]} \n Equation réduite de (CD) : {self.valeurs[3]}x + {self.valeurs[2]}"
        resultat3 =  f"Equation réduite de (AB) : {self.valeurs[2]}x + {self.valeurs[3]} \n Equation réduite de (CD) : {self.valeurs[0]}x + {self.valeurs[1]}"
        A = self.valeurs[4] # Récupération des coordonnées
        B = self.valeurs[5]
        C = self.valeurs[6]
        D = self.valeurs[7]
        points = [A, B, C, D]

        # Créer un graphique Matplotlib
        compteur_pts = 0
        fig, ax = plt.subplots(figsize=(3, 2))  # Largeur = 5 pouces, Hauteur = 4 pouces

        l_pts = ["A","B","C","D"]
        for x, y in points:
            
            ax.scatter(x, y, color='blue', marker='o', label=f"({x}, {y})")
            ax.text(x, y, f"({x}, {y})", ha='center', va='bottom')  # Ajouter l'étiquette
            ax.text(x, y-0.3, l_pts[compteur_pts], ha='center', va='top') # Ajout nom des points
            compteur_pts+=1

        # Supprimer les axes
        ax.axis('off')  # Ajouter cette ligne pour masquer les axes

        # ======= Convertir Matplotlib en Surface Pygame =======
        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.buffer_rgba()

        # Création d'une surface Pygame à partir du graphique Matplotlib
        size = canvas.get_width_height()
        graph_surface = pygame.image.fromstring(raw_data.tobytes(), size, "RGBA")

        self.stockageValues = points
        self.listeConstruction = [(graph_surface, points), resultat, resultat2, resultat3]

    def ExoNv3(self) -> None:
        """Méthode de création de l'exo 4 : deux niveaux de difficulté
        Input / Output : None"""
        self.ErrorGeneration = False

        if not INFOS["Difficulte"]: # facile
            eqt = r"$\left\{ \begin{array}{lr} %sx + %sy & = %s \\ %sx - %sy & = %s \end{array} \right.$" % (self.nb1, self.nb2, self.nb5, self.nb3, self.nb4, self.nb6)
            # etape 1 
            self.nb4 *= -1 # car - dans l'eqt
        
        else:
            eqt = r"$\left\{ \begin{array}{lr} %sx - %sy & = %s \\ - %sx + %sy & = %s \end{array} \right.$" % (self.nb1, self.nb2, self.nb5, self.nb3, self.nb4, self.nb6)

            self.nb2 *= -1
            self.nb3 *= -1

        # Étape 1 : Multiplier les coefficients
        newNb1 = self.nb3 * self.nb1
        newNb2 = self.nb3 * self.nb2
        newNb5 = self.nb3 * self.nb5
        newNb3 = self.nb1 * self.nb3
        newNb4 = self.nb1 * self.nb4
        newNb6 = self.nb1 * self.nb6

        # Étape 2 : Éliminer une variable pour trouver y
        newY = newNb2 - newNb4
        newValue = newNb5 - newNb6

        if newY == 0:
            self.ErrorGeneration = True
            return None

        # Simplification avec le PGCD
        division = self.pgcd(newValue, newY)
        newValue = newValue // division
        newY = newY // division

        if newY == 1:  # y est entier
            y = newValue
        else:  # Vérification si la division donne un entier
            if newValue % newY == 0:
                y = newValue // newY
            else:
                self.ErrorGeneration = True
                return None

        # Étape 4 : Calculer x en fonction de y
        newValue2 = self.nb5 - (self.nb2 * y)
        division = self.pgcd(self.nb1, newValue2)
        newX = self.nb1 // division
        newValue2 = newValue2 // division

        if newX == 1:  # x est entier
            x = newValue2
        else:  # Vérification si la division donne un entier
            if newValue2 % newX == 0:
                x = newValue2 // newX
            else:
                self.ErrorGeneration = True
                return None

        if not self.ErrorGeneration:
            resultat = f"x = {x} ; y = {y}"
            resultat2 = f"x = {self.nb1 - x} ; y = {y*2}"
            resultat3 = f"x = {x*3} ; y = {self.nb2+y}"

            self.stockageValues = (self.nb1, self.nb2, self.nb3, self.nb4, self.nb5, self.nb6)
            self.listeConstruction = [eqt, resultat, resultat2, resultat3, ]

    def ExoBoss1(self):
              #fonction de lancement / relancement si les calculs ne sont pas aux normes attendues
        def reload_function():
            XI = 0.0001 # Set des valeurs initiales pour pouvoir rentrer dans la boucle
            YI = 0.0001
            while XI != round(XI,1) or XI != round(XI, 2) or XI != round(XI, 3) or YI != round(YI,1) or YI != round(YI, 2) or YI != round(YI, 3): # Conditon : pas plus de 1 o 2 chiffres après la virgules

                # Calcul coef dirrecteur de l'équation réduite sous la forme mx + p
                m1 = 0.01 # Set valeur initiale pour rentrer dans la boucle
                while m1 != round(m1,1):
                    XA = random.randint(-10,10) # Création de valeurs aléatoires
                    XB = random.randint(-10,10)
                    YA = random.randint(-10,10)
                    YB = random.randint(-10,10)

                    A = (XA, YA) 
                    B = (XB, YB) 

                    if (XA != 0 and XB != 0 and YA != 0 and YB != 0 ) and (XB != XA and YB != YA):
                        m1 = (B[1]- A[1]) / (B[0] - A[0])
                    p1 = A[1] - (m1*A[0]) 

                # Calcul coef dirrecteur de l'équation réduite sous la forme mx + p
                m2 = 0.01 # Set valeur initiale pour rentrer dans la boucle
                while m2 != round(m2,1):

                    XC = random.randint(-10,10) # Création de valeurs aléatoires
                    XD = random.randint(-10,10)
                    YC = random.randint(-10,10)
                    YD = random.randint(-10,10)

                    C = (XC, YC)
                    D = (XD, YD)

                    if (XC != 0 and XD != 0 and YC != 0 and YD != 0)  and (XD != XC and YD != YC):
                        m2 = (D[1]- C[1]) / (D[0] - C[0])
                    p2 = C[1] - (m2*C[0]) 


                if m1 != m2: # Calcul des coordonnées du point d'intersection
                    nbx = m1 - m2
                    nb = -p1 + p2
                    XI = nb/nbx
                    YI = m1*XI + p1


            norme_AI = sqrt((XI - XA)**2 + (YI - YA)**2) # Calculs des longueurs des [AI] et [CI]
            norme_CI = sqrt((XI - XC)**2 + (YI - YC)**2)

            # Création de la permière partie des résultats en fonction des valeurs de calculs
            if norme_AI == norme_CI:
                intersection = False
            else:
                intersection = True


            # Bout de script pour le calcul du volumes des barrils
            largeur_barril = random.randint(25,80)
            longeur_barril = random.randint(55,140)

            while longeur_barril < largeur_barril:
                largeur_barril = random.randint(25,80)
                longeur_barril = random.randint(55,140)
            
            base = pi*(largeur_barril/2)**2
            volume = base*longeur_barril
            #conversion en litre, car les données sont en cm
            volume_L = volume/1000
            volume_L = volume_L*85
            volume_L = round(volume_L,2)

            return (intersection,volume_L,[A, B, C, D, longeur_barril, largeur_barril]) # On retourne s'il y a intersection, le volume en litre, les coordonnées de points et les dimensions des barils, qui serviront à l'utilisateurs pour faire ses calculs

        valeur = reload_function() # Chargement de la fonction principal 

        if valeur[0]:
            resultat = f"Les deux bateaux vont s'entrechoquer !, Volume total transporté est de {valeur[1]} L d'huile d'olive"
            resultat2 = f"Les deux bateaux ne vont pas s'entrechoquer !, Volume total transporté est de {round(sqrt(valeur[1]), 1)}"
            resultat3 = f"Les deux bateaux vont s'entrechoquer !, Volume total transporté est de {valeur[1]*1000}"
        else:
            resultat = f"Les deux bateaux ne vont pas s'entrechoquer !, Volume total transporté est de {valeur[1]}"
            resultat2 = f"Les deux bateaux vont s'entrechoquer !, Volume total transporté est de {valeur[1]*1000} L d'huile d'olive"
            resultat3 = f"Les deux bateaux ne vont pas s'entrechoquer !, Volume total transporté est de {round(sqrt(valeur[1]), 1)}"
    

        self.listeConstruction = [valeur, resultat, resultat2, resultat3]

    
    def ExoNv4(self) -> None:
        """Méthode de création de l'exo 5 : deux niveaux de difficulté
        Input / Output : None"""
        self.ErrorGeneration = False

        eqt = r"$ P(x) =  %sx^2 + %sx + %x $" %(self.a, self.b, self.c)

        delta = self.b**2 - 4*self.a*self.c

        # values
        if delta > 0:
            x1 = round((-self.b - sqrt(delta) )/( self.a*2), 2)
            x2 = round((-self.b + sqrt(delta) )/( self.a*2), 2)

            valueError1 = round((-self.a + sqrt(self.b))/ self.c, 2)
            valueError2 = round((-self.b + self.a)/ self.b, 2)
            valueError3 = round(sqrt((self.b + self.a)**2), 2)
            valueError4 = round((-self.a -self.c) / self.b, 2)

        elif delta == 0:
            xSimple = round((-self.b) / (2*self.a) , 2)

            valueError1 = round((self.a) / 2*self.b, 2)
            valueError2 = round((-self.b) / (self.c + 2*self.a), 2)
        
        else:
            valueError1 = round((-self.a + sqrt(self.b))/ self.c, 2)
            valueError2 = round((-self.a -self.c) / self.b, 2)
            valueError3 = round((-self.b) / (self.c + 2*self.a), 2)

        # réponses
        if delta > 0:
            resultat = f"P(0) admet 2 solutions : x1 = {x1}; x2 = {x2}"
            resultat2 = f"P(0) admet 2 solutions : x1 = {valueError1}; x2 = {valueError3}" 
            resultat3 = f"P(0) admet 2 solutions : x1 = {valueError2}; x2 = {valueError4}"

        elif delta == 0:
            resultat = f"P(0) admet une seule et unique soluion : x = {xSimple}"
            resultat2 = f"P(0) admet une seule et unique soluion : x = {valueError1}"
            resultat3 = f"P(0) admet une seule et unique soluion : x = {valueError2}"
        
        else: 
            resultat = f"P(0) admet aucune solution dans R. "
            resultat2 = f"P(0) admet 2 solutions : x1 = {valueError1}; x2 = {valueError2}"
            resultat3 = f"P(0) admet une seule et unique soluion : x = {valueError3}"

        self.stockageValues = (self.a, self.b, self.c)
        self.listeConstruction = [eqt, resultat, resultat2, resultat3]


    def ExoNv5(self) -> None:
        """Méthode de création de l'exo 6 : deux niveaux de difficulté
        Input / Output : None"""

        def EvaluerFonction(fonction, coef, x):
            """Évalue la fonction à un point donné (f(x))."""
            if "Xcarre" in fonction:
                return coef * (x ** 2)
            elif "XexposantN" in fonction:
                coef, exposant =coef
                return coef * (x ** exposant)
            elif "racinecarreX" in fonction:
                return round(coef * (x ** 0.5), 2)
            elif "expX" in fonction:
                return round(exp(coef*x),2) # Approximation de e
            elif "X" in fonction:
                return coef * x
            elif "C" in fonction:
                return coef
            return 0

        def EvaluerDerivee(fonction, coef, x):
            """Évalue la dérivée de la fonction à un point donné (f'(x))."""
            if "Xcarre" in fonction:
                return 2 * coef * x
            elif "XexposantN" in fonction:
                coef, exposant = coef
                return round(coef * exposant * (x ** (exposant - 1)), 2)
            elif "racinecarreX" in fonction:
                return round(coef * (1 / (2 * (x ** 0.5))), 2)
            elif "expX" in fonction:
                return round((coef * exp(coef * x)), 2)
            elif "X" in fonction:
                return coef
            elif "C" in fonction:
                return 0
            return 0

        listElement = ["Xcarre", "XexposantN", "racinecarreX", "X", "C", "expX"]
        fonctionElement = choice(listElement)

        # création fonction f(x)
        if fonctionElement == "Xcarre":
            coef = randint(2, 5)
            strLatex = r"$ f(x) = %sx^2 $"% (coef)
        elif fonctionElement == "XexposantN":
            coef = (randint(2, 5), randint(2, 5))
            strLatex = r"$ f(x) = %sx^{%s} $"% (coef[0], coef[1])
        elif fonctionElement == "racinecarreX":
            coef = randint(2, 5)
            strLatex = r"$ f(x) = %s \sqrt{x} " % (coef)
        elif fonctionElement == "X":
            coef = randint(2, 5)
            strLatex = r"$ f(x) = %sx $" % (coef)
        elif fonctionElement == "C":
            coef = randint(2, 5)
            strLatex = r"$ f(x) = %s $" % (coef)
        elif fonctionElement == "expX":
            coef = randint(2, 5)
            strLatex = r"$ f(x) = e^%s $" % (coef)

        coefElement = coef
        eqt = strLatex


        f1 = EvaluerFonction(fonctionElement, coef,  2)
        fPrime1 = EvaluerDerivee(fonctionElement, coef, 2) 

        if f1 - 2 * fPrime1 < 0:    
            resultat = f"y = {fPrime1}x  {round(f1 - 2 * fPrime1, 2)}"
        else:
            resultat = f"y = {fPrime1}x + {round(f1 - 2 * fPrime1, 2)}"

        if f1*2 + fPrime1 < 0: # valeur fausses
            resultat2 = f"y = {fPrime1/2}x {f1*2 + fPrime1}"
        else:
            resultat2 = f"y = {fPrime1/2}x + {f1*2 + fPrime1}"

        if -f1 < 0:   # valeur fausses
            resultat3 = f"y = {f1*2 + fPrime1}x {-f1}"
        else:
            resultat3 = f"y = {f1*2 + fPrime1}x + {-f1}"

        
        self.stockageValues = ([fonctionElement], [coefElement]) # sous forme de list pour pymaths correction
        self.listeConstruction = [eqt, resultat, resultat2, resultat3]

    def ExoNv6(self) -> None:
        """Méthode de création de l'exo 7 : deux niveaux de difficulté
        Input / Output : None"""

        #script generation des suites
        U0 = random.randint(-10,10)
        r = random.randint(-10,10)
        n = random.randint(4,15)

        while U0 == 0 or r == 0: #on évite les valeurs == 0
            U0 = random.randint(-10,10)
            r = random.randint(-10,10)


        if not INFOS["Difficulte"]: # suite SA
            U1 = U0 + r
            U2 = U1 + r
            eqt = r"$ U_{n} = U_{0} + n \times r ; \quad U_{0} = %s ; \quad U_{1} = %s ; \quad U_{2} = %s $ " % (U0, U1, U2)
            somme_suite = (n/2)*(2*U0+(n-1)*r)

        
        else : #suite SG
            U1 = U0*r
            U2 = U0*(r**2)
            eqt = r"$ U_{n} = U_{0} + r^n ; \quad U_{0} = %s ; \quad U_{1} = %s ; \quad U_{2} = %s $ " % (U0, U1, U2)
            somme_suite = U0*((1-(r**n))/(1-r))


        # formatage des résultats 
        resultat = f"La somme de la suite est : {somme_suite}"
        resultat2 = f"La somme de la suite est : {somme_suite-1000}"
        resultat3 = f"La somme de la suite est : {somme_suite+(U0*r**3)}"

        self.stockageValues = (U0, r, n)
        self.listeConstruction = [eqt, resultat, resultat2, resultat3, n]

    def ExoBoss2(self) -> None:
        """Méthode de création de l'exo 8 : deux niveaux de difficulté
        Input / Output : None"""
        
        #brique de lait exo
        a = random.randint(14,46) # random de la valeur de la longueur de la feille
        while a%2 != 0 :
            a = random.randint(14,46)

        y_max = 0
        x_max = 0
        for x in range(int(a/2 + 1)) : # calcul dérivée + max volume avec comparaison en brute force
            if (x*(a**2))/2 - 2*a*(x**2) + 2*(x**3) > y_max :
                x_max = x
                y_max = (x*(a**2))/2 - 2*a*(x**2) + 2*(x**3)

        #conversion en litre
        v_l = y_max/1000

        #formatage résultats
        add_value = random.randint(-5,5)
        while add_value ==0:
            add_value = random.randint(-5,5)


        #Suite

        #exo suite SG avec calcul en fonction du nb d'année (n) et du % d'inflation
        U0 = 1.20
        r = 1+(random.randint(10,80)/1000)
        n = random.randint(5,10)
        Un = U0*(r**n)


        #formatage réponse : 
        resultat = f"{round(v_l,2)} Litres; {round(Un,2)} €"
        resultat2= f"{round((y_max/1000)*choice((0.5, 1.5)),2)} Litres; {abs(round(Un*2,2))} €"
        resultat3 = f"{round(Un+U0,2)} Litres; {abs(round(v_l + add_value,2))} €"


        infos = [a,n,r] # liste avec les infos données à l'utilisateur
        self.stockageValues = infos
        self.listeConstruction = [infos, resultat, resultat2, resultat3]


    def StockageValues(self):
        """Chargement des données JSON aux index indiqués pour pouvoir les stocker"""
        try: # Si le chargement est possible
            with open(join("data","exercicesValues.json"), "r") as f: # ouvrir le fichier json en mode lecture
                self.donnees = json.load(f) # chargement des données
        except (FileNotFoundError, json.JSONDecodeError): # Sinon relève une erreur et arrêt du programme
            assert ValueError("Error load JSON file") # stop du programme avec l'assert (programmation défensive)
        
        
        newKey = f"Exo{len(self.donnees)+1}"
        newExo =  {
            "Niveau" : NIVEAU["Niveau"],
            "Exo" : NIVEAU["Map"],
            "Difficulte" : INFOS["Difficulte"],
            "Values" : self.stockageValues
        }

        self.donnees[newKey] = newExo

        # Sauvegarde des données dans le fichier JSON avec une indentation pour un format "lisible"
        with open(join("data","exercicesValues.json"), "w") as f: # ouverture du fichier json en mode écriture
            json.dump(self.donnees, f, indent=4) # chargement dans le fichier json de l'élément données (possédent les index de position et les valeurs à stocker)


    def Choix(self) -> list:
        """Méthode choix de création de l'exo en fonction du niveau
        Input : None
        Ouput : list"""
        self.ErrorGeneration = False
        
        if NIVEAU["Niveau"] == "Seconde": # appel de la bonne méthode
            if NIVEAU["Map"] == "NiveauPlaineRiviere":
                self.ExoNv0()
                while self.ErrorGeneration:
                    self.CreateValues()
                    self.ExoNv0()
            elif NIVEAU["Map"] == "NiveauMedievale":
                self.ExoNv1()
            elif NIVEAU["Map"] == "NiveauBaseFuturiste":
                self.ExoNv2()
            elif NIVEAU["Map"] == "NiveauMordor":
                if not INFOS["DemiNiveau"]:
                    self.ExoNv3()
                else:
                    self.ExoBoss1()
                while self.ErrorGeneration:
                    self.CreateValues()
                    self.ExoNv3()
        elif NIVEAU["Niveau"] == "Premiere":
            if NIVEAU["Map"] == "NiveauMedievale":
                self.ExoNv4()
            elif NIVEAU["Map"] == "NiveauBaseFuturiste":
                self.ExoNv5()
            elif NIVEAU["Map"] == "NiveauMordor":
                if not INFOS["DemiNiveau"]:
                    self.ExoNv6()
                else:
                    self.ExoBoss2()

     
        # add json values exo 
        if NIVEAU["Map"] != "NiveauMordor":
            self.StockageValues()
        else:
            if not INFOS["DemiNiveau"] :
                self.StockageValues()

        return self.listeConstruction
