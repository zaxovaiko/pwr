# --------------------------------------------------------------------------
# ------------  Metody Systemowe i Decyzyjne w Informatyce  ----------------
# --------------------------------------------------------------------------
#  Zadanie 3: Regresja logistyczna
#  autorzy: A. Gonczarek, J. Kaczmar, S. Zareba, P. Dąbrowski
#  2019
# --------------------------------------------------------------------------

import numpy as np


def sigmoid(x):
    """
    Wylicz wartość funkcji sigmoidalnej dla punktów *x*.

    :param x: wektor wartości *x* do zaaplikowania funkcji sigmoidalnej Nx1
    :return: wektor wartości funkcji sigmoidalnej dla wartości *x* Nx1
    """
    return 1/(1+np.exp(-x))


def logistic_cost_function(w, x_train, y_train):
    """
    Wylicz wartość funkcji logistycznej oraz jej gradient po parametrach.

    :param w: wektor parametrów modelu Mx1
    :param x_train: zbiór danych treningowych NxM
    :param y_train: etykiety klas dla danych treningowych Nx1
    :return: krotka (log, grad), gdzie *log* to wartość funkcji logistycznej,
        a *grad* jej gradient po parametrach *w* Mx1
    """

    sigma = sigmoid(x_train @ w)
    n = sigma.shape[0]

    logarithm = sum(y_train*np.log(sigma)+(1-y_train)*np.log(1-sigma))/(-n)
    grad = x_train.transpose() @ (sigma - y_train) / n
    return logarithm, grad


def gradient_descent(obj_fun, w0, epochs, eta):
    """
    Dokonaj *epochs* aktualizacji parametrów modelu metodą algorytmu gradientu
    prostego, korzystając z kroku uczenia *eta* i zaczynając od parametrów *w0*.
    Wylicz wartość funkcji celu *obj_fun* w każdej iteracji. Wyznacz wartość
    parametrów modelu w ostatniej epoce.

    :param obj_fun: optymalizowana funkcja celu, przyjmująca jako argument
        wektor parametrów *w* [wywołanie *val, grad = obj_fun(w)*]
    :param w0: początkowy wektor parametrów *w* Mx1
    :param epochs: liczba epok algorytmu gradientu prostego
    :param eta: krok uczenia
    :return: krotka (w, log_values), gdzie *w* to znaleziony optymalny
        punkt *w*, a *log_values* to lista wartości funkcji celu w każdej
        epoce (lista o długości *epochs*)
    """
    # obj_fun - gradient descent
    w = w0
    log_values = np.zeros(epochs)

    for i in range(epochs):
        val, grad = obj_fun(w)
        if i != 0:
            log_values[i-1] = val
        w = w - (eta*grad)

    val, grad = obj_fun(w)
    log_values[-1] = val

    return w, log_values


def stochastic_gradient_descent(obj_fun, x_train, y_train, w0, epochs, eta, mini_batch):
    """
    # Dokonaj *epochs* aktualizacji parametrów modelu metodą stochastycznego
    # algorytmu gradientu prostego, korzystając z kroku uczenia *eta*, paczek
    # danych o rozmiarze *mini_batch* i zaczynając od parametrów *w0*. Wylicz
    # wartość funkcji celu *obj_fun* w każdej iteracji. Wyznacz wartość parametrów
    # modelu w ostatniej epoce.
    #
    # :param obj_fun: optymalizowana funkcja celu, przyjmująca jako argumenty
    #     wektor parametrów *w*, paczkę danych składających się z danych
    #     treningowych *x* i odpowiadających im etykiet *y*
    #     [wywołanie *val, grad = obj_fun(w, x, y)*]
    # :param w0: początkowy wektor parametrów *w* Mx1
    # :param epochs: liczba epok stochastycznego algorytmu gradientu prostego
    # :param eta: krok uczenia
    # :param mini_batch: rozmiar paczki danych / mini-batcha
    # :return: krotka (w, log_values), gdzie *w* to znaleziony optymalny
    #     punkt *w*, a *log_values* to lista wartości funkcji celu dla całego
    #     zbioru treningowego w każdej epoce (lista o długości *epochs*)    
    """
    w = w0
    log_values = np.zeros(epochs)

    X = np.array_split(x_train, x_train.shape[0] / mini_batch)
    Y = np.array_split(y_train, y_train.shape[0] / mini_batch)
    for k in range(0, epochs):
        for m in range(0, len(Y)):
            grad_w = obj_fun(w, X[m], Y[m])[1]
            w = w - eta * np.asarray(grad_w)
        log_values[k] = obj_fun(w, x_train, y_train)[0]
    return w, log_values


