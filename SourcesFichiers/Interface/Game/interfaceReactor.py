from settings import * 
from SourcesFichiers.Elements.sprites import *

class ReactorInterface(object):

    def __init__(self, gestionnaire) ->None:
        """Méthode initialisation de l'interface de book.
        Input : gestionnaire = self méthode d'appel"""
           
        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale

        self.gestionnaire = gestionnaire

        # Surface pour le fond transparent
        self.backgroundSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.backgroundSurface.fill((50, 50, 50, 200))  # Fond gris avec alpha (200)

        # Surface principale pour les éléments de l'interface
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH /2, WINDOW_HEIGHT / 2), pygame.SRCALPHA)
        self.interfaceSurface.fill((0, 0, 0, 0))  # Transparent par défaut


        # timer auto update   
        self.last_lower_time = pygame.time.get_ticks()  # Temps de la dernière baisse de température
        self.lower_interval = 1000  # Intervalle de secondes
        self.clicks = 0

        # timer click btn delays
        self.last_click_time = 0
        self.click_delay = 500    

        # close interface cross
        self.surfaceCloseCross = pygame.Surface((24,24))
        self.isCrossCloseHover = False
        self.crossClose = pygame.image.load(join("Image","Interface", "Croix", "x-mark.png")).convert_alpha()
        self.crossClose2 = pygame.image.load(join("Image","Interface", "Croix", "x-mark2.png")).convert_alpha()



        self.reactor = Reactor()
        self.surfaceReactor = self.reactor.Update()
        self.surfaceReactor = self.reactor.Update()

    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill("#000000")
        text = FONT["FONT36"].render(TEXTE["Elements"]["InterfaceReactor"]["Title"], True, (255,255,255))
        self.interfaceSurface.blit(text, (10,10))

        # heure 
        current_time = time.strftime("%H:%M:%S")
        time_text = FONT["FONT24"].render(f"{TEXTE["Elements"]["InterfaceReactor"]["Heure"]} : {current_time}", True, WHITE)
        self.interfaceSurface.blit(time_text, (425, 50))

        # etat réacteur
        if self.clicks == 0 :
            etats = f"{TEXTE["Elements"]["InterfaceReactor"]["EtatName"]} : {TEXTE["Elements"]["InterfaceReactor"]["Etat"]["Inactif"]}"
            colorE = (132, 148, 129)
        else:
            etats = f"{TEXTE["Elements"]["InterfaceReactor"]["EtatName"]} : {TEXTE["Elements"]["InterfaceReactor"]["Etat"]["Actif"]}"
            colorE = (53, 153, 34)
        etat_text = FONT["FONT24"].render(etats, True, colorE)
        self.interfaceSurface.blit(etat_text, (425, 75))

        # statue reacteur     
        temp = self.reactor.calculate_total_temperature() 
        status = f"{TEXTE["Elements"]["InterfaceReactor"]["StatueName"]} : {TEXTE["Elements"]["InterfaceReactor"]["Statue"]["Null"]}"
        colorS = WHITE
        if temp < 500 :
            status = f"{TEXTE["Elements"]["InterfaceReactor"]["StatueName"]} : {TEXTE["Elements"]["InterfaceReactor"]["Statue"]["Normal"]}"
            colorS = WHITE
        elif temp < 800 :
            status = f"{TEXTE["Elements"]["InterfaceReactor"]["StatueName"]} : {TEXTE["Elements"]["InterfaceReactor"]["Statue"]["Instable"]}"
            colorS = ORANGE
        else :
            status = f"{TEXTE["Elements"]["InterfaceReactor"]["StatueName"]} : {TEXTE["Elements"]["InterfaceReactor"]["Statue"]["Critique"]}"
            colorS = RED
        text_status = FONT["FONT24"].render(status, True, colorS)
        self.interfaceSurface.blit(text_status, (425, 100))

        # temperature
        temp_text = FONT["FONT24"].render(f"{TEXTE["Elements"]["InterfaceReactor"]["Temperature"]} : {temp:.2f} °C", True, WHITE)
        self.interfaceSurface.blit(temp_text, (425, 125))


        # button puissance
        self.surfaceBtnPuissance = pygame.Surface((150,50))
        self.btnRectPuissance = pygame.Rect(425, 175, 150, 50)
        self.surfaceBtnPuissance.fill(RED)
        self.textS = TEXTE["Elements"]["InterfaceReactor"]["AddPuissance"]
        self.textSkip = FONT["FONT20"].render(self.textS, True, (10,10,10))
        self.surfaceBtnPuissance.blit(self.textSkip, (0,0))
        self.interfaceSurface.blit(self.surfaceBtnPuissance, (self.btnRectPuissance.x, self.btnRectPuissance.y))

        # close element
        self.surfaceCloseCross.fill("#ffffff")
        self.rectCloseCross = pygame.Rect(self.interfaceSurface.get_width() - 34, 10, 24, 24)
        if self.isCrossCloseHover:
            self.surfaceCloseCross.blit(self.crossClose2, (0,0))
        else:
            self.surfaceCloseCross.blit(self.crossClose, (0,0))
        self.interfaceSurface.blit(self.surfaceCloseCross, (self.rectCloseCross.x, self.rectCloseCross.y))





    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()
        
        # crash jeu 
        if self.clicks > 10:
            INFOS["CrashGame"] = True

        if self.clicks == 1:
            STATE_HELP_INFOS[0] = "SeePNJ"
            INFOS["ReactorOn"] = True
            # changer toutes les portes : ouvrir 
            allCollisionSprites = self.gestionnaire.gestionnaire.collisionSprites
            allSprites = self.gestionnaire.gestionnaire.allSprites
            for sprite in allCollisionSprites:
                if sprite.id == "DoorFuturisteClose":
                    pos = sprite.pos
                    sprite.kill()
                    OpenDoor = pygame.image.load(join("Image", "Obstacle", "Door", "DoorFuturisteBaseOpen.png")).convert_alpha()
                    Sprites(pos, OpenDoor, "DoorFuturisteOpen", allSprites, layer=1)


        if event.type == pygame.MOUSEBUTTONDOWN:  # Si un clic souris est détecté
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time

                local_pos = GetLocalPos(event, self.interfaceSurface, (320, 180))
                if local_pos:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.btnRectPuissance.collidepoint(local_pos):
                            self.surfaceReactor = self.reactor.Update()
                            self.clicks += 1

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.rectCloseCross.collidepoint(local_pos):
                            # fermeture interface
                            self.gestionnaire.CloseAllInterface()
        if event.type == pygame.MOUSEMOTION:
            local_pos = GetLocalPos(event, self.interfaceSurface, (320, 180))
            if local_pos:
                # cross close interface
                self.isCrossCloseHover = self.rectCloseCross.collidepoint(local_pos)


        # Baisser la température toutes les secondes
        current_time = pygame.time.get_ticks()
        if current_time - self.last_lower_time >= self.lower_interval:
            self.reactor.UpdateAuto()
            self.last_lower_time = current_time 
                

        self.interfaceSurface.blit(self.surfaceReactor, (10, 30))

        self.displaySurface.blit(self.backgroundSurface, (0,0))
        self.displaySurface.blit(self.interfaceSurface, (320,180)) # pos topleft







