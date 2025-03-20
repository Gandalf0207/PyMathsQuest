from settings import *
from SourcesFichiers.Interface.Game.interfaceBook import *
from SourcesFichiers.Interface.Game.interfaceBundle import *
from SourcesFichiers.Interface.Game.interfaceMenuHome import *
from SourcesFichiers.Interface.Game.interfacePNJ import *
from SourcesFichiers.Interface.Game.interfaceReactor import *
from SourcesFichiers.Interface.Game.interfaceSettings import *
from SourcesFichiers.Interface.Game.interfaceSound import *
from SourcesFichiers.Interface.Game.interfaceExo import *
from SourcesFichiers.Interface.Other.interfaceCredits import *


class GestionGameInterfaces(object):
    def __init__(self, gestionnaire, gestionSoundFond, gestionCours):
        
        self.gestionnaire = gestionnaire
        self.gestionSoundFond = gestionSoundFond
        self.gestionCours = gestionCours

        # interfaces globales
        self.isInterfaceOPEN = False # bool général
        self.isInterfaceHomeMenuOpen = False # bool menu home
        self.isInterfaceCreditOpen = False
        self.isPNJInterfaceOpen = False # bool PNJ
        self.isInterfaceExoOpen = False # bool exo

        # interface map 3
        self.isInterfaceRectorOpen = False # bool reactor
        
        # hotbar bol check
        self.isInterfaceSettingsOpen = False # bool settings
        self.isInterfaceSoundOpen = False # bool volume
        self.isInterfaceBundleOpen = False # bool bundle
        self.isInterfaceBookOpen = False # bool book

        # element d'update
        self.interface = None

        # sauvgarde des obj qui ne doivent pas etre reset : 
        self.keepReactorObject = ReactorInterface(self)


        # timer click skip
        self.last_click_time = 0
        self.click_delay = 50    


    def CloseAllInterface(self):
        if INFOS:
            INFOS["TotalExo"] += 1 #abandon de l'exo (fermure de la fenetre)
        INFOS["Exo"] = False

        # interfaces globales
        self.isInterfaceOPEN = False
        self.isInterfaceHomeMenuOpen = False 
        self.isInterfaceCreditOpen = False
        self.isPNJInterfaceOpen = False 
        self.isInterfaceExoOpen = False 

        # interface map 3
        self.isInterfaceRectorOpen = False 
        
        # hotbar bol check
        self.isInterfaceSettingsOpen = False
        self.isInterfaceSoundOpen = False 
        self.isInterfaceBundleOpen = False 
        self.isInterfaceBookOpen = False 

        # reset 
        self.interface = None

        INFOS["HideHotBar"] = False
        INFOS["Hover"] = False # reset cursor

    def GestionInterfaceGlobale(self, event):
        # interface element hotbar hotbar
        if not self.isInterfaceCreditOpen:
            if event.key == KEYSBIND["settings"]:
                self.GestionInterfaceSpecifique("Settings")
            elif event.key == KEYSBIND["sound"]:
                self.GestionInterfaceSpecifique("Sound")
            elif event.key == KEYSBIND["inventory"]:
                self.GestionInterfaceSpecifique("Bundle")
            elif event.key == KEYSBIND["book"]:
                self.GestionInterfaceSpecifique("Book")


        # close interface open
        if event.key == KEYSBIND["echap"] and self.isInterfaceOPEN: # Close général interface build
            
            if self.isInterfaceCreditOpen:
                self.MiseAJourInterfaceCredits()
            elif self.isInterfaceExoOpen:
                INFOS["Exo"] = False
                self.CloseAllInterface()
            else:
                self.CloseAllInterface()

            INFOS["Hover"] = False # reset cursor
            # on réinitialise les niveaux audio.
            self.gestionnaire.GameTool.gestionSoundDialogues.StopDialogue()

        elif event.key == KEYSBIND["echap"]:
            self.isInterfaceOPEN = True
            self.isInterfaceHomeMenuOpen = True
            self.interface = HomeMenuInterface(self)
            INFOS["Hover"] = False # reset cursor

    def MiseAJourInterfaceCredits(self):
        if self.isInterfaceCreditOpen:
            self.isInterfaceOPEN = True
            self.isInterfaceCreditOpen = False
            self.isInterfaceSettingsOpen = True
            self.interface = HomeMenuInterface(self)     
        else:
            self.isInterfaceOPEN = True
            self.isInterfaceCreditOpen = True
            self.isInterfaceSettingsOpen = False
            self.interface = CreditsInterfaceGame(self)       
        INFOS["Hover"] = False # reset cursor

    
    def MiseAJourInterfaceExo(self, interfaceOBJ):
        
        self.isInterfaceOPEN = True
        self.isInterfaceExoOpen = True
        self.interface = interfaceOBJ


    def GestionInterfaceSpecifique(self, argsSpecifique, elementSelf = None):
        
        #timer pour évier le spam
        current_time = pygame.time.get_ticks()
        if current_time - self.last_click_time > self.click_delay:
            self.last_click_time = current_time

            if self.interface != None and elementSelf != None and argsSpecifique not in ["PNJOpen", "PNJClose"] :
                pass
            elif self.interface != None and self.isInterfaceOPEN and argsSpecifique not in ["PNJOpen", "PNJClose"]:
                self.CloseAllInterface()
            else:
                
                if argsSpecifique == "Settings":
                    self.isInterfaceOPEN = True # update element global
                    self.isInterfaceSettingsOpen = True
                    self.interface = SettingsInterface(self)
                    INFOS["Hover"] = False # reset cursor


                elif argsSpecifique == "Sound":
                    self.isInterfaceOPEN = True # update element global
                    self.isInterfaceSoundOpen = True
                    self.interface = SoundInterface(self)
                    INFOS["Hover"] = False # reset cursor


                elif argsSpecifique == "Bundle":
                    self.isInterfaceOPEN = True # update element global
                    self.isInterfaceBundleOpen = True
                    self.interface = BundleInterface(self)
                    INFOS["Hover"] = False # reset cursor


                elif argsSpecifique == "Book":
                    self.isInterfaceOPEN = True # update element global
                    self.isInterfaceBookOpen = True
                    self.interface = BookInterface(self, self.gestionCours)
                    INFOS["Hover"] = False # reset cursor

                
                elif argsSpecifique == "PNJOpen":
                    if not self.isPNJInterfaceOpen:
                        self.isInterfaceOPEN = True # update element global
                        self.isPNJInterfaceOpen = True
                        self.interface = PNJInterface(elementSelf)
                    INFOS["Hover"] = False # reset cursor

                
                elif argsSpecifique == "PNJClose":
                    if self.isPNJInterfaceOpen:
                        self.CloseAllInterface() 
                        self.gestionnaire.GameTool.gestionSoundDialogues.StopDialogue()


                elif argsSpecifique == "ReactorBloc":
                    self.isInterfaceOPEN = True # update element global
                    self.isInterfaceRectorOpen = True
                    self.interface = self.keepReactorObject
                    INFOS["Hover"] = False # reset cursor


                

    def Update(self, event):

        if self.interface:
            INFOS["HideHotBar"] = True
            self.interface.Update(event)


