import socket
from Jessy_part import *

pions_blanc = [[1 if (i + j) % 2 == 0 else -2 for i in range(10)] for j in range(4)]
grille_vide = [[1 if (i + j) % 2 == 0 else -1 for i in range(10)] for j in range(2)]
pions_noir = [[1 if (i + j) % 2 == 0 else 2 for i in range(10)] for j in range(4)]
grille_init = pions_blanc + grille_vide + pions_noir



grille_test= [
    [ 1, -2,  1, -2,  1, -2,  1, -2,  1, -2],
    [-2,  1, -2,  1, -2,  1, -2,  1, -2,  1],
    [ 1, -2,  1, -2,  1, -2,  1, -2,  1, -2],
    [-2,  1, -2,  1, -2,  1, -2,  1, -2,  1],
    [ 1, -1,  1, -1,  1, -1,  1, -1,  1, -1],
    [-1,  1, -1,  1, -1,  1, -1,  1, -1,  1],
    [ 1,  2,  1,  2,  1,  2,  1,  2,  1,  2],
    [ 2,  1,  2,  1,  2,  1,  2,  1,  2,  1],
    [ 1,  2,  1,  2,  1,  2,  1,  2,  1,  2],
    [ 2,  1,  2,  1,  2,  1,  2,  1,  2,  1]
]

assert grille_init == grille_test, "problème dans la grille init" 

def deplacement(grid, x, y, direction, lenght):
    
    left_value = grid[x-lenght][y-lenght]
    right_value = grid[x-lenght][y+lenght]
    if left_value == -1:
        if direction == 'g':
            grid[x-lenght][y-lenght] = grid[x][y]
            grid[x][y] = -1
    if right_value == -1:
        if direction == 'd':
            grid[x-lenght][y+lenght] = grid[x][y]
            grid[x][y] = -1
                
    else:
        print("déplacement impossible")


# Tests de déplacements
p.affiche(grille_init)
deplacement(grille_init, 6, 1, 'g', 1)
p.affiche(grille_init)
p.affiche(grille_init)