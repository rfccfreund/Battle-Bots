import random
import gameboard as gb
import matplotlib.pyplot as plt
import numpy as np
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

    player1_score = np.array(agents[0].all_scores())
    player2_score = np.array(agents[1].all_scores())
    player3_score = np.array(agents[2].all_scores())

    plt.plot(player1_score, marker=".", linestyle='None')
    plt.plot(player2_score, marker="+", linestyle='None')
    plt.plot(player3_score, marker="D", linestyle='None')
    plt.show()

    # after the strategy is defined by the loop we set the policy to one. Returns a list of best moves
    players[0].strategy(gb.secondGame, 4, gb.Start)
    print("\n")
    players[1].strategy(gb.secondGame, 4, gb.Start)
    print("\n")
    players[2].strategy(gb.secondGame, 4, gb.Start)
