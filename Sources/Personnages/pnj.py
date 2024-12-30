from settings import *
from ScriptAlgo.astar import *
from Sources.Elements.interface import *

class PNJ(pygame.sprite.Sprite):
    
    def __init__(self, pos : tuple, pathIMAGE : list,numpnj : str,  groups : any) -> None:
        """Méthode initialisation object pnj
        Input : pos : tuple, pathIMAGE : list, numpnj : str, groups : element pygame. Output : None"""

        # initialiation elements
        super().__init__(groups)
        self.numPNJ = numpnj
        self.pos = (pos[0] // CASEMAP, pos[1] // CASEMAP) # pos sur double list

        # images + hitbox
        self.image = pygame.image.load(join("Images","PNJ", pathIMAGE[0], pathIMAGE[1])).convert_alpha() 
        self.rect = self.image.get_frect(center = pos)        
        self.hitbox = self.rect.inflate(-60,0)
        # Centrer la hitbox par rapport à l'image
        self.hitbox.center = self.rect.center

        # bool de check  : double dialogues discussion
        self.discussion = False


class GestionPNJ(object):
    def __init__(self, displaySurface : any, niveau : int, allpnjGroup : any, INTERFACE_OPEN : bool, mapCollision : list) -> None:
        """Méthode initialisation gestion principal pnj : proche, interface discussion...
        Input : displaySurface / allpnGroupe : pygame element, niveau : int, INTERFACE_OPEN : bool (check all interface), mapCollision : list (check path cinématique)"""

        # Initialisation valeur de main
        self.displaySurface = displaySurface        
        self.allPNJ = allpnjGroup
        self.niveau = niveau
        self.INTERFACE_OPEN = INTERFACE_OPEN
        self.map = mapCollision # obstacle pour cinématique déplacement 

        # Initialisation value de base
        self.npc_screen_pos = [0,0]
        self.camera_offset = [0,0]
        self.distanceMax = 200

        # infos de la map 
        self.map_width = LONGUEUR * CASEMAP
        self.map_height = LARGEUR * CASEMAP

        # state interface de base
        self.openInterface = False
        
        # stockage des valeurs du pnj actuel
        self.pnjObj = None
        self.pnjActuel = None
        self.coordsPNJActuel = None
        self.interface = False
        
        # proximité pnj player
        self.check = False

        # infos cinématique
        self.cinematique = False
        self.cinematiqueObject = None

        # chagement dictionnaires des dialogues 
        self.allDialogues = self.loadAllDialogues()

    def LoadJsonMapValue(self, index1 :str, index2 :str) -> list:
        """Récupération des valeur stockées dans le fichier json pour les renvoyer quand nécéssaire à l'aide des indices données pour les récupérer"""
        # récupération des valeurs stocké dans le json
        with open(join("Sources","Ressources","AllMapValue.json"), "r") as f: # ouvrir le fichier json en mode e lecture
            loadElementJson = json.load(f) # chargement des valeurs
        return loadElementJson[index1].get(index2, None) # on retourne les valeurs aux indices de liste quisont données


    def CinematiqueBuild(self) -> None:
        """Méthode construction cinématique object. Lancement au prochain update.
        Input / Ouput : None"""

        self.cinematique = True
        
        if self.niveau ==0:
            goal = self.LoadJsonMapValue("coordsMapObject","ArbreSpecial Coords")
            pathAcces = ["-", "A", "P", "S"]

        
        self.cinematiqueObject = CinematiquePNJ(goal, self.pnjObj, self.map, pathAcces)

    def EndCinematique(self) -> None:
        """Met fin à la cinématique.
        Input / Output : None"""

        self.cinematique = False
        self.cinematiqueObject = None


    def Vu(self) -> None:
        """Méthode : modification état de discussion pnj (Principale -> Aternatif)
        Input / Output : None"""

        # modification de l'object pnj. Intermédiaire : class d'appel
        self.pnjObj.discussion = True


    def loadAllDialogues(self) -> None:
        """Méthode de chargement du dictionnaire des dialogues.
        Input / Output : None"""

        # ouverture fichier json
        with open(join("Sources", "Ressources","Dialogues.json"), 'r') as file:
            data = json.load(file)
            return data #retour du dictionnaire de données (dialogues)


    def isClose(self, playerPos : tuple) -> bool:
        """Méthode de vérification de proximité d'un pnj avec le joueur
        Input : tuple , Output : bool"""

        # parcours de tout les object pnj
        for pnjObject in self.allPNJ:
            
            # affection des valeurs relatives au pnj
            coordPNJ = pnjObject.pos 
            pnjActuel = pnjObject.numPNJ 

            # Calculer la distance entre le joueur et le PNJ
            distance = sqrt((playerPos[0] - coordPNJ[0] * CASEMAP)**2 + (playerPos[1] - coordPNJ[1] * CASEMAP)**2)
            
            self.camera_offset[0] = max(0, min(playerPos[0] - WINDOW_WIDTH // 2, self.map_width - WINDOW_WIDTH))
            self.camera_offset[1] = max(0, min(playerPos[1] - WINDOW_HEIGHT // 2, self.map_height - WINDOW_HEIGHT))

            # Limiter la caméra pour ne pas montrer le vide
            self.npc_screen_pos = [coordPNJ[0] * CASEMAP - self.camera_offset[0], coordPNJ[1]*CASEMAP - self.camera_offset[1]]

            if distance <= self.distanceMax:
                # valeur importante du pnj à proximité
                self.pnjObj = pnjObject
                self.pnjActuel = pnjActuel
                self.coordsPNJActuel = coordPNJ

                # Dessiner la boîte d'indication "Press E"
                font = pygame.font.Font(None, 24)
                text_surface = font.render("Press E", True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.topleft = (self.npc_screen_pos[0] - 20, self.npc_screen_pos[1] - 40)
                
                # Dessine le fond de la bulle
                bubble_rect = text_rect.inflate(20, 10)
                pygame.draw.rect(self.displaySurface, (0, 0, 0), bubble_rect)
                pygame.draw.rect(self.displaySurface, (255, 255, 255), bubble_rect, 2)
                
                # Affiche le texte
                self.displaySurface.blit(text_surface, text_rect)

                # pnj à proximité
                return True
            
            # pas de pnj à proximité
            return False
        

    def OpenInterfaceElementClavier(self, INTERFACE_OPEN : bool) -> bool:
        """Méthode ouverture / création / fermeture interface de discussion pnj par clavier
        Input : INTERFE_OPEN : bool (interface générale check); Output : bool"""

        self.INTERFACE_OPEN = INTERFACE_OPEN

        if not self.INTERFACE_OPEN: # sécurité
            self.openInterface = False 

        if self.check: # si pnj à proximité
            if not self.openInterface and not self.INTERFACE_OPEN: # aucun interfac ouvert
                # ouverture interface
                self.openInterface = True
                self.INTERFACE_OPEN = True
                self.Interface = PNJInterface(self)
        else:
            if self.openInterface: # si interface déjà ouvert
                # fermeture
                self.openInterface = False
                self.INTERFACE_OPEN = False

        # retour state interface global
        return self.INTERFACE_OPEN


    def update(self, playerPos : tuple, INTERFACE_OPEN : bool, event: any) -> bool:
        """Méthode d'update de l'interface d'appel de discussion + gestion pnj / proximité.
        Intput : playerPos : tuple, INTERFACE_OPEN : bool, event : element pygame. Output : bool"""

        self.INTERFACE_OPEN = INTERFACE_OPEN

        if not self.INTERFACE_OPEN: # sécurité
            self.openInterface = False 

        self.check = self.isClose(playerPos) # sécurité 2
        if not self.check: # si pas de proximité, fermeture de l'interface s'il est ouvert
            if self.openInterface:
                self.openInterface = False
                self.INTERFACE_OPEN = False 

        if self.openInterface: # update de l'interface s'il existe
            self.Interface.Update(event)

        # retour state interface global + etat cinématique
        return self.INTERFACE_OPEN, self.cinematique, self.cinematiqueObject






class CinematiquePNJ(object):
    def __init__(self, goal, pnjObject, mapCalcul, pathAccessible) -> None:
        # Initialisation des valeurs
        self.pnjObject = pnjObject
        self.pos = self.pnjObject.pos  # Position sur la double liste
        self.goal = (goal[0], goal[1])
        self.mapCalcul = mapCalcul
        self.pathAccessible = pathAccessible

        # Récupération des attributs graphiques du PNJ
        self.rect = self.pnjObject.rect  # Utiliser la hitbox comme référence principale
        self.hitbox = self.pnjObject.hitbox  # Synchroniser avec la hitbox du PNJ
        self.speed = 300

        # Calcul et définition du chemin
        self.GetPath()
        self.SetPath()

    def GetPath(self):
        """Calcul du chemin à l'aide de l'algorithme A*"""
        self.pathDeplacement = Astar(self.pos, self.goal, self.mapCalcul, self.pathAccessible).a_star()
        self.pathDeplacement = [(x * CASEMAP, y * CASEMAP) for x, y in self.pathDeplacement]  # Conversion en coordonnées pygame

    def SetPath(self):
        """Définit un nouveau chemin pour le PNJ"""
        if self.pathDeplacement:  # Vérifier que le chemin n'est pas vide
            self.pointSuivant = self.pathDeplacement.pop(0)  # Prendre le premier point comme cible
        else:
            self.pointSuivant = None  # Pas de chemin à suivre

    def ModifSpeed(self):
        nbPoint = len(self.pathDeplacement)
        if nbPoint > 30:
            while self.speed != 800:
                self.speed = self.speed + 1 if self.speed < 800 else self.speed - 1
        elif nbPoint > 15 :
            while self.speed != 500:
                self.speed = self.speed + 1 if self.speed < 500 else self.speed - 1
        else:
            while self.speed != 300:
                self.speed = self.speed + 1 if self.speed < 300 else self.speed - 1

    def Move(self, dt: int) -> None:
        """Déplace le PNJ vers le point cible selon les coordonnées données par la cinématique.
        Input : dt : int (delta time)
        Output : None
        """
        if self.pointSuivant:  # Vérifie si un point cible existe
            # Extraire les coordonnées cibles
            target_x, target_y = self.pointSuivant

            # Calcul des différences entre la position actuelle et la cible
            dx = target_x - self.hitbox.x
            dy = target_y - self.hitbox.y

            # Distance totale au point cible
            distance = sqrt(dx**2 + dy**2)

            if distance == 0:  # Si le PNJ est déjà sur la cible
                if self.pathDeplacement:  # Passer au point suivant si disponible
                    self.pointSuivant = self.pathDeplacement.pop(0)
                else:
                    self.pointSuivant = None  # Fin du chemin
                return

            # Si la distance restante est inférieure au déplacement possible
            if distance <= self.speed * dt:
                # Atteindre directement la cible
                self.hitbox.topleft = (target_x, target_y)
                self.rect.topleft = self.hitbox.topleft  # Synchroniser la rect
                if self.pathDeplacement:  # Passer au prochain point
                    self.pointSuivant = self.pathDeplacement.pop(0)
                else:
                    self.pointSuivant = None  # Fin du chemin
            else:
                # Calcul du déplacement proportionnel à la direction
                move_x = (self.speed * dt * dx) / distance
                move_y = (self.speed * dt * dy) / distance

                # Appliquer le déplacement
                self.hitbox.x += move_x
                self.hitbox.y += move_y
                self.rect.topleft = self.hitbox.topleft  # Synchroniser la rect

    def Replacement(self):
        """Replace le PNJ une case au-dessus de la position cible."""
        # Positionner le PNJ en fonction de l'objectif
        target_x, target_y = self.goal[0], self.goal[1] - 1  # Une case au-dessus

        # Ajuster les positions de la hitbox et du rectangle
        self.hitbox.center = (target_x * CASEMAP, target_y * CASEMAP)  # Position en pixels
        self.rect.center = self.hitbox.center  # Synchroniser la rect avec la hitbox

        # Mettre à jour la position logique de l'objet PNJ si nécessaire
        self.pnjObject.pos = (target_x, target_y)


    def Update(self, dt):
        self.ModifSpeed()
        self.Move(dt)
        if self.pathDeplacement != []:
            return True, False
        else:
            return False, True