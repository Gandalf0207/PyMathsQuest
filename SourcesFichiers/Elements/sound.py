from settings import *
from Sound.BandeSonore.NiveauPlaineRiviere import *

class GestionSoundFond(object):

    def __init__(self):
        pygame.mixer.init()

        # canaux vocaux pour les musiques en parrallèles
        self.canal0 = pygame.mixer.Channel(0) # bande son
        self.canal1 = pygame.mixer.Channel(1) # dialogues

        # effet sonores
        self.canal2 = pygame.mixer.Channel(2) # river 
        self.canal3 = pygame.mixer.Channel(3) # marcher

        # bool de check
        self.grassFoot = True

        # load sounds
        self.LoadSounds()

    def LoadSounds(self):
        
        #bande son 
        self.bandeSon1 = join("Sound", "BandeSonore", "NiveauPlaineRiviere", "Nocyfer - alive (alternate stripped version) 2025-01-29 21_46.mp3")              
        self.bandeSon2 = join("Sound", "BandeSonore", "NiveauPlaineRiviere", "Nocyfer - therapy (instrumental slowed) 2025-01-29 21_46.mp3")
        self.bandeSon3 = join("Sound", "BandeSonore", "NiveauMedievale", "Nocyfer - Darkest Hour 2025-01-29 21_40.mp3")
        self.bandeSon4 = join("Sound", "BandeSonore", "NiveauMedievale", "Nocyfer - hurt me bad 2025-02-24 19_28.mp3")
        self.bandeSon5 = join("Sound", "BandeSonore", "NiveauBaseFuturiste", "Nocyfer - odyssey 2025-02-24 19_28.mp3")

    def BandeSon(self):
        if not self.canal0.get_busy():
            musique_list = []

            attente = randint(30, 60)  # Attente aléatoire
            time.sleep(attente)

            if NIVEAU["Map"] == "NiveauPlaineRiviere": # lieux
                musique_list = [self.bandeSon1, self.bandeSon2]
            
            elif NIVEAU["Map"] == "NiveauMedievale":
                musique_list = [self.bandeSon3, self.bandeSon4]

            elif NIVEAU["Map"] == "NiveauBaseFuturiste":
                musique_list = [self.bandeSon5]

            else:
                time.sleep(5)  # Vérifie la condition toutes les 5 secondes

            if musique_list != []:
                # play de la mudique
                musique_choisie = choice(musique_list)
                try :
                    self.musicFond = pygame.mixer.Sound(musique_choisie)
                    self.canal0.set_volume(SOUND["BandeSon"])
                    self.canal0.play(self.musicFond)
                except:
                    INFOS["ErrorLoadElement"] = True


    def Update(self):
        self.canal0.set_volume(SOUND["BandeSon"])



