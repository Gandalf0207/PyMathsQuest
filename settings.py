from random import randint, random, choice
from random import *
import random
import os
import time
import gc
import json
import heapq
import copy
from typing import Union
import pygame 
from os.path import join 
from os import walk
import threading
from math import *
import math
import sys
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import matplotlib
from math import atan2, degrees


plt.rc('text', usetex=True)  # Active l'utilisation de LaTeX
plt.rc('font', family='serif')  # Définit une police compatible
matplotlib.use('Agg')

# Methode Utile : 

# get values
def LoadJsonMapValue(index1 :str, index2 :str) -> list:
    """Récupération des valeur stockées dans le fichier json pour les renvoyer quand nécéssaire à l'aide des indices données pour les récupérer"""
    
    # récupération des valeurs stocké dans le json
    with open(join("SourcesFichiers","Ressources","AllMapValue.json"), "r") as f: # ouvrir le fichier json en mode e lecture
        loadElementJson = json.load(f) # chargement des valeurs
    return loadElementJson[index1].get(index2, None) # on retourne les valeurs aux indices de liste quisont données

# add values
def AjoutJsonMapValue(value :list, index1 :str, index2 :str) -> None:
    """Chargement des données JSON aux index indiqués pour pouvoir les stocker"""
    try: # Si le chargement est possible
        with open(join("SourcesFichiers","Ressources","AllMapValue.json"), "r") as f: # ouvrir le fichier json en mode lecture
            donnees = json.load(f) # chargement des données
    except (FileNotFoundError, json.JSONDecodeError): # Sinon relève une erreur et arrêt du programme
        assert ValueError("Error load JSON file") # stop du programme avec l'assert (programmation défensive)

    donnees[f"{index1}"][f"{index2}"] = value # Ajout valeurs aux indexs donnés

    # Sauvegarde des données dans le fichier JSON avec une indentation pour un format "lisible"
    with open(join("SourcesFichiers","Ressources","AllMapValue.json"), "w") as f: # ouverture du fichier json en mode écriture
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


def wrap_text_2(text, font, max_width):
    """Divise le texte en lignes tout en gardant les sauts de ligne d'origine"""
    paragraphs = text.split("\n")  # Séparer en paragraphes
    wrapped_lines = []

    for paragraph in paragraphs:
        words = paragraph.split(" ")
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()  # Tester avec un mot en plus
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                wrapped_lines.append(current_line)  # Ajouter la ligne terminée
                current_line = word  # Commencer une nouvelle ligne

        if current_line:
            wrapped_lines.append(current_line)  # Ajouter la dernière ligne du paragraphe

        wrapped_lines.append("")  # Ajouter une ligne vide pour séparer les paragraphes

    return wrapped_lines[:-1]  # Supprimer la dernière ligne vide en trop

def GetLocalPos(event, interfaceSurface, PosBlit):
    # Coordonnées globales de l'événement
    global_pos = event.pos  # Coordonnées globales dans la fenêtre

    # Rect global de la surface de l'interface
    surface_rect = pygame.Rect(PosBlit[0],PosBlit[1], interfaceSurface.get_width(), interfaceSurface.get_height())

    # Vérifiez si le clic est sur l'interface
    if surface_rect.collidepoint(global_pos):
        # Convertissez en coordonnées locales
        local_pos = (global_pos[0] - surface_rect.x, global_pos[1] - surface_rect.y)
        return local_pos
    return False

def ChangeCursor(boolCheck, etatCursor):
    if boolCheck:
        match etatCursor:
            case "Hand" :
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            case "Interdit":
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_NO)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


# Couleurs (température froide à chaude)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
SCROLLBAR_COLOR = (180, 180, 180)  # Couleur de la scrollbar
SCROLLBAR_HOVER = (150, 150, 150)  # Couleur au survol

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
    "FONT20U" : None,
    "FONT22" : None,
    "FONT24" : None,
    "FONT30" : None,
    "FONT36" : None,
    "FONT36B" : None,
    "FONT50" : None,
    "FONT74" : None,
}


STATE_HELP_INFOS = ["SeePNJ"] # list pour pouvoir etre modifié : tips

NIVEAU = {
     # niveau
    "Niveau" : "Seconde",
    "All" : False, 

    # map
    "Map" : "NiveauBaseFuturiste",
}
# box infos globales
INFOS = {
    "GameStart" : False,
    "ErrorLoad" : False,
    "GameEnd" : False,
    "CrashGame" : False,
    
    "Difficulte" : False,
    
    "Exo" : False, 
    "ExoPasse" : False,
    
    "DemiNiveau" : True,
    "ChangementNiveau" : False,
    
    "HideHotBar" : False,
    "RebindingKey": False,
    "ReactorOn" : False,
    "HidePlayer" : False,

    "Hover" : False,
}

DICOLANGUE = {
    "Fr" : True,
    "En" : False,
    "Es" : False,
}

SOUND = {
    "BandeSon" : 0.5,
    "Dialogue" : 0.8,
    "EffetSonore" : 0.05,
}

KEYSBIND = {
    "up": None,
    "down": None,
    "left": None,
    "right": None,
    "skip": None,
    "inventory": None,
    "settings": None,
    "book": None,
    "sound": None,
    "action": None,
    "echap": None,
    "hideHotBar": None,
}

# texte : tout le texte
TEXTE = {
    "Dialogues" : None,
    "Elements" : None
}

# inventaires 
INVENTORY = {
    "Pickaxe" : 0,
    "OldAxe" : 0,
    "Showel" : 0,
    "Planks" : 0,
    "Boat" : 0,
    "Key" : 0,
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
    "PNJ5" : False, 
    "PNJ6" : False, 
    "PNJ7" : False,
}


# infos map tiers
EspacementPointRepereRiviere = 15
EspacementPointRepereRiviere2 = 7
CoupageMapRiviere = 50 # 1/3 de la longueur
CoupageMapRiviere2 = 75 # 1/3 de la longueur

CouloirRiviere = 4