from settings import *

class CreditsInterfaceGame():
    def __init__(self, gestionnaire: any) -> None:
        """Initialisation de l'interface des crédits."""
        self.gestionnaire = gestionnaire
        self.displaySurface = pygame.display.get_surface()
        
        # Fond semi-transparent
        self.backgroundSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        self.backgroundSurface.fill((50, 50, 50, 200))

        # Interface principale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH , WINDOW_HEIGHT), pygame.SRCALPHA)
        
        # Création de la boîte des crédits
        self.box_width = (WINDOW_WIDTH ) - 40
        self.box_height = (WINDOW_HEIGHT ) - 150
        self.box_x = 20
        self.box_y = 80
        heightBoxText = 2000 if not POLICEECRITURE["Dyslexique"] else 3000
        self.textSurface = pygame.Surface((self.box_width, heightBoxText), pygame.SRCALPHA)
        self.textSurface.fill((255, 255, 255))
        
        self.create_credits_text()
        
        # Gestion du scrolling
        self.scroll_y = 0
        self.max_scroll = max(0, self.textSurface.get_height() - (self.box_height - 40))
        self.scrollbar_width = 8
        self.scrollbar_x = self.box_x + self.box_width - self.scrollbar_width - 5
        self.scrollbar_height = max(20, (self.box_height - 40) * (self.box_height - 40) / self.textSurface.get_height())
        self.scrollbar_y = self.box_y
        self.scrolling = False

    def create_credits_text(self) -> None:
        """Génération du texte des crédits avec mise en page."""
        y_offset = 20
        font = FONT["FONT50"]
        credits = TEXTE["Elements"]["Crédits"]

        for section, content in credits.items():
            title = font.render(section.upper(), True, (0, 0, 0))
            self.textSurface.blit(title, (20, y_offset))
            y_offset += font.get_height() + 10
            
            if isinstance(content, dict):
                for role, person in content.items():
                    text = font.render(f"{role}: {person}", True, (50, 50, 50))
                    self.textSurface.blit(text, (40, y_offset))
                    y_offset += font.get_height()
            elif isinstance(content, list):
                for person in content:
                    text = font.render(person, True, (50, 50, 50))
                    self.textSurface.blit(text, (40, y_offset))
                    y_offset += font.get_height()
            
            y_offset += 20  # Espace entre sections

    def Update(self, event) -> None:
        """Mise à jour de l'affichage et gestion du scroll."""
        
        self.interfaceSurface.fill((255, 255, 255))
        # texte titre
        self.interfaceSurface.fill((255,255,255,255))
        textT = FONT["FONT74"].render(TEXTE["Elements"]["GameName"], True, (10,10,10))
        self.interfaceSurface.blit(textT, textT.get_rect(center=(self.interfaceSurface.get_width()//2 , 50)))


        # Affichage du texte des crédits avec scrolling
        self.interfaceSurface.blit(self.textSurface, (self.box_x + 20, self.box_y + 20), (0, self.scroll_y, self.box_width - 40, self.box_height - 40))

        # Scrollbar
        if self.max_scroll > 0:
            self.scrollbar_y = self.box_y + (self.scroll_y / self.max_scroll) * (self.box_height - self.scrollbar_height)
            pygame.draw.rect(self.interfaceSurface, (100, 100, 100), (self.scrollbar_x, self.scrollbar_y, self.scrollbar_width, self.scrollbar_height), border_radius=4)

        self.displaySurface.blit(self.interfaceSurface, (0,0))

        # Gestion des événements
        if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
            self.handle_scroll(event)
        
        if INFOS["EndGame"]:  # Auto-scroll continue à la fin du jeu
            self.scroll_y += 0.1  # On ajoute la vitesse au scroll_y
            self.scroll_y = min(self.scroll_y, self.max_scroll)  # On empêche de dépasser la limite
            
            if event.type == pygame.KEYDOWN:
                if event.key == KEYSBIND["echap"]:
                    INFOS["CrashGame"] = True
                    
            if self.scroll_y == self.max_scroll:
                INFOS["CrashGame"] = True


    def handle_scroll(self, event) -> None:
        """Gestion du scrolling avec la molette et la barre de défilement."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Molette haut
                self.scroll_y = max(self.scroll_y - 30, 0)
            elif event.button == 5:  # Molette bas
                self.scroll_y = min(self.scroll_y + 30, self.max_scroll)
            
            if self.scrollbar_x <= event.pos[0] <= self.scrollbar_x + self.scrollbar_width and \
               self.scrollbar_y <= event.pos[1] <= self.scrollbar_y + self.scrollbar_height:
                self.scrolling = True
        
        elif event.type == pygame.MOUSEBUTTONUP:
            self.scrolling = False
        
        elif event.type == pygame.MOUSEMOTION and self.scrolling:
            rel_y = event.rel[1]
            new_scroll_y = self.scroll_y + (rel_y * self.max_scroll / (self.box_height - self.scrollbar_height))
            self.scroll_y = min(max(new_scroll_y, 0), self.max_scroll)
