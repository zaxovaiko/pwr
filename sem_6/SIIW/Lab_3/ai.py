import copy
import time
import stats
import config
import game


# FIXME: Move to heur.py
def score_simple_heuristic(player):
    return sum(player.field)


def against_heuristic(moving, player, state):
    if state.against and moving != state.turn:
        return float('inf')
    return score_simple_heuristic(player)


def save_cell(moving, player, state):
    if state.against and moving == state.turn:
        return float('inf')
    return score_simple_heuristic(player)


def additional_move(turn, player, state):
    if turn == state.turn:
        return float('inf')
    return score_simple_heuristic(player)


def minimax_with_pruning(alpha, beta, current_depth=0, expecting_max=True, incoming_state=None, target_depth=config.DEFAULT_DEPTH, moving=0, heur=None):
    config.COUNTER += 1

    # turns which each of players can choose
    player = incoming_state.players[incoming_state.turn]
    options = [i for i in range(len(player.field) - 1) if player.field[i]]
    
    if current_depth == target_depth - 1 or len(options) == 0:
        if heur == 'default':
            return [score_simple_heuristic(player), None]
        elif heur == 'move':
            return [additional_move(moving, player, incoming_state), None]
        elif heur == 'eat':
            return [against_heuristic(moving, player, incoming_state), None]
        elif heur == 'save':
            return [save_cell(moving, player, incoming_state), None]

    state = copy.deepcopy(incoming_state)
    states = [[i, game.compute_move(state, i)] for i in options]  # calcualte new game states

    max_item = [0, None]
    min_item = [float('inf'), None]

    if expecting_max:
        for i, s in states:
            value, _ = minimax_with_pruning(
                alpha, beta, current_depth + 1, s.turn == moving, s, target_depth, moving, heur)
            if max_item[0] < value:
                max_item = [value, i]
            alpha = max(alpha, max_item[0])
            if beta <= alpha:
                break
        return max_item

    for i, s in states:
        value, _ = minimax_with_pruning(
            alpha, beta, current_depth + 1, s.turn == moving, s, target_depth, moving, heur)
        if min_item[0] > value:
            min_item = [value, i]
        beta = min(beta, min_item[0])
        if beta <= alpha:
            break
    return min_item


def minimax(current_depth=0, expect_max=True, incoming_state=None, target_depth=config.DEFAULT_DEPTH, moving=0, heur=None):
    config.COUNTER += 1

    player = incoming_state.players[incoming_state.turn]
    options = [i for i in range(len(player.field) - 1) if player.field[i]]

    if current_depth == target_depth - 1 or len(options) == 0:
        if heur == 'default':
            return [score_simple_heuristic(player), None]
        elif heur == 'move':
            return [additional_move(moving, player, incoming_state), None]
        elif heur == 'eat':
            return [against_heuristic(moving, player, incoming_state), None]
        elif heur == 'save':
            return [save_cell(moving, player, incoming_state), None]

    state = copy.deepcopy(incoming_state)
    states = [[i, game.compute_move(state, i)] for i in options]

    max_item = [0, None]
    min_item = [float('inf'), None]

    for i, s in states:
        value, _ = minimax(current_depth + 1, s.turn == moving, s, target_depth, moving, heur)
        if expect_max and max_item[0] < value:
            max_item = [value, i]
        if not expect_max and min_item[0] > value:
            min_item = [value, i]
    return max_item if state.turn == moving else min_item


def recommend_move(turn, depth, algorithm):
    t0 = time.time()
    config.COUNTER = 0

    _, alpha_beta_idx = minimax_with_pruning(float('-inf'), float('inf'), incoming_state=config.STATE, target_depth=depth, moving=turn, heur=config.HEURISTICS[turn])
    stats.ALPHA_BETA[turn]['nodes'].append(config.COUNTER)
    stats.ALPHA_BETA[turn]['times'].append(time.time() - t0)

    t1 = time.time()
    config.COUNTER = 0

    if depth < 8:
        # < 8 because we can wait for a long time to solve > 8 depth
        _, minimax_idx = minimax(incoming_state=config.STATE, target_depth=depth, moving=turn, heur=config.HEURISTICS[turn])
        stats.MINIMAX[turn]['nodes'].append(config.COUNTER)
        stats.MINIMAX[turn]['times'].append(time.time() - t1)

    return minimax_idx if algorithm == 'minimax' else alpha_beta_idx
