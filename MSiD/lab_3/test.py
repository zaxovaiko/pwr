# --------------------------------------------------------------------------
# ------------  Metody Systemowe i Decyzyjne w Informatyce  ----------------
# --------------------------------------------------------------------------
#  Zadanie 3: Regresja logistyczna
#  autorzy: A. Gonczarek, J. Kaczmar, S. Zareba
#  2017
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# ----------------- TEN PLIK MA POZOSTAĆ NIEZMODYFIKOWANY ------------------
# --------------------------------------------------------------------------

import functools
import pickle
from unittest import TestCase, TestSuite, TextTestRunner, defaultTestLoader

import numpy as np

from content import (f_measure, gradient_descent, logistic_cost_function, model_selection,
                     prediction, regularized_logistic_cost_function, sigmoid,
                     stochastic_gradient_descent)

with open('test_data.pkl', mode='rb') as file_:
    TEST_DATA = pickle.load(file_)


class TestRunner:
    def __init__(self):
        self.runner = TextTestRunner(verbosity=2)

    def run(self):
        test_suite = TestSuite(tests=[
            defaultTestLoader.loadTestsFromTestCase(TestSigmoid),
            defaultTestLoader.loadTestsFromTestCase(TestLogisticCostFunction),
            defaultTestLoader.loadTestsFromTestCase(TestGradientDescent),
            defaultTestLoader.loadTestsFromTestCase(TestStochasticGradientDescent),
            defaultTestLoader.loadTestsFromTestCase(TestRegularizedLogisticCostFunction),
            defaultTestLoader.loadTestsFromTestCase(TestPrediction),
            defaultTestLoader.loadTestsFromTestCase(TestFMeasure),
            defaultTestLoader.loadTestsFromTestCase(TestModelSelection),
        ])
        return self.runner.run(test_suite)


class TestSigmoid(TestCase):
    def test_sigmoid(self):
        arg = TEST_DATA['sigm']['arg']
        val_expected = TEST_DATA['sigm']['val']

        val = sigmoid(arg)

        self.assertEqual(np.shape(val), (2, 1))
        np.testing.assert_almost_equal(val, val_expected)


class TestLogisticCostFunction(TestCase):
    def test_logstic_cost_function_val(self):
        w = TEST_DATA['cost']['w']
        x_train = TEST_DATA['cost']['x_train']
        y_train = TEST_DATA['cost']['y_train']
        log_expected = TEST_DATA['cost']['L']

        log, _ = logistic_cost_function(w, x_train, y_train)

        self.assertEqual(np.size(log), 1)
        self.assertAlmostEqual(log, log_expected)

    def test_logstic_cost_function_grad(self):
        w = TEST_DATA['cost']['w']
        x_train = TEST_DATA['cost']['x_train']
        y_train = TEST_DATA['cost']['y_train']
        grad_expected = TEST_DATA['cost']['grad']

        _, grad = logistic_cost_function(w, x_train, y_train)

        self.assertEqual(np.shape(grad), (20, 1))
        np.testing.assert_almost_equal(grad, grad_expected)


class TestGradientDescent(TestCase):
    def test_gradient_descent_w(self):
        x_train = TEST_DATA['opt']['x_train']
        y_train = TEST_DATA['opt']['y_train']
        obj_fun = functools.partial(logistic_cost_function, x_train=x_train, y_train=y_train)
        w0 = np.copy(TEST_DATA['opt']['w0'])
        epochs = TEST_DATA['opt']['epochs']
        eta = TEST_DATA['opt']['step']
        w_expected = TEST_DATA['opt']['w']

        w, _ = gradient_descent(obj_fun, w0, epochs, eta)

        self.assertEqual(np.shape(w), (2, 1))
        np.testing.assert_almost_equal(w, w_expected)

    def test_gradient_descent_func_values(self):
        x_train = TEST_DATA['opt']['x_train']
        y_train = TEST_DATA['opt']['y_train']
        obj_fun = functools.partial(logistic_cost_function, x_train=x_train, y_train=y_train)
        w0 = np.copy(TEST_DATA['opt']['w0'])
        epochs = TEST_DATA['opt']['epochs']
        eta = TEST_DATA['opt']['step']
        log_values_expected = TEST_DATA['opt']['func_values']

        _, log_values = gradient_descent(obj_fun, w0, epochs, eta)

        self.assertEqual(len(log_values), 100)
        np.testing.assert_almost_equal(log_values, log_values_expected)


