import markovGame as mg
import rl_bot
import matplotlib.pyplot as plt
import numpy as np

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

# game object takes a gameMap, a list of nodes, and a policy
firstGame = mg.MGame(gameMap, nodes, 5)

test_bot = rl_bot.RL_Bot(nodes, .33)


# play game function takes a bot and game object and runs the game
def playGame(game, bot):
    bot_choice = A
    while game.game_over():
        move = bot.step(game.find_bot_move(bot_choice))
        game.update_moves(move)
        bot.update_values(move.score(), move)
        bot_choice = move

        game.next_turn()

    bot.update_rewards(game.num_moves())
    bot.expected_values()
    game.game_reset()


# run_num returns the number of times the game has run. This alllows us to alter the number of runs
if __name__ == '__main__':
    while test_bot.run_num() < 150:
        playGame(firstGame, test_bot)

    ypoints = np.array(test_bot.all_scores())

    plt.plot(ypoints, marker=".", linestyle='None')
    plt.show()

    # after the strategy is defined by the loop we set the policy to one. Returns a list of best moves
    test_bot.strategy(firstGame, 5, A)
