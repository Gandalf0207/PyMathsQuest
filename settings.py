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


EspacementPointRepereRiviere = 15
CoupageMapRiviere = 50 # 1/3 de la longueur
CouloirRiviere = 4