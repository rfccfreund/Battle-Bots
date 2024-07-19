import gameboard as gb
import rl_bot
import matplotlib.pyplot as plt
import numpy as np

# game object takes a gameMap, a list of nodes, and a policy


player1 = rl_bot.RL_Bot(gb.nodes, .6)
player2 = rl_bot.RL_Bot(gb.nodes, .15)

players = [player1, player2]


# play game function takes a bot and game object and runs the game
def play_game(game, bots):

    for bot in bots:
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


# run_num returns the number of times the game has run. This allows us to alter the number of runs
if __name__ == '__main__':
    while players[1].run_num() < 50:
        play_game(gb.firstGame, players)

    player1_score = np.array(players[0].all_scores())
    player2_score = np.array(players[1].all_scores())

    plt.plot(player1_score, marker=".", linestyle='None')
    plt.plot(player2_score, marker=".", linestyle='None')
    plt.show()

    # after the strategy is defined by the loop we set the policy to one. Returns a list of best moves
    players[0].strategy(gb.firstGame, 10, gb.A)
    print("\n")
    players[1].strategy(gb.firstGame, 10, gb.A)
