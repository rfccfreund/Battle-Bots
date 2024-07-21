import markovGame as mg

# define the nodes object which make up the game

Start = mg.Node(name='Start', points=0)
A = mg.Node(name='A', points=1)
B = mg.Node('B', 2)
C = mg.Node('C', 3)
D = mg.Node('D', 4)
E = mg.Node('E', 8)
F = mg.Node('F', 5)
G = mg.Node('G', 4)

I = mg.Node('I', (7, 6, 8))
J = mg.Node('J', (12, 13, 13))

# list of nodes
nodes = [Start, A, B, C, D, E, F, G]

# game map that shows how the nodes connect.
game_map_easy = {Start: (A), A: (B, C), B: (D, E), C: (F, G)}

firstGame = mg.MGame(game_map_easy, nodes, 3)
