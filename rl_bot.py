import random


class RL_Bot():
    def __init__(self, environment):
        self.threshold = .5
        self.reward = {}
        self.policy = {}
        self.memory = {}
        self.moves = {}
        self.runs = 0
        self.environment = environment

        self.set_environment(environment)

    def step(self, moves):
        best_path = 0
        move = moves[0]

        for x in moves:
            if self.get_value(x) > best_path:
                move = x

        if random.random() < self.threshold:
            return move
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

    def update_rewards(self):
        self.runs += 1
        for key in self.memory:
            if self.memory[key] > 0:
                self.reward[key] += self.memory[key]
                self.policy[key] = (self.reward[key] / self.runs)
                self.memory[key] = 0

    def expected_values(self):
        for key in self.policy:
            print(key, ": ", self.policy[key])
        print("\n")

    def run_num(self):
        return self.runs
