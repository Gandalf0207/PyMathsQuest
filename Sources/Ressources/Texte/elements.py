from settings import *

ElementsFr = {
    "GameName" : "PyMathsQuest",
    "Loading" : "Chargement",
    "Interaction" : "Appuyer sur E",
    "LevelSup" : "Vous passez au niveau suppérieur !",
    "Humour" : "Humour, second degré",

    "HomeInterface" : {
        "Niveau" : {
            "Title" : "Niveau",
            "Consignes" : "Choisissez un niveau",
            "Seconde" : "Seconde",
            "Premiere" : "Premiere",
            "Terminale" : "Terminale",
            "All": "Tous",
        },
        "Difficulte" : {
            "Title" : "Difficulté",
            "Consignes" : "Choisissez un niveau",
            "Simple" : "Simple",
            "Difficile" : "Difficile",
        },
        "Langue" : {
            "Title" : "Langue",
            "Consignes" : "Choisissez un niveau",
            "Français" : "Français",
            "Anglais" : "Anglais",
            "Espagnol" : "Espagnol"
        },

        "InterfaceCondition" : {
            "ConditionsUtilisation" : """1. Liberté d'utilisation, de modification et de distribution
                    Ce programme est sous licence GPL v3+, ce qui signifie que vous êtes libre de :

                    Exécuter le logiciel pour tout usage (personnel, éducatif, commercial, etc.).
                    Étudier, modifier et améliorer son code source.
                    Redistribuer des copies du programme, modifiées ou non, à condition de respecter la même licence.
                    2. Code source et contributions
                    Le code source du projet est accessible sur GitHub :
                    👉 https://github.com/Gandalf0207/Py-Maths-Quest

                    Toute contribution est la bienvenue tant qu'elle respecte les termes de la GPL v3.

                    3. Aucune garantie
                    Ce logiciel est fourni "tel quel", sans garantie d'aucune sorte. Les auteurs ne peuvent être tenus responsables d'éventuels dommages résultant de son utilisation.

                    4. Utilisation de bibliothèques open source
                    Ce projet utilise des bibliothèques open-source telles que Python, Tkinter, Matplotlib, LaTeX, etc. Nous respectons et apprécions le travail de leurs créateurs et nous conformons aux licences respectives de ces bibliothèques.

                    5. Crédits et cadre de réalisation
                    Ce projet a été développé par LUBAN Théo & PLADEAU Quentin dans le cadre du cours de NSI en terminale. Un grand merci à ESCOUTE Cédric et Patrice-Florent Marie-Jeanne pour leur soutien et leur enseignement.

                    6. Mise à jour des conditions
                    Ces conditions peuvent être mises à jour à tout moment. Consultez le dépôt GitHub pour toute information sur la licence et les modifications du projet.

                    © 2025 - Py-Maths-Quest
                    Publié sous licence GPL v3+ """,

            "Title" : "Termes et conditions d'utilisation"

        },

        "TexteConditions" : "J'accepte les licenes, termes et conditions d'Utilisations.",
        "Lancer" : "Commencer",


    },


    "InterfacePNJ" : {
        "SkipButton" : "Suivant",
        "Oui" : "Oui",
        "Non" : "Non",

    },

    "InterfaceReactor": {
        "Title" : "Réacteur nucléraire Centrale",
        "Texte" : "Appuyer pour allumer le réacteur",
        "Heure" : "Heure",
        "Temperature" : "Température",
        "EtatName" : "Etat",
        "StatueName" : "Statue",
        "Etat" : {
            "Inactif" : "Inactif",
            "Actif" : "Actif",
        },
        "Statue" : {
            "Null" : "Null",
            "Normal" : "Normal",
            "Instable" : "Instable",
            "Critique" : "Critique",
        },
        "AddPuissance" : "Augmenter la puissance",    
    },

    "InterfaceHomeMenu" : {
        "Title" : "Menu",

    },

    "HotBar" : {
        "Settings" : {
            "Title" : "Paramettres",
            "Language" : "Langue",
            "TypeLanguage" : {
                "Fr" : "Français",
                "En" : "Anglais",
                "Es" : "Espagnol",
            },
            "PressKey" : "Appuyez sur une touche...",

            },
        "Sound" : {
            "Title" : "Volume",
            }, 
        "Bundle" : {
            "Title" : "Inventaire",
            },
        "Book" : {
            "Title" : "Livre de cours"
            },  

        "IdeaTips": {
            "NiveauPlaineRiviere" : {
                "SeePNJ" : "Discuter avec le pnj sur la map. Regarder la minimap",
                "LearnCrossBridge" : "Traverser le pont. Se rapprocher du pont qui se trouve à côté du bûcheron.",
                "BuildBridge" : "Construire le pont. Se rapprocher de la rivière pour pouvoir construire",
                "CrossBridge" : "Traverser le pont pour acceder à la suite.",
                "MineRock" : "Utiliser la pioche pour casser le rocher qui bloque le pont de sortie",
            },

           "NiveauMedievale" : {
                "SeePNJ" : "Discuter avec le pnj sur la map. Regarder la minimap et suivez le chemin !",
                "BuildBridge" : "Construire le pont. Se rapprocher de la rivière en suivant le chemin pour pouvoir construire",
                "CrossBridge" : "Traverser le pont pour acceder à la suite.",
                "FindWell" : "Trouver le puits au centre du village et frabriquer un bateau.",
                "PlaceBoat" : "Vous devez placer le bateau dans la rivière.",
                "NavigateBoat" : "Vous devez rentrer dans le bateau pour pouvoir acceder au chateau.",
                "OpenDoor" : "Vous devez ouvrir le chateau pour acceder à la suite.",
                "OpenPortail" : "Vous devez réouvrir le portail",
            },

            "NiveauBaseFuturiste" : {
                "SeePNJ" : "Discuter avec le pnj sur la map. Regarder la minimap et suivez le chemin !",
                "Electricity" : "Vous devez activer l'électricité",
                "UseVent" : "Vous devez utiliser les conduits d'aération", 
                "EscapeVaisseau": "Vous devez vous échaper du vaisseau par la porte arrière."
            },

            "NiveauMordor" : {
                "SeePNJ" : "Discuter avec le pnj sur la map. Regarder la minimap et suivez le chemin !",
                "CrossBridge" : "Vous devez traverser le pont pour acceder à la suite",
            },
        },
    },

    "NiveauPlaineRiviere" : {
        "Cinematique1End" : "Le bûcheron a coupé l'arbre, vous pouvez traverser la rivière !",
        "TraverserPont" : "Vous venez de traverser le pont",
        "BuildBridge" : "Vous venez de construire le pont",
        "BreakRock" : "Vous venez de casser le rocher avec votre pioche",
        "MakeExo" : "Pour pouvoir traverser le pont,  vous devez résoudre cet exercice.",

        "ExoTexte" : {
            "Seconde" :{
                "Numero0" :{
                    "Title" : "Exercice équation du premier degré",

                    "DifficulteTrue" : {
                        "Consigne" : "Trouver la valeur de x dans cette équation du premier degré :",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },

                    "DifficulteFalse" : {
                        "Consigne" : "Trouver la valeur de x dans cette équation du premier degré :",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },
                }

            },         
            "Premiere" :{
                
            },

            "Terminale" : {

            },

            
        }
    },

    "NiveauMedievale" : {
        "Cinematique1End" : "Le pnj à fuis à travers le portail, vous devez le rallumer",
        "TraverserPont" : "Vous venez de traverser le pont",
        "CantTraverserPont" : "Le garde est devant le pont, vous ne pouvez pas le traverser.",
        "BuildBridge" : "Vous venez de construire le pont",
        "CutTree" : "Vous venez de couper un arbre",
        "RemoveSouche" : "Vous venez de retirer une souche d'arbre",
        "NeedPlanks" : "Vous devez avoir 3 planches pour pouvoir construire le bateau",
        "CraftBoat" : "Vous avez fabriqué un bateau",
        "PlaceBoat" : "Vous avez placé le bateau sur la rivière",
        "UseBoat" : "Vous naviguez sur la rivière et arrivez dans l'enceinte du château.",
        "UseBoat2" : "Vous naviguez sur la rivière et sortez de l'enceinte du château.",
        "GetCours" : "Vous obtenez un bout du parchemin de cours ! gg à toi ", 
        "OpenChateau" : "Vous entrez dans le chateau de bobini",
        "OpenPortail" : "Vous devez réouvvrir le portail pour acceder à la suite", 
        "MakeExo" : "Pour réouvir le portail, vous devez résoudre cet exercice",

        "ExoTexte" : {
            "Seconde" :{
                "Numero0" :{
                    "Title" : "Calculs de Volumes",

                    "DifficulteTrue" : {
                        "Consigne" : " A l'aide des valeurs données, veuillez calculer le volume total de la figure représentée ci-dessous.:",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },

                    "DifficulteFalse" : {
                        "Consigne" : "A l'aide des valeurs données, veuillez calculer le volume demandé du cube de côté c, de la sphère de rayon r et du cone de hauter h et de diametre de base d:",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },
                },

            },         
            "Premiere" :{
                
            },

            "Terminale" : {

            },
        }

    },


    "NiveauBaseFuturiste" : {
        "Cinematique1End" : "Le pnj à fuis à travers le portail, vous devez le rallumer",
        "UseVent" : "Vous vous baladez dans les conduits d'aération.", 
        "MakeExo" : "Pour réouvir le portail, vous devez résoudre cet exercice",
        "PiloteMoveCafet" : "Le pilote s'est déplacé dans la salle de lancement, rejoignez le !",
        "VaisseauSpacial" : "Vous montez dans le vaisseau",
        "CrashVaisseau" : "Le vaisseau s'est crash, soit meilleur stp",
        "ExoTexte" : {
            "Seconde" :{
                "Numero0" :{
                    "Title" : "Calculs de Volumes",

                    "DifficulteTrue" : {
                        "Consigne" : " A l'aide des valeurs données, veuillez calculer le volume total de la figure représentée ci-dessous.:",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },

                    "DifficulteFalse" : {
                        "Consigne" : "A l'aide des valeurs données, veuillez calculer le volume demandé du cube de côté c, de la sphère de rayon r et du cone de hauter h et de diametre de base d:",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },
                },

            },         
            "Premiere" :{
                
            },

            "Terminale" : {

            },
        }

    },


    "NiveauMordor" : {
        "MakeExo" : "Pour réouvir le portail, vous devez résoudre cet exercice",
        "GoPrison" : "Vous êtes emprisonné par l'Orc.",
        "Parchemin" : "Vous obtenez le parchemin",
        "ParcheminVu" : "Vous avez déjà obtenu le perchemin",
        "Key" : "Vous trouvez des clés dans le pot",
        "Key2" : "Le pot est vide",
        "OpenDoor" : "Vous venez d'ouvrir la porte de la cellule",
        "KillPNJ3" : "Vous venez de tuer le garde, vous pouvez continuer votre route",
        "LeavePNJ2" : "Votre ami est parti, il vous remercie pour votre aide",
        "TraverserPont" : "Vous traversez le pont",

        "ExoTexte" : {
            "Seconde" :{
                "Numero0" :{
                    "Title" : "Calculs de Volumes",

                    "DifficulteTrue" : {
                        "Consigne" : " A l'aide des valeurs données, veuillez calculer le volume total de la figure représentée ci-dessous.:",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },

                    "DifficulteFalse" : {
                        "Consigne" : "A l'aide des valeurs données, veuillez calculer le volume demandé du cube de côté c, de la sphère de rayon r et du cone de hauter h et de diametre de base d:",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },
                },

            },         
            "Premiere" :{
                
            },

            "Terminale" : {

            },
        }

    },
    
}





























