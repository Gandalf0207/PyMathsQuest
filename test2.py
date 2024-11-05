def tracer_diagonale(grille, a, b):
    x1, y1 = a
    x2, y2 = b
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        grille[y1][x1] = 1  # On marque la position dans la grille
        if (x1, y1) == (x2, y2):
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

# Initialisation de la grille et des points
grille = [[0 for _ in range(10)] for _ in range(10)]
a = (2, 3)
b = (7, 8)

# Tracer la ligne diagonale
tracer_diagonale(grille, a, b)

# Afficher la grille pour vérifier le résultat
for ligne in grille:
    print(ligne)