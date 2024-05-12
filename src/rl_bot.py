import random


class RL_Bot():
    def __init__(self, environment, threshold):
        self.threshold = threshold
        self.reward = {}
        self.policy = {}
        self.memory = {}
        self.moves = {}
        self.runs = 0
        self.scores = []
        self.environment = environment

        self.set_environment(environment)

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

        if random.random() < self.threshold:
            return move
        #
        elif len(moves) == 1:
            return move
        else:
            y = list(moves)
            y.remove(move)
            return random.choice(y)

    def set_environment(self, key):
        for key in self.environment:
            self.reward[key] = 0
            self.memory[key] = 0
            self.policy[key] = 0
            self.moves[key] = 0

    def get_value(self, move):
        return self.policy[move]

    def update_values(self, value, move):
        for x in self.memory:
            if self.memory[x] > 0:
                self.memory[x] += value

        self.memory[move] += value

    def update_rewards(self, moves):
        self.runs += 1
        score = 0

        for x in (self.memory.values()):
            score += x
        score = score / 5.0
        self.scores.append(score)

        if len(self.scores) >= 2:
            if self.scores[-1] > self.scores[-2]:
               if self.threshold < 0.97:
                    self.threshold += .025

        for key in self.memory:
            if self.memory[key] > 0:
                self.reward[key] += self.memory[key]
                self.policy[key] = (self.reward[key] / moves[key])
                self.memory[key] = 0

    def expected_values(self):
        for key in self.policy:
            print(key, ": ", self.policy[key])
        print("Policy: ", self.threshold)

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

            strategy.append(optimal_move)
            steps -= 1
        for x in strategy:
            print(x, end=" ")

    def run_num(self):
        return self.runs

    def all_scores(self):
        return self.scores
