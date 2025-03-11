from settings import *
from SourcesFichiers.Ressources.Texte.creationTexte import *

class SettingsInterface(object):

    def __init__(self, gestionnaire: any) ->None:
        """Méthode initialisation de l'interface de settings.
        Input : gestionnaire = self méthode d'appel
        Output : None"""
        
        # Initialisation
        self.gestionnaire = gestionnaire
        
        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),  pygame.SRCALPHA)
        self.interfaceSurface.fill("#ffffff")

        # timer click
        self.last_click_time = 0
        self.click_delay = 500   

        self.button_positions = {}  # Stocke les positions des boutons de touche
        self.buttonsLangue = {}

        # close interface cross
        self.surfaceCloseCross = pygame.Surface((24,24))
        self.isCrossCloseHover = False
        self.crossClose = pygame.image.load(join("Image","Interface", "Croix", "x-mark.png")).convert_alpha()
        self.crossClose2 = pygame.image.load(join("Image","Interface", "Croix", "x-mark2.png")).convert_alpha()




    def BuildInterfaceBind(self):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill((100,100,100,180))  # Fond semi-transparent
        self.interfaceSurface.blit(overlay, (0, 0))

        # Dessiner la boîte au centre
        box_rect = pygame.Rect(225, 140, 200, 50)
        pygame.draw.rect(self.interfaceSurface, (200,200,200), box_rect)
        pygame.draw.rect(self.interfaceSurface, (0,0,0), box_rect, 2)

        # Texte d'instruction
        text_surface = FONT["FONT20"].render(TEXTE["Elements"]["HotBar"]["Settings"]["PressKey"], True, (0,0,0))
        self.interfaceSurface.blit(text_surface, (box_rect.x + 18, box_rect.y + 15))


    def BuildInterface(self) -> None:
        """Méthode : Création de tous les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill("#ffffff")
        text = FONT["FONT36"].render(TEXTE["Elements"]["HotBar"]["Settings"]["Title"], True, (0, 0, 0))
        self.interfaceSurface.blit(text, (10, 10))

        # LANGUE
        # langue settings
        textLangue = FONT["FONT20"].render(TEXTE["Elements"]["HotBar"]["Settings"]["Language"], True, (10, 10, 10))
        self.interfaceSurface.blit(textLangue, (10, 50))

        y_offsetLangue = 75  # Position initiale en vertical
        x_offsetLangue = 10  # Position initiale en horizontal
        self.buttonsLangue = {}  # Dictionnaire pour stocker les boutons

        for action, key in DICOLANGUE.items():  
            # Création du rectangle pour chaque bouton (position dynamique)
            rectButtonLangue = pygame.Rect(x_offsetLangue, y_offsetLangue, 100, 50)
            
            if key:
                # Dessiner le rectangle du bouton
                pygame.draw.rect(self.interfaceSurface, (112, 193, 255), rectButtonLangue)
                #Dessiner le contour du bouton (bordure noire)
                pygame.draw.rect(self.interfaceSurface, (0, 0, 0), rectButtonLangue, width=3)
            else:
                # Dessiner le rectangle du bouton
                pygame.draw.rect(self.interfaceSurface, (200,200,200), rectButtonLangue)
            
            
            # Dessiner le texte du bouton
            texteButtonLangue = FONT["FONT20"].render(
                TEXTE["Elements"]["HotBar"]["Settings"]["TypeLanguage"][action], True, (50, 50, 50)
            )
            texte_pos = (
                rectButtonLangue.x + (rectButtonLangue.width - texteButtonLangue.get_width()) // 2,
                rectButtonLangue.y + (rectButtonLangue.height - texteButtonLangue.get_height()) // 2,
            )
            self.interfaceSurface.blit(texteButtonLangue, texte_pos)

            # Ajouter le bouton au dictionnaire
            self.buttonsLangue[action] = rectButtonLangue  

            # Déplacer vers le bas pour le prochain bouton
            y_offsetLangue += 60  # 50 de hauteur + 10 de marge


        # BIND KEYS
        y_offset = 50  # Position initiale en vertical
        x_offset = 150  # Position initiale en horizontal (colonne 1)
        column_width = 150  # Largeur de la colonne pour le décalage
        max_height = self.interfaceSurface.get_height()  # Hauteur de l'interface
        button_width = 60  # Largeur du bouton
        button_height = 25  # Hauteur du bouton

        self.button_positions.clear()  # Vider les anciennes positions
        listeAllBindInt = []
        for keyElement in KEYSBIND:
            listeAllBindInt.append(KEYSBIND[keyElement])

        for action, key in KEYSBIND.items():
            # Affichage du libellé (non cliquable)
            text_label = FONT["FONT20"].render(f"{action.capitalize()} :", True, (0,0,0))
            self.interfaceSurface.blit(text_label, (x_offset, y_offset + 5))  # Position fixe du libellé

            # Bouton pour la touche (cliquable)
            text_key = pygame.key.name(key)  # Nom de la touche
            key_rect = pygame.Rect(x_offset + 75, y_offset, button_width, button_height)  # Position et taille du bouton
            nbOccurence = listeAllBindInt.count(key)
            
            # Dessiner les boutons avec des couleurs selon leur état
            if nbOccurence > 1:  # La touche est déjà liée en rouge
                pygame.draw.rect(self.interfaceSurface, (255, 31, 53), key_rect)  # Rouge clair
                pygame.draw.rect(self.interfaceSurface, (110, 2, 2), key_rect, 2)  # Bordure rouge
                text_surface = FONT["FONT20"].render(text_key, True, (110, 2, 2))  # Texte en rouge foncé
            else:
                pygame.draw.rect(self.interfaceSurface, (200, 200, 200), key_rect)  # Gris clair par défaut
                pygame.draw.rect(self.interfaceSurface, (0, 0, 0), key_rect, 2)  # Bordure noire
                text_surface = FONT["FONT20"].render(text_key, True, (0, 0, 0))  # Texte en noir

            self.interfaceSurface.blit(text_surface, (key_rect.x + 5, key_rect.y + 5))

            # Sauvegarder la position du bouton de la touche
            self.button_positions[action] = key_rect

            # Calcul du prochain y_offset
            y_offset += button_height + 20  # Décalage vertical pour la prochaine ligne

            # Si la hauteur dépasse celle de l'interface, déplacer vers la colonne suivante
            if y_offset + button_height > max_height:
                y_offset = 50  # Réinitialiser le y_offset
                x_offset += column_width  # Décaler vers la droite pour une nouvelle colonne

        # close element
        self.surfaceCloseCross.fill("#ffffff")
        self.rectCloseCross = pygame.Rect(self.interfaceSurface.get_width() - 34, 10, 24, 24)
        if self.isCrossCloseHover:
            self.surfaceCloseCross.blit(self.crossClose2, (0,0))
        else:
            self.surfaceCloseCross.blit(self.crossClose, (0,0))
        self.interfaceSurface.blit(self.surfaceCloseCross, (self.rectCloseCross.x, self.rectCloseCross.y))





    def ChangeLangue(self, action):
        """Méthode de changement de langue dans les fichier du jeu.
        Input / Output : None"""

        for keyLangue in DICOLANGUE:
            DICOLANGUE[keyLangue] = False if keyLangue != action else True
        LoadTexte() # load nouveau texte (changement de langue)

    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()

        # rebinding
        if INFOS["RebindingKey"]:
            self.BuildInterfaceBind()


        self.displaySurface.blit(self.interfaceSurface, (320,180)) # pos topleft


        # Gestion des clics de souris
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            # delay de click
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time
            
                local_pos = GetLocalPos(event, self.interfaceSurface, (320, 180))
                if local_pos:

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Vérifier si un bouton de langue a été cliqué
                        if not INFOS["RebindingKey"]:
                            for action, rectButtonLangue in self.buttonsLangue.items():  # Parcourt le dictionnaire
                                if rectButtonLangue.collidepoint(local_pos):
                                    self.ChangeLangue(action)  # Change la langue en fonction du bouton cliqué

                        if not INFOS["RebindingKey"]:  # Si on n'est PAS en mode rebind
                            for action, rect in self.button_positions.items():
                                if rect.collidepoint(local_pos):
                                    INFOS["RebindingKey"] = action  # Déclencher le mode rebind


                    if event.type == pygame.MOUSEBUTTONDOWN and not INFOS["RebindingKey"]:
                        if self.rectCloseCross.collidepoint(local_pos):
                            # fermeture interface
                            self.gestionnaire.CloseAllInterface()

        if event.type == pygame.MOUSEMOTION:
            local_pos = GetLocalPos(event, self.interfaceSurface, (320, 180))
            if local_pos:              
                # cross close interface
                if event.type == pygame.MOUSEMOTION and not INFOS["RebindingKey"]:
                    # cross close interface
                    self.isCrossCloseHover = self.rectCloseCross.collidepoint(local_pos)