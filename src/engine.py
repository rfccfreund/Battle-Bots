import gameboard as gb


# play game function takes a bot and game object and runs the game
def play_game(game, bots):
    for bot in bots:
        bot_loc = gb.Start
        while game.game_over():
            move = bot.step(game.find_bot_move(bot_loc))
            game.update_moves(move)
            bot.score_move(move.score())
            bot.add_move(move)

            bot_loc = move

            game.next_turn()

        bot.add_game_score()
        bot.update_rewards()
        bot.update_policy()
        bot.update_explore_co()
        bot.expected_values()
        bot.player_cleanup()
        game.game_reset()
