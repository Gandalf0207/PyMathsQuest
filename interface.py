from settings import *

class SettingsInterface(object):
    def __init__(self, gestionnaire):
        self.displaySurface = pygame.display.get_surface()
        self.gestionnaire = gestionnaire

        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),  pygame.SRCALPHA)
        self.interfaceSurface.fill("#ffffff")

        self.font = pygame.font.Font(None, 36)
        self.titreText = "Settings"


    def BuildInterface(self):
        text = self.font.render(self.titreText, True, (0,0,0))
        self.interfaceSurface.blit(text, (10,10))

    def CloseInterface(self):
        self.gestionnaire.InterfaceOpen = False
        self.gestionnaire.INTERFACE_OPEN = False

    def Update(self):
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (320,180))


        # Fermer l'interface avec ESC
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:  # Fermer avec ESC
            self.CloseInterface()


class SoudInterface(object):
    def __init__(self, gestionnaire):
        self.displaySurface = pygame.display.get_surface()
        self.gestionnaire = gestionnaire

    def BuildInterface(self):
        pass

    def CloseInterface(self):
        self.gestionnaire.InterfaceOpen = False
        self.gestionnaire.INTERFACE_OPEN = False


    def Update(self):
        pass

class BundleInterface(object):
    def __init__(self, gestionnaire):
        self.displaySurface = pygame.display.get_surface()
        self.gestionnaire = gestionnaire

    def BuildInterface(self):
        pass

    def CloseInterface(self):
        self.gestionnaire.InterfaceOpen = False
        self.gestionnaire.INTERFACE_OPEN = False


    def Update(self):
        pass

class BookInterface(object):
    def __init__(self, gestionnaire):
        self.displaySurface = pygame.display.get_surface()
        self.gestionnaire = gestionnaire

    def BuildInterface(self):
        pass

    def CloseInterface(self):
        self.gestionnaire.InterfaceOpen = False
        self.gestionnaire.INTERFACE_OPEN = False


    def Update(self):
        pass