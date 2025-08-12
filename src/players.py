import reinforcement_learning_bot as rlb
import config


def make_players(nodes, exploration_coefficients, num_players):
    """
    Create player objects with varying exploration coefficients.
    
    Args:
        nodes: List of nodes in the game environment
        exploration_coefficients (list): List of exploration coefficients for each player
        num_players (int): Number of players to create
        
    Returns:
        list: List of ReinforcementLearningBot instances
    """
    starters = []

    for i in range(num_players):
        starters.append(rlb.ReinforcementLearningBot(nodes, exploration_coefficients[i]))

    return starters
