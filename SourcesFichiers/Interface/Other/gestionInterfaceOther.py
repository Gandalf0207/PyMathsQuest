from settings import *
from SourcesFichiers.Interface.Other.interfaceStartMenu import *
from SourcesFichiers.Interface.Other.interfaceEnd import *
from SourcesFichiers.Interface.Other.interfaceCredits import *

class GestionOtherInterface(object):

    def __init__(self, gestionnaire: any) -> None:
        """Initialisation de l'interface."""
        
        self.gestionnaire = gestionnaire
        self.homeInterface = HomeInterface(self)
        self.endInterface = EndInterface(self)
        self.creditInterface = CreditsInterfaceGame(self)
        self.creditsOn = False

    def Update(self, event, type) -> None:
        """Gestion des événements et mise à jour de l'interface."""

        if type == "Start":
            self.homeInterface.Update(event)
        elif type == "End" : 
            if not self.creditsOn :
                self.endInterface.Update(event)
            else:
                self.creditInterface.Update(event)
