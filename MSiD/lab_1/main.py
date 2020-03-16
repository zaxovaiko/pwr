# --------------------------------------------------------------------------
# ------------  Metody Systemowe i Decyzyjne w Informatyce  ----------------
# --------------------------------------------------------------------------
#  Zadanie 1: Regresja liniowa
#  autorzy: A. Gonczarek, J. Kaczmar, S. Zareba
#  2017
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# ----------------- TEN PLIK MA POZOSTAC NIEZMODYFIKOWANY ------------------
# --------------------------------------------------------------------------

import os
import pickle
import warnings
from time import sleep

import matplotlib.pyplot as plt
import numpy as np

from content import least_squares, model_selection, regularized_model_selection
from test import TestRunner
from utils import polynomial


def target_output(x):
    return np.sin(2 * np.pi * x)


def plot_model(x_train, y_train, x, y_obj, y_model, x_val=None, y_val=None,
               train_err=None, val_err=None):
    x_min = np.min([np.min(x_train), np.min(x)])
    x_max = np.max([np.max(x_train), np.max(x)])
    y_min = -1.5
    y_max = 1.5
    int_x = x_max - x_min
    x_beg = x_min - int_x / 14.0
    x_end = x_max + int_x / 14.0
    x_ticks = [x_min, x_max]
    int_y = y_max - y_min
    y_ticks = [y_min, y_min + 0.5 * int_y, y_max]

    sub.set_xlim(x_beg, x_end)
    sub.set_ylim(1.1 * y_min, 1.1 * y_max)
    sub.set_xticks(x_ticks)
    sub.set_yticks(y_ticks)
    sub.plot(x_train, y_train, 'o', markerfacecolor='none', markeredgecolor='blue',
             markersize=8, markeredgewidth=2)
    sub.plot(x, y_obj, '-g', linewidth=2)
    sub.plot(x, y_model, '-r', linewidth=2)
    if x_val is not None and y_val is not None:
        sub.plot(x_val, y_val, 'o', markerfacecolor='none', markeredgecolor='red',
                 markersize=8, markeredgewidth=2)
    if train_err is not None and val_err is not None:
        sub.text(0, -1.3, 'Train error: {0:.5f}\nVal error:    {1:.5f}'.format(
            train_err, val_err), bbox={'facecolor': 'none', 'pad': 10})


if __name__ == "__main__":
    # Ignorowanie warningow
    warnings.filterwarnings("ignore")

    # Odpalenie testow
    test_runner = TestRunner()
    results = test_runner.run()

    if results.failures:
        exit()
    sleep(0.1)

    # Ladowanie danych
    with open(os.path.join(os.path.dirname(__file__), 'data.pkl'), mode='rb') as file:
        data = pickle.load(file)
    x_plot = np.arange(0, 1.01, 0.01)
    y_obj = target_output(x_plot)

    # Dopasowanie wielomianow metoda najmniejszych kwadratow
    print('\n--- Dopasowanie wielomianow metoda najmniejszych kwadratow ---')
    print('-------------- Liczba punktow treningowych N=8. --------------')
    fig = plt.figure(figsize=(12, 6), num='Zadanie najmniejszych kwadratow dla N=8')

    for i in range(8):
        w, err = least_squares(data['x_train_8'], data['y_train_8'], i)
        y_model = polynomial(x_plot, w)
        sub = fig.add_subplot(2, 4, i + 1)
        plot_model(data['x_train_8'], data['y_train_8'], x_plot, y_obj, y_model)
        sub.set_title("M = {}".format(i))

    plt.tight_layout()
    plt.draw()
    print('\n--- Wcisnij klawisz, aby kontynuowac ---')
    plt.waitforbuttonpress(0)

    print('\n--- Dopasowanie wielomianow metoda najmniejszych kwadratow ---')
    print('-------------- Liczba punktow treningowych N=50. --------------')
    fig = plt.figure(figsize=(12, 6), num='Zadanie najmniejszych kwadratow dla N=50')

    for i in range(8):
        w, err = least_squares(data['x_train_50'], data['y_train_50'], i)
        y_model = polynomial(x_plot, w)
        sub = fig.add_subplot(2, 4, i + 1)
        plot_model(data['x_train_50'], data['y_train_50'], x_plot, y_obj, y_model)
        sub.set_title("M = {}".format(i))

    plt.tight_layout()
    plt.draw()
    print('\n--- Wcisnij klawisz, aby kontynuowac ---')
    plt.waitforbuttonpress(0)

    # Selekcja modelu
    print('\n--- Selekcja modelu dla liniowego zadania najmniejszych kwadratow ---')
    print('---------------- Modele wielomianowe stopnia M=0,...,7 ----------------')
    print('- Liczba punktow treningowych N=50. Liczba punktow walidacyjnych N=20 -')

    M_values = range(0, 7)
    w, train_err, val_err = model_selection(data['x_train_50'], data['y_train_50'],
                                            data['x_val_20'], data['y_val_20'], M_values)
    M = np.shape(w)[0] - 1
    y_model = polynomial(x_plot, w)

    fig = plt.figure(figsize=(6, 5), num='Selekcja modelu dla M')
    sub = fig.add_subplot(1, 1, 1)
    sub.set_title('Najlepsze M={}'.format(M))
    plot_model(data['x_train_50'], data['y_train_50'], x_plot, y_obj, y_model,
               data['x_val_20'], data['y_val_20'], train_err, val_err)

    plt.tight_layout()
    plt.draw()
    print('\n--- Wcisnij klawisz, aby kontynuowac ---')
    plt.waitforbuttonpress(0)

    print('\n--- Selekcja modelu dla liniowego zadania najmniejszych kwadratow z regularyzacja ---')
    print('-- Stopien M=7. Liczba punktow treningowych N=50. Liczba punktow walidacyjnych N=20 --')

    M = 7
    lambdas = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300]
    w, train_err, val_err, best_lambda = regularized_model_selection(data['x_train_50'],
                                                                     data['y_train_50'],
                                                                     data['x_val_20'],
                                                                     data['y_val_20'],
                                                                     M, lambdas)
    y_model = polynomial(x_plot, w)

    fig = plt.figure(figsize=(6, 5), num='Selekcja modelu dla parametru regularyzacji')
    sub = fig.add_subplot(1, 1, 1)
    sub.set_title('M={}    Najlepsze $\lambda$={}'.format(M, best_lambda))
    plot_model(data['x_train_50'], data['y_train_50'], x_plot, y_obj, y_model,
               data['x_val_20'], data['y_val_20'],
               train_err, val_err)

    plt.tight_layout()
    plt.draw()
    print('\n--- Wcisnij klawisz, aby kontynuowac ---')
    plt.waitforbuttonpress(0)
