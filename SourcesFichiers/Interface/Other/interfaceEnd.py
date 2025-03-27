#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

from settings import *
from SourcesFichiers.Ressources.PyMathsMaKEpdf import *

class EndInterface():
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire

        # Création éléments
        self.displaySurface = pygame.display.get_surface() # surface générale
        self.interfaceSurface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT),  pygame.SRCALPHA)
        self.interfaceSurface.fill((0,0,0,0))

        self.isHoverBtnQuitter = False
        self.isHoverBtnPDF = False
        self.isPDF = False
        try :
            self.btnTexture = pygame.image.load(join("Image","Interface", "Button", "Start.png")).convert_alpha()
            self.btnTextureHover = pygame.image.load(join("Image","Interface", "Button", "StartHover.png")).convert_alpha()

            self.medailleDiament = pygame.image.load(join("Image", "Medaille", "Diament.png"))
            self.medailleOr = pygame.image.load(join("Image", "Medaille", "Or.png"))
            self.medailleArgent = pygame.image.load(join("Image", "Medaille", "Argent.png"))
            self.medailleBronze = pygame.image.load(join("Image", "Medaille", "Bronze.png"))
            self.bcgEnd = pygame.image.load(join("Image", "Interface", "End.png"))

        except:
            INFOS["ErrorLoadElement"] = True

        self.medailleSurface = pygame.Surface((128, 128), pygame.SRCALPHA)



        self.percentageReussite = None


        # timer click btn delays
        self.last_click_time = 0
        self.click_delay = 500  

    def GetReussite(self):
            # récupération des valeurs stocké dans le json
        win = INFOS["ExoReussit"]
        total = INFOS["TotalExo"]
        self.percentageReussite = int(round(win/total, 3)*100)

        if self.percentageReussite == 100:
            self.medailleSurface.blit(self.medailleDiament,(0,0) )
        elif self.percentageReussite >= 80:
            self.medailleSurface.blit(self.medailleOr, (0,0))
        elif self.percentageReussite >=40:
            self.medailleSurface.blit(self.medailleArgent, (0,0))
        else :
            self.medailleSurface.blit(self.medailleBronze, (0,0))

    def SavePdf(self):
        
        # aide ia / internet pour l'ouverture d'un interface window de path
        from ctypes import wintypes
        # Structure pour le filtre des fichiers (PDF uniquement)
        class OPENFILENAME(ctypes.Structure):
            _fields_ = [
                ("lStructSize", wintypes.DWORD),
                ("hwndOwner", wintypes.HWND),
                ("hInstance", wintypes.HINSTANCE),
                ("lpstrFilter", wintypes.LPCWSTR),
                ("lpstrCustomFilter", wintypes.LPWSTR),
                ("nMaxCustFilter", wintypes.DWORD),
                ("nFilterIndex", wintypes.DWORD),
                ("lpstrFile", wintypes.LPWSTR),
                ("nMaxFile", wintypes.DWORD),
                ("lpstrFileTitle", wintypes.LPWSTR),
                ("nMaxFileTitle", wintypes.DWORD),
                ("lpstrInitialDir", wintypes.LPCWSTR),
                ("lpstrTitle", wintypes.LPCWSTR),
                ("Flags", wintypes.DWORD),
                ("nFileOffset", wintypes.WORD),
                ("nFileExtension", wintypes.WORD),
                ("lpstrDefExt", wintypes.LPCWSTR),
                ("lCustData", wintypes.LPARAM),
                ("lpfnHook", wintypes.LPVOID),
                ("lpTemplateName", wintypes.LPCWSTR),
            ]

        ofn = OPENFILENAME()
        
        buffer = ctypes.create_unicode_buffer(260)  # Stocke le chemin sélectionné
        buffer.value = "PyMathsQuestCorrectionsExercices"
        ofn.lStructSize = ctypes.sizeof(OPENFILENAME)
        ofn.lpstrFilter = "PDF Files\0*.pdf\0All Files\0*.*\0"
        ofn.lpstrFile = ctypes.cast(buffer, wintypes.LPWSTR) 
        ofn.nMaxFile = 260
        ofn.lpstrDefExt = "pdf"
        ofn.lpstrTitle = "Enregistrer le fichier PDF"

        if ctypes.windll.comdlg32.GetSaveFileNameW(ctypes.byref(ofn)):
            return buffer.value  # Retourne le chemin choisi par l'utilisateur
        
        return None  # Si l'utilisateur annule

    def PdfGeneration(self):
        objMakePDF = MakePDFWithPyMaths()
        objMakePDF.GetExoValues()
        objMakePDF.GenerateCorrection()

        filePath  =  self.SavePdf()
        if not filePath:
            filePath = "PyMaths.pdf"
        objMakePDF.CompilPDF(filePath)
        self.gestionnaire.gestionnaire.checkLoadingDone = True



    def BluidInterface(self):
        
        # texte titre
        self.interfaceSurface.blit(self.bcgEnd, (0,0))
        textT = FONT["FONT74"].render(TEXTE["Elements"]["GameName"], True, (10,10,10))
        self.interfaceSurface.blit(textT, textT.get_rect(center=(self.interfaceSurface.get_width()//2 , 50)))

        textR = f"{TEXTE["Elements"]["Reussite"]} {self.percentageReussite} %"
        textReussite = FONT["FONT36"].render(textR, True, (10,10,10))
        self.interfaceSurface.blit(textReussite, textReussite.get_rect(center=(self.interfaceSurface.get_width()//2, 150)))

        # medaille
        self.interfaceSurface.blit(self.medailleSurface, self.medailleSurface.get_rect(center =( self.interfaceSurface.get_width()//2, 250)))
        
        #pourcentage réussite"


        # btn crédits
        self.surfaceBtnPDF = pygame.Surface((350, 100))
        self.btnRectPDF = pygame.Rect(((WINDOW_WIDTH//2) - self.surfaceBtnPDF.get_width() //2), 425, 350, 100)
        if self.isHoverBtnPDF or self.isPDF:
            self.surfaceBtnPDF.blit(self.btnTextureHover, (0,0))
        else:
            self.surfaceBtnPDF.blit(self.btnTexture, (0,0))

        self.textP = TEXTE["Elements"]["InterfaceEnd"]["PDFGeneration"] if not self.isPDF else TEXTE["Elements"]["InterfaceEnd"]["PDFGenere"]
        self.textPDF = FONT["FONT30"].render(self.textP, True, (10,10,10))
        self.surfaceBtnPDF.blit(self.textPDF, self.textPDF.get_rect(center=(self.surfaceBtnPDF.get_width()//2, self.surfaceBtnPDF.get_height()//2)))
        self.interfaceSurface.blit(self.surfaceBtnPDF, (self.btnRectPDF.x, self.btnRectPDF.y))

        # btn leave
        self.surfaceBtnQuitter = pygame.Surface((350, 100), pygame.SRCALPHA)
        self.btnRectQuitter = pygame.Rect(((WINDOW_WIDTH//2) - self.surfaceBtnQuitter.get_width() //2), 550, 350, 100)
        if self.isHoverBtnQuitter:
            self.surfaceBtnQuitter.blit(self.btnTextureHover, (0,0))
        else:
            self.surfaceBtnQuitter.blit(self.btnTexture, (0,0))

        self.textQ = TEXTE["Elements"]["InterfaceEnd"]["Quitter"]
        self.textQuitter = FONT["FONT50"].render(self.textQ, True, (10,10,10))
        self.surfaceBtnQuitter.blit(self.textQuitter, self.textQuitter.get_rect(center=(self.surfaceBtnQuitter.get_width()//2, self.surfaceBtnQuitter.get_height()//2)))
        self.interfaceSurface.blit(self.surfaceBtnQuitter, (self.btnRectQuitter.x, self.btnRectQuitter.y))

        pass

    def Update(self, event):

        if self.percentageReussite == None:
            self.GetReussite()

        # construction d'update
        self.BluidInterface()
        self.displaySurface.blit(self.interfaceSurface, (0, 0)) # pos topleft

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # delay de click
            current_time = pygame.time.get_ticks()
            if current_time - self.last_click_time > self.click_delay:
                self.last_click_time = current_time
            

                if self.btnRectPDF.collidepoint(event.pos) and not self.isPDF: # générer le pdf
                    self.isPDF = True
                    self.gestionnaire.gestionnaire.checkLoadingDone = False
                    self.gestionnaire.gestionnaire.fondu_au_noir()
                    threading.Thread(target=self.PdfGeneration, daemon=True).start()
                    
                    self.gestionnaire.gestionnaire.ChargementEcran()


                if self.btnRectQuitter.collidepoint(event.pos):
                    self.gestionnaire.creditsOn = True

        if event.type == pygame.MOUSEMOTION:
            # Obtenir la position locale de la souris dans l'interface
            hovered_btn = None
            if self.btnRectPDF.collidepoint(event.pos) and not self.isPDF:
                hovered_btn = "PDF"
            if self.btnRectQuitter.collidepoint(event.pos):
                hovered_btn = "Quitter"

            # Mise à jour des états des boutons
            self.isHoverBtnPDF = (hovered_btn == "PDF")
            self.isHoverBtnQuitter = (hovered_btn == "Quitter")

            # Modifier le curseur si sur un bouton, sinon le réinitialiser
            INFOS["Hover"] = bool(hovered_btn)