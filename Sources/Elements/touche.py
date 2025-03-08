from settings import *

class BindKey(object):

    def __init__(self):
        """Initialisation des touches et chargement depuis le fichier si existant"""
        self.file_path = "keybinds.json"
        self.default_keybinds = {
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

        # Charger les touches existantes ou créer un fichier avec les touches par défaut
        self.keybinds = self.load_keybinds()


    def load_keybinds(self):
        """Charge les touches depuis le fichier JSON si existant, sinon utilise les valeurs par défaut"""
        if os.path.exists(self.file_path):  # Vérifie si le fichier existe
            try:
                with open(self.file_path, "r") as file:
                    saved_keybinds = json.load(file)

                # Vérifier et compléter avec les touches par défaut si certaines manquent
                for key in self.default_keybinds:
                    if key not in saved_keybinds:
                        saved_keybinds[key] = self.default_keybinds[key]

                return saved_keybinds  # Retourne les touches récupérées du fichier
            except (json.JSONDecodeError, IOError):
                pass
        # Si fichier inexistant ou corrompu, on utilise les valeurs par défaut et on les sauvegarde
        self.save_keybinds(self.default_keybinds)
        return self.default_keybinds
    
    def save_keybinds(self, keybinds):
        """Sauvegarde les touches dans le fichier JSON"""
        with open(self.file_path, "w") as file:
            json.dump(keybinds, file, indent=4)


    # mise à jour du dictionnaire de settings des touches
    def Update(self):
        for key in self.keybinds:
            KEYSBIND[key] = self.keybinds[key]
        self.save_keybinds(self.keybinds)
