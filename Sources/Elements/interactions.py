from settings import *

class Interactions(object):

    def __init__(self, gestionnaire):

        self.player = None
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.gestionnaire = gestionnaire

        self.camera_offset = [0,0]
        self.npc_screen_pos = [0,0]

        self.distanceMax = 100 # depuis centre element pont

        # infos de la map 
        self.map_width = LONGUEUR * CASEMAP
        self.map_height = LARGEUR * CASEMAP

        # infos pont coords
        self.Obj = None
        self.coordObjActuel = None
        self.ObjectId = None

        self.interactionGroup = None


    def MakeTraverser(self):
        if self.Isclose():
            self.gestionnaire.fondu_au_noir()

            if INFOS["Niveau"] == 0:

                # action si c'est un pont
                if self.ObjectId == "pont1" or self.ObjectId == "pont2" :
                    if not self.Obj.InfoExo or INFOS["ExoPasse"]:
                        
                        # on change l'etat du bloc car l'exo est réussit
                        if INFOS["ExoPasse"]:
                            self.Obj.InfoExo = False
                            INFOS["ExoPasse"] = False
                            INFOS["Exo"] = False
                            INFOS["ChangementNiveau"] = True


                        self.gestionnaire.textScreen(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["TraverserPont"])

                        if self.player.rect.x < self.coordObjActuel[0]:
                            self.player.rect.x += CASEMAP*2
                            STATE_HELP_INFOS[0] = "SeePNJ"
                        else:
                            self.player.rect.x -= CASEMAP*2
                            STATE_HELP_INFOS[0] = "CrossBridge"

                        self.player.hitbox_rect.center = self.player.rect.center
                        
                        self.gestionnaire.ouverture_du_noir(self.player.rect.center)

                    else:
                        INFOS["Exo"] = True
                        self.gestionnaire.textScreen(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["MakeExo"])
                    
                    
                    
                # action si c'est le rocher de fin
                elif self.ObjectId == "ExitRock":
                    self.gestionnaire.textScreen(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["BreakRock"])
                    self.Obj.kill()

                    self.gestionnaire.ouverture_du_noir(self.player.rect.center)





    def Isclose(self):
        for Object in self.interactionGroup:
            coordsObj = (Object.pos[0] + CASEMAP // 2, Object.pos[1] + CASEMAP // 2) # top left coords -> center coords
            playerPos = self.player.rect.center # center player
            

            # Calculer la distance entre le joueur et le PNJ
            distance = sqrt((playerPos[0] - coordsObj[0])**2 + (playerPos[1] - coordsObj[1])**2)
            
            self.camera_offset[0] = max(0, min(playerPos[0] - WINDOW_WIDTH // 2, self.map_width - WINDOW_WIDTH))
            self.camera_offset[1] = max(0, min(playerPos[1] - WINDOW_HEIGHT // 2, self.map_height - WINDOW_HEIGHT))

            # Limiter la caméra pour ne pas montrer le vide
            self.npc_screen_pos = [coordsObj[0]  - self.camera_offset[0], coordsObj[1] - self.camera_offset[1]]

 

            if distance <= self.distanceMax:

                # valeur importante du pnj à proximité
                self.Obj = Object
                self.coordObjActuel = Object.pos
                self.ObjectId = Object.id

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

    def Update(self, player, interactionGroup):
        self.interactionGroup = interactionGroup
        self.player = player
        self.Isclose()
