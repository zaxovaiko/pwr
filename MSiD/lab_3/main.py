import functools
import pickle
import warnings
from time import sleep

import matplotlib.image as mpimg
import matplotlib.patches as patches
import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt

from content import (gradient_descent, logistic_cost_function, model_selection, prediction,
                     stochastic_gradient_descent)
from test import TestRunner
from utils import hog

PICKLE_FILE_PATH = 'data.pkl'
TEST_FILE_PATH = 'test_data.pkl'
EPOCHS = 100
MINIBATCH_SIZE = 50
PATCH_WIDTH = 92
PATCH_HEIGHT = 112
STEP = 20
marker_positions = []


def load_data():
    with open(PICKLE_FILE_PATH, 'rb') as f:
        return pickle.load(f)


def plot_f_values(f1, f2):
    plt.rcParams['image.cmap'] = 'gray'
    plt.rcParams['image.interpolation'] = 'none'
    plt.style.use(['dark_background'])
    xs = range(len(f1))

    plt.title("Porownanie algorytmow GD i SGD")
    plt.ylabel('Wartosc funkcji celu')
    plt.xlabel('Numer iteracji')

    gd_line, = plt.plot(xs, f1, 'r-', color='#FFCC55', label='GD')
    sgd_line, = plt.plot(xs, f2, 'r-', color='#FF5533', label='SGD')
    plt.legend(handles=[gd_line, sgd_line])
    fig = plt.gcf()
    fig.canvas.set_window_title('Wartości funkcji celu dla GD i SGD')
    plt.draw()
    plt.waitforbuttonpress(0)


def plot_theta_lambda(F_vals, theta_vals, lambda_vals):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(F_vals)
    fig.colorbar(cax)

    ax.set_xticklabels([''] + theta_vals[::2])
    ax.set_yticklabels([''] + lambda_vals)
    ax.xaxis.set_label_position('bottom')
    ax.xaxis.set_tick_params(labelbottom=True, labeltop=False, top=False)
    ax.set_xlabel(r'Prog klasyfikacji $\theta$')
    ax.set_ylabel('Parametr regularyzacji $\lambda$')
    plt.title("Selekcja modelu dla regresji logistycznej")
    plt.axis('tight')
    fig = plt.gcf()
    fig.canvas.set_window_title('Wartości miary F w ciagu walidacyjnym')
    plt.draw()
    plt.waitforbuttonpress(0)


def face_detect_patch(patch, w, theta):
    patch = patch / 255.0
    hog_patch = hog(patch)
    return prediction(np.transpose(np.concatenate(([[1]], hog_patch))), w, theta)


def get_patch(img, x, y):
    x1, x2 = x, x + PATCH_WIDTH
    y1, y2 = y, y + PATCH_HEIGHT
    return img[y1: y2, x1: x2]


def animate(i, ax, patch, patch_positions, img, w, theta):
    markers = []
    for position in marker_positions:
        markers.append(patches.Rectangle(position, PATCH_WIDTH, PATCH_HEIGHT, fill=False, color='g',
                                         linewidth=3))

    for marker in markers:
        ax.add_patch(marker)
    if i > len(patch_positions) - 1:
        return [patch] + markers

    img_size = img.shape
    x, y = patch_positions[i]
    patch.set_xy([x, img_size[0] - PATCH_HEIGHT - y])

    cut_out = get_patch(img, x, y)

    if face_detect_patch(cut_out, w, theta):
        marker_position = [x, img_size[0] - PATCH_HEIGHT - y]
        marker_positions.append(marker_position)
        marker = patches.Rectangle(marker_position, PATCH_WIDTH, PATCH_HEIGHT, fill=False,
                                   color='g', linewidth=3)
        ax.add_patch(marker)
        markers.append(marker)

    return [patch] + markers


