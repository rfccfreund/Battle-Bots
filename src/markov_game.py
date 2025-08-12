import random


class Node:
    """Represents a node in the game with a name and possible point values."""
    
    def __init__(self, name, points):
        """
        Initialize a node.
        
        Args:
            name (str): The name/identifier of the node
            points (tuple): Tuple of possible point values for this node
        """
        self.name = name
        self.values = points

    def __str__(self):
        """Return the string representation of the node."""
        return self.name

    def score(self):
        """Return a random score from the possible point values."""
        return random.choice(self.values)

    def location(self):
        """Return the location name of the node."""
        return self.name


class MarkovGame:
    """Simple game made of nodes in a predetermined structure."""
    
    def __init__(self, game_map, nodes, max_turns):
        """
        Initialize the Markov game.
        
        Args:
            game_map (dict): Mapping of nodes to their possible moves
            nodes (list): List of all nodes in the game
            max_turns (int): Maximum number of turns allowed
        """
        self.turns = 0
        self.nodes = nodes
        self.score = 0
        self.moves = {}
        self.game_map = game_map
        self.is_active = True
        self.total_games = 0
        self.max_turns = max_turns

        for node in self.nodes:
            self.moves[node] = 0

    def find_bot_move(self, node):
        """Find possible moves from a given node."""
        return self.game_map[node]

    def update_moves(self, move):
        """Update the move count for a specific move."""
        self.moves[move] += 1

    def get_move_counts(self):
        """Return the move counts for all nodes."""
        return self.moves

    def game_over(self):
        """Check if the game is over."""
        return self.is_active

    def game_reset(self):
        """Reset the game state for a new game."""
        self.is_active = True
        self.turns = 0
        self.score = 0
        self.moves = {}

        for node in self.nodes:
            self.moves[node] = 0

    def next_turn(self):
        """Advance to the next turn and check if game should end."""
        self.turns += 1

        if self.turns >= self.max_turns:
            self.is_active = False

    def get_current_turn(self):
        """Return the current turn number."""
        return self.turns

    def record_game(self):
        """Record that a game has been completed."""
        self.total_games += 1

    def game_count(self):
        """Return the total number of games played."""
        return self.total_games

    def game_summary(self):
        """Print a summary of the game strategy and final score."""
        print("Strategy: ", self.moves, "Final Score: ", self.score)