def regularized_logistic_cost_function(w, x_train, y_train, regularization_lambda):
    """
    Wylicz wartość funkcji logistycznej z regularyzacją l2 oraz jej gradient
    po parametrach.

    :param w: wektor parametrów modelu Mx1
    :param x_train: zbiór danych treningowych NxM
    :param y_train: etykiety klas dla danych treningowych Nx1
    :param regularization_lambda: parametr regularyzacji l2
    :return: krotka (log, grad), gdzie *log* to wartość funkcji logistycznej
        z regularyzacją l2, a *grad* jej gradient po parametrach *w* Mx1
    """
    val, grad = logistic_cost_function(w, x_train, y_train)
    val += 0.5*regularization_lambda*np.sum(w[1:] ** 2)
    grad[1:] = np.add(grad[1:], regularization_lambda * w[1:])
    return val, grad


def prediction(x, w, theta):
    """
    Wylicz wartości predykowanych etykiet dla obserwacji *x*, korzystając
    z modelu o parametrach *w* i progu klasyfikacji *theta*.

    :param x: macierz obserwacji NxM
    :param w: wektor parametrów modelu Mx1
    :param theta: próg klasyfikacji z przedziału [0,1]
    :return: wektor predykowanych etykiet ze zbioru {0, 1} Nx1
    """
    return sigmoid(x @ w) >= theta


def f_measure(y_true, y_pred):
    """
    Wylicz wartość miary F (F-measure) dla zadanych rzeczywistych etykiet
    *y_true* i odpowiadających im predykowanych etykiet *y_pred*.

    :param y_true: wektor rzeczywistych etykiet Nx1
    :param y_pred: wektor etykiet predykowanych przed model Nx1
    :return: wartość miary F (F-measure)
    """
    TP = np.sum(np.logical_and(y_pred, y_true))
    FP = np.sum(np.logical_and(y_pred, np.logical_not(y_true)))
    FN = np.sum(np.logical_and(np.logical_not(y_pred), y_true))

    return (2*TP)/(2*TP+FP+FN)


def model_selection(x_train, y_train, x_val, y_val, w0, epochs, eta, mini_batch, lambdas, thetas):
    """
    Policz wartość miary F dla wszystkich kombinacji wartości regularyzacji
    *lambda* i progu klasyfikacji *theta. Wyznacz parametry *w* dla modelu
    z regularyzacją l2, który najlepiej generalizuje dane, tj. daje najmniejszy
    błąd na ciągu walidacyjnym.

    :param x_train: zbiór danych treningowych NxM
    :param y_train: etykiety klas dla danych treningowych Nx1
    :param x_val: zbiór danych walidacyjnych NxM
    :param y_val: etykiety klas dla danych walidacyjnych Nx1
    :param w0: początkowy wektor parametrów *w* Mx1
    :param epochs: liczba epok stochastycznego algorytmu gradientu prostego
    :param eta: krok uczenia
    :param mini_batch: rozmiar paczki danych / mini-batcha
    :param lambdas: lista wartości parametru regularyzacji l2 *lambda*,
        które mają być sprawdzone
    :param thetas: lista wartości progów klasyfikacji *theta*,
        które mają być sprawdzone
    :return: krotka (regularization_lambda, theta, w, F), gdzie
        *regularization_lambda* to wartość regularyzacji *lambda* dla
        najlepszego modelu, *theta* to najlepszy próg klasyfikacji,
        *w* to parametry najlepszego modelu, a *F* to macierz wartości miary F
        dla wszystkich par *(lambda, theta)* #lambda x #theta
    """
    F = []
    results = []
    for l in lambdas:
        w, _ = stochastic_gradient_descent(lambda w, x, y: regularized_logistic_cost_function(w, x, y, l),
                                           x_train, y_train, w0, epochs, eta, mini_batch)
        F_row = []
        for t in thetas:
            y_pred = prediction(x_val, w, t)
            f = f_measure(y_val, y_pred)
            results.append((l, t, w))
            F_row.append(f)

        F.append(F_row)

    regularization_lambda, theta, w = results[int(np.argmax(F))]

    return regularization_lambda, theta, w, F