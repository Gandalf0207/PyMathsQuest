from settings import *

class BindKey(object):

    def __init__(self):
        """Méthode initialisation valeurs pour la création du stup des touches"""

        # ecriture dans le fichier
        with open("keybinds.json", "w") as valueFileJson: 
            self.keybinds = {
                "up": pygame.K_z,
                "down": pygame.K_s,
                "left": pygame.K_q,
                "right": pygame.K_d,
                "skip": pygame.K_SPACE,
                "inventory": pygame.K_i,
                "settings": pygame.K_p,
                "book": pygame.K_b,
                "sound": pygame.K_v,
                "action": pygame.K_e,
                "echap": pygame.K_ESCAPE,
                "hideHotBar": pygame.K_m,
            }
            json.dump(self.keybinds, valueFileJson, indent=4) 
    
    # mise à jour du dictionnaire de settings des touches
    def Update(self):
        for key in self.keybinds:
            KEYSBIND[key] = self.keybinds[key]
