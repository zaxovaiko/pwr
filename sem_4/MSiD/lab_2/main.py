# --------------------------------------------------------------------------
# ------------  Metody Systemowe i Decyzyjne w Informatyce  ----------------
# --------------------------------------------------------------------------
#  Zadanie 2: k-NN i Naive Bayes
#  autorzy: A. Gonczarek, J. Kaczmar, S. Zareba
#  2017
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# ----------------- TEN PLIK MA POZOSTAĆ NIEZMODYFIKOWANY ------------------
# --------------------------------------------------------------------------

import pickle
import warnings
from time import sleep

import matplotlib.pyplot as plt
import numpy as np

from content import (classification_error, estimate_a_priori_nb, estimate_p_x_y_nb,
                     hamming_distance, model_selection_knn, model_selection_nb, p_y_x_knn, p_y_x_nb,
                     sort_train_labels_knn)
from test import TestRunner


def plot_a_b_errors(errors, a_points, b_points):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(errors)
    fig.colorbar(cax)
    plt.title("Selekcja modelu dla NB")
    ax.set_xticklabels([''] + a_points)
    ax.set_yticklabels([''] + b_points)
    ax.xaxis.set_label_position('bottom')
    ax.xaxis.set_tick_params(labelbottom=True, labeltop=False, top=False)
    ax.set_xlabel('Parametr b')
    ax.set_ylabel('Parametr a')
    plt.draw()
    plt.waitforbuttonpress(0)


def plot_error_NB_KNN(error_NB, error_KNN):
    plt.figure()
    plt.rcParams['image.cmap'] = 'gray'
    plt.rcParams['image.interpolation'] = 'none'
    plt.style.use(['dark_background'])
    labels = ["Naive Bayes", "KNN"]
    data = [error_NB, error_KNN]

    xlocations = np.array(range(len(data))) + 0.5
    width = 0.5
    plt.bar(xlocations, data, width=width, color='#FFCC55')
    plt.xticks(xlocations, labels)
    plt.xlim(0, xlocations[-1] + width * 2 - .5)
    plt.title("Porownanie modeli - blad klasyfikacji")
    plt.gca().get_xaxis().tick_bottom()
    plt.gca().get_yaxis().tick_left()
    plt.draw()
    plt.waitforbuttonpress(0)


def classification_KNN_vs_no_neighbours(xs, ys):
    plt.rcParams['image.cmap'] = 'gray'
    plt.rcParams['image.interpolation'] = 'none'
    plt.style.use(['dark_background'])
    plt.xlabel('Liczba sasiadow k')
    plt.ylabel('Blad klasyfikacji')
    plt.title("Selekcja modelu dla k-NN")

    plt.plot(xs, ys, 'r-', color='#FFCC55')
    plt.draw()
    plt.waitforbuttonpress(0)


def word_cloud(frequencies, title):
    from wordcloud import WordCloud
    wordcloud = WordCloud(font_path='DroidSansMono.ttf',
                          relative_scaling=1.0).generate_from_frequencies(frequencies)
    plt.title(title)
    plt.imshow(wordcloud)
    plt.axis("off")
    return wordcloud


def word_clouds(list_of_frequencies, topics):
    fig = plt.figure(num='Rozklad slow w poszczegolnych klasach dla modelu NB')
    plt.rcParams['image.cmap'] = 'gray'
    plt.rcParams['image.interpolation'] = 'none'
    plt.style.use(['dark_background'])
    for idx, (topic, frequencies) in enumerate(zip(topics, list_of_frequencies)):
        location = 221 + idx
        plt.subplot(location)
        wordcloud = word_cloud(frequencies, topic)
        plt.axis("off")
        plt.imshow(wordcloud)
    plt.draw()
    plt.waitforbuttonpress(0)


def run_unittests():
    test_runner = TestRunner()
    results = test_runner.run()
    if results.failures or results.errors:
        exit()
    sleep(0.1)


def load_data():
    PICKLE_FILE_PATH = 'data.pkl'
    with open(PICKLE_FILE_PATH, 'rb') as f:
        return pickle.load(f)


def run_training():
    data = load_data()

    # KNN model selection
    k_values = range(1, 201, 2)
    print('\n------------- Selekcja liczby sasiadow dla modelu dla KNN -------------')
    print('-------------------- Wartosci k: 1, 3, ..., 200 -----------------------')
    print('--------------------- To moze potrwac ok. 1 min ------------------------')

    error_best, best_k, errors = model_selection_knn(data['Xval'],
                                                     data['Xtrain'],
                                                     data['yval'],
                                                     data['ytrain'],
                                                     k_values)
    print('Najlepsze k: {num1} i najlepszy blad: {num2:.4f}'.format(num1=best_k, num2=error_best))
    print('\n--- Wcisnij klawisz, aby kontynuowac ---')
    classification_KNN_vs_no_neighbours(k_values, errors)
    a_values = [1, 3, 10, 30, 100, 300, 1000]
    b_values = [1, 3, 10, 30, 100, 300, 1000]

    print('\n----------------- Selekcja parametrow a i b dla NB --------------------')
    print('--------- Wartosci a i b: 1, 3, 10, 30, 100, 300, 1000 -----------------')
    print('--------------------- To moze potrwac ok. 1 min ------------------------')

    # NB model selection
    error_best, best_a, best_b, errors = model_selection_nb(data['Xtrain'], data['Xval'],
                                                            data['ytrain'],
                                                            data['yval'], a_values, b_values)

    print('Najlepsze a: {}, b: {} i najlepszy blad: {:.4f}'.format(best_a, best_b, error_best))
    print('\n--- Wcisnij klawisz, aby kontynuowac ---')
    plot_a_b_errors(errors, a_values, b_values)
    p_x_y = estimate_p_x_y_nb(data['Xtrain'], data['ytrain'], best_a, best_b)

    classes_no = p_x_y.shape[0]
    print('\n------Wizualizacja najbardziej popularnych slow dla poszczegolnych klas------')
    print('--Sa to slowa o najwyzszym prawdopodobienstwie w danej klasie dla modelu NB--')

    try:
        groupnames = data['groupnames']
        words = {}
        for x in range(classes_no):
            indices = np.argsort(p_x_y[x, :])[::-1][:50]
            words[groupnames[x]] = {word: prob for word, prob in
                                    zip(data['wordlist'][indices], p_x_y[x, indices])}
        word_clouds(words.values(), words.keys())
    except Exception:
        print('---Wystapil problem z biblioteka wordcloud--- ')

    print('\n--- Wcisnij klawisz, aby kontynuowac ---')

    print('\n----------------Porownanie bledow dla KNN i NB---------------------')

    Dist = hamming_distance(data['Xtest'], data['Xtrain'])
    y_sorted = sort_train_labels_knn(Dist, data['ytrain'])
    p_y_x = p_y_x_knn(y_sorted, best_k)
    error_KNN = classification_error(p_y_x, data['ytest'])

    p_y = estimate_a_priori_nb(data['ytrain'])
    p_y_x = p_y_x_nb(p_y, p_x_y, data['Xtest'])
    error_NB = classification_error(p_y_x, data['ytest'])

    plot_error_NB_KNN(error_NB, error_KNN)
    print('\n--- Wcisnij klawisz, aby kontynuowac ---')


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    run_unittests()
    run_training()
