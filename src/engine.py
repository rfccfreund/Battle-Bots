import gameboard as gb
import numpy as np
import matplotlib.pyplot as plt


def play_game(game, bots):
    """
    Play a single game with the given bots.
    
    Takes a list of bots and game object and runs the game for each bot.
    
    Args:
        game: The game object to play
        bots: List of bot players
    """
    for bot in bots:
        bot_location = gb.start_node()  # Start is a special node which can only be moved from
        
        while game.game_over():
            move = bot.step(game.find_bot_move(bot_location))
            game.update_moves(move)
            bot.score_move(move.score())
            bot.add_move(move)

            bot_location = move
            game.next_turn()

        """
        Post-game the bot uses the new information gained to update its knowledge of the game structure.
        With the updated game structure, the bot updates its optimal play strategy and adjusts its 
        exploration coefficient to explore less as it achieves higher and higher scores.
        """
        bot.add_game_score()
        bot.update_rewards()
        bot.update_policy()
        bot.update_exploration_coefficient()
        # bot.expected_values() prints expected value of each node - useful for debugging
        bot.player_cleanup()
        game.record_game()
        game.game_reset()


def graph_game_scores(players):
    """
    Create a visualization of game scores to see how each bot is learning.
    
    Args:
        players: List of player bots to graph
    """
    scores = []
    labels = []

    for player in players:
        scores.append(np.array(player.all_scores()))
        labels.append(str(player.get_initial_exploration_coefficient()))

    game_numbers = np.linspace(1, len(scores[0]), len(scores[0]))
    fig, ax = plt.subplots()

    for score_index in range(len(scores)):
        ax.scatter(game_numbers, scores[score_index], label=labels[score_index])

    ax.set_xlabel('Number of Games')
    ax.set_ylabel('Score')
    ax.legend()
    plt.show()


def optimal_play(players, game, moves, start):
    """
    Display the optimal strategy for each player.
    
    Args:
        players: List of player bots
        game: The game object
        moves (int): Number of moves to plan
        start: Starting node for the strategy
    """
    for player in players:
        player.strategy(game, moves, start)
        print("\n")
