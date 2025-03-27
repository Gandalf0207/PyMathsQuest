#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

from settings import *
from SourcesFichiers.ScriptAlgo.liaisonAtoB import *


class RiverCreator(object):

    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.longueur = 150 # river uniquement sur les grandes map
        self.largeur = 75
        self.listeCheminRiviere = []
        self.listePointRepere = []
        self.EspacementPointRepereRiviere = 15
        self.CoupageMapRiviere = 50 if NIVEAU["Map"] != "NiveauMedievale" else 75
        self.CouloirRiviere = 4

    def SetAndSave(self, numero):
                    # On ajoute les pts repère sur la map + les point spéciaux (haut et bas ) directement car collision avec montagne, donc il faut une ligne de 4 droite minimum
        for coordsPointRepere in self.listePointRepere: # positions de tout les points repère de la riviere
            self.gestionnaire.map[coordsPointRepere[1]][coordsPointRepere[0]] = "#" # on ajoute les pts repère sur la map normal (comme précédement)
            self.gestionnaire.baseMap[coordsPointRepere[1]][coordsPointRepere[0]] = "#"   # ajoute egalement les points repères de la riviere sur la map de base
            self.listeCheminRiviere.append([coordsPointRepere[0],coordsPointRepere[1]]) # forme [x,y]

        
        # Pour tout les points repère, on lie des points A et B entre eux avec le script crée pour l'occasion ! (confection maison)
        for nbPointRepereRiviere in range(len(self.listePointRepere)-1): # boucle avec indice -1 car on envoie le pts actuelle et le suivant pour les lier (n et  n+1)
            start = [self.listePointRepere[nbPointRepereRiviere][0], self.listePointRepere[nbPointRepereRiviere][1]] # fomre [x,y] start = aux coords du points actuel 
            goal = [self.listePointRepere[nbPointRepereRiviere+1][0], self.listePointRepere[nbPointRepereRiviere+1][1]] # fomre [x,y]   goal = coords du points suivant
            path = LiaisonAtoB(start, goal).GetPos()     # path de coords en [x,y]  script fait maison pour relier les points entre deux, on obtient une liste de position, correspondant au chemin à suivre


            # On recup la list de déplacement et on ajoute la rivière aux deux map
            for coords in path: # parcourt de la liste
                self.gestionnaire.map[coords[1]][coords[0]] = "#"  # ajout de l'element rivière sur la map (collision)
                self.gestionnaire.baseMap[coords[1]][coords[0]] = "#" # ajout de l'element rivière sur la map (base)
                self.listeCheminRiviere.append([coords[0],coords[1]]) # forme [x,y]  # stock des coords de toute la riviere dans la liste des coordonnées

        AjoutJsonMapValue(self.listeCheminRiviere, "coordsMapBase", f"Riviere{numero} Coords") # stockage des valeurs dans le fichier json

    def Reset(self):
        self.listeCheminRiviere = []
        self.listePointRepere = []

    def River0CreationVecticale(self, num):
        self.Reset()
        coordsPts1Riviere = [randint(0,6),0]
        self.listePointRepere.append(coordsPts1Riviere)
        
        coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1]+4] # on crée le second point avec une hauteur de + 4
        self.listePointRepere.append(coordsPts2Riviere) # forme [x,y] on ajoute le second point dans la liste

        # Point de haut en bas
        nbPts = self.largeur // self.EspacementPointRepereRiviere    # placement tout les 15 de hauteur ...   
        verifLigne5 = randint(1,(nbPts-1)) # choix du lieu pour la ligne de 5 droite pour sécu pos de pnj spécial et arbre spécial
        for nbPointRepere in range(1, nbPts):
            if verifLigne5 == nbPointRepere:
                pACoordsligne5 = [randint(0,6),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map pour les rivière de bordure
    
                self.listePointRepere.append(pACoordsligne5) # Ajout du point A car il devient un point repère à relier
                pBcoordsligne5 = [pACoordsligne5[0], nbPointRepere*self.EspacementPointRepereRiviere + 5] # forme [x, y]
                self.listePointRepere.append(pBcoordsligne5) # Ajout du point B car il devient un point repère à relier
            else:
                coords = [randint(0,6),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map pour les rivière de bordure       
                self.listePointRepere.append(coords) # on ajoute ces points dans la liste des points à relier

        coordsPts3Riviere = [randint(0,6),self.largeur-5] # on créer le point 1 de la map pour les rivière de bordure
        
        # Point du bas (dernier element)
        # permet de créer une ligne pour éviter les collisions avec les bordures
        self.listePointRepere.append(coordsPts3Riviere) # forme [x,y]  on ajoute l'avant dernier point repère
        coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1]+4] # on crée le dernier point avec une huteur de +4
        self.listePointRepere.append(coordsPts4Riviere) # forme [x,y] on ajoute le dernier point repère de la riviere
        self.SetAndSave(num)

    def River1CreationVecticale(self, num):
        self.Reset()
        coordsPts1Riviere = [randint((self.CoupageMapRiviere - self.CouloirRiviere),(self.CoupageMapRiviere + self.CouloirRiviere)),0] # on créer le point 1 de la map
        self.listePointRepere.append(coordsPts1Riviere)
        
        coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1]+4] # on crée le second point avec une hauteur de + 4
        self.listePointRepere.append(coordsPts2Riviere) # forme [x,y] on ajoute le second point dans la liste

        # Point de haut en bas
        nbPts = self.largeur // self.EspacementPointRepereRiviere    # placement tout les 15 de hauteur ...   
        verifLigne5 = randint(1,(nbPts-1)) # choix du lieu pour la ligne de 5 droite pour sécu pos de pnj spécial et arbre spécial
        for nbPointRepere in range(1, nbPts):
            if verifLigne5 == nbPointRepere:
                pACoordsligne5 = [randint((self.CoupageMapRiviere - self.CouloirRiviere),(self.CoupageMapRiviere + self.CouloirRiviere)), nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map
    
                self.listePointRepere.append(pACoordsligne5) # Ajout du point A car il devient un point repère à relier
                pBcoordsligne5 = [pACoordsligne5[0], nbPointRepere*self.EspacementPointRepereRiviere + 5] # forme [x, y]
                self.listePointRepere.append(pBcoordsligne5) # Ajout du point B car il devient un point repère à relier
            else:
                coords = [randint((self.CoupageMapRiviere - self.CouloirRiviere),(self.CoupageMapRiviere + self.CouloirRiviere)),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map
                self.listePointRepere.append(coords) # on ajoute ces points dans la liste des points à relier

        coordsPts3Riviere = [randint((self.CoupageMapRiviere - self.CouloirRiviere),(self.CoupageMapRiviere + self.CouloirRiviere)),self.largeur-5] # on créer le point 1 de la map
        # Point du bas (dernier element)
        # permet de créer une ligne pour éviter les collisions avec les bordures
        self.listePointRepere.append(coordsPts3Riviere) # forme [x,y]  on ajoute l'avant dernier point repère
        coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1]+4] # on crée le dernier point avec une huteur de +4
        self.listePointRepere.append(coordsPts4Riviere) # forme [x,y] on ajoute le dernier point repère de la riviere
        self.SetAndSave(num)

    def River2CreationVecticale(self, num):
        self.Reset()
        coordsPts1Riviere = [randint((2*self.CoupageMapRiviere - self.CouloirRiviere),(2*self.CoupageMapRiviere + self.CouloirRiviere)),0] # on créer le point 1 de la map
        self.listePointRepere.append(coordsPts1Riviere)
        
        coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1]+4] # on crée le second point avec une hauteur de + 4
        self.listePointRepere.append(coordsPts2Riviere) # forme [x,y] on ajoute le second point dans la liste

        # Point de haut en bas
        nbPts = self.largeur // self.EspacementPointRepereRiviere    # placement tout les 15 de hauteur ...   
        verifLigne5 = randint(1,(nbPts-1)) # choix du lieu pour la ligne de 5 droite pour sécu pos de pnj spécial et arbre spécial
        for nbPointRepere in range(1, nbPts):
            if verifLigne5 == nbPointRepere:
                pACoordsligne5 = [randint((2*self.CoupageMapRiviere - self.CouloirRiviere),(2*self.CoupageMapRiviere + self.CouloirRiviere)),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map
    
                self.listePointRepere.append(pACoordsligne5) # Ajout du point A car il devient un point repère à relier
                pBcoordsligne5 = [pACoordsligne5[0], nbPointRepere*self.EspacementPointRepereRiviere + 5] # forme [x, y]
                self.listePointRepere.append(pBcoordsligne5) # Ajout du point B car il devient un point repère à relier
            else:
                coords = [randint((2*self.CoupageMapRiviere - self.CouloirRiviere),(2*self.CoupageMapRiviere + self.CouloirRiviere)),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map
                self.listePointRepere.append(coords) # on ajoute ces points dans la liste des points à relier

        coordsPts3Riviere = [randint((2*self.CoupageMapRiviere - self.CouloirRiviere),(2*self.CoupageMapRiviere + self.CouloirRiviere)),self.largeur-5] # on créer le point 1 de la map
        # Point du bas (dernier element)
        # permet de créer une ligne pour éviter les collisions avec les bordures
        self.listePointRepere.append(coordsPts3Riviere) # forme [x,y]  on ajoute l'avant dernier point repère
        coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1]+4] # on crée le dernier point avec une huteur de +4
        self.listePointRepere.append(coordsPts4Riviere) # forme [x,y] on ajoute le dernier point repère de la riviere
        self.SetAndSave(num)

    def River3CreationVecticale(self, num):
        self.Reset()
        coordsPts1Riviere = [randint(LONGUEUR-7, LONGUEUR-2),0]
        self.listePointRepere.append(coordsPts1Riviere)
        
        coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1]+4] # on crée le second point avec une hauteur de + 4
        self.listePointRepere.append(coordsPts2Riviere) # forme [x,y] on ajoute le second point dans la liste

        # Point de haut en bas
        nbPts = self.largeur // self.EspacementPointRepereRiviere    # placement tout les 15 de hauteur ...   
        verifLigne5 = randint(1,(nbPts-1)) # choix du lieu pour la ligne de 5 droite pour sécu pos de pnj spécial et arbre spécial
        for nbPointRepere in range(1, nbPts):
            if verifLigne5 == nbPointRepere:
                pACoordsligne5 = [randint(LONGUEUR-7, LONGUEUR-2),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map
    
                self.listePointRepere.append(pACoordsligne5) # Ajout du point A car il devient un point repère à relier
                pBcoordsligne5 = [pACoordsligne5[0], nbPointRepere*self.EspacementPointRepereRiviere + 5] # forme [x, y]
                self.listePointRepere.append(pBcoordsligne5) # Ajout du point B car il devient un point repère à relier
            else:
                coords = [randint(LONGUEUR-7, LONGUEUR-2),nbPointRepere*self.EspacementPointRepereRiviere] # on créer le point 1 de la map
                self.listePointRepere.append(coords) # on ajoute ces points dans la liste des points à relier

        coordsPts3Riviere = [randint(LONGUEUR-7, LONGUEUR-2),self.largeur-5] # on créer le point 1 de la map
        # Point du bas (dernier element)
        # permet de créer une ligne pour éviter les collisions avec les bordures
        self.listePointRepere.append(coordsPts3Riviere) # forme [x,y]  on ajoute l'avant dernier point repère
        coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1]+4] # on crée le dernier point avec une huteur de +4
        self.listePointRepere.append(coordsPts4Riviere) # forme [x,y] on ajoute le dernier point repère de la riviere
        self.SetAndSave(num)
     
    def River2BisCreationVecticale(self, num):
        self.Reset()
        coordsPts1Riviere = [randint(LONGUEUR - 7, LONGUEUR - 2), 25]
        self.listePointRepere.append(coordsPts1Riviere)  # Ajouter le premier point repère

        coordsPts2Riviere = [coordsPts1Riviere[0], coordsPts1Riviere[1] + 4]
        self.listePointRepere.append(coordsPts2Riviere)

        nbPts = (self.largeur - 25) // self.EspacementPointRepereRiviere
        verifLigne5 = randint(1, (nbPts - 1))  # Position pour une section droite spéciale de la rivière
        
        # Ajout des points repères intermédiaires
        for nbPointRepere in range(1, nbPts):
            if verifLigne5 == nbPointRepere:  # Cas d'une ligne droite pour PNJ et éléments spéciaux
                pACoordsligne5 = [randint(LONGUEUR - 7, LONGUEUR - 2),nbPointRepere * self.EspacementPointRepereRiviere + 25]
                
                self.listePointRepere.append(pACoordsligne5)  # Ajouter le point A
                pBcoordsligne5 = [pACoordsligne5[0], pACoordsligne5[1] + 5]
                self.listePointRepere.append(pBcoordsligne5)  # Ajouter le point B
            else:
                coords = [randint(LONGUEUR - 7, LONGUEUR - 2),nbPointRepere * self.EspacementPointRepereRiviere + 25]
                self.listePointRepere.append(coords)

        coordsPts3Riviere = [randint(LONGUEUR - 7, LONGUEUR - 2), self.largeur - 5]
        self.listePointRepere.append(coordsPts3Riviere)
        
        coordsPts4Riviere = [coordsPts3Riviere[0], coordsPts3Riviere[1] + 4]
        self.listePointRepere.append(coordsPts4Riviere)
        self.SetAndSave(num)

    def River3CreationHorizontale(self, num):
        self.Reset()
        allCoordsRiviere1 = LoadJsonMapValue("coordsMapBase", "Riviere1 Coords")
        coordsPts1Riviere = choice(allCoordsRiviere1)
        while not (25 <= coordsPts1Riviere[1] <= 35):  # Assure que le point est dans une zone spécifique
            coordsPts1Riviere = choice(allCoordsRiviere1)
        self.listePointRepere.append(coordsPts1Riviere)  # Ajouter le premier point repère
        
        coordsPts2Riviere = [coordsPts1Riviere[0] + 4, coordsPts1Riviere[1]]
        self.listePointRepere.append(coordsPts2Riviere)

        nbPts = (self.longueur - 75) // self.EspacementPointRepereRiviere
        verifLigne5 = randint(1, (nbPts - 1))  # Position pour une section droite spéciale de la rivière
        
        # Ajout des points repères intermédiaires
        for nbPointRepere in range(1, nbPts):
            if verifLigne5 == nbPointRepere:  # Cas d'une ligne droite pour PNJ et éléments spéciaux
                pACoordsligne5 = [nbPointRepere * self.EspacementPointRepereRiviere + 75,randint((30 - self.CouloirRiviere), (30 + self.CouloirRiviere))]
                
                self.listePointRepere.append(pACoordsligne5)  # Ajouter le point A
                pBcoordsligne5 = [pACoordsligne5[0] + 5, pACoordsligne5[1]]
                self.listePointRepere.append(pBcoordsligne5)  # Ajouter le point B
            else:
                coords = [nbPointRepere * self.EspacementPointRepereRiviere + 75, randint((30 - self.CouloirRiviere), (30 + self.CouloirRiviere))]
                self.listePointRepere.append(coords)

        allCoordsRiviere2 = LoadJsonMapValue("coordsMapBase", "Riviere2 Coords")
        coordsPts3Riviere = allCoordsRiviere2[0]
        self.listePointRepere.append(coordsPts3Riviere)

        x = coordsPts3Riviere[0]
        c = 0
        while x + c < LONGUEUR - 1:
            c += 1
        coordsPts4Riviere = [x + c, coordsPts3Riviere[1]]
        self.listePointRepere.append(coordsPts4Riviere)
        self.SetAndSave(num)