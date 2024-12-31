from settings import *

class Traverser(object):

    def __init__(self, gestionnaire):
        self.player = None
        self.allPont = None
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.gestionnaire = gestionnaire

        self.camera_offset = [0,0]
        self.distanceMax = 200

        # infos de la map 
        self.map_width = LONGUEUR * CASEMAP
        self.map_height = LARGEUR * CASEMAP

        # infos pont coords
        self.coordPontActuel = None


    def MakeTraverser(self):
        if self.Isclose():
            self.gestionnaire.fondu_au_noir()
            self.gestionnaire.textScreen("Vous venez de traverser le pont")

            if self.player.rect.x < self.coordPontActuel[0]:
                self.player.rect.x += CASEMAP*2
            else:
                self.player.rect.x -= CASEMAP*2

            self.player.hitbox_rect.center = self.player.rect.center


            self.gestionnaire.ouverture_du_noir(self.player.rect.center)



    def Isclose(self):
        for pontObject in self.allPont:
            coordsPont = pontObject.pos
            playerPos = self.player.rect.center
            

            # Calculer la distance entre le joueur et le PNJ
            distance = sqrt((playerPos[0] - coordsPont[0])**2 + (playerPos[1] - coordsPont[1])**2)
            
            self.camera_offset[0] = max(0, min(playerPos[0] - WINDOW_WIDTH // 2, self.map_width - WINDOW_WIDTH))
            self.camera_offset[1] = max(0, min(playerPos[1] - WINDOW_HEIGHT // 2, self.map_height - WINDOW_HEIGHT))

            # Limiter la caméra pour ne pas montrer le vide
            self.npc_screen_pos = [coordsPont[0]  - self.camera_offset[0], coordsPont[1] - self.camera_offset[1]]

 

            if distance <= self.distanceMax:
                # valeur importante du pnj à proximité
                self.pontObj = pontObject
                self.coordPontActuel = pontObject.pos

                # Dessiner la boîte d'indication "Press E"
                font = pygame.font.Font(None, 24)
                text_surface = font.render("Press M", True, (255, 255, 255))
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

    def Update(self, player, groupePont):
        self.player = player
        self.allPont = groupePont
        self.Isclose()
