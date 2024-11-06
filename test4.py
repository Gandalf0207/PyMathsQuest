import re

chaine = "[[3, 50], [2, 50], [1, 50], [0, 50], [4, 50], [15, 49], [30, 48], [45, 50], [60, 54], [71, 50], [70, 50], [71, 50], [72, 50]]"
# Supprimer les crochets [[ et ]] avec re.sub
nouvelle_chaine = re.sub(r"^\[", "{", chaine)
nouvelle_chaine = re.sub(r"\]$", "}", nouvelle_chaine)


print(nouvelle_chaine)