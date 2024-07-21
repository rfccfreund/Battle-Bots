import random


class RL_Bot():
    def __init__(self, environment, explore_co):
        self.environment = environment

        self.explore_co = explore_co  # used to calc optimization vs exploration play

        self.scores = []  # list of points for one game
        self.game_hist = []  # long term game history

        self.reward = {}  # store the value one games of any point
        self.policy = {}  # store long term value of each point

        self.memory = {}
        self.player_moves = []

        self.set_environment()

    def set_environment(self):
        for key in self.environment:
            self.reward[key] = 0
            self.memory[key] = 0
            self.policy[key] = 0

    def update_explore_co(self):  # if most recent score > prior run bot explores less
        if len(self.game_hist) >= 2:
            temp_list = set(self.game_hist)
            temp_list.remove(max(temp_list))
            if self.game_hist[-1] > max(temp_list):
                if self.explore_co < 0.95:
                    self.explore_co += .04


    def score_move(self, score):
        self.scores.append(score)

    def add_move(self, move):
        self.player_moves.append(move)

    def add_game_score(self):
        final_score = sum(self.scores)
        self.game_hist.append(final_score)

    def update_policy(self):
        for key, value in self.policy.items():
            self.policy[key] = (value * len(self.game_hist) + self.reward[key]) / len(self.game_hist)

    def player_cleanup(self):
        for key in self.environment:
            self.reward[key] = 0

        self.player_moves = []
        self.scores = []

    # step function takes a set of moves and returns one to the game
    def step(self, moves):
        # set a default move and set the best path to zero
        best_path = 0
        move = moves[0]

        # iterate through the moves assigning the highest to
        for x in moves:
            if self.get_value(x) > best_path:
                best_path = self.get_value(x)
                move = x

        if random.random() < self.explore_co:  # high explore_co -> less exploration
            return move

        elif len(moves) == 1:
            return move
        else:
            y = list(moves)
            y.remove(move)
            return random.choice(y)

    def get_value(self, move):
        return self.policy[move]

    def update_rewards(self):
        for move in self.player_moves:
            if self.reward[move] == self.memory[move]:
                self.reward[move] = sum(self.scores)
                if len(self.scores) > 0:
                    self.scores.pop(0)

        for key in self.environment:
            self.memory[key] = self.reward[key]

    def expected_values(self):
        for key in self.policy:
            print(key, ": ", self.policy[key])
        print("Policy: ", self.explore_co)

    def strategy(self, game, steps, start):

        strategy = []

        while steps > 0:
            current_best = 0
            moves = game.find_bot_move(start)
            for x in moves:
                if self.get_value(x) > current_best:
                    current_best = self.get_value(x)
                    optimal_move = x.location()
                    start = x

            if optimal_move:
                strategy.append(optimal_move)
            steps -= 1
        for x in strategy:
            print(x, end=" ")

    def all_scores(self):
        return self.game_hist
