#Projet : PyMathsQuest
#Auteurs : LUBAN Théo & PLADEAU Quentin

from settings import *
from SourcesFichiers.Ressources.PyMathsSources.sources.PyMaths import *
class MakePDFWithPyMaths(object):
    def __init__(self):
        self.InstancePyMaths = Generation()
        self.doc = self.InstancePyMaths.GetDoc()
        self.title = "PyMathsQuest correction exercices"

    def GetExoValues(self):
        with open(join("data","exercicesValues.json"), "r") as f: # ouvrir le fichier json en mode e lecture
            self.allExoValues = json.load(f) # chargement des valeurs

    def CompilPDF(self, filePath):
        self.InstancePyMaths.BuildPdf(self.title, filePath)

    def GenerateCorrection(self):
        self.InstancePyMaths.FirstPage(self.title)

        for i, exo in enumerate(self.allExoValues):

            if self.allExoValues[exo]["Niveau"] == "Seconde":

                if self.allExoValues[exo]["Exo"] == "NiveauPlaineRiviere":
                    self.valuesExo = self.allExoValues[exo]["Values"]
                    if not self.allExoValues[exo]["Difficulte"]:
                        ex = Eqt1deg(self.doc, i, 1, self.valuesExo[0], self.valuesExo[1], self.valuesExo[2], self.valuesExo[3], 0, 0)
                        ex.GestionAllExoEqt1deg()
                    else:
                        ex = Eqt1deg(self.doc, i, 2, self.valuesExo[0], self.valuesExo[1], self.valuesExo[2], self.valuesExo[3], self.valuesExo[4], self.valuesExo[5])
                        ex.GestionAllExoEqt1deg()

                elif self.allExoValues[exo]["Exo"] == "NiveauMedievale":
                    self.valuesExo = self.allExoValues[exo]["Values"]
                    if not self.allExoValues[exo]["Difficulte"]:
                        ex = Volumes(self.doc, i, 1, self.valuesExo[0], self.valuesExo[1], self.valuesExo[2], self.valuesExo[3], self.valuesExo[4], self.valuesExo[5], self.valuesExo[6])         
                        ex.AddVolumesTitreConsigne()
                        ex.AdConsigneVCube(1)
                        ex.AddConsigneVSphere(2)
                        ex.AddConsigneVCone(3)
                        self.doc.append(NewPage())
                        ex.AddCorrectionCube(1)
                        ex.AddCorrectionVSphere(2)
                        ex.AddCorrectionVCone(3)
                        self.doc.append(NewPage())
                    else:
                        ex = Volumes(self.doc, i, 2, self.valuesExo[0], self.valuesExo[1], self.valuesExo[2], self.valuesExo[3], self.valuesExo[4], self.valuesExo[5], self.valuesExo[6])         
                        ex.GestionAllExoVolumes()

                elif self.allExoValues[exo]["Exo"] == "NiveauBaseFuturiste":
                    pass  # pas de correction encore disponible

                elif self.allExoValues[exo]["Exo"] == "NiveauMordor":
                    self.valuesExo = self.allExoValues[exo]["Values"]
                    if not self.allExoValues[exo]["Difficulte"]:
                        ex = Eqt2Incs(self.doc, i, 1, self.valuesExo[0], self.valuesExo[1], self.valuesExo[2], self.valuesExo[3], self.valuesExo[4], self.valuesExo[5])
                        ex.GestionAllExoEqt2Incs()
                    else:
                        ex = Eqt2Incs(self.doc, i, 2, self.valuesExo[0], self.valuesExo[1], self.valuesExo[2], self.valuesExo[3], self.valuesExo[4], self.valuesExo[5])
                        ex.GestionAllExoEqt2Incs()

            elif self.allExoValues[exo]["Niveau"] == "Premiere":

                if self.allExoValues[exo]["Exo"] == "NiveauMedievale": # pas de niveau de difficulté
                    self.valuesExo = self.allExoValues[exo]["Values"]
                    ex =  Poly2deg(self.doc,i, self.valuesExo[0], self.valuesExo[1], self.valuesExo[2])
                    ex.AddPoly2DegTitreConsigne()
                    ex.AddConsigneDelta(1)
                    ex.AddConsigneSolutionsDelta(2)
                    self.doc.append(NewPage())
                    ex.AddPoly2DegTitreCorrection()
                    ex.AddCorrectionDelta(1)
                    ex.AddCorrectionSolutionsDelta(2)
                    self.doc.append(NewPage())
                    
                elif self.allExoValues[exo]["Exo"] == "NiveauBaseFuturiste": # pas de niveau de difficulté
                    self.valuesExo = self.allExoValues[exo]["Values"]
                    ex = Derives(self.doc, i, 0,0,0,0,0,0,0,0,0,0, self.valuesExo[0], self.valuesExo[1])
                    ex.GestionAllExoDerives()     

                elif self.allExoValues[exo]["Exo"] == "NiveauMordor":
                    pass # pas de correction encore disponible