import os
import time
import copy
import random
from state import State
from colorama import init


init(autoreset=True)

CALC_DEPTH = 5
BOT_ALG = 'minimax'
PLAYER_A = 'bot'
PLAYER_B = 'bot'
STATE = State()


def print_field():
    # os.system('cls')
    print()
    print()
    print(STATE.players[0])
    print(STATE.players[1])


def minimax(current_depth=0, node=0, expecting_max=True, incoming_state=None, target_depth=CALC_DEPTH):
    state = copy.deepcopy(incoming_state)
    player = state.players[state.turn]

    if current_depth == target_depth - 1:
        return player.field[6], node

    # options which each of players can choose
    options = [i for i in range(len(player.field) - 1) if player.field[i]]
    if len(options) == 0:
        return player.field[6], node

    states = [(i, compute_move(state, i)) for i in options]
    if expecting_max:
        return max([minimax(current_depth + 1, i, False, s, target_depth) for i, s in states], key=lambda x: x[0])
    return min([minimax(current_depth + 1, i, True, s, target_depth) for i, s in states], key=lambda x: x[0])


def compute_move(state, cell):
    state = copy.deepcopy(state)
    turn = state.turn
    length = state.players[turn].field[cell]
    state.players[turn].field[cell] = 0

    is_moving_again = False
    for i in range(length):
        player_index = (((cell + i + 1) // 7) % 2) ^ turn
        field_index = (cell + i + 1) % 7

        state.players[player_index].field[field_index] += 1
        if field_index != 6 and i == length - 1 and state.players[player_index].field[field_index] == 1 and state.players[player_index ^ 1].field[5 - field_index] != 0 and turn != player_index ^ 1: 
            state.players[player_index].field[6] += state.players[player_index ^ 1].field[5 - field_index] + 1
            state.players[player_index].field[field_index] = 0
            state.players[player_index ^ 1].field[5 - field_index] = 0
    
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
            if sum_a == sum_b:
                return True, None
            return True, 0 if sum_a > sum_b else 1
    return False, None


def ask_for_user_input(player):
    while True:
        inp = input('Enter index [1-6]: ')
        if inp == 'exit': exit(0)
        try:
            idx = int(inp) - 1
            if idx != 7 and player.field[idx] != 0: 
                return idx
            print('Cell is empty, enter another number')
        except: pass


def choose_random_cell(player):
    idx = random.choice([i for i in range(len(player.field) - 1) if player.field[i]])
    print('Choosen idx: ', idx)
    return idx


while True:
    won, player = check_win(STATE)
    print_field()

    if won:
        if player not in [0, 1]: print('Draw!')
        else: print(STATE.players[player].get_name() + ' won!')
        break

    player = STATE.players[STATE.turn]
    print('\n', player.get_name() + ' turn')

    if STATE.turn == 1:
        if PLAYER_A == 'bot': 
            if BOT_ALG == 'minimax':
                _, idx = minimax(incoming_state=STATE, target_depth=7)
            else:
                idx = choose_random_cell(player)
        if PLAYER_A == 'user': idx = ask_for_user_input(player)
        
    if STATE.turn == 0:
        if PLAYER_B == 'bot': 
            if BOT_ALG == 'minimax':
                _, idx = minimax(incoming_state=STATE, target_depth=5)
            else:
                idx = choose_random_cell(player)
        if PLAYER_B == 'user': idx = ask_for_user_input(player)
    
    print(idx)
    # time.sleep(0.25)
    STATE = compute_move(STATE, idx)
