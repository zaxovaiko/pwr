import game
import stats
import config


if __name__ == '__main__':
    while True:
        won, player = game.check_win(config.STATE)
        game.print_field()

        if won:
            print('Draw!' if player not in [0, 1] else config.STATE.players[player].get_name() + ' won!')
            break

        player = config.STATE.players[config.STATE.turn]
        print('\n', player.get_name() + ' turn')

        config.STATE = game.compute_move(config.STATE, game.make_turn(player))

    stats.show_summary()
    stats.show_stats()
