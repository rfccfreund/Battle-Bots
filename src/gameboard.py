import markovGame as mg

# define the nodes object which make up the game
A = mg.Node(name='A', points=(2, 3, 3))
B = mg.Node('B', (4, 5))
C = mg.Node('C', (2, 2, 3))
D = mg.Node('D', (4, 6, 5, 7))
E = mg.Node('E', (8, 6))
F = mg.Node('F', (5, 6, 7, 6))
G = mg.Node('G', (2, 3, 3))
H = mg.Node('G', (4, 2, 2))
I = mg.Node('I', (7, 6, 8))
J = mg.Node('J', (12, 13, 13))

# list of nodes
nodes = [A, B, C, D, E, F, G, H, I, J]

# game map that shows how the nodes connect.
gameMap = {A: (B, C), B: (D, E), C: (E, F), D: (G, H), E: (G, I), F: (H, J), G: (A, C), H: (A,), I: (B, C), J: (D, A)}

firstGame = mg.MGame(gameMap, nodes, 100)
