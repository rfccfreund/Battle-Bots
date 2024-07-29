import rl_bot as br


# create player objects with varying exploration coeeficents
def make_players(nodes, exploration_co, num_players):
    starters = []

    for x in range(0, num_players):
        starters.append(br.RL_Bot(nodes, exploration_co[x]))

    return starters
