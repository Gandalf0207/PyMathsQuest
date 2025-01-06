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

LONGUEUR = 150
LARGEUR = 75
CASEMAP = 128
CELL_SIZE = 2
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720 
COORS_BOX_ALL_SETTINGS = (WINDOW_WIDTH-436, WINDOW_HEIGHT-160)
COORDS_BOX_IDEAS_TIPS = (320, WINDOW_HEIGHT-160)

INFOS = {
    "Niveau" : 0,
    "Langue" : "Fr"
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