import matplotlib.pyplot as plt


MINIMAX = [{'nodes': [], 'times': []}, {'nodes': [], 'times': []}]
ALPHA_BETA = [{'nodes': [], 'times': []}, {'nodes': [], 'times': []}]


def show_summary():
    print('[Player 1] Summary nodes MINIMAX: ', sum(MINIMAX[0]['nodes']))
    print('[Player 1] Summary nodes ALPHA_BETA: ', sum(ALPHA_BETA[0]['nodes']))

    print('[Player 2] Summary nodes MINIMAX: ', sum(MINIMAX[1]['nodes']))
    print('[Player 2] Summary nodes ALPHA_BETA: ', sum(ALPHA_BETA[1]['nodes']))

    print('[Player 1] Time execution MINIMAX: ', sum(MINIMAX[0]['times']))
    print('[Player 1] Time execution ALPHA_BETA: ', sum(ALPHA_BETA[0]['times']))

    print('[Player 2] Time execution MINIMAX: ', sum(MINIMAX[1]['times']))
    print('[Player 2] Time execution ALPHA_BETA: ', sum(ALPHA_BETA[1]['times']))


def show_stats():
    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(range(len(MINIMAX[0]['nodes'])), MINIMAX[0]['nodes'], color='red', label='Minimax')
    axarr[0].plot(range(len(ALPHA_BETA[0]['nodes'])), ALPHA_BETA[0]['nodes'], color='green', label='Alpha-Beta')
    axarr[0].set_title('Player 1 node visits')

    axarr[1].plot(range(len(MINIMAX[1]['nodes'])), MINIMAX[1]['nodes'], color='red', label='Minimax')
    axarr[1].plot(range(len(ALPHA_BETA[1]['nodes'])), ALPHA_BETA[1]['nodes'], color='green', label='Alpha-Beta')
    axarr[1].set_title('Player 2 node visits')

    plt.legend(loc="upper left")
    plt.show()

    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(range(len(MINIMAX[0]['times'])), MINIMAX[0]['times'], color='red', label='Minimax')
    axarr[0].plot(range(len(ALPHA_BETA[0]['times'])), ALPHA_BETA[0]['times'], color='green', label='Alpha-Beta')
    axarr[0].set_title('Player 1 turn time execution')

    axarr[1].plot(range(len(MINIMAX[1]['times'])), MINIMAX[1]['times'], color='red', label='Minimax')
    axarr[1].plot(range(len(ALPHA_BETA[1]['times'])), ALPHA_BETA[1]['times'], color='green', label='Alpha-Beta')
    axarr[1].set_title('Player 2 turn time execution')

    plt.legend(loc="upper left")
    plt.show()