class Reactor(object):
    def __init__(self):
        # Surface du reactor
        self.surfaceRecactorStatue = pygame.Surface((550, 400), pygame.SRCALPHA)
        self.surfaceRecactorStatue.fill((255,255,255,0))  

        self.hex_radius = 10  # Rayon de chaque petit hexagone
        self.hexagons = self.draw_large_hexagon()

        self.last_temperature_stage = 0

        self.colorTemp =  {
            BLUE: 1,
            CYAN: 2,
            GREEN: 3,
            YELLOW: 4,
            ORANGE: 5,
            RED: 6
        }

    # Fonction pour dessiner un grand hexagone composé de petits hexagones
    def draw_large_hexagon(self):
        # Le grand hexagone sera composé de 5 lignes avec le nombre d'hexagones suivant : 3, 4, 5, 4, 3
        hex_width = 2 * self.hex_radius# Largeur de l'hexagone
        hex_height = int(1.5 * self.hex_radius) +4  # Hauteur avec chevauchement vertical

        nbColonneHEXAGONE = [1, 4, 7, 10, 13, 12, 13, 12, 13, 12, 13, 12, 13, 10, 7, 4, 1]
        posStartY = [6 * hex_height, 4.5 * hex_height, 3 * hex_height, 1.5 * hex_height, 0, 0.5 * hex_height,
                    0, 0.5 * hex_height, 0, 0.5 * hex_height, 0, 0.5 * hex_height, 0, 1.5 * hex_height, 3 * hex_height,
                    4.5 * hex_height, 6 * hex_height]

        XDepart = 50

        hexagons = []  # Liste pour enregistrer tous les hexagones

        # Correction du calcul des positions x et y
        for row_idx, colonne in enumerate(nbColonneHEXAGONE):
            for nbExa in range(colonne):
                # Calcul des offsets pour chaque hexagone
                offset_x = row_idx * hex_width  # Décalage horizontal pour chaque hexagone
                offset_y = hex_height * (nbExa + 1) # Décalage vertical basé sur l'index de ligne

                # Position de chaque hexagone par rapport au point haut-gauche
                x = XDepart + offset_x
                y = posStartY[row_idx] + offset_y # Utilisation de posStartY pour ajuster la position Y

                # Créer un hexagone et l'ajouter à la liste
                hexagons.append(Hexagon(x, y, self.hex_radius))

        return hexagons
    
    # Fonction pour déterminer la couleur de l'hexagone en fonction du stade de la température
    def get_color_for_temperature(self, temperature_stage):
        """Retourne la couleur associée à un certain stade de température."""
        if temperature_stage <= 1:
            return BLUE
        elif temperature_stage <= 2:
            return CYAN
        elif temperature_stage <= 3:
            return GREEN
        elif temperature_stage <= 4:
            return YELLOW
        elif temperature_stage <= 5:
            return ORANGE
        else:
            return RED

    # Fonction pour gérer l'activation des hexagones
    def activate_hexagons(self, hexagons, num_activated):
        """Active un certain nombre d'hexagones au hasard et leur attribue une couleur en fonction de la température."""
        try :
            activated = random.sample(hexagons, num_activated)  # Sélectionner au hasard les hexagones à activer
            for hexagon in activated:
                hexagon.color = self.get_color_for_temperature(hexagon.temp)  # Changer la couleur en fonction de la température
                if hexagon.color != RED:
                    hexagon.temp += 1
        except:
            pass


    def calculate_total_temperature(self, ):
        total_temperature = 0
        for hexagon in self.hexagons:
            weight = self.colorTemp.get(hexagon.color, 0)
            total_temperature += weight
        return total_temperature

    def draw_temperature_gauge(self, temperature, max_temperature):
        gauge_x = 10
        gauge_y = 10
        gauge_width = 30
        gauge_height = 275
        pygame.draw.rect(self.surfaceRecactorStatue, BLACK, (gauge_x, gauge_y, gauge_width, gauge_height))


        fill_height = int((temperature / max_temperature) * gauge_height)

        if temperature <= max_temperature * 0.2:
            gauge_color = BLUE
        elif temperature <= max_temperature * 0.4:
            gauge_color = CYAN
        elif temperature <= max_temperature * 0.6:
            gauge_color = GREEN
        elif temperature <= max_temperature * 0.8:
            gauge_color = YELLOW
        elif temperature <= max_temperature * 0.9:
            gauge_color = ORANGE
        else:
            gauge_color = RED

        pygame.draw.rect(self.surfaceRecactorStatue, WHITE, (gauge_x, gauge_y, gauge_width, gauge_height), 2)
        pygame.draw.rect(self.surfaceRecactorStatue, gauge_color, (gauge_x, gauge_y + gauge_height - fill_height, gauge_width, fill_height))


    def Update(self):
        # Calculer combien d'hexagones activer et quel est le stade de température
        num_to_activate = int(len(self.hexagons) * (random.randint(2,5) / 10))  # Calculer combien d'hexagones activer
        self.activate_hexagons(self.hexagons, num_to_activate)

        # Dessiner tous les hexagones
        for hexagon in self.hexagons:
            hexagon.draw(self.surfaceRecactorStatue)

        total_temperature = self.calculate_total_temperature()
        self.draw_temperature_gauge(total_temperature, max_temperature=len(self.hexagons) * 6)

        return self.surfaceRecactorStatue

    def UpdateAuto(self):

        num_to_deactivate = int(len(self.hexagons) * (random.randint(1,5) / 200))  # Calculer combien d'hexagones activer

        try :
            deactivated = random.sample(self.hexagons, num_to_deactivate)  # Sélectionner au hasard les hexagones à activer
            for hexagon in deactivated:
                if hexagon.color == RED:
                    hexagon.temp -= 1
                    hexagon.color = ORANGE
                elif hexagon.color == ORANGE:
                    hexagon.temp -= 1
                    hexagon.color = YELLOW
                elif hexagon.color == YELLOW:
                    hexagon.temp -= 1
                    hexagon.color = GREEN
                elif hexagon.color == GREEN:
                    hexagon.temp -= 1
                    hexagon.color = CYAN
                elif hexagon.color == CYAN:
                    hexagon.temp -= 1
                    hexagon.color = BLUE
        except:
            pass
        # Dessiner tous les hexagones
        for hexagon in self.hexagons:
            hexagon.draw(self.surfaceRecactorStatue)

        total_temperature = self.calculate_total_temperature()
        self.draw_temperature_gauge(total_temperature, max_temperature=len(self.hexagons) * 6)

        return self.surfaceRecactorStatue

# Classe pour représenter un hexagone
class Hexagon:
    def __init__(self, x, y, radius, color=BLUE):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.temp = 0

    def draw(self, surface):
        """Dessiner l'hexagone à sa position actuelle"""
        x_center = self.x + self.radius
        y_center = self.y + (self.radius * math.sqrt(3) / 2)  # Hauteur du triangle équilatéral
        angle = 60  # Chaque angle d'un hexagone est de 60°

        # Calcul des 6 sommets
        points = [
            (x_center + self.radius * math.cos(math.radians(angle * i)),
             y_center + self.radius * math.sin(math.radians(angle * i)))
            for i in range(6)
        ]

        # Dessiner l'hexagone
        pygame.draw.polygon(surface, self.color, points, 1)