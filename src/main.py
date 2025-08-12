import random
import gameboard as gb
import engine
import players
import config


# Set RNG seed to reproduce results to test code changes
random.seed(config.RANDOM_SEED)


def main():
    """
    Main function to run the reinforcement learning game simulation.
    
    Players' defining characteristic is their threshold to explore vs optimize with known information,
    which is captured in a player's exploration coefficient. For example, a coefficient of 0.25 means
    that 25% of the time the player will optimize, while 75% of the time they choose a random
    alternative to the optimal path.
    
    The program makes a bot for each value stored in exploration_coefficients.
    """
    exploration_coefficients = config.EXPLORATION_COEFFICIENTS
    agents = players.make_players(gb.nodes_hard, exploration_coefficients, config.NUM_PLAYERS)
    game = gb.choose_game(config.DEFAULT_GAME_DIFFICULTY)

    while game.game_count() < config.MAX_GAMES:  # Alter number to change number of times the game is played
        engine.play_game(game, agents)

    engine.graph_game_scores(agents)
    engine.optimal_play(agents, game, config.STRATEGY_PLANNING_STEPS, gb.start_node())


if __name__ == '__main__':
    main()
