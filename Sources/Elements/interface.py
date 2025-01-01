from settings import *
from Sources.Texte.creationTexte import *

class SettingsInterface(object):

    def __init__(self, gestionnaire: any) ->None:
        """Méthode initialisation de l'interface de settings.
        Input : gestionnaire = self méthode d'appel"""
        
        # Initialisation
        self.gestionnaire = gestionnaire
        
        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),  pygame.SRCALPHA)
        self.interfaceSurface.fill("#ffffff")

        # texte 
        self.font = pygame.font.Font(None, 36)
        self.font1 = pygame.font.Font(None, 20)

        self.last_click_time = 0
        self.click_delay = 500   



    def BuildInterface(self) -> None:
        """Méthode : Création de tous les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill("#ffffff")
        text = self.font.render(TEXTE["Elements"]["HotBar"]["Settings"]["Title"], True, (0, 0, 0))
        self.interfaceSurface.blit(text, (10, 10))

        # langue settings
        textLangue = self.font1.render(TEXTE["Elements"]["HotBar"]["Settings"]["Language"], True, (10, 10, 10))
        self.interfaceSurface.blit(textLangue, (10, 50))

        # bouton langue
        self.rectButtonLangue = pygame.Rect(10, 75, 100, 50)  # Définir la taille et position du bouton

        # Dessiner le rectangle du bouton sur la surface
        pygame.draw.rect(self.interfaceSurface, (200, 200, 200), self.rectButtonLangue)

        # Dessiner le texte à l'intérieur du bouton
        texteButtonLangue = self.font1.render(TEXTE["Elements"]["HotBar"]["Settings"]["TypeLanguage"], True, (50, 50, 50))
        texte_pos = (
            self.rectButtonLangue.x + (self.rectButtonLangue.width - texteButtonLangue.get_width()) // 2,
            self.rectButtonLangue.y + (self.rectButtonLangue.height - texteButtonLangue.get_height()) // 2,
        )
        self.interfaceSurface.blit(texteButtonLangue, texte_pos)

    def ChangeLangue(self):
        INFOS["Langue"] = "En" if INFOS["Langue"] == "Fr" else "Fr"
        LoadTexte()


    def CloseInterface(self) -> None:
        """Méthode de fermeture de l'interface. Input / Output : None"""

        # changement des boolean de check
        self.gestionnaire.InterfaceOpen = False
        self.gestionnaire.INTERFACE_OPEN = False


    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (320,180)) # pos topleft

        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:  # Fermer avec ESC
            self.CloseInterface()

        # Gestion des clics de souris
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            # delay de click
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time
            
                # Coordonnées globales de l'événement
                global_pos = event.pos  # Coordonnées globales dans la fenêtre

                # Rect global de la surface de l'interface
                surface_rect = pygame.Rect(320, 180, self.interfaceSurface.get_width(), self.interfaceSurface.get_height())

                # Vérifiez si le clic est sur l'interface
                if surface_rect.collidepoint(global_pos):
                    # Convertissez en coordonnées locales
                    local_pos = (global_pos[0] - surface_rect.x, global_pos[1] - surface_rect.y)

                    # Vérifiez si le clic est sur le bouton de langue
                    if self.rectButtonLangue.collidepoint(local_pos):
                        self.ChangeLangue()
            



        


class SoudInterface(object):

    def __init__(self, gestionnaire: any) ->None:
        """Méthode initialisation de l'interface de sound.
        Input : gestionnaire = self méthode d'appel"""
        
        # Initialisation
        self.gestionnaire = gestionnaire
        
        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),  pygame.SRCALPHA)
        self.interfaceSurface.fill("#ffffff")

        # texte 
        self.font = pygame.font.Font(None, 36)


    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill("#ffffff")
        text = self.font.render(TEXTE["Elements"]["HotBar"]["Sound"]["Title"], True, (0,0,0))
        self.interfaceSurface.blit(text, (10,10))


    def CloseInterface(self) -> None:
        """Méthode de fermeture de l'interface. Input / Output : None"""

        # changement des boolean de check
        self.gestionnaire.InterfaceOpen = False
        self.gestionnaire.INTERFACE_OPEN = False


    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (320,180)) # pos topleft

        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:  # Fermer avec ESC
            self.CloseInterface()


class BundleInterface(object):

    def __init__(self, gestionnaire: any) ->None:
        """Méthode initialisation de l'interface de bundle.
        Input : gestionnaire = self méthode d'appel"""
        
        # Initialisation
        self.gestionnaire = gestionnaire
        
        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),  pygame.SRCALPHA)
        self.interfaceSurface.fill("#ffffff")

        # texte 
        self.font = pygame.font.Font(None, 36)


    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill("#ffffff")
        text = self.font.render(TEXTE["Elements"]["HotBar"]["Bundle"]["Title"], True, (0,0,0))
        self.interfaceSurface.blit(text, (10,10))


    def CloseInterface(self) -> None:
        """Méthode de fermeture de l'interface. Input / Output : None"""

        # changement des boolean de check
        self.gestionnaire.InterfaceOpen = False
        self.gestionnaire.INTERFACE_OPEN = False


    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (320,180)) # pos topleft

        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:  # Fermer avec ESC
            self.CloseInterface()


