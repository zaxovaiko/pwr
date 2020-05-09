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
from unittest import TestCase, TestSuite, TextTestRunner, makeSuite

import numpy as np

from content import (design_matrix, least_squares, mean_squared_error, model_selection,
                     regularized_least_squares, regularized_model_selection)

with open(os.path.join(os.path.dirname(__file__), 'test_data.pkl'), mode='rb') as file:
    TEST_DATA = pickle.load(file)


class TestRunner:
    def __init__(self):
        self.runner = TextTestRunner(verbosity=2)

    def run(self):
        test_suite = TestSuite(tests=[
            makeSuite(TestMeanSquaredError),
            makeSuite(TestDesignMatrix),
            makeSuite(TestLeastSquares),
            makeSuite(TestRegularizedLeastSquares),
            makeSuite(TestModelSelection),
            makeSuite(TestRegularizedModelSelection)
        ])
        return self.runner.run(test_suite)


class TestMeanSquaredError(TestCase):
    def test_mean_squared_error(self):
        x = TEST_DATA['mean_error']['x']
        y = TEST_DATA['mean_error']['y']
        w = TEST_DATA['mean_error']['w']
        err_expected = TEST_DATA['mean_error']['err']

        err = mean_squared_error(x, y, w)

        self.assertEqual(np.size(err), 1)
        self.assertEqual(np.array(err).shape, ())  # err must be a single number
        self.assertAlmostEqual(err, err_expected)


class TestDesignMatrix(TestCase):
    def test_design_matrix(self):
        x_train = TEST_DATA['design_matrix']['x_train']
        M = TEST_DATA['design_matrix']['M']
        dm_expected = TEST_DATA['design_matrix']['dm']

        dm = design_matrix(x_train, M)

        self.assertEqual(np.shape(dm), (20, 8))
        np.testing.assert_almost_equal(dm, dm_expected)


class TestLeastSquares(TestCase):
    def test_least_squares_w(self):
        x_train = TEST_DATA['ls']['x_train']
        y_train = TEST_DATA['ls']['y_train']
        M = TEST_DATA['ls']['M']
        w_expected = TEST_DATA['ls']['w']

        w, _ = least_squares(x_train, y_train, M)

        self.assertEqual(np.shape(w), (7, 1))
        np.testing.assert_almost_equal(w, w_expected)

    def test_least_squares_err(self):
        x_train = TEST_DATA['ls']['x_train']
        y_train = TEST_DATA['ls']['y_train']
        M = TEST_DATA['ls']['M']
        err_expected = TEST_DATA['ls']['err']

        _, err = least_squares(x_train, y_train, M)

        self.assertEqual(np.size(err), 1)
        self.assertAlmostEqual(err, err_expected)


class TestRegularizedLeastSquares(TestCase):
    def test_regularized_least_squares_w(self):
        x_train = TEST_DATA['rls']['x_train']
        y_train = TEST_DATA['rls']['y_train']
        M = TEST_DATA['rls']['M']
        w_expected = TEST_DATA['rls']['w']
        regularization_lambda = TEST_DATA['rls']['lambda']

        w, _ = regularized_least_squares(x_train, y_train, M, regularization_lambda)

        self.assertEqual(np.shape(w), (5, 1))
        np.testing.assert_almost_equal(w, w_expected)

    def test_regularized_least_squares_err(self):
        x_train = TEST_DATA['rls']['x_train']
        y_train = TEST_DATA['rls']['y_train']
        M = TEST_DATA['rls']['M']
        err_expected = TEST_DATA['rls']['err']
        regularization_lambda = TEST_DATA['rls']['lambda']

        _, err = regularized_least_squares(x_train, y_train, M, regularization_lambda)

        self.assertEqual(np.size(err), 1)
        self.assertAlmostEqual(err, err_expected)