class TestStochasticGradientDescent(TestCase):
    def test_stochastic_gradient_descent_w(self):
        x_train = TEST_DATA['sopt']['x_train']
        y_train = TEST_DATA['sopt']['y_train']
        w0 = np.copy(TEST_DATA['sopt']['w0'])
        epochs = TEST_DATA['sopt']['epochs']
        eta = TEST_DATA['sopt']['step']
        mini_batch = TEST_DATA['sopt']['mini_batch']
        w_expected = TEST_DATA['sopt']['w']

        w, _ = stochastic_gradient_descent(logistic_cost_function, x_train, y_train, w0, epochs,
                                           eta, mini_batch)

        self.assertEqual(np.shape(w), (2, 1))
        np.testing.assert_almost_equal(w, w_expected)

    def test_stochastic_gradient_descent_func_values(self):
        x_train = TEST_DATA['sopt']['x_train']
        y_train = TEST_DATA['sopt']['y_train']
        w0 = np.copy(TEST_DATA['sopt']['w0'])
        epochs = TEST_DATA['sopt']['epochs']
        eta = TEST_DATA['sopt']['step']
        mini_batch = TEST_DATA['sopt']['mini_batch']
        log_values_expected = TEST_DATA['sopt']['func_values']

        _, log_values = stochastic_gradient_descent(logistic_cost_function, x_train, y_train, w0,
                                                     epochs, eta, mini_batch)

        self.assertEqual(len(log_values), 100)
        np.testing.assert_almost_equal(log_values, log_values_expected)


class TestRegularizedLogisticCostFunction(TestCase):
    def test_regularized_logstic_cost_function_val(self):
        w = TEST_DATA['rcost']['w']
        x_train = TEST_DATA['rcost']['x_train']
        y_train = TEST_DATA['rcost']['y_train']
        reg_lambda = TEST_DATA['rcost']['lambda']
        val_expected = TEST_DATA['rcost']['L']

        val, _ = regularized_logistic_cost_function(w, x_train, y_train, reg_lambda)

        self.assertEqual(np.size(val), 1)
        self.assertAlmostEqual(val, val_expected)

    def test_regularized_logstic_cost_function_grad(self):
        w = TEST_DATA['rcost']['w']
        x_train = TEST_DATA['rcost']['x_train']
        y_train = TEST_DATA['rcost']['y_train']
        reg_lambda = TEST_DATA['rcost']['lambda']
        grad_expected = TEST_DATA['rcost']['grad']

        _, grad = regularized_logistic_cost_function(w, x_train, y_train, reg_lambda)

        self.assertEqual(np.shape(grad), (20, 1))
        np.testing.assert_almost_equal(grad, grad_expected)


class TestPrediction(TestCase):
    def test_prediction(self):
        x = TEST_DATA['pred']['x']
        w = TEST_DATA['pred']['w']
        theta = TEST_DATA['pred']['theta']
        y_expected = TEST_DATA['pred']['y']

        y = prediction(x, w, theta)

        self.assertEqual(np.shape(y), (50, 1))
        np.testing.assert_almost_equal(y, y_expected)


class TestFMeasure(TestCase):
    def test_f_measure(self):
        y = TEST_DATA['fm']['y']
        y_pred = TEST_DATA['fm']['y_pred']
        f_expected = TEST_DATA['fm']['f']

        f = f_measure(y, y_pred)

        self.assertEqual(np.size(f), 1)
        self.assertAlmostEqual(f, f_expected)


