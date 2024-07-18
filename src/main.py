import gameboard as gb
import rl_bot
import matplotlib.pyplot as plt
import numpy as np

# game object takes a gameMap, a list of nodes, and a policy


test_bot = rl_bot.RL_Bot(gb.nodes, .33)


# play game function takes a bot and game object and runs the game
def play_game(game, bot):
    bot_choice = gb.A
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
        play_game(gb.firstGame, test_bot)

    ypoints = np.array(test_bot.all_scores())

    plt.plot(ypoints, marker=".", linestyle='None')
    plt.show()

    # after the strategy is defined by the loop we set the policy to one. Returns a list of best moves
    test_bot.strategy(gb.firstGame, 5, gb.A)
