from settings import *
from ScriptAlgo import astar
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
    def __init__(self, displaySurface : any, niveau : int, allpnjGroup : any, INTERFACE_OPEN : bool) -> None:
        """Méthode initialisation gestion principal pnj : proche, interface discussion...
        Input : displaySurface / allpnGroupe : pygame element, niveau : int, INTERFACE_OPEN : bool (check all interface)"""

        # Initialisation valeur de main
        self.displaySurface = displaySurface        
        self.allPNJ = allpnjGroup
        self.niveau = niveau
        self.INTERFACE_OPEN = INTERFACE_OPEN

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

        # chagement dictionnaires des dialogues 
        self.allDialogues = self.loadAllDialogues()
    

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

        # retour state interface global
        return self.INTERFACE_OPEN
        

class DeplacementPNJ(object):
    def __init__(self):
        pass

    def GetPath(self):
        pass

    def Move(self):
        pass

    def Update(self):
        pass