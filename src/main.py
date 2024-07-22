import random

import gameboard as gb
import rl_bot
import matplotlib.pyplot as plt
import numpy as np

# game object takes a gameMap, a list of nodes, and a policy

random.seed(42)

player1 = rl_bot.RL_Bot(gb.nodes, .25)
player2 = rl_bot.RL_Bot(gb.nodes, .5)
player3 = rl_bot.RL_Bot(gb.nodes, .75)

players = [player1, player2, player3]


# play game function takes a bot and game object and runs the game
def play_game(game, bots):

    for bot in bots:
        bot_choice = gb.Start
        while game.game_over():
            move = bot.step(game.find_bot_move(bot_choice))
            game.update_moves(move)
            bot.score_move(move.score())
            bot.add_move(move)

            bot_choice = move

            game.next_turn()

        bot.add_game_score()
        bot.update_rewards()
        bot.update_policy()
        bot.update_explore_co()
        bot.expected_values()
        bot.player_cleanup()
        game.game_reset()


# run_num returns the number of times the game has run. This allows us to alter the number of runs
if __name__ == '__main__':
    while len(players[2].all_scores()) < 50:
        play_game(gb.firstGame, players)

    player1_score = np.array(players[0].all_scores())
    player2_score = np.array(players[1].all_scores())
    player3_score = np.array(players[2].all_scores())

    plt.plot(player1_score, marker=".", linestyle='None')
    plt.plot(player2_score, marker="+", linestyle='None')
    plt.plot(player3_score, marker="D", linestyle='None')
    plt.show()

    # after the strategy is defined by the loop we set the policy to one. Returns a list of best moves
    players[0].strategy(gb.firstGame, 3, gb.Start)
    print("\n")
    players[1].strategy(gb.firstGame, 3, gb.Start)
    print("\n")
    players[2].strategy(gb.firstGame, 3, gb.Start)
