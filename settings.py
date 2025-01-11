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
def LoadJsonMapValue(self, index1 :str, index2 :str) -> list:
    """Récupération des valeur stockées dans le fichier json pour les renvoyer quand nécéssaire à l'aide des indices données pour les récupérer"""
    
    # récupération des valeurs stocké dans le json
    with open(join("Sources","Ressources","AllMapValue.json"), "r") as f: # ouvrir le fichier json en mode e lecture
        loadElementJson = json.load(f) # chargement des valeurs
    return loadElementJson[index1].get(index2, None) # on retourne les valeurs aux indices de liste quisont données

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








LONGUEUR = 150
LARGEUR = 75
CASEMAP = 128
CELL_SIZE = 2
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720 
COORS_BOX_ALL_SETTINGS = (WINDOW_WIDTH-436, WINDOW_HEIGHT-160)
COORDS_BOX_IDEAS_TIPS = (320, WINDOW_HEIGHT-160)

FONT20 = pygame.font.Font(None, 20)
FONT30


STATE_HELP_INFOS = ["SeePNJ"] # list pour pouvoir etre modifié
INFOS = {
    "Niveau" : 0,
    "Langue" : "Fr", 
    "Difficulte" : False,
    "Exo" : False, 
    "ExoPasse" : False,
    "ChangementNiveau" : False
}

TEXTE = {
    "Dialogues" : None,
    "Elements" : None
}

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

PNJ = {
    "PNJ1" : False,
    "PNJ2" : False, 
    "PNJ3" : False, 
    "PNJ4" : False, 
    "PNJ5" : False
}




EspacementPointRepereRiviere = 15
CoupageMapRiviere = 50 # 1/3 de la longueur
CouloirRiviere = 4