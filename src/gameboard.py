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

# Nodes for medium game
A2 = mg.Node(name='A2', points=(1, 1))
B2 = mg.Node('B2', (2, 3))
C2 = mg.Node('C2', (3, 5))
D2 = mg.Node('D2', (4, 7))
E2 = mg.Node('E2', (9, 11))
F2 = mg.Node('F2', (5, 6))
G2 = mg.Node('G2', (4, 5))
H2 = mg.Node('H2', (7, 8))
I2 = mg.Node('I2', (8, 9))
J2 = mg.Node('J2', (12, 13))
K2 = mg.Node('K2', (8, 9))
L2 = mg.Node('L2', (10, 11))
M2 = mg.Node('M2', (13, 14))
N2 = mg.Node('N2', (11, 12))
O2 = mg.Node('O2', (10, 11))




# list of nodes for each game
nodes = [Start, A, B, C, D, E, F, G]

nodes_m = [Start, A2, B2, C2, D2, E2, F2, G2, H2, I2, J2, K2, L2, M2, N2, O2]

nodes_h = [Start, A, B, C, D, E, F, G]

# game map that shows how the nodes connect for each game
game_map_easy = {Start: (A, A), A: (B, C), B: (D, E), C: (F, G)}

game_map_medium = {Start: (A2, A2), A2: (B2, C2),
                   B2: (D2, E2), C2: (F2, G2),
                   D2: (H2, I2), E2: (J2, K2), F2: (L2, M2), G2: (N2, O2)}


# Creation game objects to be used in main. Each game requires a map, a list of nodes, and a number of turns
firstGame = mg.MGame(game_map_easy, nodes, 3)

secondGame = mg.MGame(game_map_medium, nodes_m, 4)
