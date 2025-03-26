from settings import *
from SourcesFichiers.Elements.sprites import *

class Interactions(object):

    def __init__(self, gestionnaire : any, gameInterfaces) -> None:
        """Méthode initialisation de la gestion avec les interactions (pont, rocher... ) sauf pnj
        Input : gestionanire (self parent)
        Output : None"""

        self.displaySurface = pygame.display.get_surface() # surface générale
        self.gestionnaire = gestionnaire
        self.gameInterfaces = gameInterfaces
        self.player = None

        # element interactions
        self.camera_offset = [0,0]
        self.npc_screen_pos = [0,0]
        self.distanceMax = 150 # depuis centre element pont

        # infos de la map 
        self.map_width = LONGUEUR * CASEMAP
        self.map_height = LARGEUR * CASEMAP

        # infos pont coords
        self.Obj = None
        self.coordObjActuel = None
        self.ObjectId = None

        # groupe interactions
        self.interactionGroup = None

        # stockag value 
        self.GetCoursTableCraft = False 
        self.boatPlacementPlayerPos = []
        self.electricityOn = False

        # stockage value
        self.pot  = False
        self.parchemin = False


    def Interagir(self, groups, interactionGroups) -> None:
        """Méthode de calcul d'interaction entre chaque element en fonction des niveaux
        Input / Output : None"""

        if self.Isclose(): # si proximité


            # niveau 0
            if NIVEAU["Map"] == "NiveauPlaineRiviere":
                # animation 
                self.gestionnaire.fondu_au_noir()

                # action si c'est un pont 
                if self.ObjectId == "Pont1" or self.ObjectId == "Pont2" or self.ObjectId == "Pont3":
                    if not self.Obj.InfoExo: # si c'est pas le pont d'exo
                        # text animation
                        self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["TraverserPont"])

                        # deplacement player
                        if self.player.rect.x < self.coordObjActuel[0]:
                            self.player.rect.x = self.coordObjActuel[0] + CASEMAP
                            STATE_HELP_INFOS[0] = "SeePNJ" # update tips player
                        else:
                            self.player.rect.x = self.coordObjActuel[0] - CASEMAP
                            STATE_HELP_INFOS[0] = "CrossBridge" # update tips player
                        self.player.rect.y = self.coordObjActuel[1]
                        self.player.hitbox_rect.center = self.player.rect.center
                        
                        # fin animation
                        self.gestionnaire.ouverture_du_noir(self.player.rect.center)

                    else: # si c'est le pont exo
                        INFOS["Exo"] = True # lancement exo dans main (changement variable)
                        self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["MakeExo"]) # text animation
                    
                # si c'est le rocher qui est destructible
                elif self.ObjectId == "ExitRock":
                    self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["BreakRock"]) # text 

                    self.Obj.kill() # destrcution rocher

                    STATE_HELP_INFOS[0] = "CrossBridge"
                    self.gestionnaire.ouverture_du_noir(self.player.rect.center) # fin animation


            elif NIVEAU["Map"] == "NiveauMedievale":
                

                if self.ObjectId == "Arbre" or self.ObjectId == "Arbre1" or self.ObjectId == "Souche" or self.ObjectId == "Souche1" :
                        # animation 
                        pos = self.Obj.pos
                        #gestion arbre
                        self.Obj.kill()
                        
                        self.gestionnaire.fondu_au_noir()
                        # texte animation
                        if self.ObjectId in ["Arbre", "Arbre1"]:
                            self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["CutTree"])
                        else:
                            self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["RemoveSouche"])

                        if self.ObjectId == "Arbre":
                            #creation souche
                            try :
                                soucheArbre = pygame.image.load(join("Image", "Obstacle", "Souche.png")).convert_alpha()
                                groups = (groups[0], groups[1], interactionGroups)
                                CollisionSprites(pos, soucheArbre,  "Souche", groups)
                            except:
                                INFOS["ErrorLoadElement"] = True
                            INVENTORY["Planks"] += 1

                        elif self.ObjectId == "Arbre1": 
                            try :
                                soucheArbre2 = pygame.image.load(join("Image", "Obstacle", "Souche2.png")).convert_alpha()
                                groups = (groups[0], groups[1], interactionGroups)
                                CollisionSprites(pos, soucheArbre2,  "Souche1", groups)
                            except:
                                INFOS["ErrorLoadElement"] = True
                            INVENTORY["Planks"] += 2

                        elif self.ObjectId == "Souche" or self.ObjectId == "Souche1":
                            #creation boue
                            try :
                                boueImage = pygame.image.load(join("Image", "Sol", "Mud.png")).convert_alpha()
                                Sprites(pos, boueImage, "Mud", groups[0]) # création de la boue
                            except:
                                INFOS["ErrorLoadElement"] = True
                            INVENTORY["Planks"] += 1 if self.ObjectId == "Souche" else 2


                        # réouverture
                        self.gestionnaire.ouverture_du_noir(self.player.rect.center)
                
                # action si c'est un pont 
                if self.ObjectId == "Pont2":
                    # animation 
                    self.gestionnaire.fondu_au_noir()

                    if not self.Obj.InfoExo: # si c'est pas le pont d'exo
                        # text animation
                        self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["TraverserPont"])

                        # deplacement player
                        if self.player.rect.x < self.coordObjActuel[0]:
                            self.player.rect.x = self.coordObjActuel[0] + CASEMAP
                            STATE_HELP_INFOS[0] = "SeePNJ" # update tips player
                        else:
                            self.player.rect.x = self.coordObjActuel[0] - CASEMAP
                            STATE_HELP_INFOS[0] = "CrossBridge" # update tips player
                        
                        self.player.rect.y = self.coordObjActuel[1]
                        self.player.hitbox_rect.center = self.player.rect.center
                        
                        # fin animation
                        self.gestionnaire.ouverture_du_noir(self.player.rect.center)

                if self.ObjectId == "Pont4":
                    # animation 
                    self.gestionnaire.fondu_au_noir()

                    # deplacement player
                    if self.player.rect.y < self.coordObjActuel[1]:
                        self.player.rect.y = self.coordObjActuel[1] + CASEMAP*2
                        # text animation
                        self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["TraverserPont"])

                        # action pour traverser
                        STATE_HELP_INFOS[0] = "SeePNJ" # update tips player
                    else:
                        self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["CantTraverserPont"])

                    self.player.rect.x = self.coordObjActuel[0]
                    self.player.hitbox_rect.center = self.player.rect.center
                    
                    # fin animation
                    self.gestionnaire.ouverture_du_noir(self.player.rect.center)  

                # table de craft interactions
                if self.ObjectId == "TableCraft":
                    # animation 
                    self.gestionnaire.fondu_au_noir()

                    if not self.GetCoursTableCraft and NIVEAU["Niveau"] == "Seconde":  # get du cours uniquement sur le cours de seconde
                        self.GetCoursTableCraft = True
                        INFOS["GetCours"] +=1
                        self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["GetCours"])

                    if INVENTORY["Planks"] < 3:
                        self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["NeedPlanks"])
                    else:
                        self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["CraftBoat"])
                        INVENTORY["Planks"] -= 3
                        INVENTORY["Boat"] += 1
                        STATE_HELP_INFOS[0] = "PlaceBoat" # update tips player

                    self.gestionnaire.ouverture_du_noir(self.player.rect.center)

                
                if self.ObjectId == "BoatObj":
                    # animation 
                    self.gestionnaire.fondu_au_noir()

                    # check pos player et pos de référence
                    coordsPtsRefRiverTpChateau = LoadJsonMapValue("coordsMapObject", "RiverBoatTPChateau coords")
                    coordsBoat = [(self.Obj.pos[0]) // CASEMAP, (self.Obj.pos[1]) // CASEMAP ] 

                    if coordsPtsRefRiverTpChateau != coordsBoat : 
                        # texte animation : 
                        self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["UseBoat"])

                        # sauvgarde pos
                        self.boatPlacementPlayerPos = [self.Obj.pos, self.player.rect.center] # sauvgarde
                        
                        # deplacement bateau
                        self.Obj.pos = (coordsPtsRefRiverTpChateau[0]*CASEMAP, coordsPtsRefRiverTpChateau[1]*CASEMAP)
                        self.Obj.hitbox.topleft = self.Obj.pos
                        self.Obj.rect.topleft = self.Obj.hitbox.topleft
                        
                        # deplacement player
                        self.player.hitbox_rect.center = ((coordsPtsRefRiverTpChateau[0]+1)*CASEMAP +64, coordsPtsRefRiverTpChateau[1]*CASEMAP +64 ) # +64 center case à coté
                        self.player.rect.center = self.player.hitbox_rect.center
                        

                        STATE_HELP_INFOS[0] = "SeePNJ"

                    else:
                        # texte animation : 
                        self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["UseBoat2"])

                        # deplacement bateau
                        self.Obj.pos = self.boatPlacementPlayerPos[0]
                        self.Obj.hitbox.topleft = self.Obj.pos
                        self.Obj.rect.topleft = self.Obj.hitbox.topleft
                        
                        # deplacement player
                        self.player.hitbox_rect.center = self.boatPlacementPlayerPos[1] 
                        self.player.rect.center = self.player.hitbox_rect.center
                        
                        STATE_HELP_INFOS[0] = "NavigateBoat"

                        
                    self.gestionnaire.ouverture_du_noir(self.player.rect.center)


                # interaction porte chateau
                if self.ObjectId == "DoorChateau":
                    INVENTORY["Key"] -=1
                    # animation 
                    self.gestionnaire.fondu_au_noir()

                    INFOS["DemiNiveau"] = True      
                    STATE_HELP_INFOS[0] = "SeePNJRoi"   

                # interaction cerlce exo map n°2
                if self.ObjectId == "CerclePortal":
                    # animation 
                    self.gestionnaire.fondu_au_noir()
                    
                    INFOS["Exo"] = True # lancement exo dans main (changement variable)
                    self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["MakeExo"]) # text animation
            


            elif NIVEAU["Map"] == "NiveauBaseFuturiste":

                if self.ObjectId == "ReactorBloc":
                    self.gameInterfaces.GestionInterfaceSpecifique("ReactorBloc")

                # vent tp 
                if self.ObjectId == "Vent":
                    # animation 
                    self.gestionnaire.fondu_au_noir()

                    self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["UseVent"]) # text animation
                    coordsVentActuel = [self.Obj.pos[0] // CASEMAP, self.Obj.pos[1]//CASEMAP]

                    allObj = LoadJsonMapValue("coordsMapObject", "ObjAPlacer")
                    allVents = []
                    for obj in allObj:
                        if obj[3] == "Vent1":
                            allVents.append([obj[0], obj[1]])
                        if obj[3] == "Vent2":
                            allVents.append([obj[0], obj[1]])


                    if [allVents[1][0], allVents[1][1]] == coordsVentActuel:
                        coordsTarget = [(allVents[0][0] + 1)*CASEMAP +64, allVents[0][1] * CASEMAP +64] # + 64 pour center
                    else:
                        coordsTarget = [(allVents[1][0] -1)*CASEMAP +64 , allVents[1][1] * CASEMAP +64]

                    self.player.hitbox_rect.center = coordsTarget
                    self.player.rect.center = self.player.hitbox_rect.center

                    if not self.electricityOn:
                        if [allVents[1][0], allVents[1][1]] == coordsVentActuel:
                            STATE_HELP_INFOS[0] = "SeePNJ2"
                        else:
                            STATE_HELP_INFOS[0] = "UseVent"

                    self.gestionnaire.ouverture_du_noir(self.player.rect.center)
                
                if self.ObjectId == "DoorFuturisteVaisseau":
                    self.gestionnaire.fondu_au_noir()

                    INFOS["Exo"] = True # lancement exo dans main (changement variable)
                    self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["MakeExo"]) # text animation

            elif NIVEAU["Map"] == "NiveauMordor":

                if self.ObjectId == "Parchemin":
                    
                    # on donne le cours
                    self.gestionnaire.fondu_au_noir()
                    
                    self.parchemin = True
                    self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["Parchemin"]) # text animation
                    INFOS["GetCours"] +=1

                    if self.parchemin and self.pot:
                        STATE_HELP_INFOS[0] = "OpenDoorCellule"
                    
                    self.Obj.kill()

                    self.gestionnaire.ouverture_du_noir(self.player.rect.center)


                if self.ObjectId == "Pot":
                    # on donne le cours
                    self.gestionnaire.fondu_au_noir()

                    if not self.pot:
                        self.pot = True
                        INVENTORY["Key"] += 1
                        self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["Key"]) # text animation
                    else:
                        self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["Key2"]) # text animation
             
                    if self.parchemin and self.pot:
                        STATE_HELP_INFOS[0] = "OpenDoorCellule"
                    
                    self.gestionnaire.ouverture_du_noir(self.player.rect.center)

                if self.ObjectId == "DoorCellule":
                    self.gestionnaire.fondu_au_noir() # animation

                    pos = self.Obj.pos
                    try:
                        doorOpen = pygame.image.load(join("Image", "Obstacle", "Door", "IronBarsDoorOpen.png")).convert_alpha()
                        Sprites(pos, doorOpen, "OpenDoor", groups[0])
                    except:
                        INFOS["ErrorLoadElement"] = True
                    self.Obj.kill()
                    self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["OpenDoorCellule"]) # text animation


                    if not PNJ["PNJ2"]:
                        STATE_HELP_INFOS[0] = "OpenDoorCellule"
                    else:
                        STATE_HELP_INFOS[0] = "SeePNJ"


                    self.gestionnaire.ouverture_du_noir(self.player.rect.center)

                if self.ObjectId == "DoorPrison":
                    self.gestionnaire.fondu_au_noir() # animation

                    pos = self.Obj.pos
                    try:
                        doorOpen = pygame.image.load(join("Image", "Obstacle", "Door", "CastleWallDoorOpen.png")).convert_alpha()
                        Sprites(pos, doorOpen, "OpenDoorPrison", groups[0])
                    except:
                        INFOS["ErrorLoadElement"] = True
                    self.Obj.kill()
                    
                    self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["OpenDoorPrison"]) # text animation


                    STATE_HELP_INFOS[0] = "CrossBridge"


                    self.gestionnaire.ouverture_du_noir(self.player.rect.center)   

                if self.ObjectId == "Pont5":
                    # animation 
                    self.gestionnaire.fondu_au_noir()
                    self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["TraverserPont"])
                    # deplacement player
                    if self.player.rect.x < self.coordObjActuel[0]:
                        self.player.rect.x = self.coordObjActuel[0] + CASEMAP
                        STATE_HELP_INFOS[0] = "SeePNJ" # update tips player
                    else:
                        self.player.rect.x = self.coordObjActuel[0] - CASEMAP
                        STATE_HELP_INFOS[0] = "CrossBridge" # update tips player
                    
                    self.player.rect.y = self.coordObjActuel[1]
                    self.player.hitbox_rect.center = self.player.rect.center    
                    # fin animation
                    self.gestionnaire.ouverture_du_noir(self.player.rect.center) 

                if self.ObjectId == "DoorVolcan" : 
                    self.gestionnaire.fondu_au_noir()
                    INFOS["Exo"] = True # lancement exo dans main (changement variable)
                    self.gestionnaire.textScreen(TEXTE["Elements"][NIVEAU["Map"]]["MakeExo"]) # text animation

                if self.ObjectId == "Portal":
                    INFOS["EndPhase"] = True # gestion de fin du jeu




    def Isclose(self) -> bool :
        """Méthode calcul de proximité entre le player et les obj interactions
        Input : None
        Ouput : bool"""
        
        for Object in self.interactionGroup: # parcours all obj 

            coordsObj = (Object.pos[0] + CASEMAP // 2, Object.pos[1] + CASEMAP // 2) # top left coords -> center coords
            playerPos = self.player.rect.center # center player
            

            # Calculer la distance entre le joueur et le PNJ
            distance = sqrt((playerPos[0] - (coordsObj[0]))**2 + (playerPos[1] - (coordsObj[1]))**2)
            
            self.camera_offset[0] = max(0, min(playerPos[0] - WINDOW_WIDTH // 2, self.map_width - WINDOW_WIDTH))
            self.camera_offset[1] = max(0, min(playerPos[1] - WINDOW_HEIGHT // 2, self.map_height - WINDOW_HEIGHT))

            # Limiter la caméra pour ne pas montrer le vide
            self.npc_screen_pos = [coordsObj[0]  - self.camera_offset[0], coordsObj[1] - self.camera_offset[1]]

            # modif disatance spécifique
            if Object.id == "DoorCellule":
                self.distanceMax = 225
            elif Object.id == "Pot":
                self.distanceMax = 130
            else:
                self.distanceMax = 150

 
            if distance <= self.distanceMax:
                # vrif de possibilité + action possible en fonction de l'avancement
                if Object.id == "ExitRock" and NIVEAU["Map"] == "NiveauPlaineRiviere" and not PNJ["PNJ3"]:
                    return False
                if Object.id in ["Arbre", "Arbre1", "Souche", "Souche1"] and (NIVEAU["Map"] == "NiveauMedievale" and not PNJ["PNJ1"]):
                    return False
                if Object.id == "TableCraft" and NIVEAU["Map"] == "NiveauMedievale" and not PNJ["PNJ2"]:
                    return False
                if Object.id == "DoorChateau" and NIVEAU["Map"] == "NiveauMedievale" and not PNJ["PNJ3"]:
                    return False
                if Object.id  == "Vent" and not PNJ["PNJ1"]:
                    return False
                if Object.id == "ReactorBloc" and not PNJ["PNJ2"]:
                    return False
                if Object.id  == "DoorFuturisteVaisseau" and not PNJ["PNJ7"]:
                    return False
                if Object.id == "DoorCellule" and (INVENTORY["Key"] < 1 or not self.parchemin):
                    return False
                if Object.id == "DoorPrison" and not PNJ["PNJ3"]:
                    return False
                if Object.id == "DoorVolcan" and not PNJ["PNJ4"]:
                    return False

                # valeur importante de l'obj interactions
                self.Obj = Object
                self.coordObjActuel = Object.pos
                self.ObjectId = Object.id

                # Dessiner la boîte d'indication "Press E"
                text_surface = FONT["FONT24"].render(TEXTE["Elements"]["Interaction"], True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.topleft = (self.npc_screen_pos[0] - 20, self.npc_screen_pos[1] - 40)
                
                # Dessine le fond de la bulle
                bubble_rect = text_rect.inflate(20, 10)
                pygame.draw.rect(self.displaySurface, (0, 0, 0), bubble_rect)
                pygame.draw.rect(self.displaySurface, (255, 255, 255), bubble_rect, 2)
                
                # Affiche le texte
                self.displaySurface.blit(text_surface, text_rect)

                # element à proximité
                return True
            
        # pas d'element à proximité
        return False

    def Update(self, player : tuple, interactionGroup : any) -> None:
        """Méthode update de toutes les interaction possibles (hors pnj)
        Input : player pos : tuple
                interactionGroup : element pygame
        Output : None"""

        self.interactionGroup = interactionGroup # maj groupe
        self.player = player 
        self.Isclose() # affichage texte d'interaction si proximité