class TestModelSelection(TestCase):
    def test_model_selection_w(self):
        x_train = TEST_DATA['ms']['x_train']
        y_train = TEST_DATA['ms']['y_train']
        x_val = TEST_DATA['ms']['x_val']
        y_val = TEST_DATA['ms']['y_val']
        M_values = TEST_DATA['ms']['M_values']
        w_expected = TEST_DATA['ms']['w']

        w, _, _ = model_selection(x_train, y_train, x_val, y_val, M_values)

        self.assertEqual(np.shape(w), (5, 1))
        np.testing.assert_almost_equal(w, w_expected)

    def test_model_selection_train_err(self):
        x_train = TEST_DATA['ms']['x_train']
        y_train = TEST_DATA['ms']['y_train']
        x_val = TEST_DATA['ms']['x_val']
        y_val = TEST_DATA['ms']['y_val']
        M_values = TEST_DATA['ms']['M_values']
        train_err_expected = TEST_DATA['ms']['train_err']

        _, train_err, _ = model_selection(x_train, y_train, x_val, y_val, M_values)

        self.assertEqual(np.size(train_err), 1)
        self.assertAlmostEqual(train_err, train_err_expected)

    def test_model_selection_val_err(self):
        x_train = TEST_DATA['ms']['x_train']
        y_train = TEST_DATA['ms']['y_train']
        x_val = TEST_DATA['ms']['x_val']
        y_val = TEST_DATA['ms']['y_val']
        M_values = TEST_DATA['ms']['M_values']
        val_err_expected = TEST_DATA['ms']['val_err']

        _, _, val_err = model_selection(x_train, y_train, x_val, y_val, M_values)

        self.assertEqual(np.size(val_err), 1)
        self.assertAlmostEqual(val_err, val_err_expected)


class TestRegularizedModelSelection(TestCase):
    def test_regularized_model_selection_w(self):
        x_train = TEST_DATA['rms']['x_train']
        y_train = TEST_DATA['rms']['y_train']
        x_val = TEST_DATA['rms']['x_val']
        y_val = TEST_DATA['rms']['y_val']
        M = TEST_DATA['rms']['M']
        lambda_values = TEST_DATA['rms']['lambda_values']
        w_expected = TEST_DATA['rms']['w']

        w, _, _, _ = regularized_model_selection(x_train, y_train, x_val, y_val, M, lambda_values)

        self.assertEqual(np.shape(w), (8, 1))
        np.testing.assert_almost_equal(w, w_expected)

    def test_regularized_model_selection_train_err(self):
        x_train = TEST_DATA['rms']['x_train']
        y_train = TEST_DATA['rms']['y_train']
        x_val = TEST_DATA['rms']['x_val']
        y_val = TEST_DATA['rms']['y_val']
        M = TEST_DATA['rms']['M']
        lambda_values = TEST_DATA['rms']['lambda_values']
        train_err_expected = TEST_DATA['rms']['train_err']

        _, train_err, _, _ = regularized_model_selection(
            x_train, y_train, x_val, y_val, M, lambda_values)

        self.assertEqual(np.size(train_err), 1)
        self.assertAlmostEqual(train_err, train_err_expected)

    def test_regularized_model_selection_val_err(self):
        x_train = TEST_DATA['rms']['x_train']
        y_train = TEST_DATA['rms']['y_train']
        x_val = TEST_DATA['rms']['x_val']
        y_val = TEST_DATA['rms']['y_val']
        M = TEST_DATA['rms']['M']
        lambda_values = TEST_DATA['rms']['lambda_values']
        val_err_expected = TEST_DATA['rms']['val_err']

        _, _, val_err, _ = regularized_model_selection(
            x_train, y_train, x_val, y_val, M, lambda_values)

        self.assertEqual(np.size(val_err), 1)
        self.assertAlmostEqual(val_err, val_err_expected)

    def test_regularized_model_selection_lambda(self):
        x_train = TEST_DATA['rms']['x_train']
        y_train = TEST_DATA['rms']['y_train']
        x_val = TEST_DATA['rms']['x_val']
        y_val = TEST_DATA['rms']['y_val']
        M = TEST_DATA['rms']['M']
        lambda_values = TEST_DATA['rms']['lambda_values']
        lambda_expected = TEST_DATA['rms']['lambda']

        _, _, _, lambda_ = regularized_model_selection(
            x_train, y_train, x_val, y_val, M, lambda_values)

        self.assertEqual(np.size(lambda_), 1)
        self.assertAlmostEqual(lambda_, lambda_expected)
