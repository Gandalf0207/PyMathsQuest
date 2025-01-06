from settings import *

class ConstruirePont(object):

    def __init__(self, gestionnnaire):
        self.gestionnaire = gestionnnaire

        self.riviere2 = self.LoadJsonMapValue("coordsMapBase", "Riviere2 Coords")
        self.map = self.LoadJsonMapValue("coordsMapBase", "AllMapInfo")

        self.posPossible = self.posPossibleBuild()
        self.construit = False
        self.distanceMax = 100
        self.npc_screen_pos = [0,0]

        self.camera_offset = [0,0]
        # infos de la map 
        self.map_width = LONGUEUR * CASEMAP
        self.map_height = LARGEUR * CASEMAP

        self.displaySurface = pygame.display.get_surface()

    def getConstructionStatue(self):
        return self.construit
    
    def posPossibleBuild(self):
        listCoordPossible = []
        for coords in self.riviere2:
            if self.map[coords[1]][coords[0]-1] == "-" and  self.map[coords[1]][coords[0]+1] == "-":
                listCoordPossible.append(coords) # adaptation coords map pygame
        return listCoordPossible


    def LoadJsonMapValue(self, index1 :str, index2 :str) -> list:
        """Récupération des valeur stockées dans le fichier json pour les renvoyer quand nécéssaire à l'aide des indices données pour les récupérer"""
        # récupération des valeurs stocké dans le json
        with open(join("Sources","Ressources","AllMapValue.json"), "r") as f: # ouvrir le fichier json en mode e lecture
            loadElementJson = json.load(f) # chargement des valeurs
        return loadElementJson[index1].get(index2, None) # on retourne les valeurs aux indices de liste quisont données

    def BuildBridge(self, allPont, loadMapElement, playerPos):

        if self.ConstructionPossible(playerPos) and  INVENTORY["Planks"] > 0:
            INVENTORY["Planks"] -=1

            self.gestionnaire.fondu_au_noir()
            self.gestionnaire.textScreen(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["BuildBridge"])


            coords = (self.coordsRiviere[0]*CASEMAP, self.coordsRiviere[1]*CASEMAP)
            loadMapElement.AddPont(allPont, "pont2", coords)
            self.construit = True

            self.gestionnaire.ouverture_du_noir(playerPos)

            self.gestionnaire.ideaTips.UpdateTexte()


        
    def ConstructionPossible(self, playerPos):

        # parcours de tout les coords possibles
        for coords in self.posPossible:
            
            
            # affection des valeurs 
            coordRiviere = coords


            # Calculer la distance entre le joueur et le PNJ
            distance = sqrt(( (coordRiviere[0] * CASEMAP + 64) - playerPos[0])**2 + ((coordRiviere[1] * CASEMAP + 64) - playerPos[1])**2)
            

            self.camera_offset[0] = max(0, min(playerPos[0] - WINDOW_WIDTH // 2, self.map_width - WINDOW_WIDTH))
            self.camera_offset[1] = max(0, min(playerPos[1] - WINDOW_HEIGHT // 2, self.map_height - WINDOW_HEIGHT))

            # Limiter la caméra pour ne pas montrer le vide
            self.npc_screen_pos = [coordRiviere[0] * CASEMAP - self.camera_offset[0], coordRiviere[1]*CASEMAP - self.camera_offset[1]]


            if distance <= self.distanceMax:

                square_color = (255, 0, 0)  # Rouge
                SQUARE_SIZE = 128
                square_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
                square_surface.fill(square_color)
                self.displaySurface.blit(square_surface, (coords[0]*CASEMAP, coords[1]*CASEMAP))
                
                # valeur importante du pnj à proximité
                self.coordsRiviere = coords

                # Dessiner la boîte d'indication "Press E"
                font = pygame.font.Font(None, 24)
                text_surface = font.render(TEXTE["Elements"]["Niveau0"]["CanBuildBridge"], True, (255, 255, 255))
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
        
            

    def Update(self, playerPos):
        self.ConstructionPossible(playerPos)




# à patch detection pos player riviere
# à patch creation pont"
# structure de detection