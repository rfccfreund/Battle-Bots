"""
Configuration file for the reinforcement learning game.
Contains all magic numbers and configurable parameters.
"""

# Game Configuration
MAX_GAMES = 1000
EASY_GAME_TURNS = 3
MEDIUM_GAME_TURNS = 4
HARD_GAME_TURNS = 5

# Exploration Coefficients
EXPLORATION_COEFFICIENTS = [0.25, 0.5, 0.75]
NUM_PLAYERS = 3
DEFAULT_GAME_DIFFICULTY = 3

# RL Bot Configuration
EXPLORATION_INCREMENT = 0.04
MAX_EXPLORATION_COEFFICIENT = 0.95
MIN_GAMES_FOR_EXPLORATION_UPDATE = 3
SMOOTHING_FACTOR = 0.01

# Strategy Planning
STRATEGY_PLANNING_STEPS = 5

# Random Seed
RANDOM_SEED = 0
