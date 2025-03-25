from settings import *

class AdminInterface():
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.pnjGroup = self.gestionnaire.gestionnaire.allPNJ
        self.player = self.gestionnaire.gestionnaire.player

         # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),  pygame.SRCALPHA)
        self.interfaceSurface.fill((255,255,255))

        self.last_click_time = 0
        self.click_delay = 300

        self.hauteurAct =  100
        self.Outils()

    
    def Outils(self):
        self.btnPnjDico = {}
        self.nvBtn = {}
        self.coursBtn = {}
        self.otherBtn = {}

        # pnj button
        for pnj in self.pnjGroup:
            rect_button = pygame.Rect(85, self.hauteurAct, 75, 35)
            self.btnPnjDico[pnj.numPNJ] = rect_button
            self.hauteurAct += 40  # Espacement des boutons

        self.hauteurAct = 100

        # niveau btn
        listNv = ["NV1", "NV2", "NV3", "NV4"]
        for niveau in listNv:
            rect_niveau= pygame.Rect(185, self.hauteurAct, 75, 35)
            self.nvBtn[niveau] = rect_niveau
            self.hauteurAct += 40  # Espacement des boutons

        self.hauteurAct = 100

        # list add cours
        listCours = [ "+", "-"]
        for coursBtnElement in listCours:
            rect_cours= pygame.Rect(285, self.hauteurAct, 75, 35)
            self.coursBtn[coursBtnElement] = rect_cours
            self.hauteurAct += 40  # Espacement des boutons   

        self.hauteurAct = 100
        
        # other btn (no clip, demi nv, ouvrir exo)
        listOtherBtn = ["NoClip", "OpenExo", "DemiNV"]
        for btnOther in listOtherBtn:
            rect_btnOthers= pygame.Rect(385, self.hauteurAct, 75, 35)
            self.otherBtn[btnOther] = rect_btnOthers
            self.hauteurAct += 40  # Espacement des boutons   

        try:
            self.bcgImage = pygame.image.load(join("Image", "Interface", "Baseinterface.png")).convert_alpha()
            self.iggyImage = pygame.image.load(join("Image", "Interface", "Iggy.png")).convert_alpha()
            self.ImageInterface = pygame.Surface((100,100), pygame.SRCALPHA)
            self.ImageInterface.fill((255,255,255, 0))
            self.ImageInterface.blit(self.iggyImage, (0,0))
        except:
            INFOS["ErrorLoadElement"] = True



    def TpPlayerPnj(self, name):
        for pnj in self.pnjGroup:
            if pnj.numPNJ == name:
                self.player.hitbox_rect.center = (pnj.pos[0]*CASEMAP, pnj.pos[1]*CASEMAP)
                self.player.rect.center = (pnj.pos[0]*CASEMAP, pnj.pos[1]*CASEMAP)

    def ChangeNv(self, nv):
        INFOS["AdminReset"] = True

        if nv == "NV1":
            nvName = "NiveauPlaineRiviere"
        elif nv == "NV2":
            nvName = "NiveauMedievale"
        elif nv == "NV3":
            nvName = "NiveauBaseFuturiste"
        elif nv == "NV4":
            nvName = "NiveauMordor"

        NIVEAU["Map"] = nvName
        INFOS["ExoPasse"] = True
    
    def ChangeCours(self, element):
        if element == "+":
            INFOS["GetCours"] += 1
        else:
            if INFOS["GetCours"] > 1:
                INFOS["GetCours"] -= 1
        
        print(INFOS["GetCours"])

    def OtherBtnGestion(self, btnType):
        if btnType == "NoClip":
            if INFOS["NoClip"]:
                INFOS["NoClip"] = False
            else:
                INFOS["NoClip"] = True
        
        elif btnType == "OpenExo":
            if NIVEAU["Map"] not in ["NiveauPlaineRiviere", "NiveauMordor"]:
                self.gestionnaire.gestionnaire.demiNiveau = True # evite le rechargement
                INFOS["DemiNiveau"] = True                 
            INFOS["Exo"] = True # lancement exo dans main (changement variable)
        
        elif btnType == "DemiNV":
            if NIVEAU["Map"] != "NiveauPlaineRiviere":
                INFOS["DemiNiveau"] = True  

    def BuildInterface(self) -> None:
        """Méthode : Création de tout les éléments composant l'interface. Input / Output : None"""

        # base
        self.interfaceSurface.blit(self.bcgImage, (0,0))
        self.interfaceSurface.blit(self.ImageInterface, (self.interfaceSurface.get_width()-120, self.interfaceSurface.get_height()-120))

        # titre
        TitreT = FONT["FONT36"].render(TEXTE["Elements"]["AdminPanel"]["Title"], True, BLACK)
        self.interfaceSurface.blit(TitreT, (10, 10))  

        listText = ["TP", "Niveau", "Cours", "Autre"]  
        for i, text in enumerate(listText):
            textE = FONT["FONT24"].render(TEXTE["Elements"]["AdminPanel"][text], True, BLACK)   
            self.interfaceSurface.blit(textE, ((85 + 100*i), 80))  

        # Dessiner les boutons dans le panneau admin
        for name, rect in self.btnPnjDico.items():
            pygame.draw.rect(self.interfaceSurface, (200,200,200), rect)
            pygame.draw.rect(self.interfaceSurface, BLACK, rect, 2)  # Bordure
            text_surface = FONT["FONT16"].render(name, True, WHITE)
            self.interfaceSurface.blit(text_surface, (rect.x + (rect.width - text_surface.get_width()) // 2, rect.y + 10))

        # niveau
        for name, rect in self.nvBtn.items():
            pygame.draw.rect(self.interfaceSurface, (200,200,200), rect)
            pygame.draw.rect(self.interfaceSurface, BLACK, rect, 2)  # Bordure
            text_surface = FONT["FONT16"].render(name, True, WHITE)
            self.interfaceSurface.blit(text_surface, (rect.x + (rect.width - text_surface.get_width()) // 2, rect.y + 10))

        # cours btn
        for name, rect in self.coursBtn.items():
            pygame.draw.rect(self.interfaceSurface, (200,200,200), rect)
            pygame.draw.rect(self.interfaceSurface, BLACK, rect, 2)  # Bordure
            text_surface = FONT["FONT16"].render(name, True, WHITE)
            self.interfaceSurface.blit(text_surface, (rect.x + (rect.width - text_surface.get_width()) // 2, rect.y + 10))

        # other btn 
        for name, rect in self.otherBtn.items():
            color = (200,200, 200)
            if name == "NoClip" and INFOS["NoClip"]:
                color = (112, 193, 255)
            pygame.draw.rect(self.interfaceSurface, color, rect)
            pygame.draw.rect(self.interfaceSurface, BLACK, rect, 2)  # Bordure
            text_surface = FONT["FONT16"].render(name, True, WHITE)
            self.interfaceSurface.blit(text_surface, (rect.x + (rect.width - text_surface.get_width()) // 2, rect.y + 10))
 

    def Update(self, event) -> None:
        """Méthode d'update de l'interface. Input / Output : None"""

        # construction d'update
        self.BuildInterface()
        self.displaySurface.blit(self.interfaceSurface, (320,180)) # pos topleft

        if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time
                
                local_pos = GetLocalPos(event, self.interfaceSurface, (320, 180))
                if local_pos:
                    if event.type == pygame.MOUSEMOTION:
                        # cross close interface
                        pass

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for name, rect in self.btnPnjDico.items():
                            if rect.collidepoint(local_pos):
                                self.TpPlayerPnj(name)
                        for nv, rect in self.nvBtn.items():
                            if rect.collidepoint(local_pos):
                                self.ChangeNv(nv)
                        for cours, rect in self.coursBtn.items():
                            if rect.collidepoint(local_pos):
                                self.ChangeCours(cours)
                        for otherBtn, rect in self.otherBtn.items():
                            if rect.collidepoint(local_pos):
                                self.OtherBtnGestion(otherBtn)