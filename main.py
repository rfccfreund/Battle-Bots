import markovGame as mg
import rl_bot

A = mg.Node(name='A', points=(2, 3, 5))
B = mg.Node('B', (4, 5))
C = mg.Node('C', (1, 2, 6))
D = mg.Node('D', (2, 3, 5, 7))
E = mg.Node('E', (3, 8))
F = mg.Node('F', (4, 5, 7, 6))

nodes = [A, B, C, D, E, F]
gameMap = {A: (B, C), B: (D, E), C: (E, F), D: (A,), E: (A,), F: (A,)}
firstGame = mg.MGame(gameMap, nodes, 1)

test_bot = rl_bot.RL_Bot(nodes)


def playGame(game, bot):
    bot_choice = A
    while game.game_over():
        move = bot.step(game.find_bot_move(bot_choice))
        bot.update_values(move.score(), move)
        bot_choice = move

        game.next_turn()

    bot.update_rewards()
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
    while test_bot.run_num() < 1000:
        playGame(firstGame, test_bot)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
