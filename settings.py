from random import randint, random, choice
from random import *
import os
import time
import json
import heapq
import copy
from typing import Union
import pygame 
from os.path import join 
from os import walk
import threading
from math import *
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import matplotlib

plt.rc('text', usetex=True)  # Active l'utilisation de LaTeX
plt.rc('font', family='serif')  # Définit une police compatible
matplotlib.use('Agg')

# Methode Utile : 

# get values
def LoadJsonMapValue(index1 :str, index2 :str) -> list:
    """Récupération des valeur stockées dans le fichier json pour les renvoyer quand nécéssaire à l'aide des indices données pour les récupérer"""
    
    # récupération des valeurs stocké dans le json
    with open(join("Sources","Ressources","AllMapValue.json"), "r") as f: # ouvrir le fichier json en mode e lecture
        loadElementJson = json.load(f) # chargement des valeurs
    return loadElementJson[index1].get(index2, None) # on retourne les valeurs aux indices de liste quisont données

# add values
def AjoutJsonMapValue(value :list, index1 :str, index2 :str) -> None:
    """Chargement des données JSON aux index indiqués pour pouvoir les stocker"""
    try: # Si le chargement est possible
        with open(join("Sources","Ressources","AllMapValue.json"), "r") as f: # ouvrir le fichier json en mode lecture
            donnees = json.load(f) # chargement des données
    except (FileNotFoundError, json.JSONDecodeError): # Sinon relève une erreur et arrêt du programme
        assert ValueError("Error load JSON file") # stop du programme avec l'assert (programmation défensive)

    donnees[f"{index1}"][f"{index2}"] = value # Ajout valeurs aux indexs donnés

    # Sauvegarde des données dans le fichier JSON avec une indentation pour un format "lisible"
    with open(join("Sources","Ressources","AllMapValue.json"), "w") as f: # ouverture du fichier json en mode écriture
        json.dump(donnees, f, indent=4) # chargement dans le fichier json de l'élément données (possédent les index de position et les valeurs à stocker)



# texte wrap pygame
def wrap_text(text, font, max_width):
            words = text.split(' ')
            lines = []
            current_line = ''

            for word in words:
                test_line = f"{current_line} {word}".strip()
                if font.size(test_line)[0] <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word
            if current_line:
                lines.append(current_line)
            return lines







# INFOS FIXES
LONGUEUR = 150
LARGEUR = 75
CASEMAP = 128
CELL_SIZE = 2
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720 
COORS_BOX_ALL_SETTINGS = (WINDOW_WIDTH-436, WINDOW_HEIGHT-160)
COORDS_BOX_IDEAS_TIPS = (320, WINDOW_HEIGHT-160)

# font tool box
FONT = {
    "FONT20" : None,
    "FONT22" : None,
    "FONT24" : None,
    "FONT30" : None,
    "FONT36" : None,
    "FONT36B" : None,
}


STATE_HELP_INFOS = ["SeePNJ"] # list pour pouvoir etre modifié : tips

# box infos globales
INFOS = {
    "Niveau" : 0,
    "Langue" : "Fr", 
    "Difficulte" : False,
    "Exo" : False, 
    "ExoPasse" : False,
    "ChangementNiveau" : False
}

# texte : tout le texte
TEXTE = {
    "Dialogues" : None,
    "Elements" : None
}

# inventaires 
INVENTORY = {
    "Planks" : 0,
    "OldAxe" : 0,
    "Pickaxe" : 0,
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "e" : 0,
    "f" : 0,
    "g" : 0,
    "h" : 0,
    "i" : 0,
}

# check pnj parlé ou non 
PNJ = {
    "PNJ1" : False,
    "PNJ2" : False, 
    "PNJ3" : False, 
    "PNJ4" : False, 
    "PNJ5" : False
}


# infos map tiers
EspacementPointRepereRiviere = 15
EspacementPointRepereRiviere2 = 7
CoupageMapRiviere = 50 # 1/3 de la longueur
CoupageMapRiviere2 = 75 # 1/3 de la longueur

CouloirRiviere = 4