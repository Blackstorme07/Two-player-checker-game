import socket
pions_blanc = [[1 if (i + j) % 2 == 0 else -1 for i in range(10)] for j in range(4)]
grille_vide = [0 if (i + j) % 2 == 0 else -1 for i in range(10) for j in range(2)]
pions_noir = [-2 if (i + j) % 2 == 0 else -1 for i in range(10) for j in range(4)]

pions_blanc.append(grille_vide)
pions_blanc.append(pions_noir)
print(pions_blanc)
# grille_test = [
#     []
#     []
#     []
#     []
#     []
#     []
#     []
#     []
#     []
#     []
# ]