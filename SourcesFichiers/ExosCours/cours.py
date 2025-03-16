from settings import *


 # \textit car \text dépend de asmath une lib latex --> nécessite installation pour pymath
COURS = {
    "Seconde" : {
        "NiveauPlaineRiviere" : {
            "Cours0" : {
                0 : [False, "De façon intuitive, une égalité fonctionne un peu comme une balance à deux plateaux ⚖️ : si on effectue une opération dans un des membres, il faut réaliser la même opération dans l’autre pour garder l'équilibre."],
            }, 

            "Cours1" : {
                0 : [False, "Quelques propriétés : On peut ajouter (ou soustraire) un même nombre aux deux membres d'une égalité."],
                1 : [True, r"$ a = b \quad \text{ équivaut à } \quad a + c = b + c $"],
                2 : [True, r"$ a = b \quad \text{ équivaut à } \quad a - c = b - c $"],
                3 : [False, "On peut multiplier (ou diviser) les deux membres d'une égalité par un même nombre non nul."],
                4 : [True, r"$ a = b \quad \text{équivaut à} \quad a \times c = b \times c $"],
                5 : [True, r"$ a = b \quad \text{équivaut à} \quad \frac{a}{b} = \frac{b}{c} \quad \left( c \ne 0  \right) $"],
                6 : [False, "Exemple :"],
                7 : [True, r"$ 5x + 2 = 17 $"],
                8 : [True, r"$ 5x + 2 - 2 = 17 - 2 $"],
                9 : [True, r"$ \frac{5x}{5} = \frac{15}{5} $"],
                10 : [True, r"$ x = 3 $"],
            }, 

            "Cours2" : {
                0 : [False, "Si il y a des x dans les deux membres de l’équation il faut tout mettre dans le même."],
                1 : [False, "Exemple : "],
                2 : [True, r"$ 3x + 2 = 5x + 3 $"],
                3 : [True, r"$ \quad \text{équivaut à} \quad 3x + 2 - 5x = 5x + 3 - 5x  $"],
                4 : [True, r"$ \quad \text{équivaut à} \quad -2x + 2 = 3 $"],
                5 : [False, "et ainsi de suite..."],
            }, 

        }, 

        "NiveauMedievale" : {
            "Cours0" : {
                0 : [False, "La formule de l’aire d’un disque est :"],
                1 : [True, r"$ \pi \times \text{rayon}^2 $"],
                2 : [False, "l’aire d’un triangle est :"],
                3 : [True, r"$ \frac{\text{longueur} \times \text{largeur}}{2} $"],
                4 : [False, "et celle d’un carré ou d’un rectangle est"],
                5 : [True, r"$ \text{longueur} \times \text{largeur} $"],
            }, 

            "Cours1" : {
                0 : [False, "Le volume du cylindre est :"],
                1 : [True, r"$ \text{base} \times \text{hateur} \leftrightarrow \pi \times \text{rayon}^2 \times h $"],
                2 : [False, "De manière plus générale le volume d’une multitude de solide se calcule simplement par :"],
                3 : [True, r"$ \text{base} \times \text{hauteur} $"],
            }, 

            "Cours2" : {
                0 : [False, "Le volume du cône est celui du cylindre divisé par 3 soit :"],
                1 : [True, r"$ \frac{\pi \times \text{rayon}^2 \times h}{3} $"],
                2 : [False, "Le volume d’une pyramide est celui du prisme droit que l’on divise par 3 soit "],
                3 : [True, r"$ \frac{\text{Vprimse}}{3} $"],
            }, 

            "Cours3" : {
                0 : [False, "La formule pour calculer le volume d’un sphère est :"],
                1 : [True, r"$ \frac{4}{3} \times \pi \times r^3 $"],
            }, 
        }, 

        "NiveauBaseFuturiste" : {
            "Cours0" : {
                0 : [False, "L’équation d’une droite se présente sous la forme : "],
                1 : [True, r"$ y = mx + p $"],
                2 : [False, "avec m en tant que coefficient directeur et p l’ordonné à l’origine."],
            }, 

            "Cours1" : {
                0 : [False, "Les droites parallèles à l’axe des ordonnées (“droite verticale”) ne se présentent pas sous la forme"],
                1 : [True, r"$ y = mx + p $"],
                2 : [False, "mais ont une équation de la forme : "],
                3 : [True, r"$ x = c $"],
                4 : [False, "avec c un nombre."],
                5 : [False, "Par exemple : "],
                6 : [True, r"$ x = 2 $"],
                7 : [False, "est une droite verticale qui passe par l’abscisse 2."],
            }, 

            "Cours2" : {
                0 : [False, "Dans une équation sous forme"],
                1 : [True, r"$ y = mx + p $"],
                2 : [False, "passant par les points A(xA;yA) et B(xB;yB), p est l’ordonnée à l’origine pour trouver p, on utilise les coordonnées d’un point de la droite par exemple avec le point A(xA; yA), on a"],
                3 : [True, r"$ p = yA - m \times xA $"],
                4 : [False, "et pour trouver m on a :"],
                5 : [True, r"$ m = \frac{yB - yA}{xB - xA} $"],
            }, 
            
            "Cours3" : {
                0 : [False, "Pour trouver les coordonnées du point d’intersection de 2 droites il faut trouver quand l’équation réduite 1 est égale à l’équation réduite 2 soit :"],
                1 : [True, r"$ mx + p = m’x + p’ $"],      
            }, 
        
            "Cours4" : {
                0 : [False, "Une fonction affine admet une expression algébrique de la forme : "],
                1 : [True, r"$ f(x) = mx + p $"],
                2 : [False, "et sa représentation graphique est une droite."],
                3 : ["Image", join("Image", "Cours", "CoursSecondeEqtDroite.png")],
            }, 
        }, 

        "NiveauMordor" : {
            "Cours0" : {
                0 : [False, "Il y a 2 manières pour résoudre un système à doubles inconnues, la fin est la même mais la réflexion n’est pas la même, il y a donc la résolution par substitution et la résolution par combinaisons linéaires, un système à double inconnues peut permettre de trouver les coordonnées d’un point d’intersection."],
            }, 

            "Cours1" : {
                0 : [False, "La méthode de substitution consiste à isoler une des variables dans l'une des équations et à substituer cette expression dans l'autre équation. Cela permet de réduire le système à une seule équation avec une seule inconnue, qui peut alors être résolue."],
            }, 

            "Cours2" : {
                0 : [False, "Exemple de résolution par substitution :"],
                1 : [True, r"$ x + y = 5 $"],
                2 : [True, r"$ 2x - y = 1 $"],
                3 : [False, "1. Isoler une variable à l’aide d’une équation :"],
                4 : [True, r"$ y = 5 - x  $"],
                5 : [False, "2. Substituer y par c-x dans l’autre équation :"],
                6 : [True, r"$ 2x - (5 - x) = 1 $"],
                7 : [False, "3. Résoudre pour trouver x :"],
                8 : [True, r"$ 2x - 5 + x = 1  $"],
                9 : [True, r"$ 3x - 5 = 1  $"],
                10 : [True, r"$ 3x = 6  $"],
                11 : [True, r"$ x = 2  $"],
                12 : [False, "4. Remplacer x par 2 et trouver y :"],
                13 : [True, r"$ y = 5 - 2 = 3  $"],
                14 : [False, "Solution"],
                15 : [True, r"$ x = 2, y = 3 $"],
            }, 
            
            "Cours3" : {
                0 : [False, "La méthode de combinaisons linéaires consiste à manipuler les équations pour éliminer l'une des variables. Cette manipulation se fait généralement en multipliant les équations par des coefficients appropriés afin d'obtenir des coefficients opposés pour une des variables, puis en additionnant ou soustrayant les équations."],
            }, 
        
            "Cours4" : {
                0 : [False, "Exemple de résolution par combinaison linéaire :"],
                1 : [True, r"$ 2x + y = 5 $"],
                2 : [True, r"$ 3x - y = 4 $"],
                3 : [False, "1. Additionner les deux équations pour éliminer y  :"],
                4 : [True, r"$ (2x + y) + (3x - y) = 5 + 4 $"],
                5 : [True, r"$ 2x + 3x + y - y = 9 $"],
                6 : [True, r"$ 5x = 9 $"],
                7 : [True, r"$  x = \frac{9}{5} $"],
                8 : [False, "Remplacer x par 9/5 dans la première équation pour trouver y  :"],
                9 : [True, r"$ 2 \times \frac{9}{5} + y = 5 $"],
                10 : [True, r"$ \frac{18}{5} + y = 5 $"],
                11 : [True, r"$ y = 5 - \frac{18}{5} $"],
                12 : [True, r"$ y = \frac{25}{5} - \frac{18}{5} $"],
                13 : [True, r"$ y = \frac{7}{5} $"],
                14 : [False, "Solution"],
                15 : [True, r"$ x = \frac{9}{5} ; y = \frac{7}{5} $"],
            }, 
        },
    },

    "Premiere" : {
        "NiveauPlaineRiviere" : {
            "Cours0" : {
                0 : [False, "Un polynôme du second degré admet comme forme développée :"],
                1 : [True, r"$ P(x)= ax^2 + bx + c $"],
                2 : [False, "avec a, b et c des coefficients et "],
                3 : [True, r"$ a \ne 0 $"],
                4 : [False, "Chaque polynôme admet une forme canonique sous la forme"],
                5 : [True, r"$ a \left( x - \alpha \right) ^2 + \beta $"],
                6 : [True, r"$ \alpha = \frac{-b}[2a] $"],
                7 : [True, r"$ \beta \frac{- \delta}[4a] $"],
                8 : [True, r"$ \delta b^2 -4ac $"],
            }, 

            "Cours1" : {
                0 : [False, "Pour résoudre P(x) = 0 il faut déterminer le discriminant delta :"],
                1 : [False, "Si le delta > 0, P(x) admet deux solutions distinctes :"],
                2 : [True, r"$ x1 = -b - \frac{\sqrt{delta}}{2a} $"],
                3 : [True, r"$ x2 = -b + \frac{\sqrt{delta}}{2a} $"],
                4 : [False, "Remarque : Il peut se factoriser par"],
                5 : [True, r"$ P(x)= a(x - x1)(x - x2) $"],
                6 : [False, "Si delta = 0 alors il n’en admet qu’une unique dite double :"],
                7 : [True, r"$ x = \alpha = \frac{-b}{2a} $"],
                8 : [False, "Remarque : Il se factorise par"],
                9 : [True, r"$ a(x - \alpha)^2 $"],
                10 : [False, "Si delta < 0 il n’admet pas de solution et ne se factorise pas"],
            }, 

            "Cours2" : {
                0 : [False, "Pour déterminer le signe du polynôme P(x), on doit utiliser le discriminant delta et alpha."],
                1 : [False, "Lorsque delta > 0 : "],
                2 : [False, "P(x) est du signe de a à l'extérieur des racines x1 et x2 ​,c'est-à-dire sur les intervalles "],
                3 : [True, r"$ \left] -\infty , x1 \right[ \text{et} \left] x2, +\infty \right[ $"],
                4 : [False, "il est du signe opposé à a entre les racines, c'est-à-dire sur l'intervalle"],
                5 : [True, r"$ \left] x1, x2 \right[ $"],
                6 : [False, "Lorsque delta = 0 : "],
                7 : [False, "P(x)  est toujours du signe de a sur R excepté à x = alpha où il est nulle."],
                8 : [False, "Lorsque delta < 0 : "],
                9 : [False, "P(x) est toujours du signe de a"],
                10 : [False, "Variations : "],
                11 : [False, "Lorsque a est positif la courbe représentative de P(x) décroît jusqu’à x=alpha puis croît."],
                12 : [False, "Lorsque a est négatif la courbe croît jusqu’à x=alpha puis décroît."],
            }, 

        }, 

        "NiveauMedievale" : {
            "Cours0" : {
                0 : [False, "Le taux de variation d’une fonction f en un point a est une mesure de la rapidité avec laquelle f change près de a. On dit que f est dérivable en a si la limite suivante existe : [Remplacer x par a]"],
                1 : [False, "Si cette limite existe, elle est appelée la dérivée de f en a et est notée"],
                2 : [True, r"$ f'(a) $"]
            }, 

            "Cours1" : {
                0 : [False, "La dérivée d'une fonction en un point donne la pente de la tangente à la courbe de la fonction en ce point. Elle se calcule grâce la formule"],
                1 : [True, r"$ T : y = f'(a)(x-a) + f(a) $"],
                2 : [False, "avec a un point de la courbe."],
            
            }, 

            "Cours2" : {
                0 : [True, r"$ \text{Dérivée d'une constante : Si} f(x) = c$ \text{alors} f'(x) = 0"],
                1 : [True, r"$ \text{Dérivée de} x^n \text{: Si} f(x) = x^n \text{alors} f'(x) = nx^{n-1} $"],
                2: [True, r"$ \text{Dérivée de} nx \text{: Si} f(x) = xn \text{alors} f'(x) = n $"],
                3 : [True, r"$ \text{Dérivée de} \text{: Si} f(x) = \frac{1}{x} \text{alors} f'(x) = -\frac{1}{x^2} $"],
                4 : [True, r"$ \text{Dérivée de} \text{: Si} f(x) = \sqrt{x} \text{alors} f'(x) = \frax{1}{2 \sqrt{x}} $"],
                5 : [True, r"$ \text{Somme et Différence : Si} f(x) = u+v \text{alors} f'(x) = u' + v'$"],
                6 : [True, r"$ \text{Produits : Si} f(x) = uv, \text{alors} f'(x) = u'v + uv' $"],
                7 : [True, r"$ \text{Quotient : Si} f(x) = \frac{u}{v} \text{alors} f'(x) = \frac{u'v - uv'}{v^2}  $"],

            }, 
            
            "Cours3" : {
                0 : [False, "Une dérivée peut servir à connaître les intervalles croissant et décroissant de la courbe, lorsque f’(x) > 0 alors f(x) est croissant et lorsque f’(x) < 0 alors f(x) est décroissant."],
            }, 
        
        },
        "NiveauBaseFuturiste" : {
            "Cours0" : {
                0 : [False, "Une suite est une liste ordonnée de nombres, on la définit souvent par : une relation de récurrence avec le terme n+1 noté Un+1  en fonction du terme n noté Un. Avec l’expression de récurrence, il est nécessaire de connaître un terme de la suite (par exemple U0 ou U1 etc…) pour calculer les autres. Ou une formule explicite qui permet d’exprimer directement le terme Un en fonction de l’indice n."],
            }, 

            "Cours1" : {
                0 : [False, "Dans une suite arithmétique le terme Un+1 se calcule à l’aide du terme précédent Un auquel on additionne ou on retranche une constante nommée raison, notée r. "],
                1 : [False, "La relation de récurrence de la suite se note :"],
                2 : [True, r"$ U_{n+1} = U_{n} + r $"],
                3 : [False, "avec U0 le premier terme de la suite."], 
                4 : [False, "La formule explicite de la suite se note :"],
                5 : [True, r"$ U_{n} = U_{0} + n \times r $"],
                6 : [False, "Exemple de la suite Un de premier terme U0 = 1 et de raison r =2 : "],
                7 : [False, "Forme de récurrence :"],
                8 : [True, r"$ U_{n+1} = U_{n} + 2 $"],
                9 : [False, "Formule explicite : "],
                10 : [True, r"$ U_{n} = 1 + 2n $"],
            }, 

            "Cours2" : {
                0 : [False, "Dans une suite géométrique le terme Vn+1 se calcule à l’aide du terme précédent Vn auquel on multiplie une constante (la raison), notée q."],
                1 : [False, "La relation de récurrence de la suite se note :"],
                2 : [True, r"$ V_{n+1} = V_{n} \ times q $"],
                3 : [False, "avec V0 le premier terme de la suite."],
                4 : [False, "La formule explicite de la suite se note :"],
                5 : [True, r"$ V_{n} = V_{0} \times q^n $"],
                6 : [False, "Exemple de la suite Vn de premier terme V0 = 0,5 et de raison q =1,7:"],
                7 : [False, "Forme de récurrence :"],
                8 : [True, r"$ V_{n+1} = V_{n} \times 1.7 $"],
                9 : [False, "Formule explicite "],
                10 : [True, r"$ V_{n} = 0.5 \times 1.7n $"],
            }, 

            "Cours3" : {
                0 : [False, "Pour reconnaître si une suite est une suite arithmétique on peut vérifier si la différence"],
                1 : [True, r"$ U_{n+1} - U_{n} $"],
                2 : [False, "est constante pour tout entier naturel n, ce qui donnera la raison par la même occasion."],
                3 : [False, "Pour reconnaître si une suite est une suite géométrique on peut vérifier si le rapport"],
                4 : [True, r"$ \frac{V_{n+1}}{V_{n}} $"],
                5 : [False, "est constant pour tout entier naturel n, ce qui donnera la raison par la même occasion."],
            }, 
            "Cours4" : {
                0 : [False, "La somme des n premiers termes d’une suite arithmétique se calcule avec la formule :"],
                1 : [True, r"$ S_{n} = \text{nombre de termes} \times \frac{\text{premier terme} + \text{dernier terme}}{2} $"],
                2 : [False, "La somme des n premiers termes d’une suite géométrique se calcule avec la formule :"],
                3 : [True, r"$ S_{n} = \text{premier terme} \times \frac{1 - \text{raison}^\text{nombre de termes}}{1 - \text{raison}} $"],
            }, 
        }, 

        "NiveauMordor" : {
            "Cours0" : {
                0 : [],
            }, 

            "Cours1" : {
                0 : [],
            }, 

            "Cours2" : {
                0 : [],
            }, 
            
            "Cours3" : {
                0 : [],
            }, 
        
            "Cours4" : {
                0 : [],
            }, 
        },
    }, 

    "Terminale" : {
        "NiveauPlaineRiviere" : {
            "Cours0" : {
                0 : [],
            }, 

            "Cours1" : {
                0 : [],
            }, 

            "Cours2" : {
                0 : [],
            },
        },

        "NiveauMedievale" : {
            "Cours0" : {
                0 : [],
            }, 

            "Cours1" : {
                0 : [],
            }, 

            "Cours2" : {
                0 : [],
            }, 

            "Cours3" : {
                0 : [],
            }, 
        }, 

        "NiveauBaseFuturiste" : {
            "Cours0" : {
                0 : [],
            }, 

            "Cours1" : {
                0 : [],
            }, 

            "Cours2" : {
                0 : [],
            }, 
            
            "Cours3" : {
                0 : [],
            }, 
        
            "Cours4" : {
                0 : [],
            }, 
        }, 

        "NiveauMordor" : {
            "Cours0" : {
                0 : [],
            }, 

            "Cours1" : {
                0 : [],
            }, 

            "Cours2" : {
                0 : [],
            }, 
            
            "Cours3" : {
                0 : [],
            }, 
        
            "Cours4" : {
                0 : [],
            }, 
        },
    },
}
