import pygame.locals
from settings import * 

class BookInterface(object):

    def __init__(self, gestionnaire: any, gestionCours) ->None:
        """Méthode initialisation de l'interface de book.
        Input : gestionnaire = self méthode d'appel"""
        
        # Initialisation
        self.gestionnaire = gestionnaire
        self.gestionCours = gestionCours
        
        # Surface pour le fond transparent
        self.backgroundSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.backgroundSurface.fill((50, 50, 50, 200))  # Fond gris avec alpha (200)

        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH*(3/4), WINDOW_HEIGHT*(3/4)),  pygame.SRCALPHA)

        self.surfaceGauche = pygame.Surface((370, 400), pygame.SRCALPHA)
        self.surfaceDroite = pygame.Surface((390, 400), pygame.SRCALPHA)

        # close interface cross
        self.surfaceCloseCross = pygame.Surface((24,24), pygame.SRCALPHA)
        self.isCrossCloseHover = False
        try:
            self.crossClose = pygame.image.load(join("Image","Interface", "Croix", "x-mark.png")).convert_alpha()
            self.crossClose2 = pygame.image.load(join("Image","Interface", "Croix", "x-mark2.png")).convert_alpha()

            # book bcg
            self.bookBcg = pygame.image.load(join("Image", "Interface", "Book.png")).convert_alpha()
            self.interfaceSurface.blit(self.bookBcg, (0,0))
        except:
            INFOS["ErrorLoadElement"] = True

        
        self.maxHeight = self.surfaceGauche.get_height()
        self.maxWidth = self.surfaceDroite.get_width()

        # timer click btn delays
        self.last_click_time = 0
        self.click_delay = 500  

        # Navigation et gestion des pages
        self.pagesAct = 0
        self.compteur = INFOS["GetCours"]  # Nombre de cours obtenus
        self.hauteurAct = 0

        # rect collision page
        self.rectBtnAdd = pygame.Rect(self.interfaceSurface.get_width()-88, 500, 75, 50)
        self.rectBtnRemove = pygame.Rect(0, 500, 100, 50)

    def PageSuivante(self):
        """Passe à la page suivante si disponible."""
        if self.pagesAct < self.compteur - 1:
            self.pagesAct += 1

    def PagePrecedente(self):
        """Revient à la page précédente si possible."""
        if self.pagesAct > 0:
            self.pagesAct -= 1


    def BuildInterface(self) -> None:
        """Construction de l'interface complète du livre."""
        # Fond du livre
        self.interfaceSurface.blit(self.bookBcg, (0, 0))
        self.surfaceDroite.fill((255, 255, 255, 0))  # Page droite en blanc
        self.surfaceGauche.fill((255, 255, 255, 0))  # Page gauche en blanc
        
        self.SeparationPage()  # Ajout du contenu des pages

        # cross croix
        self.surfaceCloseCross.fill((0,0,0,0)) 
        self.rectCloseCross = pygame.Rect(self.interfaceSurface.get_width() - 39, 5, 24, 24) 
        if self.isCrossCloseHover: 
            self.surfaceCloseCross.blit(self.crossClose2, (0,0)) 
        else: 
            self.surfaceCloseCross.blit(self.crossClose, (0,0)) 
        self.interfaceSurface.blit(self.surfaceCloseCross, (self.rectCloseCross.x, self.rectCloseCross.y))




    def SeparationPage(self):
        """Affiche les cours en les répartissant correctement sur les deux pages (gauche et droite)."""
        # Limite les cours à ceux débloqués
        CoursNiveauSco = self.gestionCours.coursNiveauScolaire[:self.compteur]
        self.hauteurAct = 5  # Position initiale pour l'affichage

        # Indices pour les pages
        start_index = self.pagesAct * 2  # Départ pour cette double page
        end_index = min(start_index + 2, len(CoursNiveauSco))  # Fin sans dépasser les limites
        coursParPages = CoursNiveauSco[start_index:end_index]

        # Parcourt les cours à afficher sur les deux pages
        for page_position, cours in enumerate(coursParPages):  # 0 = page gauche, 1 = page droite
            if not cours:
                continue  # Si un cours est vide ou None, on passe au suivant

            for element in cours:
                # Validation de la structure de l'élément
                if not isinstance(element, list) or len(element) < 2:
                    print(f"Structure d'élément incorrecte détectée : {element}")
                    continue

                # Gestion des images
                if element[0] == "Image":
                    try:
                        imageSurf = pygame.image.load(element[1]).convert_alpha()
                        if page_position == 0:  # Page gauche
                            self.surfaceGauche.blit(
                                imageSurf,
                                imageSurf.get_rect(center=(self.surfaceGauche.get_width() // 2, self.hauteurAct + 125))
                            )
                        else:  # Page droite
                            self.surfaceDroite.blit(
                                imageSurf,
                                imageSurf.get_rect(center=(self.surfaceDroite.get_width() // 2, self.hauteurAct + 125))
                            )
                        self.hauteurAct += imageSurf.get_height() + 125  # Décalage pour le prochain élément
                    except pygame.error as e:
                        print(f"Erreur de chargement de l'image : {e}")
                        INFOS["ErrorLoadElement"] = True

                # Gestion des surfaces LaTeX
                elif element[0]:
                    surface = element[1]
                    if page_position == 0:  # Page gauche
                        self.surfaceGauche.blit(
                            surface,
                            surface.get_rect(center=(self.surfaceGauche.get_width() // 2, self.hauteurAct + 10))
                        )
                    else:  # Page droite
                        self.surfaceDroite.blit(
                            surface,
                            surface.get_rect(center=(self.surfaceDroite.get_width() // 2, self.hauteurAct + 10))
                        )
                    self.hauteurAct += surface.get_height() + 10  # Décalage pour le prochain élément

                # Gestion des textes
                else:
                    texte = element[1]
                    wrapped_lines = wrap_text(texte, FONT["FONT18"], self.surfaceGauche.get_width() - 20)
                    line_height = FONT["FONT18"].size("Tg")[1]
                    for line in wrapped_lines:
                        line_surface = FONT["FONT18"].render(line, True, (0, 0, 0))
                        if page_position == 0:  # Page gauche
                            self.surfaceGauche.blit(line_surface, (20, self.hauteurAct))
                        else:  # Page droite
                            self.surfaceDroite.blit(line_surface, (20, self.hauteurAct))
                        self.hauteurAct += line_height  # Décalage pour chaque ligne

            # Réinitialisation de la hauteur pour chaque page
            self.hauteurAct = 5

            # Numérotation des pages
            numero_page = f"{start_index + 1}" if page_position == 0 else f"{end_index}"
            textSurf = FONT["FONT16"].render(numero_page, True, (0, 0, 0))
            surface = self.surfaceGauche if page_position == 0 else self.surfaceDroite
            surface.blit(textSurf, textSurf.get_rect(center=(surface.get_width() // 2, surface.get_height() - 10)))






    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()

        self.interfaceSurface.blit(self.surfaceGauche, (70, 30))
        self.interfaceSurface.blit(self.surfaceDroite, (500, 30))   

        self.displaySurface.blit(self.backgroundSurface, (0,0)) # bcg gris
        self.displaySurface.blit(self.interfaceSurface, (160, 90)) # pos topleft


        if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):

            local_pos = GetLocalPos(event, self.interfaceSurface, (160, 90))
            if local_pos:
                if event.type == pygame.MOUSEMOTION:
                    # cross close interface
                    check = False
                    self.isCrossCloseHover = self.rectCloseCross.collidepoint(local_pos)
                    self.btnLeftHover = self.rectBtnRemove.collidepoint(local_pos)
                    self.btnRightHoer = self.rectBtnAdd.collidepoint(local_pos)
                    if self.isCrossCloseHover or self.btnLeftHover or self.btnRightHoer:
                        check = True
                    INFOS["Hover"] = check   

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #  check timer
                    current_time = pygame.time.get_ticks()
                    if current_time - self.last_click_time > self.click_delay:
                        self.last_click_time = current_time

                        if self.rectCloseCross.collidepoint(local_pos):
                            # fermeture interface
                            self.gestionnaire.CloseAllInterface()
                        
                        if self.rectBtnAdd.collidepoint(local_pos):
                            self.PageSuivante()
                        if self.rectBtnRemove.collidepoint(local_pos):
                            self.PagePrecedente()
