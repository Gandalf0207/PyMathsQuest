from settings import *
from Sources.Ressources.Texte.creationTexte import *

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




    def ChangeLangue(self, action):
        """Méthode de changement de langue dans les fichier du jeu.
        Input / Output : None"""

        for keyLangue in DICOLANGUE:
            DICOLANGUE[keyLangue] = False if keyLangue != action else True
        LoadTexte() # load nouveau texte (changement de langue)


    def CloseInterface(self) -> None:
        """Méthode de fermeture de l'interface. Input / Output : None"""

        # changement des boolean de check
        self.gestionnaire.CloseInterface()


    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()

        # rebinding
        if INFOS["RebindingKey"]:
            self.BuildInterfaceBind()


        self.displaySurface.blit(self.interfaceSurface, (320,180)) # pos topleft



        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()
        if keys[KEYSBIND["echap"]]:  # Fermer avec ESC
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

                    # Vérifier si un bouton de langue a été cliqué
                    if not INFOS["RebindingKey"]:
                        for action, rectButtonLangue in self.buttonsLangue.items():  # Parcourt le dictionnaire
                            if rectButtonLangue.collidepoint(local_pos):
                                self.ChangeLangue(action)  # Change la langue en fonction du bouton cliqué

                    if not INFOS["RebindingKey"]:  # Si on n'est PAS en mode rebind
                        for action, rect in self.button_positions.items():
                            if rect.collidepoint(local_pos):
                                INFOS["RebindingKey"] = action  # Déclencher le mode rebind
                    



        


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

        # Propriétés des sliders
        self.slider_x = 50  # Position X des sliders
        self.slider_width = 540
        self.slider_height = 20
        self.cursor_width = 10

        # Définition des sliders (Musique, Effets, Voix)
        self.sliders = [
            {"label": "Musique", "y": 100, "Element" : "BandeSon"},
            {"label": "Voix", "y": 300, "Element" : "Dialogue"},  
            {"label": "Effets Sonores", "y": 200, "Element" : "EffetSonore"},  
        ]
        self.dragging = None



    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill("#ffffff")
        text = FONT["FONT36"].render(TEXTE["Elements"]["HotBar"]["Sound"]["Title"], True, (0,0,0))
        self.interfaceSurface.blit(text, (10,10))

        for i, slider in enumerate(self.sliders):
            # Position du curseur
            cursor_x = self.slider_x + int(SOUND[slider["Element"]] * (self.slider_width - self.cursor_width))

            # Dessiner le titre du slider
            text = FONT["FONT20"].render(slider["label"], True, (0, 0, 0))
            self.interfaceSurface.blit(text, (self.slider_x, slider["y"] - 45))

            # Dessiner la barre de volume
            pygame.draw.rect(self.interfaceSurface, (200, 200, 200), (self.slider_x, slider["y"], self.slider_width, self.slider_height))

            # Dessiner le curseur
            pygame.draw.rect(self.interfaceSurface, (255, 0, 0), (cursor_x, slider["y"] - 5, self.cursor_width, self.slider_height + 10))

            # Afficher le volume en %
            volume_percent = int(SOUND[slider["Element"]] * 100)
            volume_text = FONT["FONT20"].render(f"{volume_percent}%", True, (0, 0, 0))
            text_rect = volume_text.get_rect(center=(cursor_x + self.cursor_width // 2, slider["y"] - 20))
            self.interfaceSurface.blit(volume_text, text_rect)

    def CloseInterface(self) -> None:
        """Méthode de fermeture de l'interface. Input / Output : None"""
        # changement des boolean de check
        self.gestionnaire.CloseInterface()

    def Update(self, event) -> None:
        """Mise à jour de l'interface et gestion des interactions."""
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (320,180))

        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()
        if keys[KEYSBIND["echap"]]:  # Fermer avec ESC
            self.CloseInterface()

        # Coordonnées globales de l'événement
        global_pos = pygame.mouse.get_pos()

        # Convertir les coordonnées globales en locales
        surface_rect = pygame.Rect(320, 180, self.interfaceSurface.get_width(), self.interfaceSurface.get_height())

        if surface_rect.collidepoint(global_pos):
            local_pos = (global_pos[0] - surface_rect.x, global_pos[1] - surface_rect.y)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = local_pos
                for i, slider in enumerate(self.sliders):
                    if self.slider_x <= mouse_x <= self.slider_x + self.slider_width and \
                       slider["y"] - 5 <= mouse_y <= slider["y"] + self.slider_height + 5:
                        self.dragging = i  # On stocke l'index du slider actif

            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = None  # On arrête le glissement

            elif event.type == pygame.MOUSEMOTION and self.dragging is not None:
                mouse_x, _ = local_pos
                slider = self.sliders[self.dragging]

                # Déplacer le curseur
                new_x = min(max(mouse_x - self.cursor_width // 2, self.slider_x), self.slider_x + self.slider_width - self.cursor_width)
                SOUND[slider["Element"]] = (new_x - self.slider_x) / (self.slider_width - self.cursor_width)
                self.gestionnaire.gestionSound.Update()




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

        # load image
        self.LoadImage()
        self.CreateElementRect()


    def LoadImage(self) -> None:
        """Méthode chargement des images Input / Output : None"""

        self.planks = pygame.image.load(join("Images", "Item", "PlanksItem.png")).convert_alpha()
        self.oldAxe = pygame.image.load(join("Images", "Item", "OldAxeItem.png")).convert_alpha()
        self.pickaxe = pygame.image.load(join("Images", "Item", "Pickaxe.png")).convert_alpha()
        self.boat = pygame.image.load(join("Images", "Item", "Boat.png")).convert_alpha()
        self.keys = pygame.image.load(join("Images", "Item", "Keys.png")).convert_alpha()
        self.showel = pygame.image.load(join("Images", "Item", "OldAxeItem.png")).convert_alpha()

    def CreateElementRect(self) -> None:
        """Méthode de création des slots et de leurs attributs
        Input / Output : None"""

        # surface slot inventaire
        self.surfaceSlot1 = pygame.Surface((96,96))
        self.surfaceSlot2 = pygame.Surface((96,96))
        self.surfaceSlot3 = pygame.Surface((96,96))
        self.surfaceSlot4 = pygame.Surface((96,96))
        self.surfaceSlot5 = pygame.Surface((96,96))
        self.surfaceSlot6 = pygame.Surface((96,96))
        self.surfaceSlot7 = pygame.Surface((96,96))
        self.surfaceSlot8 = pygame.Surface((96,96))
        self.surfaceSlot9 = pygame.Surface((96,96))
        self.surfaceSlot10 = pygame.Surface((96,96))
        self.surfaceSlot11 = pygame.Surface((96,96))
        self.surfaceSlot12 = pygame.Surface((96,96))

        # all slots
        self.allSurfaceSlot = [self.surfaceSlot1, self.surfaceSlot2, self.surfaceSlot3, self.surfaceSlot4, self.surfaceSlot5, self.surfaceSlot6, self.surfaceSlot7, self.surfaceSlot8, self.surfaceSlot9, self.surfaceSlot1, self.surfaceSlot11, self.surfaceSlot12]
        
        #all coords slots
        self.coordsSurface = [
                            (56,40), (198,40), (345,40), (492, 40), 
                            (51, 156), (198, 156), (345, 156), (492, 156), 
                            (51, 262), (198, 262), (345, 262), (492, 262) ]

    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill("#ffffff")
        text = FONT["FONT36"].render(TEXTE["Elements"]["HotBar"]["Bundle"]["Title"], True, (0,0,0))
        self.interfaceSurface.blit(text, (10,10))

        indice = 0
        for key in INVENTORY: # pour tout les élément dans l'inventaire
            elementSlot = self.allSurfaceSlot[indice] # get slot
            elementSlot.fill((255,255,255)) # clear slot

            # définition de l'image en fonction de l'item de l'inventaire
            if key == "OldAxe" and INVENTORY["OldAxe"] > 0: 
                surf = self.oldAxe
            elif key == "Planks" and INVENTORY["Planks"] > 0: 
                surf = self.planks
            elif key == "Pickaxe" and INVENTORY["Pickaxe"] > 0: 
                surf = self.pickaxe
            elif key == "Boat" and INVENTORY["Boat"] > 0: 
                surf = self.boat
            elif key == "Key" and INVENTORY["Key"] >0:
                surf = self.keys
            elif key == "Showel" and INVENTORY["Showel"] >0:
                surf = self.showel
            else:
                surf = None
            
            # s'il y a un item à afficher
            if surf != None:
                # ajout de l'item dans le slot
                elementSlot.blit(surf, (0,0))

                # text nombre items
                textCount = FONT["FONT20"].render(f"{INVENTORY[key]}", True, (50,50,50))
                elementSlot.blit(textCount, (70,70))

                # affichage slot
                self.interfaceSurface.blit(elementSlot, self.coordsSurface[indice])


                indice += 1 # on change de slot

        
    def CloseInterface(self) -> None:
        """Méthode de fermeture de l'interface. Input / Output : None"""

        # changement des boolean de check
        self.gestionnaire.CloseInterface()


    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (320,180)) # pos topleft

        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()
        if keys[KEYSBIND["echap"]]:  # Fermer avec ESC
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


    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # texte titre
        self.interfaceSurface.fill("#ffffff")
        text = FONT["FONT36"].render(TEXTE["Elements"]["HotBar"]["Book"]["Title"], True, (0,0,0))
        self.interfaceSurface.blit(text, (10,10))


    def CloseInterface(self) -> None:
        """Méthode de fermeture de l'interface. Input / Output : None"""

        # changement des boolean de check
        self.gestionnaire.CloseInterface()


    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (320,180)) # pos topleft

        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()
        if keys[KEYSBIND["echap"]]:  # Fermer avec ESC
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

        # Position du PNJ
        self.pnj_position = (100, 100)  # Position du PNJ (à gauche)

        # Variables pour le texte du pnj
        self.pnj_text = None
        self.pnj_displayed_text = ""  # Texte affiché du PNJ
        self.pnj_index = 0  # Index pour le texte du PNJ
        self.compteurDialogue = 1
        self.nombreDialogue = len(TEXTE["Dialogues"][NIVEAU["Map"]][self.gestionnaire.pnjActuel]["Principal"]) if not self.gestionnaire.pnjObj.discussion else len(TEXTE["Dialogues"][NIVEAU["Map"]][self.gestionnaire.pnjActuel]["Alternatif"])

        # timer click skip
        self.last_click_time = 0
        self.click_delay = 500    

        # chargement des éléments autre
        self.loadPNG()

        if self.gestionnaire.pnjObj.QuestionDone and not self.gestionnaire.pnjObj.discussion: # add 1 : skp dialogue question
            self.loadText(1)
        else:
            self.loadText()
        


    def loadText(self, skipDialogueQuestion = 0 ) -> None:
        """Méthode de chargement des dialogues en fontion du pnj et du niveau et de l'avancement de discussion. 
        Input / Output : None"""

        # variables de base
        self.pnj_displayed_text = ""
        self.pnj_index = 0

        # chargement au dialogue suivant si on a dejé faitune qustions
        self.compteurDialogue += skipDialogueQuestion

        # check déjà discuter avec pnj
        if not self.gestionnaire.pnjObj.discussion:
            # chargement du texte
            if self.compteurDialogue <= self.nombreDialogue:
                self.pnj_text = TEXTE["Dialogues"][NIVEAU["Map"]][self.gestionnaire.pnjActuel]["Principal"][f"Dialogue{self.compteurDialogue}"]
                self.gestionnaire.gestionSound.Dialogue(self.compteurDialogue)
                self.compteurDialogue += 1 # passage au dialogue suivant
            else:
                # gestion son
                self.gestionnaire.gestionSound.StopDialogue()

                self.gestionnaire.Vu() # bool de check passage
                self.CloseInterface() # fermeture interface

                # action après discussions
                if NIVEAU["Map"] == "NiveauPlaineRiviere":
                    if self.gestionnaire.pnjActuel == "PNJ1":
                        INVENTORY["OldAxe"] += 1
                        self.gestionnaire.CinematiqueBuild() # préparation au lancement cinematique
                    elif self.gestionnaire.pnjActuel == "PNJ2":
                        INVENTORY["Planks"] += 1
                        PNJ["PNJ2"] = True
                        STATE_HELP_INFOS[0] = "BuildBridge"
                    elif self.gestionnaire.pnjActuel == "PNJ3":
                        INVENTORY["Pickaxe"] += 1
                        PNJ["PNJ3"] = True
                        STATE_HELP_INFOS[0] = "MineRock"

                if NIVEAU["Map"] == "NiveauMedievale": 
                    if self.gestionnaire.pnjActuel == "PNJ1":
                        PNJ["PNJ1"] = True
                        INVENTORY["Showel"] += 1
                        STATE_HELP_INFOS[0] = "BuildBridge"
                    elif self.gestionnaire.pnjActuel == "PNJ2":
                        PNJ["PNJ2"] = True
                        STATE_HELP_INFOS[0] = "FindWell"
                    elif self.gestionnaire.pnjActuel == "PNJ3":
                        PNJ["PNJ3"] = True
                        INVENTORY["Key"] += 1
                        STATE_HELP_INFOS[0] = "OpenDoor"
                    elif self.gestionnaire.pnjActuel == "PNJ4":
                        self.gestionnaire.CinematiqueBuild() # préparation au lancement cinematique





        else:
            # get dialogue deja vu
            if self.compteurDialogue <= self.nombreDialogue:
                self.pnj_text = TEXTE["Dialogues"][NIVEAU["Map"]][self.gestionnaire.pnjActuel]["Alternatif"][f"Dialogue{self.compteurDialogue}"]
                self.gestionnaire.gestionSound.Dialogue(self.compteurDialogue)
                self.compteurDialogue += 1 # passage au dialogue suivant
            else:
                # gestion son
                self.gestionnaire.gestionSound.StopDialogue()
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
        self.pnjName = TEXTE["Dialogues"][NIVEAU["Map"]][self.gestionnaire.pnjActuel]["Nom"]
        pnjName = FONT["FONT36B"].render(self.pnjName, True, (255,255,255))
        self.interfaceSurface.blit(pnjName, (200, 400))

        # box petite question
        if self.gestionnaire.pnjActuel == "PNJ3" and NIVEAU["Map"] == "NiveauMedievale" and not self.gestionnaire.pnjObj.QuestionDone:
            self.surfaceBtnOui = pygame.Surface((75,50))
            self.surfaceBtnNon = pygame.Surface((75,50))

            self.rectBtnOui = pygame.Rect(800, 600, 75, 50)
            self.rectBtnNon = pygame.Rect(1000, 600, 75, 50)

            self.textO = TEXTE["Elements"]["InterfacePNJ"]["Oui"]
            self.textN = TEXTE["Elements"]["InterfacePNJ"]["Non"]

            self.textOui = FONT["FONT36"].render(self.textO, True, (10,10,10))
            self.textNon = FONT["FONT36"].render(self.textN, True, (10,10,10))

            self.surfaceBtnOui.blit(self.textOui, (0,0))
            self.surfaceBtnNon.blit(self.textNon, (0,0))

            self.interfaceSurface.blit(self.surfaceBtnOui, (self.rectBtnOui.x, self.rectBtnOui.y))
            self.interfaceSurface.blit(self.surfaceBtnNon, (self.rectBtnNon.x, self.rectBtnNon.y))


        else:

            # load btn skip / lancer
            self.surfaceBtnSkip = pygame.Surface((100,50))
            self.btnRectSkip = pygame.Rect(750,600,100,50)
            self.surfaceBtnSkip.fill((255,255,255))
            self.textS = TEXTE["Elements"]["InterfacePNJ"]["SkipButton"]
            self.textSkip = FONT["FONT36"].render(self.textS, True, (10,10,10))
            self.surfaceBtnSkip.blit(self.textSkip, (0,0))
            self.interfaceSurface.blit(self.surfaceBtnSkip, (self.btnRectSkip.x, self.btnRectSkip.y))


        # bloc gestion texte 
        if self.pnj_index < len(self.pnj_text):
            self.pnj_index += 1
        # Mettre à jour le texte affiché
        self.pnj_displayed_text = self.pnj_text[:self.pnj_index]


        # Largeur maximale de la boîte de texte
        max_width = 500
        wrapped_lines = wrap_text(self.pnj_displayed_text,FONT["FONT36"], max_width)

        # Affichage des lignes
        y_offset = 420  # Position Y de départ
        line_height = FONT["FONT36"].size("Tg")[1]  # Hauteur d'une ligne
        for i, line in enumerate(wrapped_lines):
            line_surface = FONT["FONT36"].render(line, True, (255, 255, 255))
            self.interfaceSurface.blit(line_surface, (200, y_offset + i * line_height))



    def CloseInterface(self) -> None:
        """Méthode de fermeture de l'interface de discussion avec le pnj.
        Input / Output : None"""
        # couper le son si dialogue en cours + augmenter piste audio
        self.gestionnaire.gestionSound.StopDialogue()

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

        if keys[KEYSBIND["echap"]]:  # Fermer avec ESC
            self.CloseInterface()

        # Vérifie si l'événement est un clic de souris (bouton skip)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time

                if self.gestionnaire.pnjActuel == "PNJ3" and NIVEAU["Map"] == "NiveauMedievale" and not self.gestionnaire.pnjObj.QuestionDone:
                    if self.rectBtnOui.collidepoint(event.pos):
                        self.gestionnaire.pnjObj.QuestionDone =True
                        self.loadText() # pasage au dialogue suivant
                        self.BuildInterface() # build des éléments
                    
                    if self.rectBtnNon.collidepoint(event.pos):
                        self.CloseInterface()
                else:
                    # Vérifiez si le clic est dans le rectangle du bouton
                    if self.btnRectSkip.collidepoint(event.pos):
                        self.loadText() # pasage au dialogue suivant
                        self.BuildInterface() # build des éléments


        # touche espace skip des dialogues
        if keys[KEYSBIND["skip"]] : 
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time

                # pnj question avant interaction
                if  self.gestionnaire.pnjActuel == "PNJ3" and NIVEAU["Map"] == "NiveauMedievale":
                    if self.gestionnaire.pnjObj.QuestionDone: # condition spécifique
                        self.loadText()
                        self.BuildInterface()   
                else:
                    self.loadText()
                    self.BuildInterface()   