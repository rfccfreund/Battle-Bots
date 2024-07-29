import random
import gameboard as gb
import engine
import players

# set rng seed to reproduce results to test code changes
random.seed(42)

"""
Players definite characteristic is there threshold to explore vs optimize with know information, which is 
captured in a players exploration coefficient. For example a coefficient of .25 means that 25% of the time 
the player will optimize, while 75% of the time they chose a random alternative to the optimal path. 

The program makes a bot for each value stored in exploration_co
"""

exploration_co = [.25, .5, .75]
agents = players.make_players(gb.nodes_m, exploration_co, 3)


if __name__ == '__main__':
    while len(agents[2].all_scores()) < 150: # alter number to change number of times the game is played
        engine.play_game(gb.secondGame, agents)

    engine.graph_game_scores(agents)

