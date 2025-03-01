from settings import *

ElementsFr = {
    "GameName" : "PyMathsQuest",
    "Loading" : "Chargement",
    "Interaction" : "Appuyer sur E",
    "LevelSup" : "Vous passez au niveau suppérieur !",

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

