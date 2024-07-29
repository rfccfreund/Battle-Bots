import random

# simple game made of nodes in a predetermined structure
class MGame:
    def __init__(self, game_map, nodes, timelimit):
        self.turns = 0
        self.nodes = nodes
        self.score = 0
        self.moves = {}
        self.game_map = game_map
        self.notOver = True
        self.timelimit = timelimit

        for x in self.nodes:
            self.moves[x] = 0

    def find_bot_move(self, node):
        return self.game_map[node]

    def update_moves(self, move):
        self.moves[move] += 1

    def num_moves(self):
        return self.moves

    def game_over(self):
        return self.notOver

    def game_reset(self):
        self.notOver = True
        self.turns = 0
        self.score = 0
        self.moves = {}

        for x in self.nodes:
            self.moves[x] = 0

    def next_turn(self):
        self.turns += 1

        if self.turns >= self.timelimit:
            self.notOver = False

    def what_turn(self):
        return self.turns

    def game_summary(self):
        print("Strategy: ", self.moves, "Final Score: ", self.score)


class Node:
    def __init__(self, name, points):
        self.name = name
        self.values = points

    def __str__(self):
        return self.name

    def score(self):
        return random.choice(self.values)

    def location(self):
        return self.name
