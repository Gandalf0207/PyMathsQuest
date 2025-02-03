from settings import *

class BindKey(object):

    def __init__(self, ):
        try:
            with open("keybinds.json", "r") as f:
                self.keybinds = json.load(f)
        except FileNotFoundError:
            self.keybinds = {
                "up": pygame.K_z,
                "down": pygame.K_s,
                "left": pygame.K_q,
                "right": pygame.K_d,
                "skip": pygame.K_SPACE,
                "action": pygame.K_e,
            }

    def Update(self):
        for key in self.keybinds:
            KEYSBIND[key] = self.keybinds[key]
