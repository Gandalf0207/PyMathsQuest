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
        self.bandeSon1 = join("Sound", "BandeSonore",NIVEAU["Map"],"Nocyfer - alive (alternate stripped version) 2025-01-29 21_46.mp3")              
        self.bandeSon2 = join("Sound", "BandeSonore",NIVEAU["Map"],"Nocyfer - therapy (instrumental slowed) 2025-01-29 21_46.mp3")
        self.bandeSon3 = join("Sound", "BandeSonore",NIVEAU["Map"],"Nocyfer - Darkest Hour 2025-01-29 21_40.mp3")

    def BandeSon(self):
        if not self.canal0.get_busy():
            if NIVEAU["Map"] == "NiveauPlaineRiviere": # lieux
                attente = randint(10, 30)  # Attente aléatoire
                time.sleep(attente)

                musique_list = [self.bandeSon1, self.bandeSon2]
                musique_choisie = choice(musique_list)
                self.musicFond = pygame.mixer.Sound(musique_choisie)
                self.canal0.set_volume(SOUND["BandeSon"])
                self.canal0.play(self.musicFond)

            
            elif NIVEAU["Map"] == "NiveauMedievale":
                attente = randint(10, 30)  # Attente aléatoire
                time.sleep(attente)

                musique_list = [self.bandeSon3]
                musique_choisie = choice(musique_list)
                self.musicFond = pygame.mixer.Sound(musique_choisie)
                self.canal0.set_volume(SOUND["BandeSon"])
                self.canal0.play(self.musicFond)

            else:
                time.sleep(5)  # Vérifie la condition toutes les 5 secondes

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
        self.Princiapl1Map0Num0PNJ1Diag1 = join("Sound", "Dialogues", NIVEAU["Map"], "Numero0", "PNJ1", "Principal_Bucheron_Map0_Num0_PNJ1_Diag1.mp3")
        self.Princiapl1Map0Num0PNJ1Diag2 = join("Sound", "Dialogues", NIVEAU["Map"], "Numero0", "PNJ1", "Principal_Bucheron_Map0_Num0_PNJ1_Diag2.mp3")


    def Dialogue(self, compteurDialogue):
        
        # on passe au dialogue suivant donc on coupe le précédent s'il y était
        if self.canal1.get_busy():
            self.StopDialogue()
        
        # get du bon son
        if NIVEAU["Map"] == "NiveauPlaineRiviere": # lieux
            if not PNJ["PNJ1"]:
                match compteurDialogue:
                    case 1:
                        dialogue = pygame.mixer.Sound(self.Princiapl1Map0Num0PNJ1Diag1)
                    case 2:
                        dialogue = pygame.mixer.Sound(self.Princiapl1Map0Num0PNJ1Diag2)
        elif NIVEAU["Map"] == "NiveauMedievale":
            pass

        if NIVEAU["Map"] == "NiveauPlaineRiviere":
            dialogue.set_volume(SOUND["Dialogue"])

            if self.canal1.get_busy():
                self.canal1.stop()
            self.canal1.play(dialogue)

    def StopDialogue(self):
        self.canal1.stop()

