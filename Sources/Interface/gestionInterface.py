from settings import *
from Sources.Interface.interfaceBook import *
from Sources.Interface.interfaceBundle import *
from Sources.Interface.interfaceMenuHome import *
from Sources.Interface.interfacePNJ import *
from Sources.Interface.interfaceReactor import *
from Sources.Interface.interfaceSettings import *
from Sources.Interface.interfaceSound import *
from Sources.Interface.interfaceExo import *


class GestionOtherInterfaces(object):
    def __init__(self, gestionnaire):
        
        self.gestionnaire = gestionnaire

        # interfaces globales
        self.isInterfaceOPEN = False # bool général
        self.isInterfaceHomeMenuOpen = False # bool menu home
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
        self.keepReactorObject = ReactorInterface()


        # timer click skip
        self.last_click_time = 0
        self.click_delay = 50    


    def CloseAllInterface(self):

        INFOS["Exo"] = False

        # interfaces globales
        self.isInterfaceOPEN = False
        self.isInterfaceHomeMenuOpen = False 
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


    def GestionInterfaceGlobale(self, event):
        # interface element hotbar hotbar
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
            if self.isInterfaceExoOpen:
                INFOS["Exo"] = False
            self.CloseAllInterface()
            # on réinitialise les niveaux audio.
            self.gestionnaire.GameTool.gestionSoundDialogues.StopDialogue()

        elif event.key == KEYSBIND["echap"]:
            self.isInterfaceOPEN = True
            self.isInterfaceHomeMenuOpen = True
            self.interface = HomeMenuInterface(self)

    
    def MiseAJourInterfaceExo(self, interfaceOBJ):
        
        self.isInterfaceOPEN = True
        self.isInterfaceExoOpen = True
        self.interface = interfaceOBJ


    def GestionInterfaceSpecifique(self, argsSpecifique = None, ElementSelfClass = None):
        
        #timer pour évier le spam
        current_time = pygame.time.get_ticks()
        if current_time - self.last_click_time > self.click_delay:
            self.last_click_time = current_time


            if self.interface != None and self.isInterfaceOPEN and argsSpecifique not in ["PNJOpen", "PNJClose"]:
                self.CloseAllInterface()
            else:
                
                if argsSpecifique == "Settings":
                    self.isInterfaceOPEN = True # update element global
                    self.isInterfaceSettingsOpen = True
                    self.interface = SettingsInterface(ElementSelfClass)

                elif argsSpecifique == "Sound":
                    self.isInterfaceOPEN = True # update element global
                    self.isInterfaceSoundOpen = True
                    self.interface = SoundInterface(ElementSelfClass)

                elif argsSpecifique == "Bundle":
                    self.isInterfaceOPEN = True # update element global
                    self.isInterfaceBundleOpen = True
                    self.interface = BundleInterface(ElementSelfClass)

                elif argsSpecifique == "Book":
                    self.isInterfaceOPEN = True # update element global
                    self.isInterfaceBookOpen = True
                    self.interface = BookInterface(ElementSelfClass)
                
                elif argsSpecifique == "PNJOpen":
                    if not self.isPNJInterfaceOpen:
                        self.isInterfaceOPEN = True # update element global
                        self.isPNJInterfaceOpen = True
                        self.interface = PNJInterface(ElementSelfClass)
                
                elif argsSpecifique == "PNJClose":
                    if self.isPNJInterfaceOpen:
                        self.CloseAllInterface()    
                
                elif argsSpecifique == "ReactorBloc":
                    self.isInterfaceOPEN = True # update element global
                    self.isInterfaceRectorOpen = True
                    self.interface = self.keepReactorObject
                
                # other interace : EssenceBloc / LancementBloc

    def Update(self, event):

        #sécurité
        if not self.isInterfaceOPEN:
            self.CloseAllInterface() 

        if self.interface:
            self.interface.Update(event)