def animate_face_detect(w, theta):
    marker_positions = []
    img = mpimg.imread('image2017.jpg')
    fig = plt.figure(figsize=(7.5, 4.23))
    plt.axis('equal')
    plt.tight_layout()
    ax = fig.add_subplot(111)
    ax.set_xlim(0, img.shape[1])
    ax.set_ylim(0, img.shape[0])
    ax.xaxis.set_tick_params(labelbottom=False, labeltop=False, top=False, bottom=False)
    ax.yaxis.set_tick_params(left=False, labelleft=False)

    patch = patches.Rectangle((PATCH_WIDTH, PATCH_HEIGHT), 100, 120, fill=False, color='r',
                              linewidth=3)

    ax.imshow(img, extent=[0, img.shape[1], 0, img.shape[0]], aspect='auto',
              interpolation="bicubic")
    ax.add_patch(patch)
    patch_positions = []

    for y in range(0, img.shape[0] - PATCH_HEIGHT, STEP):
        for x in range(0, img.shape[1] - PATCH_WIDTH, STEP):
            patch_positions.append([x, y])

    fargs = [ax, patch, patch_positions, img, w, theta]
    anim = animation.FuncAnimation(fig, animate,
                                   fargs=fargs,
                                   # init_func=self.initialize_animation,
                                   frames=200,
                                   interval=2,
                                   blit=True, repeat=False)
    plt.draw()
    plt.waitforbuttonpress(0)


def run_unittests():
    test_runner = TestRunner()
    results = test_runner.run()
    if results.failures or results.errors:
        exit()
    sleep(0.1)


def run_training():
    data = load_data()

    print('----------Uczenie regresji logistycznej metodą gradientu prostego--------')
    print('------------------To może potrwać ok. 1 min -----------------------------')

    eta = 0.1
    theta = 0.65
    lambdas = [0, 0.00001, 0.0001, 0.001, 0.01, 0.1]
    thetas = list(np.arange(0.1, 0.9, 0.05))

    log_cost_for_data = functools.partial(logistic_cost_function, x_train=data['x_train'],
                                          y_train=data['y_train'])
    w_0 = np.zeros([data['x_train'].shape[1], 1])
    w_computed1, f_values1 = gradient_descent(log_cost_for_data, w_0, EPOCHS, eta)

    print('Wartość funkcji celu na końcu: {:.4f}'.format(f_values1[-1]))

    print('\n-------Uczenie regresji logistycznej metodą gradientu stochastycznego-----')
    print('------------------To może potrwać ok. 1 min -----------------------------')

    w_0 = np.zeros([data['x_train'].shape[1], 1])
    w_computed2, f_values2 = stochastic_gradient_descent(logistic_cost_function, data['x_train'],
                                                         data['y_train'], w_0, EPOCHS, eta,
                                                         MINIBATCH_SIZE)

    print('Wartość funkcji celu na końcu: {:.4f}'.format(f_values2[-1]))
    print('\n--- Wcisnij klawisz, aby kontynuowac ---')
    plot_f_values(f_values1, f_values2)

    print('\n-----------------------Selekcja modelu -------------------------------')
    print('--Algorytm uczący: SGD--')
    print('--Kryterium uczenia: regularized_logistic_cost_function--')
    print('--Krok uczenia: {}--'.format(eta))
    print('--Liczba epok: {}--'.format(EPOCHS))
    print('--Wielkosc mini-batcha: {}--'.format(MINIBATCH_SIZE))

    w_0 = np.zeros([data['x_train'].shape[1], 1])
    l, t, w_computed, F = model_selection(data['x_train'], data['y_train'], data['x_val'],
                                          data['y_val'], w_0, EPOCHS, eta, MINIBATCH_SIZE, lambdas,
                                          thetas)

    print('Najlepszy parametr regularyzacji lambda: {}'.format(l))
    print('Najlepszy prog klasyfikacji theta: {:.4f}'.format(t))
    print('Najlepsza wartosc miary F: {:.4f}'.format(np.max(F)))
    print('\n--- Wcisnij klawisz, aby kontynuowac ---')
    plot_theta_lambda(F, thetas, lambdas)

    print('\n------------------------DETEKCJA TWARZY-------------------------------\n')
    animate_face_detect(w_computed, t)


if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    run_unittests()

    run_training()
