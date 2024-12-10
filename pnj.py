from settings import *
from ScriptAlgo import astar

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

class GestionPNJ(object):
    def __init__(self, displaySurface, allpnj, niveau) -> None:
        self.coordsPNJList = [pnj.pos for pnj in allpnj]
        self.coordsPNJActuel = None
        self.displaySurface = displaySurface
        self.niveau = niveau
        self.distanceMax = 200
        self.map_width = LONGUEUR * CASEMAP
        self.map_height = LARGEUR * CASEMAP
        self.camera_offset = [0,0]
        self.npc_screen_pos = [0,0]
        self.openInterface = False

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e] and not self.openInterface:
            self.Interface = GestionInterfacePNJ(self)


    def isClose(self, playerPos):

        for coordPNJ in self.coordsPNJList:
            # Calculer la distance entre le joueur et le PNJ
            distance = sqrt((playerPos[0] - coordPNJ[0] * CASEMAP)**2 + (playerPos[1] - coordPNJ[1] * CASEMAP)**2)
            
            self.camera_offset[0] = max(0, min(playerPos[0] - WINDOW_WIDTH // 2, self.map_width - WINDOW_WIDTH))
            self.camera_offset[1] = max(0, min(playerPos[1] - WINDOW_HEIGHT // 2, self.map_height - WINDOW_HEIGHT))

            # Limiter la caméra pour ne pas montrer le vide
            self.npc_screen_pos = [coordPNJ[0] * CASEMAP - self.camera_offset[0], coordPNJ[1]*CASEMAP - self.camera_offset[1]]

            if distance <= self.distanceMax:
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

    def update(self, playerPos):
        check = self.isClose(playerPos)
        if check: 
            self.input()
        if self.openInterface:
            self.Interface.Update()


class GestionInterfacePNJ(object):
    def __init__(self, gestionnaire):
        print("bonjour")
        self.gestionnaire = gestionnaire

    def GetText(self):
        pass

    def OpenInterface(self):
        pass

    def CloseInterface(self):
        self.gestionnaire.openInterface = False

    def Update(self):
        pass

class DeplacementPNJ(object):
    def __init__(self):
        pass

    def GetPath(self):
        pass

    def Move(self):
        pass

    def Update(self):
        pass