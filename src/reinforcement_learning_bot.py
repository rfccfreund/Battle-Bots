import random
import config


class ReinforcementLearningBot:
    """Reinforcement learning bot that learns optimal strategies through exploration and exploitation."""
    
    def __init__(self, environment, exploration_coefficient):
        """
        Initialize the RL bot.
        
        Args:
            environment: List of nodes in the game environment
            exploration_coefficient (float): Exploration coefficient (0-1) for balancing exploration vs exploitation
        """
        self.environment = environment
        self.exploration_coefficient = exploration_coefficient  # Used to calc optimization vs exploration play
        self.initial_exploration_coefficient = exploration_coefficient

        self.scores = []  # List of points for one game
        self.game_history = []  # Long term game history

        self.reward = {}  # Store the cumulative reward of each game choice for one game
        self.policy = {}  # Store long term value of each point
        self.node_visit_count = {}

        self.memory = {}
        self.player_moves = []

        self.set_environment()

    def set_environment(self):
        """Initialize the environment-related dictionaries."""
        for key in self.environment:
            self.reward[key] = 0
            self.memory[key] = 0
            self.policy[key] = 0
            self.node_visit_count[key] = 0

    def update_exploration_coefficient(self):
        """
        Update exploration coefficient based on recent performance.
        
        If most recent score > previous high, explore less in future games.
        """
        if len(self.game_history) > config.MIN_GAMES_FOR_EXPLORATION_UPDATE:
            temp_list = set(self.game_history)
            temp_list.remove(max(temp_list))
            if self.game_history[-1] > max(temp_list):
                if self.exploration_coefficient < config.MAX_EXPLORATION_COEFFICIENT:
                    self.exploration_coefficient += config.EXPLORATION_INCREMENT

    def get_initial_exploration_coefficient(self):
        """Return the initial exploration coefficient."""
        return self.initial_exploration_coefficient

    def score_move(self, score):
        """Record the score from a move."""
        self.scores.append(score)

    def add_move(self, move):
        """Record a move made by the player."""
        self.player_moves.append(move)

    def add_game_score(self):
        """Add the final game score to the game history."""
        final_score = sum(self.scores)
        self.game_history.append(final_score)

    def update_policy(self):
        """Update the policy values based on rewards and strategy choices."""
        for key, value in self.policy.items():
            self.policy[key] = self.reward[key] / (self.node_visit_count[key] + config.SMOOTHING_FACTOR)

    def player_cleanup(self):
        """Reset player state for the next game."""
        self.player_moves = []
        self.scores = []

    def step(self, moves):
        """
        Choose the next move based on current policy and exploration strategy.
        
        Args:
            moves: List of possible moves
            
        Returns:
            Node: The chosen move
        """
        # Set a default move and set the best path to zero
        best_path = 0
        move = moves[0]

        # Iterate through the moves assigning the highest to best_path
        for move_option in moves:
            if self.get_value(move_option) > best_path:
                best_path = self.get_value(move_option)
                move = move_option

        if random.random() < self.exploration_coefficient:  # High exploration_coefficient -> less exploration
            return move
        elif len(moves) == 1:
            return move
        else:
            alternative_moves = list(moves)
            alternative_moves.remove(move)
            return random.choice(alternative_moves)

    def get_value(self, move):
        """Get the current policy value for a move."""
        return self.policy[move]

    def update_rewards(self):
        """Update rewards based on moves made and scores achieved."""
        for move in self.player_moves:
            if self.reward[move] == self.memory[move]:
                self.reward[move] += sum(self.scores)
                self.node_visit_count[move] += 1
                if len(self.scores) > 0:
                    self.scores.pop(0)

            self.memory[move] = self.reward[move]

    def expected_values(self):
        """Print the expected values for each node and current exploration coefficient."""
        for key in self.policy:
            print(key, ": ", self.policy[key])
        print("Policy: ", self.exploration_coefficient)

    def strategy(self, game, steps, start):
        """
        Calculate and display the optimal strategy for a given number of steps.
        
        Args:
            game: The game object
            steps (int): Number of steps to plan
            start: Starting node
        """
        strategy = []
        final_score = 0

        while steps > 0:
            current_best = 0
            moves = game.find_bot_move(start)
            optimal_move = None
            
            for move_option in moves:
                if self.get_value(move_option) > current_best:
                    current_best = self.get_value(move_option)
                    actual_value = move_option.score()
                    optimal_move = move_option.location()
                    start = move_option

            if optimal_move:
                strategy.append(optimal_move)
                final_score += actual_value

            steps -= 1
            
        print("The player with an exploration coefficient of", self.initial_exploration_coefficient, "makes the following moves: ", end="")
        for move in strategy:
            print(move, end=" ")

        print("for a total of", final_score, "points")

    def all_scores(self):
        """Return all game scores from the bot's history."""
        return self.game_history