class BookInterface(object):

    def __init__(self, gestionnaire: any) ->None:
        """Méthode initialisation de l'interface de book.
        Input : gestionnaire = self méthode d'appel"""
        
        # Initialisation
        self.gestionnaire = gestionnaire
        
        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),  pygame.SRCALPHA)
        self.interfaceSurface.fill("#ffffff")

        # texte 
        self.font = pygame.font.Font(None, 36)


    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill("#ffffff")
        text = self.font.render(TEXTE["Elements"]["HotBar"]["Book"]["Title"], True, (0,0,0))
        self.interfaceSurface.blit(text, (10,10))


    def CloseInterface(self) -> None:
        """Méthode de fermeture de l'interface. Input / Output : None"""

        # changement des boolean de check
        self.gestionnaire.InterfaceOpen = False
        self.gestionnaire.INTERFACE_OPEN = False


    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (320,180)) # pos topleft

        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:  # Fermer avec ESC
            self.CloseInterface()




class PNJInterface(object):

    def __init__(self, gestionnaire : any) -> None:
        """Méthode initialisation de l'interface de discussion avec les pnj.
        Input : gestionnaire (self class d'appel), Output : None."""

        # Initialisation
        self.gestionnaire = gestionnaire
        
        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale

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

        # Variables pour le texte du pnj
        self.pnj_text = None
        self.pnj_displayed_text = ""  # Texte affiché du PNJ
        self.pnj_index = 0  # Index pour le texte du PNJ
        self.compteurDialogue = 1
        self.nombreDialogue = len(TEXTE["Dialogues"][f"Niveau{INFOS["Niveau"]}"][self.gestionnaire.pnjActuel]["Principal"]) if not self.gestionnaire.pnjObj.discussion else len(TEXTE["Dialogues"][f"Niveau{INFOS["Niveau"]}"][self.gestionnaire.pnjActuel]["Alternatif"])

        # timer click skip
        self.last_click_time = 0
        self.click_delay = 500    

        # chargement des éléments autre
        self.loadPNG()
        self.loadText()


    def loadText(self) -> None:
        """Méthode de chargement des dialogues en fontion du pnj et du niveau et de l'avancement de discussion. 
        Input / Output : None"""

        # variables de base
        self.pnj_displayed_text = ""
        self.pnj_index = 0

        # check déjà discuter avec
        if not self.gestionnaire.pnjObj.discussion:
            # chargement du texte
            if self.compteurDialogue <= self.nombreDialogue:
                self.pnj_text = TEXTE["Dialogues"][f"Niveau{INFOS["Niveau"]}"][self.gestionnaire.pnjActuel]["Principal"][f"Dialogue{self.compteurDialogue}"]
                self.compteurDialogue += 1 # passage au dialogue suivant
            else:
                self.gestionnaire.Vu() # bool de check passage
                self.CloseInterface() # fermeture interface
                if INFOS["Niveau"] ==0:
                    if self.gestionnaire.pnjActuel == "PNJ1":
                        self.gestionnaire.CinematiqueBuild() # préparation au lancement cinematique
                    elif self.gestionnaire.pnjActuel == "PNJ2":
                        INVENTORY.append("Planks")
                        PNJ["PNJ2"] = True
        else:
            if self.compteurDialogue <= self.nombreDialogue:
                self.pnj_text = TEXTE["Dialogues"][f"Niveau{INFOS["Niveau"]}"][self.gestionnaire.pnjActuel]["Alternatif"][f"Dialogue{self.compteurDialogue}"]
                self.compteurDialogue += 1 # passage au dialogue suivant
            else:
                self.CloseInterface() # fermeture interface


    def loadPNG(self) -> None:
        """Méthode de chargement des images.
        Input / Output : None"""
        
        self.pnjImage = pygame.image.load(join("Images", "PNJ", "Discussion", f"Grand{self.gestionnaire.pnjActuel}.png")).convert_alpha()
        self.playerImage = pygame.image.load(join("Images", "Player", "Discussion", "GrandPlayer.png")).convert_alpha()


    def BuildInterface(self) -> None:
        """Méthode de création des éléments de l'interface de discussion avec le pnj. 
        Input / Output : None"""

        self.interfaceSurface.fill((0, 0, 0, 0))  # Réinitialiser la surface avec une transparence complète

        # load element png
        self.interfaceSurface.blit(self.pnjImage, (50,360))
        self.interfaceSurface.blit(self.playerImage, (WINDOW_WIDTH-178, 360))

        # load nom pnj + creation text du nom
        self.pnjName = TEXTE["Dialogues"][f"Niveau{INFOS["Niveau"]}"][self.gestionnaire.pnjActuel]["Nom"]
        pnjName = self.font1.render(self.pnjName, True, (255,255,255))
        self.interfaceSurface.blit(pnjName, (200, 400))

        # load btn skip / lancer
        self.surfaceBtnSkip = pygame.Surface((100,50))
        self.btnRectSkip = pygame.Rect(750,600,100,50)
        self.surfaceBtnSkip.fill((255,255,255))
        self.textS = TEXTE["Elements"]["InterfacePNJ"]["SkipButton"]
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


    def CloseInterface(self) -> None:
        """Méthode de fermeture de l'interface de discussion avec le pnj.
        Input / Output : None"""

        # Mise à jour des bool de check
        self.gestionnaire.openInterface = False
        self.gestionnaire.INTERFACE_OPEN = False


    def Update(self, event : any) -> None:
        """Méthode d'update de l'interface de discussion.
        Input : event = (element pygame), Output : None"""

        # Dessiner le fond transparent
        self.displaySurface.blit(self.backgroundSurface, (0, 0))

        # Construire et afficher l'interface avec le texte
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (0, 0))

        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:  # Fermer avec ESC
            self.CloseInterface()

        # Vérifie si l'événement est un clic de souris (bouton skip)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time

                # Vérifiez si le clic est dans le rectangle du bouton
                if self.btnRectSkip.collidepoint(event.pos):
                    self.loadText() # pasage au dialogue suivant
                    self.BuildInterface() # build des éléments
