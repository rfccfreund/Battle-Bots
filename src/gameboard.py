import markovGame as mg

# define the nodes object which make up the game

Start = mg.Node(name='Start', points=0)
A = mg.Node(name='A', points=(1, 1))
B = mg.Node('B', (2, 2))
C = mg.Node('C', (3, 3))
D = mg.Node('D', (4, 4))
E = mg.Node('E', (8, 8))
F = mg.Node('F', (5, 5))
G = mg.Node('G', (4, 4))

A_M = mg.Node(name='A', points=(1, 1))
B_M = mg.Node('B', (2, 3))
C_M = mg.Node('C', (3, 5))
D_M = mg.Node('D', (4, 7))
E_M = mg.Node('E', (9, 11))
F_M = mg.Node('F', (5, 6))
G_M = mg.Node('G', (4, 5))




# list of nodes
nodes = [Start, A, B, C, D, E, F, G]

nodes_m = [Start, A, B, C, D, E, F, G]

# game map that shows how the nodes connect.
game_map_easy = {Start: (A, A), A: (B, C), B: (D, E), C: (F, G)}

game_map_medium = {Start: (A, A), A: (B, C), B: (D, E), C: (F, G)}

firstGame = mg.MGame(game_map_easy, nodes, 3)
