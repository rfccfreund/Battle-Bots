import markovGame as mg

# define the nodes object which make up the game
A = mg.Node(name='A', points=(2, 3, 5))
B = mg.Node('B', (4, 5))
C = mg.Node('C', (1, 2, 6))
D = mg.Node('D', (4, 3, 5, 7))
E = mg.Node('E', (5, 8))
F = mg.Node('F', (4, 5, 7, 6))
G = mg.Node('G', (2, 3, 4))
H = mg.Node('G', (4, 4, 5))
I = mg.Node('I', (5, 6, 8))
J = mg.Node('J', (8, 9, 10))

# list of nodes
nodes = [A, B, C, D, E, F, G, H, I, J]

# game map that shows how the nodes connect.
gameMap = {A: (B, C), B: (D, E), C: (E, F), D: (G, H), E: (G, I), F: (H, J), G: (A, C), H: (A,), I: (E, C), J: (D, F)}

firstGame = mg.MGame(gameMap, nodes, 5)