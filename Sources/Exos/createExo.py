from settings import *
from Sources.Exos.choixExo import *
from Sources.Exos.renderLatex import *

class CreateExo:
    def __init__(self, gestionnaire):

        self.gestionnaire = gestionnaire

        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceExoSurface = pygame.Surface((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),  pygame.SRCALPHA)
        self.interfaceExoSurface.fill("#ffffff")

        self.ObjRender = RenderLatex()
        self.ObjExoChoix = GetExo()

        self.latexSurface = None

        self.font = pygame.font.Font(None, 30)

        self.indexTexte = 0


    def BuildInterface(self):
        self.interfaceExoSurface.fill("#ffffff")
        textTitre = self.font.render(TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["ExoTexte"]["Title"], True, (0, 0, 0))
        self.interfaceExoSurface.blit(textTitre, (10, 10))

        self.textConsigne = TEXTE["Elements"][f"Niveau{INFOS["Niveau"]}"]["ExoTexte"]["Consigne"]

        if self.indexTexte < len(self.textConsigne):
            self.indexTexte += 1
        # Mettre à jour le texte affiché
        self.displayed_text = self.textConsigne[:self.indexTexte]

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

        max_width = 400
        wrapped_lines = wrap_text(self.displayed_text, self.font, max_width)

        # Affichage des lignes
        y_offset = 30  # Position Y de départ
        line_height = self.font.size("Tg")[1]  # Hauteur d'une ligne
        for i, line in enumerate(wrapped_lines):
            line_surface = self.font.render(line, True, (0,0,0))
            self.interfaceExoSurface.blit(line_surface, (120, y_offset + i * line_height))
        

        self.interfaceExoSurface.blit(self.latexSurface, (10, 100))

    def start(self):
        self.infosBuild = self.ObjExoChoix.Choix()
        self.latexSurface = self.ObjRender.GetElement(self.infosBuild[0]) # on donne l'eqt


    def Update(self):
        #fermeture interface dans main
        self.interfaceExoSurface.fill("#ffffff")
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceExoSurface, (320,180))