class GestionSoundDialogues(object):
    def __init__(self):
        pygame.mixer.init()

        # canaux vocaux pour les musiques en parrallèles
        self.canal1 = pygame.mixer.Channel(1) # dialogues

        # load sounds
        self.LoadSounds()


    def LoadSounds(self):
        # dialogues

        # map 0 # pnj 1
        self.PrincipalMap0PNJ1Diag1 = join("Sound", "Dialogues", "NiveauPlaineRiviere", "PNJ1", "Principal_Bucheron_Map0_PNJ1_Diag1.mp3")
        self.PrincipalMap0PNJ1Diag2 = join("Sound", "Dialogues", "NiveauPlaineRiviere", "PNJ1", "Principal_Bucheron_Map0_PNJ1_Diag2.mp3")
        self.SecondaireMap0PNJ1Diag1 = join("Sound", "Dialogues", "NiveauPlaineRiviere", "PNJ1", "Secondaire_Bucheron_Map0_PNJ1_Diag1.mp3")

        # map 0 # pnj 2
        self.PrincipalMap0PNJ2Diag1 = join("Sound", "Dialogues", "NiveauPlaineRiviere", "PNJ2", "Principal_VoyagerCurieux_Map0_PNJ2_Diag1.mp3")
        self.PrincipalMap0PNJ2Diag2 = join("Sound", "Dialogues", "NiveauPlaineRiviere", "PNJ2", "Principal_VoyagerCurieux_Map0_PNJ2_Diag2.mp3")
        self.SecondaireMap0PNJ2Diag1 =join("Sound", "Dialogues", "NiveauPlaineRiviere", "PNJ2", "Secondaire_VoyagerCurieux_Map0_PNJ2_Diag1.mp3")

        # map 0 # pnj 3
        self.PrincipalMap0PNJ3Diag1 = join("Sound", "Dialogues", "NiveauPlaineRiviere", "PNJ3", ".mp3")
        self.SecondaireMap0PNJ3Diag1 = join("Sound", "Dialogues", "NiveauPlaineRiviere", "PNJ3", ".mp3")



        # map 1 # pnj 1
        self.PrincipalMap1PNJ1Diag1 =  join("Sound", "Dialogues", "NiveauMedievale", "PNJ1", "Principal_Fermier_Map1_PNJ1_Diag1.mp3" )
        self.PrincipalMap1PNJ1Diag2 =  join("Sound", "Dialogues", "NiveauMedievale", "PNJ1", "Principal_Fermier_Map1_PNJ1_Diag2.mp3" )
        self.SecondaireMap1PNJ1Diag1 =  join("Sound", "Dialogues", "NiveauMedievale", "PNJ1", "Secondaire_Fermier_Map1_PNJ1_Diag1.mp3" )

        # map 1 # pnj 2
        self.PrincipalMap1PNJ2Diag1 = join("Sound", "Dialogues", "NiveauMedievale", "PNJ2", "Principal_GardeDesagreable_Map1_PNJ2_Diag1.mp3")
        self.PrincipalMap1PNJ2Diag2 = join("Sound", "Dialogues", "NiveauMedievale", "PNJ2", "Principal_GardeDesagreable_Map1_PNJ2_Diag2.mp3")
        self.PrincipalMap1PNJ2Diag3 = join("Sound", "Dialogues", "NiveauMedievale", "PNJ2", "Principal_GardeDesagreable_Map1_PNJ2_Diag3.mp3")
        self.PrincipalMap1PNJ2Diag4 = join("Sound", "Dialogues", "NiveauMedievale", "PNJ2", "Principal_GardeDesagreable_Map1_PNJ2_Diag4.mp3")
        self.SecondaireMap1PNJ2Diag1 = join("Sound", "Dialogues", "NiveauMedievale", "PNJ2", "Secondaire_GardeDesagreable_Map1_PNJ2_Diag1.mp3")

        #map 1 # pnj 3
        self.PrincipalMap1PNJ3Diag1 =  join("Sound", "Dialogues", "NiveauMedievale", "PNJ3", "Principal_Minerva_Map1_PNJ3_Diag1.mp3" )
        self.PrincipalMap1PNJ3Diag2 =  join("Sound", "Dialogues", "NiveauMedievale", "PNJ3", "Principal_Minerva_Map1_PNJ3_Diag2.mp3" )
        self.SecondaireMap1PNJ3Diag1 =  join("Sound", "Dialogues", "NiveauMedievale", "PNJ3", "Secondaire_Minerva_Map1_PNJ3_Diag1.mp3" )

        #map 1 # pnj 4
        self.PrincipalMap1PNJ4Diag1 =  join("Sound", "Dialogues", "NiveauMedievale", "PNJ4", ".mp3" )
        self.PrincipalMap1PNJ4Diag2 =  join("Sound", "Dialogues", "NiveauMedievale", "PNJ4", ".mp3" )



        # map 2 # pnj 1
        self.PrincipalMap2PNJ1Diag1 = join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ1", "Principal_Michael_Map2_PNJ1_Diag1.mp3")
        self.PrincipalMap2PNJ1Diag2 = join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ1", "Principal_Michael_Map2_PNJ1_Diag2.mp3")
        self.SecondaireMap2PNJ1Diag1 = join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ1", "Secondaire_Michael_Map2_PNJ1_Diag1.mp3")

        # map 2 # pnj 2
        self.PrincipalMap2PNJ2Diag1  =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ2", "Principal_Ingenieure_Map2_PNJ2_Diag1.mp3" )
        self.PrincipalMap2PNJ2Diag2  =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ2", "Principal_Ingenieure_Map2_PNJ2_Diag2.mp3" )
        self.PrincipalMap2PNJ2Diag3 =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ2", "Principal_Ingenieure_Map2_PNJ2_Diag3.mp3" )
        self.SecondaireMap2PNJ2Diag1 =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ2", "Secondaire_Ingenieure_Map2_PNJ2_Diag1.mp3" )

        # map 2 # pnj 3
        self.PrincipalMap2PNJ3Diag1  =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ3", "Principal_Han_Map2_PNJ3_Diag1.mp3" )
        self.PrincipalMap2PNJ3Diag2  =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ3", "Principal_Han_Map2_PNJ3_Diag2.mp3" )
        self.PrincipalMap2PNJ3Diag3 =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ3", "Principal_Han_Map2_PNJ3_Diag3.mp3" )
        self.PrincipalMap2PNJ3Diag4 =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ3", ".mp3" )

        # map 2 # pnj 4
        self.PrincipalMap2PNJ4Diag1  =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ4", "Principal_Didier_Map2_PNJ4_Diag1.mp3" )
        self.PrincipalMap2PNJ4Diag2  =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ4", "Principal_Didier_Map2_PNJ4_Diag2.mp3" )
        self.PrincipalMap2PNJ4Diag3 =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ4", "Principal_Didier_Map2_PNJ4_Diag3.mp3" )
        self.SecondaireMap2PNJ4Diag1 =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ4", "Secondaire_Didier_Map2_PNJ4_Diag1.mp3" )

        # map 2 # pnj 5
        self.PrincipalMap2PNJ5Diag1 = join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ5", "Principal_Han_Map2_PNJ5_Diag1.mp3" )
        self.PrincipalMap2PNJ5Diag2 = join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ5", "Principal_Han_Map2_PNJ5_Diag2.mp3" )

        # map 2 # pnj 6
        self.PrincipalMap2PNJ6Diag1  =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ6", "Principal_Han_Map2_PNJ6_Diag1.mp3" )
        self.PrincipalMap2PNJ6Diag2  =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ6", "Principal_Han_Map2_PNJ6_Diag2.mp3" )
        self.PrincipalMap2PNJ6Diag3 =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ6", "Principal_Han_Map2_PNJ6_Diag3.mp3" )
    
        # map 2 # pnj 7
        self.PrincipalMap2PNJ7Diag1  =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ7", ".mp3" )
        self.SecondaireMap2PNJ7Diag1 =  join("Sound", "Dialogues", "NiveauBaseFuturiste", "PNJ7", ".mp3" )



        # map 3 # pnj 1
        self.PrincipalMap3PNJ1Diag1 = join("Sound", "Dialogues", "NiveauMordor", "PNJ1", ".mp3" )
        self.PrincipalMap3PNJ1Diag2 = join("Sound", "Dialogues", "NiveauMordor", "PNJ1", ".mp3" )
        self.SecondaireMap3PNJ1Diag1 =  join("Sound", "Dialogues", "NiveauMordor", "PNJ1", ".mp3" )

        # map 3 # pnj 2
        self.PrincipalMap3PNJ2Diag1 = join("Sound", "Dialogues", "NiveauMordor", "PNJ2", "Principal_PrisoniereHumaine_Map3_PNJ2_Diag1.mp3" )
        self.PrincipalMap3PNJ2Diag2 = join("Sound", "Dialogues", "NiveauMordor", "PNJ2", "Principal_PrisoniereHumaine_Map3_PNJ2_Diag2.mp3" )
        self.SecondaireMap3PNJ2Diag1 =  join("Sound", "Dialogues", "NiveauMordor", "PNJ2", "Secondaire_PrisoniereHumaine_Map3_PNJ2_Diag1.mp3" )

        # map 3 # pnj 3
        self.PrincipalMap3PNJ3Diag1 = join("Sound", "Dialogues", "NiveauMordor", "PNJ3", ".mp3" )
        self.PrincipalMap3PNJ3Diag2 = join("Sound", "Dialogues", "NiveauMordor", "PNJ3", ".mp3" )
        self.SecondaireMap3PNJ3Diag1 =  join("Sound", "Dialogues", "NiveauMordor", "PNJ3", ".mp3" )

        # map 3 # pnj 4
        self.PrincipalMap3PNJ4Diag1 = join("Sound", "Dialogues", "NiveauMordor", "PNJ4", ".mp3" )
        self.PrincipalMap3PNJ4Diag2 = join("Sound", "Dialogues", "NiveauMordor", "PNJ4", ".mp3" )
        self.SecondaireMap3PNJ4Diag1 =  join("Sound", "Dialogues", "NiveauMordor", "PNJ4", ".mp3" )
        self.SecondaireMap3PNJ4Diag2 =  join("Sound", "Dialogues", "NiveauMordor", "PNJ4", ".mp3" )
        self.SecondaireMap3PNJ4Diag3 =  join("Sound", "Dialogues", "NiveauMordor", "PNJ4", ".mp3" )

        # map 3 # pnj 5
        self.PrincipalMap3PNJ5Diag1 = join("Sound", "Dialogues", "NiveauMordor", "PNJ5", ".mp3" )
        self.PrincipalMap3PNJ5Diag2 = join("Sound", "Dialogues", "NiveauMordor", "PNJ5", ".mp3" )
        self.SecondaireMap3PNJ5Diag1 =  join("Sound", "Dialogues", "NiveauMordor", "PNJ5", ".mp3" )


    




    def Dialogue(self, compteurDialogue, pnj):
        if DICOLANGUE["Fr"]:
            dialogue = None

            # on passe au dialogue suivant donc on coupe le précédent s'il y était
            if self.canal1.get_busy():
                self.StopDialogue()
            
            try:
                # get du bon son
                if NIVEAU["Map"] == "NiveauPlaineRiviere": # lieux
                    if pnj == "PNJ1":
                        if not PNJ["PNJ1"]:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap0PNJ1Diag1)
                                case 2:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap0PNJ1Diag2)
                        else:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.SecondaireMap0PNJ1Diag1)
                    
                    elif pnj == "PNJ2":
                        if not PNJ["PNJ2"]:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap0PNJ2Diag1)
                                case 2:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap0PNJ2Diag2)
                        else:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.SecondaireMap0PNJ2Diag1)



                elif NIVEAU["Map"] == "NiveauMedievale":
                    if pnj == "PNJ1":
                        if not PNJ["PNJ1"]:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap1PNJ1Diag1)
                                case 2:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap1PNJ1Diag2)
                        else:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.SecondaireMap1PNJ1Diag1)

                    elif pnj == "PNJ2":
                        if not PNJ["PNJ2"]:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap1PNJ2Diag1)
                                case 2:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap1PNJ2Diag2)
                                case 3:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap1PNJ2Diag3)
                                case 4:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap1PNJ2Diag4)
                        else:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.SecondaireMap1PNJ2Diag1)
                    elif pnj == "PNJ3":
                        if not PNJ["PNJ3"]:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap1PNJ3Diag1)
                                case 2:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap1PNJ3Diag2)
                        else:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.SecondaireMap1PNJ3Diag1)


                    
                elif NIVEAU["Map"] == "NiveauBaseFuturiste":
                    if pnj == "PNJ1":
                        if not PNJ["PNJ1"]:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ1Diag1)
                                case 2:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ1Diag2)
                        else:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.SecondaireMap2PNJ1Diag1)
                    elif pnj == "PNJ2":
                        if not PNJ["PNJ2"]:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ2Diag1)
                                case 2:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ2Diag2)
                                case 3:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ2Diag3)
                        else:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.SecondaireMap2PNJ2Diag1)
                    elif pnj == "PNJ3":
                        if not PNJ["PNJ3"]:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ3Diag1)
                                case 2:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ3Diag2)                                
                                case 3:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ3Diag3)                                
                                case 4:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ3Diag4)
                    elif pnj == "PNJ4":
                        if not PNJ["PNJ4"]:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ4Diag1)
                                case 2:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ4Diag2)
                                case 3:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ4Diag3)
                        else:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.SecondaireMap2PNJ4Diag1)
                    elif pnj == "PNJ5":
                        if not PNJ["PNJ5"]:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ5Diag1)
                                case 2:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ5Diag2)
                    elif pnj == "PNJ6":
                        if not PNJ["PNJ6"]:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ6Diag1)
                                case 2:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ6Diag2)
                                case 3:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap2PNJ6Diag3)

                elif NIVEAU["Map"] == "NiveauMordor":
                    if pnj == "PNJ2":
                        if not PNJ["PNJ2"]:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap3PNJ2Diag1)
                                case 2:
                                    dialogue = pygame.mixer.Sound(self.PrincipalMap3PNJ2Diag2)
                        else:
                            match compteurDialogue:
                                case 1:
                                    dialogue = pygame.mixer.Sound(self.SecondaireMap3PNJ2Diag1)


                if dialogue != None:
                    dialogue.set_volume(SOUND["Dialogue"])

                    if self.canal1.get_busy():
                        self.canal1.stop()
                    self.canal1.play(dialogue)
                    
            except:
                INFOS["ErrorLoadElement"] = True

    def StopDialogue(self):
        self.canal1.stop()

