from settings import *

class PNJ(pygame.sprite.Sprite):
    def __init__(self, pos, pathIMAGE, groups) -> None:
        super().__init__(groups)
        self.image = pygame.image.load(join("Images","PNJ", pathIMAGE[0], pathIMAGE[1])).convert_alpha() 
        self.rect = self.image.get_frect(center = pos)
        
        self.hitbox = self.rect.inflate(-60,0)
 
        # Centrer la hitbox par rapport à l'image
        self.hitbox.center = self.rect.center

class GestionPNJ(object):
    def __init__(self, displaySurface) -> None:
        self.coordsPNJList = self.LoadJsonMapValue("coordsMapObject","PNJ Coords")
        self.displaySurface = displaySurface
        self.distanceMax = 200
        self.map_width = LONGUEUR * CASEMAP
        self.map_height = LARGEUR * CASEMAP
        self.camera_offset = [0,0]
        self.npc_screen_pos = [0,0]


    def isClose(self, playerPos):



        for coordPNJ in self.coordsPNJList:
            # Calculer la distance entre le joueur et le PNJ
            distance = sqrt((playerPos[0] - coordPNJ[0] * CASEMAP)**2 + (playerPos[1] - coordPNJ[1] * CASEMAP)**2)
            
            self.camera_offset[0] = max(0, min(playerPos[0] - WINDOW_WIDTH // 2, self.map_width - WINDOW_WIDTH))
            self.camera_offset[1] = max(0, min(playerPos[1] - WINDOW_HEIGHT // 2, self.map_height - WINDOW_HEIGHT))

            # Limiter la caméra pour ne pas montrer le vide
            self.npc_screen_pos = [coordPNJ[0] * CASEMAP - self.camera_offset[0], coordPNJ[1]*CASEMAP - self.camera_offset[1]]

            if distance <= self.distanceMax:
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






    def LoadJsonMapValue(self, index1 :str, index2 :str) -> list:
        """Récupération des valeur stockées dans le fichier json pour les renvoyer quand nécéssaire à l'aide des indices données pour les récupérer"""
        
        with open("AllMapValue.json", "r") as f: # ouvrir le fichier json en mode e lecture
            loadElementJson = json.load(f) # chargement des valeurs
        return loadElementJson[index1].get(index2, None) # on retourne les valeurs aux indices de liste quisont données
