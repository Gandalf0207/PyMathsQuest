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
                self.Interface = GestionInterfacePNJ(self)
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
        
    


class GestionInterfacePNJ(object):
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.displaySurface = pygame.display.get_surface()

        # Surface pour le fond transparent
        self.backgroundSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.backgroundSurface.fill((50, 50, 50, 200))  # Fond gris avec alpha (200)

        # Surface principale pour les éléments de l'interface
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.interfaceSurface.fill((0, 0, 0, 0))  # Transparent par défaut


        # Initialisation des polices
        self.font1 = pygame.font.Font(None, 36)
        self.font1.set_bold(True)

        self.font2 = pygame.font.Font(None, 36)

        # Position du PNJ
        self.pnj_position = (100, 100)  # Position du PNJ (à gauche)

        # Texte pour le PNJ
        self.pnj_text = None

        # Variables pour l'effet de texte
        self.pnj_displayed_text = ""  # Texte affiché du PNJ
        self.pnj_index = 0  # Index pour le texte du PNJ
        self.compteurDialogue = 1
        self.nombreDialogue = len(self.gestionnaire.allDialogues[f"Niveau{self.gestionnaire.niveau}"][self.gestionnaire.pnjActuel]["Principal"]) if not self.gestionnaire.pnjObj.discussion else len(self.gestionnaire.allDialogues[f"Niveau{self.gestionnaire.niveau}"][self.gestionnaire.pnjActuel]["Alternatif"])

        self.last_click_time = 0
        self.click_delay = 500    


        self.loadPNG()
        self.loadText()

    def loadText(self):
        self.pnj_displayed_text = ""
        self.pnj_index = 0

        print(self.gestionnaire.pnjObj.discussion, "on a blablaa")

        if not self.gestionnaire.pnjObj.discussion:
            if self.compteurDialogue <= self.nombreDialogue:
                self.pnj_text = self.gestionnaire.allDialogues[f"Niveau{self.gestionnaire.niveau}"][self.gestionnaire.pnjActuel]["Principal"][f"Dialogue{self.compteurDialogue}"]
                self.compteurDialogue += 1
                print(self.pnj_text)
            else:
                self.gestionnaire.Vu()
                self.CloseInterface()
        else:
            if self.compteurDialogue <= self.nombreDialogue:
                self.pnj_text = self.gestionnaire.allDialogues[f"Niveau{self.gestionnaire.niveau}"][self.gestionnaire.pnjActuel]["Alternatif"][f"Dialogue{self.compteurDialogue}"]
                self.compteurDialogue += 1
                print(self.pnj_text)
            else:
                self.CloseInterface()

    def loadPNG(self):
        self.pnjImage = pygame.image.load(join("Images", "PNJ", "Discussion", f"Grand{self.gestionnaire.pnjActuel}.png"))
        self.playerImage = pygame.image.load(join("Images", "Player", "Discussion", "GrandPlayer.png"))

    def BuildInterface(self):
        self.interfaceSurface.fill((0, 0, 0, 0))  # Réinitialiser la surface avec une transparence complète


        # load element png
        self.interfaceSurface.blit(self.pnjImage, (50,360))
        self.interfaceSurface.blit(self.playerImage, (WINDOW_WIDTH-178, 360))

        # load nom pnj
        match self.gestionnaire.pnjActuel:
            case "PNJ1":
                self.pnjName = "NameToDefined" 

        pnjName = self.font1.render(self.pnjName, True, (255,255,255))
        self.interfaceSurface.blit(pnjName, (200, 400))

        # load btn skip / lancer
        self.surfaceBtnSkip = pygame.Surface((100,50))
        self.btnRectSkip = pygame.Rect(750,600,100,50)
        self.surfaceBtnSkip.fill((255,255,255))
        self.textS = "Suivant"
        self.textSkip = self.font2.render(self.textS, True, (10,10,10))
        self.surfaceBtnSkip.blit(self.textSkip, (0,0))
        self.interfaceSurface.blit(self.surfaceBtnSkip, (self.btnRectSkip.x, self.btnRectSkip.y))

        # bloc gestion texte 
        if self.pnj_index < len(self.pnj_text):
            self.pnj_index += 1
        # Mettre à jour le texte affiché
        self.pnj_displayed_text = self.pnj_text[:self.pnj_index]


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
        wrapped_lines = wrap_text(self.pnj_displayed_text, self.font2, max_width)

        # Affichage des lignes
        y_offset = 420  # Position Y de départ
        line_height = self.font2.size("Tg")[1]  # Hauteur d'une ligne
        for i, line in enumerate(wrapped_lines):
            line_surface = self.font2.render(line, True, (255, 255, 255))
            self.interfaceSurface.blit(line_surface, (200, y_offset + i * line_height))

    def CloseInterface(self):
        self.gestionnaire.openInterface = False
        self.gestionnaire.INTERFACE_OPEN = False

    def Update(self, event):
        # Dessiner le fond transparent
        self.displaySurface.blit(self.backgroundSurface, (0, 0))

        # Construire et afficher l'interface avec le texte
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (0, 0))

        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:  # Fermer avec ESC
            self.CloseInterface()

        # Vérifie si l'événement est un clic de souris
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time

                # Vérifiez si le clic est dans le rectangle du bouton
                if self.btnRectSkip.collidepoint(event.pos):
                    self.loadText()
                    self.BuildInterface()








class DeplacementPNJ(object):
    def __init__(self):
        pass

    def GetPath(self):
        pass

    def Move(self):
        pass

    def Update(self):
        pass