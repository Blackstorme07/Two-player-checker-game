cb = (chr(9608)) + (chr(9608))
pb = ('\033[48;5;0m' + chr(9922))
db = ('\033[48;5;243m' + chr(9921)) 
        
cn = ("\033[90m" + chr(9608) + "\033[0m") + ("\033[90m" + chr(9608) + "\033[0m")
pn = ('\033[48;5;0m' + chr(9920)) 
dn = ('\033[48;5;244m' + chr(9923))
# test de commit pour voir si ça marche

r_item_blanc = [cb, pb, db]
r_item_noir = [cn, pn, dn]


class Plateau:
    def __init__(self, grille):
        self.grille = grille
        
    def affiche(grille):
        for i in range(len(grille)):
            for j in range(len(grille)):
                if j == 9:
                        space = ' \n'
                elif abs(grille[i][j]) == 2:
                        space = ' '
                else:        
                    space = ''
                if grille[i][j] > 0:
                    print(r_item_blanc[grille[i][j]-1], end=space)
                else:
                    print(r_item_noir[-(grille[i][j])-1], end=space)

show_grid = [
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
p = Plateau
print(p.affiche(show_grid))




