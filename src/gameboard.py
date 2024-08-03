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


# Nodes for hard game
A3 = mg.Node(name='A3', points=(1, 1))
B3 = mg.Node('B3', (2, 3))
C3 = mg.Node('C3', (3, 5))
D3 = mg.Node('D3', (4, 7))
E3 = mg.Node('E3', (9, 11))
F3 = mg.Node('F3', (5, 6))
G3 = mg.Node('G3', (4, 5))
H3 = mg.Node('H3', (7, 8))
I3 = mg.Node('I3', (8, 9))
J3 = mg.Node('J3', (12, 13))
K3 = mg.Node('K3', (8, 9))
L3 = mg.Node('L3', (10, 11))
M3 = mg.Node('M3', (13, 14))
N3 = mg.Node('N3', (11, 12))
O3 = mg.Node('O3', (10, 11))
P3 = mg.Node('P3', (10, 11))
Q3 = mg.Node('Q3', (10, 11))
R3 = mg.Node('R3', (10, 11))
S3 = mg.Node('S3', (10, 11))
T3 = mg.Node('T3', (10, 11))
U3 = mg.Node('U3', (10, 11))
V3 = mg.Node('V3', (10, 11))
W3 = mg.Node('W3', (10, 11))
X3 = mg.Node('X3', (10, 11))
Y3 = mg.Node('Y3', (10, 11))
Z3 = mg.Node('Z3', (10, 11))






# list of nodes for each game
nodes = [Start, A, B, C, D, E, F, G]

nodes_m = [Start, A2, B2, C2, D2, E2, F2, G2, H2, I2, J2, K2, L2, M2, N2, O2]

nodes_h = [Start, A3, B3, C3, D3, E3, F3, G3, H3, I3, J3, K3, L3, M3, N3, O3
           P3, Q3, R3, S3, T3, U3, V3, W3, X3, Y3, Z3]

# game map that shows how the nodes connect for each game
game_map_easy = {Start: (A, A), A: (B, C), B: (D, E), C: (F, G)}

game_map_medium = {Start: (A2, A2), A2: (B2, C2),
                   B2: (D2, E2), C2: (F2, G2),
                   D2: (H2, I2), E2: (J2, K2), F2: (L2, M2), G2: (N2, O2)}

game_map_hard = {Start: (A3, A3), A3: (B3, C3),
                   B3: (D3, E3), C3: (F3, G3),
                   D3: (H3, I3), E3: (J3, K3), F3: (L3, M3), G3: (N3, O3),
                   H3: (P3, Q3), I3: (R3, S3), J3: (T3, U3), K3: (), L3: (), M3: (), N3:(), O3: ()  }


# Creation game objects to be used in main. Each game requires a map, a list of nodes, and a number of turns
firstGame = mg.MGame(game_map_easy, nodes, 3)

secondGame = mg.MGame(game_map_medium, nodes_m, 4)

thirdGame = mg.MGame(game_map_hard, nodes_h, 5)
