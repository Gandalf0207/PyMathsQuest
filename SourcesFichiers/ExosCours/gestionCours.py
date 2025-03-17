from settings import * 
from SourcesFichiers.ExosCours.renderLatex import *

class GestionCours(object):
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.coursMap = []
        self.coursNiveauScolaire = []
        self.creationNewCours = CreationCours(self)

    def MakeCours(self):
        self.creationNewCours.Update()
        self.gestionnaire.checkCoursDone = True
    
    def ChangementNiveauScolaire(self):
        self.coursNiveauScolaire = []


class CreationCours(object):
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.listCoursActuel = None
        self.ObjRender = RenderLatex()

    def Update(self):
        # Récupère le niveau actuel à partir du dictionnaire Python chargé
        niveau_actuel = TEXTE["Cours"][NIVEAU["Niveau"]]

        # Parcourt chaque carte (exemple : "NiveauPlaineRiviere")
        for carte, cours in niveau_actuel.items():
            for cours_key, cours_elements in cours.items():
                listCoursNumeroFormation = []
                
                # Parcourt les éléments de chaque cours (exemple : textes, formules, images)
                for element_key, element in cours_elements.items():
                    if len(element) < 2:
                        print(f"Erreur : Structure invalide pour {cours_key} - {element_key}.")
                        continue

                    if element[0] == "Image":  # Gestion des images
                        pathlist = element[1]
                        chemin_image = os.path.join(*pathlist)
                        listCoursNumeroFormation.append(["Image", chemin_image])

                    elif element[0]:  # Si c'est une formule LaTeX
                        latex_surface = self.ObjRender.GetElement(element[1], 14)
                        listCoursNumeroFormation.append([True, latex_surface])

                    else:  # Texte simple
                        texte = element[1]
                        listCoursNumeroFormation.append([False, texte])

                # Ajoute le cours traité à la liste des cours du niveau scolaire
                self.gestionnaire.coursNiveauScolaire.append(listCoursNumeroFormation)




