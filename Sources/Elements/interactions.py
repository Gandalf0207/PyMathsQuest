from settings import *

class Interactions(object):

    def __init__(self, gestionnaire : any) -> None:
        """Méthode initialisation de la gestion avec les interactions (pont, rocher... ) sauf pnj
        Input : gestionanire (self parent)
        Output : None"""

        self.displaySurface = pygame.display.get_surface() # surface générale
        self.gestionnaire = gestionnaire
        self.player = None

        # element interactions
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


    def Interagir(self) -> None:
        """Méthode de calcul d'interaction entre chaque element en fonction des niveaux
        Input / Output : None"""

        if self.Isclose(): # si proximité

            # animation 
            self.gestionnaire.fondu_au_noir()

            # niveau 0
            if INFOS["Niveau"] == 0:

                # action si c'est un pont 
                if self.ObjectId == "pont1" or self.ObjectId == "pont2" :

                    if not self.Obj.InfoExo: # si c'est pas le pont d'exo

                        # text animation
                        self.gestionnaire.textScreen(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["TraverserPont"])

                        # deplacement player
                        if self.player.rect.x < self.coordObjActuel[0]:
                            self.player.rect.x += CASEMAP*2
                            STATE_HELP_INFOS[0] = "SeePNJ" # update tips player
                        else:
                            self.player.rect.x -= CASEMAP*2
                            STATE_HELP_INFOS[0] = "CrossBridge" # update tips player

                        self.player.hitbox_rect.center = self.player.rect.center
                        
                        # fin animation
                        self.gestionnaire.ouverture_du_noir(self.player.rect.center)

                    else: # si c'est le pont exo
                        INFOS["Exo"] = True # lancement exo dans main (changement variable)
                        self.gestionnaire.textScreen(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["MakeExo"]) # text animation
                    
                    
                    
                # si c'est le rocher qui est destructible
                elif self.ObjectId == "ExitRock":
                    self.gestionnaire.textScreen(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["BreakRock"]) # text 
                    self.Obj.kill() # destrcution rocher

                    self.gestionnaire.ouverture_du_noir(self.player.rect.center) # fin animation



    def Isclose(self) -> bool :
        """Méthode calcul de proximité entre le player et les obj interactions
        Input : None
        Ouput : bool"""

        for Object in self.interactionGroup: # parcours all obj 

            coordsObj = (Object.pos[0] + CASEMAP // 2, Object.pos[1] + CASEMAP // 2) # top left coords -> center coords
            playerPos = self.player.rect.center # center player
            

            # Calculer la distance entre le joueur et le PNJ
            distance = sqrt((playerPos[0] - coordsObj[0])**2 + (playerPos[1] - coordsObj[1])**2)
            
            self.camera_offset[0] = max(0, min(playerPos[0] - WINDOW_WIDTH // 2, self.map_width - WINDOW_WIDTH))
            self.camera_offset[1] = max(0, min(playerPos[1] - WINDOW_HEIGHT // 2, self.map_height - WINDOW_HEIGHT))

            # Limiter la caméra pour ne pas montrer le vide
            self.npc_screen_pos = [coordsObj[0]  - self.camera_offset[0], coordsObj[1] - self.camera_offset[1]]

 

            if distance <= self.distanceMax:

                # valeur importante de l'obj interactions
                self.Obj = Object
                self.coordObjActuel = Object.pos
                self.ObjectId = Object.id

                # Dessiner la boîte d'indication "Press E"
                text_surface = FONT["FONT24"].render(TEXTE["Elements"]["Interaction"], True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.topleft = (self.npc_screen_pos[0] - 20, self.npc_screen_pos[1] - 40)
                
                # Dessine le fond de la bulle
                bubble_rect = text_rect.inflate(20, 10)
                pygame.draw.rect(self.displaySurface, (0, 0, 0), bubble_rect)
                pygame.draw.rect(self.displaySurface, (255, 255, 255), bubble_rect, 2)
                
                # Affiche le texte
                self.displaySurface.blit(text_surface, text_rect)

                # element à proximité
                return True
            
        # pas d'element à proximité
        return False

    def Update(self, player : tuple, interactionGroup : any) -> None:
        """Méthode update de toutes les interaction possibles (hors pnj)
        Input : player pos : tuple
                interactionGroup : element pygame
        Output : None"""

        self.interactionGroup = interactionGroup # maj groupe
        self.player = player 
        self.Isclose() # affichage texte d'interaction si proximité
