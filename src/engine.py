import gameboard as gb
import numpy as np
import matplotlib.pyplot as plt


# play game function takes a list of bots and game object and runs the game
def play_game(game, bots):
    for bot in bots:
        bot_loc = gb.Start  # Start is a special node which can only be moved from
        while game.game_over():
            move = bot.step(game.find_bot_move(bot_loc))
            game.update_moves(move)
            bot.score_move(move.score())
            bot.add_move(move)

            bot_loc = move

            game.next_turn()

        """
        post-game the bot uses the new information gained to update its knowledge of the game structure.
        With the updated game structure, the bot updates it optimal play strategy and adjusts its 
        exploration coefficient to explore less as it achieves higher and higher scores
        """
        bot.add_game_score()
        bot.update_rewards()
        bot.update_policy()
        bot.update_explore_co()
        bot.expected_values()
        bot.player_cleanup()
        game.game_reset()


# Post game run visualization to see how each bot is learning
def graph_game_scores(players):
    scores = []
    for player in players:
        scores.append(np.array(player.all_scores()))

    x = np.linspace(1, len(scores[0]), len(scores[0]))
    fig, ax = plt.subplots()

    for score in scores:
        ax.plot(x, score)

    ax.set_xlabel('Number of Games')
    ax.set_ylabel('Score')
    plt.show()


def optimal_play(players, game, moves, start):
    for player in players:
        player.strategy(game, moves, start)
        print("\n")


