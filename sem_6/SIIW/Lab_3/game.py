import os
import copy
import random
import config
import ai
from state import State
from colorama import init


init(autoreset=True)


def print_field() -> None:
    # os.system('cls')
    print(config.STATE.players[0])
    print(config.STATE.players[1])


def compute_move(state, cell) -> State:
    # I dont remember how did I write it
    # GLHF to understand
    state = copy.deepcopy(state)
    turn = state.turn
    length = state.players[turn].field[cell]
    state.players[turn].field[cell] = 0

    is_moving_again = False
    for i in range(length):
        state.against = False
        # ... especially this part
        player_index = (((cell + i + 1) // 7) % 2) ^ turn
        field_index = (cell + i + 1) % 7

        state.players[player_index].field[field_index] += 1
        if field_index != 6 and i == length - 1 and state.players[player_index].field[field_index] == 1 and state.players[player_index ^ 1].field[5 - field_index] != 0 and turn != player_index ^ 1:
            state.players[player_index].field[6] += state.players[player_index ^ 1].field[5 - field_index] + 1
            state.players[player_index].field[field_index] = 0
            state.players[player_index ^ 1].field[5 - field_index] = 0
            state.against = True

        if i == length - 1 and field_index == 6:
            is_moving_again = True

    if not is_moving_again:
        state.turn ^= 1
    return state


def check_win(state):
    for player in state.players:
        if player.field[:6] == [0] * 6:
            # for each player collect rest of all stones and put them into store
            sum_a = sum(state.players[0].field)
            sum_b = sum(state.players[1].field)
            state.players[0].field = [0] * 6 + [sum_a]
            state.players[1].field = [0] * 6 + [sum_b]
            return True, None if sum_a == sum_b else (0 if sum_a > sum_b else 1)
    return False, None


def ask_for_user_input(player) -> int:
    # Ask user for input until receives 'exit'
    while True:
        inp = input('Enter index [1-6]: ')
        if inp == 'exit':
            exit(0)
        try:
            idx = int(inp) - 1
            if idx != 6 and player.field[idx] != 0:
                return idx
            print('Cell is empty, enter another number')
        except:
            pass


def choose_random_cell(player) -> int:
    return random.choice([i for i in range(len(player.field) - 1) if player.field[i]])


def make_turn(player):
    if config.PLAYERS[config.STATE.turn] == 'bot':
        if config.BOT_ALGORITHMS[config.STATE.turn] == 'random':
            return choose_random_cell(player)
        return ai.recommend_move(config.STATE.turn, config.DEPTHS[config.STATE.turn], config.BOT_ALGORITHMS[config.STATE.turn])
    else:
        return ask_for_user_input(player)
