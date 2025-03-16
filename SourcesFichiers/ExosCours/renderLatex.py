from settings import *

class RenderLatex:

    def __init__(self) -> None:
        """Méthode initialisation class pour rendre des eqt latex en png
        Input / Ouput : None"""

        pass

    def Render(self, eqt : any, taille) -> any:
        """
        Convertit un texte LaTeX en une image rendue avec matplotlib.
        :param text: Le texte en LaTeX à afficher.
        :param fontsize: Taille de la police.
        :return: Surface pygame contenant l'image rendue.
        """
        plt.rcParams.update({
            "text.usetex": True,
            "text.latex.preamble": r"\usepackage{amsmath,textcomp}"  # Activation des packages
        })
        # Création de la figure matplotlib
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')

        # Rendu du texte LaTeX
        ax.text(0, 0, eqt, fontsize=taille, ha='center', va='center', wrap=True)

        # Sauvegarder l'image dans un buffer
        buf = BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1)
        buf.seek(0)

        # Charger l'image avec PIL et la recadrer
        image = Image.open(buf)
        bbox = image.getbbox()
        image = image.crop(bbox)
        plt.close(fig)

        # Convertir l'image PIL en surface Pygame
        mode = image.mode
        size = image.size
        data = image.tobytes()
        return pygame.image.fromstring(data, size, mode)


    def GetElement(self, eqt : any, taille) -> any:
        """Récupérer le png de l'equation latex. Input / Output : any (element pygame image)"""
        surfaceLatex = self.Render(eqt, taille)
        return surfaceLatex