## à mettre à jour plus tard

ElementsEn = {
    "GameName" : "PyMathsQuest",
    "Loading" : "Chargement",
    "Interaction" : "Appuyer sur E",
    "MakeExo" : "Pour pouvoir traverser le pont,  vous devez résoudre cet exercice.",
    "LevelSup" : "Vous passez au niveau suppérieur !",

    "InterfacePNJ" : {
        "SkipButton" : "Suivant",
        "Oui" : "Oui",
        "Non" : "Non",

    },

    "HotBar" : {
        "Settings" : {
            "Title" : "Paramettres",
            "Language" : "Langue",
            "TypeLanguage" : {
                "Fr" : "French",
                "En" : "English",
                "Es" : "Spanish",
            },
            "PressKey" : "Appuyez sur une touche...",

            },
        "Sound" : {
            "Title" : "Volume",
            }, 
        "Bundle" : {
            "Title" : "Inventaire",
            },
        "Book" : {
            "Title" : "Livre de cours"
            },  

        "IdeaTips": {
            "NiveauPlaineRiviere" : {
                "SeePNJ" : "Discuter avec le pnj sur la map. Regarder la minimap",
                "LearnCrossBridge" : "Traverser le pont. Se rapprocher du pont qui se trouve à côté du bûcheron.",
                "BuildBridge" : "Construire le pont. Se rapprocher de la rivière pour pouvoir construire",
                "CrossBridge" : "Traverser le pont pour acceder à la suite.",
                "MineRock" : "Utiliser la pioche pour casser le rocher qui bloque le pont de sortie",
            },

           "NiveauMedievale" : {
                "SeePNJ" : "Discuter avec le pnj sur la map. Regarder la minimap et suivez le chemin !",
                "BuildBridge" : "Construire le pont. Se rapprocher de la rivière en suivant le chemin pour pouvoir construire",
                "CrossBridge" : "Traverser le pont pour acceder à la suite.",
                "FindWell" : "Trouver le puits au centre du village et frabriquer un bateau.",
                "PlaceBoat" : "Vous devez placer le bateau dans la rivière.",
                "NavigateBoat" : "Vous devez rentrer dans le bateau pour pouvoir acceder au chateau.",
                "OpenDoor" : "Vous devez ouvrir le chateau pour acceder à la suite.",
                "OpenPortail" : "Vous devez réouvrir le portail",
            },
        },
    },

    "NiveauPlaineRiviere" : {
        "Cinematique1End" : "Le bûcheron a coupé l'arbre, vous pouvez traverser la rivière !",
        "TraverserPont" : "Vous venez de traverser le pont",
        "BuildBridge" : "Vous venez de construire le pont",
        "BreakRock" : "Vous venez de casser le rocher avec votre pioche",

        "ExoTexte" : {
            "Seconde" :{
                "Numero0" :{
                    "Title" : "Exercice équation du premier degré",

                    "DifficulteTrue" : {
                        "Consigne" : "Trouver la valeur de x dans cette équation du premier degré :",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },

                    "DifficulteFalse" : {
                        "Consigne" : "Trouver la valeur de x dans cette équation du premier degré :",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },
                }

            },         
            "Premiere" :{
                
            },

            "Terminale" : {

            },

            
        }
    },

    "NiveauMedievale" : {
        "Cinematique1End" : "Le pnj à fuis à travers le portail, vous devez le rallumer",
        "TraverserPont" : "Vous venez de traverser le pont",
        "CantTraverserPont" : "Le garde est devant le pont, vous ne pouvez pas le traverser.",
        "BuildBridge" : "Vous venez de construire le pont",
        "CutTree" : "Vous venez de couper un arbre",
        "NeedPlanks" : "Vous devez avoir 3 planches pour pouvoir construire le bateau",
        "CraftBoat" : "Vous avez fabriqué un bateau",
        "PlaceBoat" : "Vous avez placé le bateau sur la rivière",
        "UseBoat" : "Vous naviguez sur la rivière et arrivez dans l'enceinte du château.",
        "UseBoat2" : "Vous naviguez sur la rivière et sortez de l'enceinte du château.",
        "GetCours" : "Vous obtenez un bout du parchemin de cours ! gg à toi ", 
        "OpenChateau" : "Vous entrez dans le chateau de bobini",
        "OpenPortail" : "Vous devez réouvvrir le portail pour acceder à la suite", 

        "ExoTexte" : {
            "Seconde" :{
                "Numero0" :{
                    "Title" : "Calculs de Volumes",

                    "DifficulteTrue" : {
                        "Consigne" : " A l'aide des valeurs données, veuillez calculer le volume total de la figure représentée ci-dessous.:",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },

                    "DifficulteFalse" : {
                        "Consigne" : "A l'aide des valeurs données, veuillez calculer le volume demandé du cube de côté c, de la sphère de rayon r et du cone de hauter h et de diametre de base d:",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },
                },

            },         
            "Premiere" :{
                
            },

            "Terminale" : {

            },
        }

    },
    
}



