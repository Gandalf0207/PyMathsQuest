from settings import * 
from SourcesFichiers.ExosCours.renderLatex import *
from SourcesFichiers.ExosCours.cours import *

class GestionCours(object):
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire
        self.coursMap = []
        self.coursNiveauScolaire = []
        self.creationNewCours = CreationCours(self)
        self.LoadCours()

    def LoadCours(self):
        TEXTE["Cours"] = COURS

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
        CoursACreer = TEXTE["Cours"][NIVEAU["Niveau"]][NIVEAU["Map"]]

        for CoursNumero in range(len(CoursACreer)):
            listCoursNumeroFormation = []
            for ElementCours in range(len(CoursACreer[f"Cours{CoursNumero}"])):
                if CoursACreer[f"Cours{CoursNumero}"][ElementCours][0] == "Image":
                    path = CoursACreer[f"Cours{CoursNumero}"][ElementCours][1]
                    listCoursNumeroFormation.append(["Image", path]) # add image path
                elif CoursACreer[f"Cours{CoursNumero}"][ElementCours][0]: # check si element latex
                    eqt = CoursACreer[f"Cours{CoursNumero}"][ElementCours][1]
                    latexSurf =self.ObjRender.GetElement(eqt, 14) # reation surface latex
                    listCoursNumeroFormation.append([True, latexSurf]) # add surface
                else:
                    listCoursNumeroFormation.append([False, CoursACreer[f"Cours{CoursNumero}"][ElementCours][1]]) # add text du cours

            self.gestionnaire.coursNiveauScolaire.append(listCoursNumeroFormation)



