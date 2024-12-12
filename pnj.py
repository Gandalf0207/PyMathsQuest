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
        self.interface = None

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
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e] and not self.openInterface:
                self.openInterface = True
                self.Interface = GestionInterfacePNJ(self)

            if keys[pygame.K_ESCAPE] and self.openInterface:
                self.openInterface = False
        else:
            self.openInterface = False

        if self.openInterface:
            self.Interface.Update()

class GestionInterfacePNJ(object):
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.displaySurface = pygame.display.get_surface()

        # Surface de l'interface de dialogue (transparent et couvrant tout l'écran)
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.interfaceSurface.set_alpha(200)  # Transparence de 220

        # Initialisation des polices
        self.font = pygame.font.Font(None, 36)

        # Position du PNJ
        self.pnj_position = (100, 100)  # Position du PNJ (à gauche)

        # Texte pour le PNJ
        self.pnj_text = "Bonjour, comment vas-tu ? Je suis très content de te voir ici ! Nous avons beaucoup à discuter, il y a plein de choses à faire ici !"

        # Variables pour l'effet de texte
        self.pnj_displayed_text = ""  # Texte affiché du PNJ
        self.pnj_index = 0  # Index pour le texte du PNJ

    def BuildInterface(self):
        # Ajouter progressivement les caractères
        if self.pnj_index < len(self.pnj_text):
            self.pnj_displayed_text += self.pnj_text[self.pnj_index]
            self.pnj_index += 1

        # Fonction simple pour découper le texte
        def wrap_text(text, font, max_width):
            words = text.split(' ')
            lines = []
            current_line = ''

            for word in words:
                test_line = f"{current_line} {word}".strip()
                if font.size(test_line)[0] <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word
            if current_line:
                lines.append(current_line)
            return lines

        # Largeur maximale de la boîte de texte
        max_width = 500
        wrapped_lines = wrap_text(self.pnj_displayed_text, self.font, max_width)

        # Affichage des lignes
        y_offset = 500  # Position Y de départ
        line_height = self.font.size("Tg")[1]  # Hauteur d'une ligne
        for i, line in enumerate(wrapped_lines):
            line_surface = self.font.render(line, True, (255, 255, 255))
            self.interfaceSurface.blit(line_surface, (200, y_offset + i * line_height))


    def CloseInterface(self):
        self.gestionnaire.openInterface = False

    def Update(self):
        # Mettre à jour l'interface
        self.interfaceSurface.fill((50, 50, 50))  # Fond gris de l'interface
        self.BuildInterface()  # Construire l'interface avec texte
        self.displaySurface.blit(self.interfaceSurface, (0, 0))  # Afficher l'interface
        
        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:  # Fermer avec ESC
            self.CloseInterface()


class DeplacementPNJ(object):
    def __init__(self):
        pass

    def GetPath(self):
        pass

    def Move(self):
        pass

    def Update(self):
        pass