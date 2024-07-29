import gameboard as gb
import numpy as np
import matplotlib.pyplot as plt


# play game function takes a bot and game object and runs the game
def play_game(game, bots):
    for bot in bots:
        bot_loc = gb.Start
        while game.game_over():
            move = bot.step(game.find_bot_move(bot_loc))
            game.update_moves(move)
            bot.score_move(move.score())
            bot.add_move(move)

            bot_loc = move

            game.next_turn()

        bot.add_game_score()
        bot.update_rewards()
        bot.update_policy()
        bot.update_explore_co()
        bot.expected_values()
        bot.player_cleanup()
        game.game_reset()


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

    # after the strategy is defined by the loop we set the policy to one. Returns a list of best moves
   #agents[0].strategy(gb.secondGame, 4, gb.Start)
   # print("\n")
   # agents[1].strategy(gb.secondGame, 4, gb.Start)
   # print("\n")
   # agents[2].strategy(gb.secondGame, 4, gb.Start)
