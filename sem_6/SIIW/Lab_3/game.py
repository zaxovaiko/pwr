import os
import time
import copy
import random
import matplotlib.pyplot as plt
from state import State
from colorama import init


init(autoreset=True)

CALC_DEPTH = 5
BOT_ALG = 'minimax'
PLAYER_A = 'bot'
PLAYER_B = 'bot'
STATE = State()
COUNTER = 0


def print_field():
    # os.system('cls')
    print(STATE.players[0])
    print(STATE.players[1])


def score_simple_heuristic(player):
    return sum(player.field)


def minimax_with_pruning(alpha, beta, current_depth=0, expecting_max=True, incoming_state=None, target_depth=CALC_DEPTH, moving=0):
    state = copy.deepcopy(incoming_state)
    player = state.players[state.turn]
    global COUNTER
    COUNTER += 1

    if current_depth == target_depth - 1:
        return [score_simple_heuristic(player), None]

    # options which each of players can choose
    options = [i for i in range(len(player.field) - 1) if player.field[i]]
    if len(options) == 0:
        return [score_simple_heuristic(player), None]

    states = [[i, compute_move(state, i)] for i in options]
    max_item = [0, None]
    min_item = [float('inf'), None]

    if expecting_max:
        for i, s in states:
            value, index = minimax_with_pruning(
                alpha, beta, current_depth + 1, s.turn == moving, s, target_depth, moving)
            if max_item[0] < value:
                max_item = [value, i]
            alpha = max(alpha, max_item[0])
            if beta <= alpha:
                break
        return max_item

    for i, s in states:
        value, index = minimax_with_pruning(
            alpha, beta, current_depth + 1, s.turn == moving, s, target_depth, moving)
        if min_item[0] > value:
            min_item = [value, i]
        beta = min(beta, min_item[0])
        if beta <= alpha:
            break
    return min_item


def minimax(current_depth=0, expect_max=True, incoming_state=None, target_depth=CALC_DEPTH, moving=0):
    state = copy.deepcopy(incoming_state)
    player = state.players[state.turn]

    global COUNTER
    COUNTER += 1

    if current_depth == target_depth - 1:
        return [score_simple_heuristic(player), None]

    # options which each of players can choose
    options = [i for i in range(len(player.field) - 1) if player.field[i]]
    if len(options) == 0:
        return [score_simple_heuristic(player), None]

    states = [[i, compute_move(state, i)] for i in options]
    max_item = [0, None]
    min_item = [float('inf'), None]

    for i, s in states:
        value, index = minimax(current_depth + 1, s.turn ==
                               moving, s, target_depth, moving)
        if expect_max and max_item[0] < value:
            max_item = [value, i]
        if not expect_max and min_item[0] > value:
            min_item = [value, i]
    return max_item if state.turn == moving else min_item


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
            state.players[player_index].field[6] += state.players[player_index ^
                                                                  1].field[5 - field_index] + 1
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
        if inp == 'exit':
            exit(0)
        try:
            idx = int(inp) - 1
            if idx != 7 and player.field[idx] != 0:
                return idx
            print('Cell is empty, enter another number')
        except:
            pass


def choose_random_cell(player):
    idx = random.choice(
        [i for i in range(len(player.field) - 1) if player.field[i]])
    print('Choosen idx: ', idx)
    return idx


counters = {
    'mm': [],
    'ab': []
}
times = {
    'mm': [],
    'ab': []
}


def recommend_move(turn, depth):
    global COUNTER
    COUNTER = 0

    t0 = time.time()
    _, idx = minimax_with_pruning(float(
        '-inf'), float('inf'), incoming_state=STATE, target_depth=depth, moving=turn)
    counters['ab'].append(COUNTER)
    times['ab'].append(time.time() - t0)

    # t1 = time.time()
    # COUNTER = 0
    # _, idx2 = minimax(incoming_state=STATE, target_depth=depth, moving=turn)
    # counters['mm'].append(COUNTER)
    # times['mm'].append(time.time() - t1)
    return idx


while True:
    won, player = check_win(STATE)
    print_field()

    if won:
        if player not in [0, 1]:
            print('Draw!')
        else:
            print(STATE.players[player].get_name() + ' won!')
        break

    player = STATE.players[STATE.turn]
    print('\n', player.get_name() + ' turn')

    if STATE.turn == 0:
        if PLAYER_A == 'bot':
            if BOT_ALG == 'minimax':
                idx = recommend_move(0, 11)
            else:
                idx = choose_random_cell(player)
        if PLAYER_A == 'user':
            idx = ask_for_user_input(player)

    if STATE.turn == 1:
        if PLAYER_B == 'bot':
            if BOT_ALG == 'minimax':
                idx = recommend_move(1, 11)
            else:
                idx = choose_random_cell(player)
        if PLAYER_B == 'user':
            idx = ask_for_user_input(player)

    STATE = compute_move(STATE, idx)


print('czas mm - ', sum(times['mm']))
print('czas ab - ', sum(times['ab']))

print('stan mm - ', sum(counters['mm']))
print('stan ab - ', sum(counters['ab']))

# plt.plot(range(len(counters['mm'])),
#          counters['mm'], color='red', label='Minimax')
# plt.plot(range(len(counters['ab'])), counters['ab'],
#          color='green', label='Alpha-Beta')
# plt.legend(loc="upper left")
# plt.show()

# plt.plot(range(len(times['mm'])), times['mm'], color='red', label='Minimax')
# plt.plot(range(len(times['ab'])), times['ab'],
#          color='green', label='Alpha-Beta')
# plt.legend(loc="upper left")
# plt.show()
