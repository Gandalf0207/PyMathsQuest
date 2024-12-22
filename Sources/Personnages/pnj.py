from settings import *
from ScriptAlgo import astar
from Sources.Elements.interface import *

class PNJ(pygame.sprite.Sprite):
    def __init__(self, pos, pathIMAGE,numpnj,  groups) -> None:
        super().__init__(groups)
        self.numPNJ = numpnj
        self.pos = (pos[0] // CASEMAP, pos[1] // CASEMAP) # pos sur double list
        print(self.pos)
        self.image = pygame.image.load(join("Images","PNJ", pathIMAGE[0], pathIMAGE[1])).convert_alpha() 
        self.rect = self.image.get_frect(center = pos)
        
        self.hitbox = self.rect.inflate(-60,0)
 
        # Centrer la hitbox par rapport à l'image
        self.hitbox.center = self.rect.center

        self.discussion = False

class GestionPNJ(object):
    def __init__(self, displaySurface, niveau, allpnjGroup, INTERFACE_OPEN) -> None:
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

        self.check = False

        self.allDialogues = self.loadAllDialogues()
    
    def Vu(self):
        self.pnjObj.discussion = True

    def loadAllDialogues(self):
        with open("Dialogues.json", 'r') as file:
            data = json.load(file)
            return data

    def isClose(self, playerPos):

        for pnjObject in self.allPNJ:
            coordPNJ = pnjObject.pos
            pnjActuel = pnjObject.numPNJ 

            # Calculer la distance entre le joueur et le PNJ
            distance = sqrt((playerPos[0] - coordPNJ[0] * CASEMAP)**2 + (playerPos[1] - coordPNJ[1] * CASEMAP)**2)
            
            self.camera_offset[0] = max(0, min(playerPos[0] - WINDOW_WIDTH // 2, self.map_width - WINDOW_WIDTH))
            self.camera_offset[1] = max(0, min(playerPos[1] - WINDOW_HEIGHT // 2, self.map_height - WINDOW_HEIGHT))

            # Limiter la caméra pour ne pas montrer le vide
            self.npc_screen_pos = [coordPNJ[0] * CASEMAP - self.camera_offset[0], coordPNJ[1]*CASEMAP - self.camera_offset[1]]

            if distance <= self.distanceMax:
                self.pnjObj = pnjObject
                self.pnjActuel = pnjActuel
                self.coordsPNJActuel = coordPNJ
                # Dessiner la boîte
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
                return True
            return False
        
    def OpenInterfaceElementClavier(self, event, INTERFACE_OPEN):
        self.INTERFACE_OPEN = INTERFACE_OPEN

        if not self.INTERFACE_OPEN: # sécurité
            self.openInterface = False 

        if self.check:
            if not self.openInterface and not self.INTERFACE_OPEN:
                self.openInterface = True
                self.INTERFACE_OPEN = True
                self.Interface = PNJInterface(self)
        else:
            if self.openInterface:
                self.openInterface = False
                self.INTERFACE_OPEN = False

        return self.INTERFACE_OPEN

    def update(self, playerPos, INTERFACE_OPEN, event):
        self.INTERFACE_OPEN = INTERFACE_OPEN

        if not self.INTERFACE_OPEN: # sécurité
            self.openInterface = False 

        self.check = self.isClose(playerPos)
        if not self.check:
            if self.openInterface:
                self.openInterface = False
                self.INTERFACE_OPEN = False 

        if self.openInterface:
            self.Interface.Update(event)


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