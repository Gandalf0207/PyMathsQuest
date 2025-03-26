### FICHIER CONTENUE PAGE 1 ###

# Module de création du Fichier Tex et convertion en pdf et autre
from pylatex import *
from pylatex.utils import *


def generate_contenue_p1(doc):

    #Page 1 titre et sous titre
    with doc.create(MiniPage(align="c")):
        doc.append(VerticalSpace("200pt"))
 
        doc.append(pylatex.Command('fontsize', arguments = ['50', '36']))
        doc.append(pylatex.Command('selectfont'))

        doc.append(bold('Py-Maths'))
        doc.append(LineBreak())
        doc.append(pylatex.Command('fontsize', arguments = ['30', '24']))
        doc.append(pylatex.Command('selectfont'))

        doc.append("Générateur d'exercices avec leurs corrections")

### FIN FICHIER CONTENUE PAGE 1 ###