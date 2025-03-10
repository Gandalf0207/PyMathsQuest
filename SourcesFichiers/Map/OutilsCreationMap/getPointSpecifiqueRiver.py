from settings import *

class GetPointSpecifiqueRiver(object):
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.longueur = 150
        self.largeur = 75

    def CheckPosRiviere(self, indice : list) -> bool:
        """Méthode permettant de regarder et de valider la position d'un element par raport à la riviere (pnj / arbre spécial)"""
        
        listePosPossible = ["-", "1", "2"] #path possible

        if indice[0] == 149: # position de la sortir sur la bordure de map (donc condition de check diférentes)
            if (self.gestionnaire.map[indice[1]][indice[0]-1] in listePosPossible) and (self.gestionnaire.map[indice[1]][indice[0]-2] in listePosPossible )and (indice[1] >=5) and (indice[1] <= 70) and (self.gestionnaire.map[indice[1]-1][indice[0]-1] in listePosPossible): 
                return True # on valide le placement
        elif (self.gestionnaire.map[indice[1]][indice[0]-1] in listePosPossible) and (self.gestionnaire.map[indice[1]][indice[0]-2] in listePosPossible )and(self.gestionnaire.map[indice[1]][indice[0]+1] in listePosPossible) and (indice[1] >=5) and (indice[1] <= 70) and (self.gestionnaire.map[indice[1]-1][indice[0]-1] in listePosPossible): 
            return True # on valide le placement
        else:
            return False # on invalide le placement

    def PlacementSpecial(self, index1, index2):
        listeCoordsElement = LoadJsonMapValue(index1, index2) # récupération de la liste de valeurs d'un element (riviere)

        Go = True
        while Go: # tant que go = True on check 
            indice = randint(0, self.largeur-1) # génération aléatoire d'un indice
            # Si true, on arreter la boucle
            if self.CheckPosRiviere(listeCoordsElement[indice]): # check si à les coords de la liste  l'indice respect les conditions pour poser l'element
                Go = False # Arret de la boucle
                
        itemCoords = listeCoordsElement[indice] # on crée un copie des coords dans la variable
        return itemCoords # return (x,y ) coord de l'element

