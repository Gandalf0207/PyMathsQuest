from settings import *

class BundleInterface(object):

    def __init__(self, gestionnaire: any) ->None:
        """Méthode initialisation de l'interface de bundle.
        Input : gestionnaire = self méthode d'appel"""
        
        # Initialisation
        self.gestionnaire = gestionnaire
        
        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),  pygame.SRCALPHA)
        self.interfaceSurface.fill((0,0,0,255))

        # close interface cross
        self.surfaceCloseCross = pygame.Surface((24,24), pygame.SRCALPHA)
        self.isCrossCloseHover = False
        self.crossClose = pygame.image.load(join("Image", "Interface", "Croix", "x-mark.png")).convert_alpha()
        self.crossClose2 = pygame.image.load(join("Image", "Interface", "Croix", "x-mark2.png")).convert_alpha()

        self.bundleBcg = pygame.image.load(join("Image", "Interface", "Inventaire.png")).convert_alpha()
        self.interfaceSurface.blit(self.bundleBcg, (0,0))


        # load image
        self.LoadImage()
        self.CreateElementRect()


    def LoadImage(self) -> None:
        """Méthode chargement des images Input / Output : None"""

        self.planks = pygame.image.load(join("Image", "Item", "PlanksItem.png")).convert_alpha()
        self.oldAxe = pygame.image.load(join("Image", "Item", "OldAxeItem.png")).convert_alpha()
        self.pickaxe = pygame.image.load(join("Image", "Item", "Pickaxe.png")).convert_alpha()
        self.boat = pygame.image.load(join("Image", "Item", "Boat.png")).convert_alpha()
        self.keys = pygame.image.load(join("Image", "Item", "Keys.png")).convert_alpha()
        self.showel = pygame.image.load(join("Image", "Item", "OldShovelItemx96.png")).convert_alpha()

    def CreateElementRect(self) -> None:
        """Méthode de création des slots et de leurs attributs
        Input / Output : None"""

        # surface slot inventaire
        self.surfaceSlot1 = pygame.Surface((96,96), pygame.SRCALPHA)
        self.surfaceSlot2 = pygame.Surface((96,96), pygame.SRCALPHA)
        self.surfaceSlot3 = pygame.Surface((96,96), pygame.SRCALPHA)
        self.surfaceSlot4 = pygame.Surface((96,96), pygame.SRCALPHA)
        self.surfaceSlot5 = pygame.Surface((96,96), pygame.SRCALPHA)
        self.surfaceSlot6 = pygame.Surface((96,96), pygame.SRCALPHA)
        self.surfaceSlot7 = pygame.Surface((96,96), pygame.SRCALPHA)
        self.surfaceSlot8 = pygame.Surface((96,96), pygame.SRCALPHA)
        self.surfaceSlot9 = pygame.Surface((96,96), pygame.SRCALPHA)
        self.surfaceSlot10 = pygame.Surface((96,96), pygame.SRCALPHA)
        self.surfaceSlot11 = pygame.Surface((96,96), pygame.SRCALPHA)
        self.surfaceSlot12 = pygame.Surface((96,96), pygame.SRCALPHA)

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
        self.interfaceSurface.fill((255,255,255,0))
        self.interfaceSurface.blit(self.bundleBcg, (0,0))

        indice = 0
        for key in INVENTORY: # pour tout les élément dans l'inventaire
            elementSlot = self.allSurfaceSlot[indice] # get slot
            elementSlot.fill((255,255,255, 0)) # clear slot

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
                elementSlot.fill((0,0,0,0))
                elementSlot.blit(surf, (0,0))

                # text nombre items
                textCount = FONT["FONT20"].render(f"{INVENTORY[key]}", True, (50,50,50))
                elementSlot.blit(textCount, (70,70))

                # affichage slot
                self.interfaceSurface.blit(elementSlot, self.coordsSurface[indice])


                indice += 1 # on change de slot

        # close element
        self.surfaceCloseCross.fill((0,0,0,0))
        self.rectCloseCross = pygame.Rect(self.interfaceSurface.get_width() - 34, 10, 24, 24)
        if self.isCrossCloseHover:
            self.surfaceCloseCross.blit(self.crossClose2, (0,0))
        else:
            self.surfaceCloseCross.blit(self.crossClose, (0,0))
        self.interfaceSurface.blit(self.surfaceCloseCross, (self.rectCloseCross.x, self.rectCloseCross.y))


    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (320,180)) # pos topleft

        if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):

            local_pos = GetLocalPos(event, self.interfaceSurface, (320, 180))
            if local_pos:
                if event.type == pygame.MOUSEMOTION:
                    # cross close interface
                    self.isCrossCloseHover = self.rectCloseCross.collidepoint(local_pos)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rectCloseCross.collidepoint(local_pos):
                        # fermeture interface
                        self.gestionnaire.CloseAllInterface()