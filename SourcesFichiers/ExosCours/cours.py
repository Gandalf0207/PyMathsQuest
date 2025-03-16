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
                5 : [False, r"$ \text{longueur} \times \text{largeur} $"],
            }, 

            "Cours1" : {
                0 : [False, "Le volume du cylindre est :"],
                1 : [True, r"$ \text{base} \times \text{hateur} \leftrightarrow \pi \times \txt{rayon}^2 \times h $"],
                2 : [False, "De manière plus générale le volume d’une multitude de solide se calcule simplement par :"],
                3 : [False, r"$ \text{base} \times \text{hauteur} $"],
            }, 

            "Cours2" : {
                0 : [False, "Le volume du cône est celui du cylindre divisé par 3 soit :"],
                1 : [True, r"$ \frac{\pi \times \text{rayon}^2 \times h}{3} $"],
                2 : [False, "Le volume d’une pyramide est celui du prisme droit que l’on divise par 3 soit "],
                3 : [True, r"$ \frac{\text{Vprimse}}{3} $"],
            }, 

            "Cours3" : {
                0 : [False, "La formule pour calculer le volume d’un sphère est :"],
                1 : [False, r"$ \frac{4}{3} \times \pi \times r^3 $"],
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
