import markovGame as mg
import rl_bot

A = mg.Node(name='A', points=(2, 3, 5))
B = mg.Node('B', (4, 5))
C = mg.Node('C', (1, 2, 6))
D = mg.Node('D', (2, 3, 5, 7))
E = mg.Node('E', (3, 8))
F = mg.Node('F', (4, 5, 7, 6))
G = mg.Node('G', (2, 3, 4))
H = mg.Node('G', (2, 7, 8))
I = mg.Node('I', (5, 6, 9))
J = mg.Node('J', (3, 4, 11))

nodes = [A, B, C, D, E, F, G, H, I, J]
gameMap = {A: (B, C), B: (D, E), C: (E, F), D: (G, H), E: (G, I), F: (H, J), G: (A, C), H: (A,), I: (E, C), J: (D, F)}
firstGame = mg.MGame(gameMap, nodes, 5)

test_bot = rl_bot.RL_Bot(nodes, .5)


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


# game.find_move(A)
# while game.game_over():
#     p_choice = input()
#     game.move(p_choice)
#
# game.game_summary()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while test_bot.run_num() < 10:
        playGame(firstGame, test_bot)

    test_bot.strategy(firstGame, 5, A)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