class TestModelSelection(TestCase):
    def test_model_selection_lambda(self):
        x_train = TEST_DATA['ms']['x_train']
        y_train = TEST_DATA['ms']['y_train']
        x_val = TEST_DATA['ms']['x_val']
        y_val = TEST_DATA['ms']['y_val']
        w0 = TEST_DATA['ms']['w0']
        epochs = TEST_DATA['ms']['epochs']
        eta = TEST_DATA['ms']['step']
        mini_batch = TEST_DATA['ms']['mini_batch']
        lambdas = TEST_DATA['ms']['lambdas']
        thetas = TEST_DATA['ms']['thetas']
        reg_lambda_expected = TEST_DATA['ms']['lambda']

        reg_lambda, _, _, _ = model_selection(x_train, y_train, x_val, y_val, w0, epochs, eta,
                                              mini_batch, lambdas, thetas)

        self.assertEqual(np.size(reg_lambda), 1)
        self.assertAlmostEqual(reg_lambda, reg_lambda_expected)

    def test_model_selection_theta(self):
        x_train = TEST_DATA['ms']['x_train']
        y_train = TEST_DATA['ms']['y_train']
        x_val = TEST_DATA['ms']['x_val']
        y_val = TEST_DATA['ms']['y_val']
        w0 = TEST_DATA['ms']['w0']
        epochs = TEST_DATA['ms']['epochs']
        eta = TEST_DATA['ms']['step']
        mini_batch = TEST_DATA['ms']['mini_batch']
        lambdas = TEST_DATA['ms']['lambdas']
        thetas = TEST_DATA['ms']['thetas']
        theta_expected = TEST_DATA['ms']['theta']

        _, theta, _, _ = model_selection(x_train, y_train, x_val, y_val, w0, epochs, eta,
                                         mini_batch, lambdas, thetas)

        self.assertEqual(np.size(theta), 1)
        self.assertAlmostEqual(theta, theta_expected)

    def test_model_selection_w(self):
        x_train = TEST_DATA['ms']['x_train']
        y_train = TEST_DATA['ms']['y_train']
        x_val = TEST_DATA['ms']['x_val']
        y_val = TEST_DATA['ms']['y_val']
        w0 = TEST_DATA['ms']['w0']
        epochs = TEST_DATA['ms']['epochs']
        eta = TEST_DATA['ms']['step']
        mini_batch = TEST_DATA['ms']['mini_batch']
        lambdas = TEST_DATA['ms']['lambdas']
        thetas = TEST_DATA['ms']['thetas']
        w_expected = TEST_DATA['ms']['w']

        _, _, w, _ = model_selection(x_train, y_train, x_val, y_val, w0, epochs, eta, mini_batch,
                                     lambdas, thetas)

        self.assertEqual(np.shape(w), (2, 1))
        np.testing.assert_almost_equal(w, w_expected)

    def test_model_selection_F(self):
        x_train = TEST_DATA['ms']['x_train']
        y_train = TEST_DATA['ms']['y_train']
        x_val = TEST_DATA['ms']['x_val']
        y_val = TEST_DATA['ms']['y_val']
        w0 = TEST_DATA['ms']['w0']
        epochs = TEST_DATA['ms']['epochs']
        eta = TEST_DATA['ms']['step']
        mini_batch = TEST_DATA['ms']['mini_batch']
        lambdas = TEST_DATA['ms']['lambdas']
        thetas = TEST_DATA['ms']['thetas']
        F_expected = TEST_DATA['ms']['F']

        _, _, _, F = model_selection(x_train, y_train, x_val, y_val, w0, epochs, eta, mini_batch,
                                     lambdas, thetas)

        self.assertEqual(np.shape(F), (3, 4))
        np.testing.assert_almost_equal(F, F_expected)
