import random
import gameboard as gb
import engine
import players

# game object takes a gameMap, a list of nodes, and a policy
random.seed(42)

exploration_co = [.25, .5, .75]
agents = players.make_players(gb.nodes_m, exploration_co, 3)

# run_num returns the number of times the game has run. This allows us to alter the number of runs
if __name__ == '__main__':
    while len(agents[2].all_scores()) < 150:
        engine.play_game(gb.secondGame, agents)

    engine.graph_game_scores(agents)

