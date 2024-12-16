from settings import *

class SettingsInterface(object):
    def __init__(self, gestionnaire):
        self.displaySurface = pygame.display.get_surface()
        self.gestionnaire = gestionnaire

    def BuildInterface(self):
        pass

    def CloseInterface(self):
        self.gestionnaire.InterfaceOpen = False

    def Update(self):
        pass

class SoudInterface(object):
    def __init__(self, gestionnaire):
        self.displaySurface = pygame.display.get_surface()
        self.gestionnaire = gestionnaire

    def BuildInterface(self):
        pass

    def CloseInterface(self):
        self.gestionnaire.InterfaceOpen = False

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

    def Update(self):
        pass