ElementsEs = {
    "GameName" : "PyMathsQuest",
    "Loading" : "Chargement",
    "Interaction" : "Appuyer sur E",
    "MakeExo" : "Pour pouvoir traverser le pont,  vous devez résoudre cet exercice.",
    "LevelSup" : "Vous passez au niveau suppérieur !",

    "InterfacePNJ" : {
        "SkipButton" : "Suivant",
        "Oui" : "Oui",
        "Non" : "Non",

    },

    "HotBar" : {
        "Settings" : {
            "Title" : "Paramettres",
            "Language" : "Langue",
            "TypeLanguage" : {
                "Fr" : "Frances",
                "En" : "Ingles",
                "Es" : "Espanol",
            },
            "PressKey" : "Appuyez sur une touche...",

            },
        "Sound" : {
            "Title" : "Volume",
            }, 
        "Bundle" : {
            "Title" : "Inventaire",
            },
        "Book" : {
            "Title" : "Livre de cours"
            },  

        "IdeaTips": {
            "NiveauPlaineRiviere" : {
                "SeePNJ" : "Discuter avec le pnj sur la map. Regarder la minimap",
                "LearnCrossBridge" : "Traverser le pont. Se rapprocher du pont qui se trouve à côté du bûcheron.",
                "BuildBridge" : "Construire le pont. Se rapprocher de la rivière pour pouvoir construire",
                "CrossBridge" : "Traverser le pont pour acceder à la suite.",
                "MineRock" : "Utiliser la pioche pour casser le rocher qui bloque le pont de sortie",
            },

           "NiveauMedievale" : {
                "SeePNJ" : "Discuter avec le pnj sur la map. Regarder la minimap et suivez le chemin !",
                "BuildBridge" : "Construire le pont. Se rapprocher de la rivière en suivant le chemin pour pouvoir construire",
                "CrossBridge" : "Traverser le pont pour acceder à la suite.",
                "FindWell" : "Trouver le puits au centre du village et frabriquer un bateau.",
                "PlaceBoat" : "Vous devez placer le bateau dans la rivière.",
                "NavigateBoat" : "Vous devez rentrer dans le bateau pour pouvoir acceder au chateau.",
                "OpenDoor" : "Vous devez ouvrir le chateau pour acceder à la suite.",
                "OpenPortail" : "Vous devez réouvrir le portail",
            },
        },
    },

    "NiveauPlaineRiviere" : {
        "Cinematique1End" : "Le bûcheron a coupé l'arbre, vous pouvez traverser la rivière !",
        "TraverserPont" : "Vous venez de traverser le pont",
        "BuildBridge" : "Vous venez de construire le pont",
        "BreakRock" : "Vous venez de casser le rocher avec votre pioche",

        "ExoTexte" : {
            "Seconde" :{
                "Numero0" :{
                    "Title" : "Exercice équation du premier degré",

                    "DifficulteTrue" : {
                        "Consigne" : "Trouver la valeur de x dans cette équation du premier degré :",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },

                    "DifficulteFalse" : {
                        "Consigne" : "Trouver la valeur de x dans cette équation du premier degré :",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },
                }

            },         
            "Premiere" :{
                
            },

            "Terminale" : {

            },

            
        }
    },

    "NiveauMedievale" : {
        "Cinematique1End" : "Le pnj à fuis à travers le portail, vous devez le rallumer",
        "TraverserPont" : "Vous venez de traverser le pont",
        "CantTraverserPont" : "Le garde est devant le pont, vous ne pouvez pas le traverser.",
        "BuildBridge" : "Vous venez de construire le pont",
        "CutTree" : "Vous venez de couper un arbre",
        "NeedPlanks" : "Vous devez avoir 3 planches pour pouvoir construire le bateau",
        "CraftBoat" : "Vous avez fabriqué un bateau",
        "PlaceBoat" : "Vous avez placé le bateau sur la rivière",
        "UseBoat" : "Vous naviguez sur la rivière et arrivez dans l'enceinte du château.",
        "UseBoat2" : "Vous naviguez sur la rivière et sortez de l'enceinte du château.",
        "GetCours" : "Vous obtenez un bout du parchemin de cours ! gg à toi ", 
        "OpenChateau" : "Vous entrez dans le chateau de bobini",
        "OpenPortail" : "Vous devez réouvvrir le portail pour acceder à la suite", 

        "ExoTexte" : {
            "Seconde" :{
                "Numero0" :{
                    "Title" : "Calculs de Volumes",

                    "DifficulteTrue" : {
                        "Consigne" : " A l'aide des valeurs données, veuillez calculer le volume total de la figure représentée ci-dessous.:",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },

                    "DifficulteFalse" : {
                        "Consigne" : "A l'aide des valeurs données, veuillez calculer le volume demandé du cube de côté c, de la sphère de rayon r et du cone de hauter h et de diametre de base d:",
                        "QCM" : "Choisissez l'unique et bonne réponse",
                    },
                },

            },         
            "Premiere" :{
                
            },

            "Terminale" : {

            },
        }

    },
    
}

