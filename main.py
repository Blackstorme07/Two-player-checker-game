import socket

pions_blanc = [[1 if (i + j) % 2 == 0 else -1 for i in range(10)] for j in range(4)]
grille_vide = [[0 if (i + j) % 2 == 0 else -1 for i in range(10)] for j in range(2)]
pions_noir = [[-2 if (i + j) % 2 == 0 else -1 for i in range(10)] for j in range(4)]
grille_init = pions_blanc + grille_vide + pions_noir
print(grille_init)

grille_test = [
[1, -1, 1, -1, 1, -1, 1, -1, 1, -1], 
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1], 
[1, -1, 1, -1, 1, -1, 1, -1, 1, -1], 
[-1, 1, -1, 1, -1, 1, -1, 1, -1, 1], 
[0, -1, 0, -1, 0, -1, 0, -1, 0, -1], 
[-1, 0, -1, 0, -1, 0, -1, 0, -1, 0], 
[-2, -1, -2, -1, -2, -1, -2, -1, -2, -1], 
[-1, -2, -1, -2, -1, -2, -1, -2, -1, -2], 
[-2, -1, -2, -1, -2, -1, -2, -1, -2, -1], 
[-1, -2, -1, -2, -1, -2, -1, -2, -1, -2]
]

def deplacement(grid, x, y, direction, lenght):
    
    left_value = grid[x-lenght][y-lenght]
    right_value = grid[x-lenght][y+lenght]
    if left_value == 0 or right_value == 0:
        if direction == 'g':
            grid[x][y], grid[x-lenght][y-lenght] = grid[x-lenght][y-lenght],\
                grid[x][y]
        if direction == 'd':
            grid[x][y], grid[x-lenght][y+lenght] = grid[x-lenght][y+lenght],\
                grid[x][y]
    else:
        print("déplacement impossible")