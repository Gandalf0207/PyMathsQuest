from settings import *

class Construire(object):

    def __init__(self, gestionnnaire : any) -> None:
        """Méthode initialisation des valeurs de la class de constrution de pont
        Input : gestionnaire (self)
        Output : /"""

        # gestionnaire (self parent)
        self.gestionnaire = gestionnnaire
        self.map = LoadJsonMapValue("coordsMapBase", "AllMapInfo")

        if INFOS["Niveau"] == 0:
            riviere = LoadJsonMapValue("coordsMapBase", "Riviere2 Coords")
        elif INFOS["Niveau"] == 1:
            riviere = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")

            river2 = LoadJsonMapValue("coordsMapBase", "Riviere2 Coords")
            river3 = LoadJsonMapValue("coordsMapBase", "Riviere3 Coords")
            allCoordsRiver123 = riviere + river2 + river3
            self.allPosPossibleBoat = self.posPossibleBuild(allCoordsRiver123)


        self.posPossiblePont = self.posPossibleBuild(riviere) # case construction possible
        self.construitPont = False # étant de la construit 
        self.placeBoat = False
        self.distanceMax = 100 # diqstance minimal pour interaction
        
        # outils 
        self.npc_screen_pos = [0,0]
        self.camera_offset = [0,0]
        # infos de la map 
        self.map_width = LONGUEUR * CASEMAP
        self.map_height = LARGEUR * CASEMAP

        # surface global
        self.displaySurface = pygame.display.get_surface()

    def getConstructionStatuePont(self) -> bool:
        """Méthode get statue pour verif main
        Input / Ouput : /"""

        return self.construitPont # etat
    
    def getPlaceStatueBoat(self) -> bool:
        """Méthode get statue pour verif main
        Input / Ouput : /"""

        return self.placeBoat # etat
    
    def posPossibleBuild(self, listCoords) -> list:
        """Métode déterminant la liste des coordonnées possible pour poser le pont
        Input : / 
        Ouput : list"""

        listCoordPossible = [] # initialisation
        for coords in listCoords: # parcours de chaque case de la rivière
            if INFOS["Niveau"] == 0:
                if self.map[coords[1]][coords[0]-1] == "-" and  self.map[coords[1]][coords[0]+1] == "-":  # vérif devant et dérierre
                    listCoordPossible.append(coords)

            elif INFOS["Niveau"] == 1:
                if self.map[coords[1]][coords[0]-1] == "-" and  self.map[coords[1]][coords[0]+1] == "-" and coords[1] > 35:  # vérif devant et derriere + hauteur 
                    listCoordPossible.append(coords)

        return listCoordPossible 


    def BuildBridge(self, loadMapElement : any, playerPos : tuple) -> None:
        """Méthode construction du pont si la construction et possible 
        Input : object pour créer le pont sur la map
                pos player (animation utilistion)
        Output : None"""

        # si construction possible et planches dans l'inventaire
        if self.ConstructionPossible(playerPos, self.posPossiblePont) and  INVENTORY["Planks"] > 0:
            INVENTORY["Planks"] -=1 # -1 aux planches

            # animation + texte
            self.gestionnaire.fondu_au_noir()
            self.gestionnaire.textScreen(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["BuildBridge"])

            # ajout du pont + mise à jour de l'état de construction 
            coords = (self.coordsRiviere[0]*CASEMAP, self.coordsRiviere[1]*CASEMAP)
            loadMapElement.AddPont("pont2", coords)
            self.construitPont = True

            # ainimation
            self.gestionnaire.ouverture_du_noir(playerPos)

            # texte tips suivant
            STATE_HELP_INFOS[0] = "CrossBridge"

    def PlaceBoat(self, loadMapElement : any, playerPos : tuple) -> None:
        # si  bateau dans l'inventaire et riviere autour
        if self.ConstructionPossible(playerPos, self.allPosPossibleBoat) and  INVENTORY["Boat"] > 0:
            INVENTORY["Boat"] -=1 # -1 aux planches

            # animation + texte
            self.gestionnaire.fondu_au_noir()
            self.gestionnaire.textScreen(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["PlaceBoat"])

            # ajout du pont + mise à jour de l'état de construction 
            coords = (self.coordsRiviere[0]*CASEMAP, self.coordsRiviere[1]*CASEMAP)
            loadMapElement.AddBoat("Boat", coords)
            self.placeBoat = True

            # ainimation
            self.gestionnaire.ouverture_du_noir(playerPos)

            # texte tips suivant
            STATE_HELP_INFOS[0] = "NavigateBoat"


        
    def ConstructionPossible(self, playerPos : tuple, listCoords) -> bool:
        """Méthode de check si la construction est possible autour de la rivière pour les cases autour du player
        Input : playerpos : tuple
        Ouput : bool """

        # parcours de tout les coords possibles
        for coords in listCoords:
            
            # affection des valeurs 
            coordRiviere = coords

            # Calculer la distance entre le joueur et le PNJ
            distance = sqrt(( (coordRiviere[0] * CASEMAP + 64) - playerPos[0])**2 + ((coordRiviere[1] * CASEMAP + 64) - playerPos[1])**2)

            self.camera_offset[0] = max(0, min(playerPos[0] - WINDOW_WIDTH // 2, self.map_width - WINDOW_WIDTH))
            self.camera_offset[1] = max(0, min(playerPos[1] - WINDOW_HEIGHT // 2, self.map_height - WINDOW_HEIGHT))

            # Limiter la caméra pour ne pas montrer le vide
            self.npc_screen_pos = [coordRiviere[0] * CASEMAP - self.camera_offset[0], coordRiviere[1]*CASEMAP - self.camera_offset[1]]


            if distance <= self.distanceMax:
                
                # coords case rivière
                self.coordsRiviere = coords

                # Dessiner la boîte d'indication "Press E"
                text_surface = FONT["FONT24"].render(TEXTE["Elements"]["Niveau0"]["CanBuildBridge"], True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.topleft = (self.npc_screen_pos[0] - 20, self.npc_screen_pos[1] - 40)
                
                # Dessine le fond de la bulle
                bubble_rect = text_rect.inflate(20, 10)
                pygame.draw.rect(self.displaySurface, (0, 0, 0), bubble_rect)
                pygame.draw.rect(self.displaySurface, (255, 255, 255), bubble_rect, 2)
                
                # Affiche le texte
                self.displaySurface.blit(text_surface, text_rect)

                # possibilité
                return True
            
        # pas de possibilité
        return False
        
            
    def Update(self, playerPos : tuple) -> None:
        """Méthode update pour afficher texte de possibilité de construction 
        Input : tuple (player pos)
        Output : None"""
        if INVENTORY["Planks"] > 0 and not self.construitPont:
            self.ConstructionPossible(playerPos, self.posPossiblePont)
        if INVENTORY["Boat"] > 0 and not self.placeBoat:
            self.ConstructionPossible(playerPos, self.allPosPossibleBoat)




# à patch detection pos player riviere
# à patch creation pont"
# structure de detection