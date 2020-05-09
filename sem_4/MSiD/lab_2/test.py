# --------------------------------------------------------------------------
# ------------  Metody Systemowe i Decyzyjne w Informatyce  ----------------
# --------------------------------------------------------------------------
#  Zadanie 2: k-NN i Naive Bayes
#  autorzy: A. Gonczarek, J. Kaczmar, S. Zareba, P. Dąbrowski
#  2019
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# ----------------- TEN PLIK MA POZOSTAĆ NIEZMODYFIKOWANY ------------------
# --------------------------------------------------------------------------

import pickle
from unittest import TestCase, TestSuite, TextTestRunner, defaultTestLoader

import numpy as np

from content import (classification_error, estimate_a_priori_nb, estimate_p_x_y_nb,
                     hamming_distance, model_selection_knn, model_selection_nb, p_y_x_knn, p_y_x_nb,
                     sort_train_labels_knn)

with open('test_data.pkl', mode='rb') as file_:
    TEST_DATA = pickle.load(file_)


class TestRunner:
    def __init__(self):
        self.runner = TextTestRunner(verbosity=2)

    def run(self):
        test_suite = TestSuite(tests=[
            defaultTestLoader.loadTestsFromTestCase(TestHamming),
            defaultTestLoader.loadTestsFromTestCase(TestSortTrainLabelsKNN),
            defaultTestLoader.loadTestsFromTestCase(TestPYXKNN),
            defaultTestLoader.loadTestsFromTestCase(TestClassificationError),
            defaultTestLoader.loadTestsFromTestCase(TestModelSelectionKNN),
            defaultTestLoader.loadTestsFromTestCase(TestEstimateAPrioriNB),
            defaultTestLoader.loadTestsFromTestCase(TestEstimatePXYNB),
            defaultTestLoader.loadTestsFromTestCase(TestPYXNB),
            defaultTestLoader.loadTestsFromTestCase(TestModelSelectionNB),
        ])
        return self.runner.run(test_suite)


class TestHamming(TestCase):
    def test_hamming_distance(self):
        X = TEST_DATA['hamming_distance']['X']
        X_train = TEST_DATA['hamming_distance']['X_train']
        dist_expected = TEST_DATA['hamming_distance']['Dist']

        dist = hamming_distance(X, X_train)

        self.assertEqual(np.shape(dist), (40, 50))
        np.testing.assert_equal(dist, dist_expected)


class TestSortTrainLabelsKNN(TestCase):
    def test_sort_train_labels_knn(self):
        dist = TEST_DATA['sort_train_labels_KNN']['Dist']
        y = TEST_DATA['sort_train_labels_KNN']['y']
        y_sorted_expected = TEST_DATA['sort_train_labels_KNN']['y_sorted']

        y_sorted = sort_train_labels_knn(dist, y)

        self.assertTrue(np.shape(y_sorted), (40, 50))
        np.testing.assert_equal(y_sorted, y_sorted_expected)


class TestPYXKNN(TestCase):
    def test_p_y_x_knn(self):
        y = TEST_DATA['p_y_x_KNN']['y']
        K = TEST_DATA['p_y_x_KNN']['K']
        p_y_x_expected = TEST_DATA['p_y_x_KNN']['p_y_x']

        p_y_x = p_y_x_knn(y, K)

        self.assertEqual(np.shape(p_y_x), (40, 4))
        np.testing.assert_almost_equal(p_y_x, p_y_x_expected)


class TestClassificationError(TestCase):
    def test_classification_error(self):
        p_y_x = TEST_DATA['error_fun']['p_y_x']
        y_true = TEST_DATA['error_fun']['y_true']
        error_val_expected = TEST_DATA['error_fun']['error_val']

        error_val = classification_error(p_y_x, y_true)

        self.assertEqual(np.size(error_val), 1)
        self.assertAlmostEqual(error_val, error_val_expected)


class TestModelSelectionKNN(TestCase):
    def test_model_selection_knn_best_error(self):
        X_val = TEST_DATA['model_selection_KNN']['Xval']
        X_train = TEST_DATA['model_selection_KNN']['Xtrain']
        y_val = TEST_DATA['model_selection_KNN']['yval']
        y_train = TEST_DATA['model_selection_KNN']['ytrain']
        K_values = TEST_DATA['model_selection_KNN']['K_values']
        error_best_expected = TEST_DATA['model_selection_KNN']['error_best']

        best_error, _, _ = model_selection_knn(X_val, X_train, y_val, y_train, K_values)

        self.assertEqual(np.size(best_error), 1)
        self.assertAlmostEqual(best_error, error_best_expected)

    def test_model_selection_knn_best_k(self):
        X_val = TEST_DATA['model_selection_KNN']['Xval']
        X_train = TEST_DATA['model_selection_KNN']['Xtrain']
        y_val = TEST_DATA['model_selection_KNN']['yval']
        y_train = TEST_DATA['model_selection_KNN']['ytrain']
        K_values = TEST_DATA['model_selection_KNN']['K_values']
        best_k_expected = TEST_DATA['model_selection_KNN']['best_K']

        _, best_k, _ = model_selection_knn(X_val, X_train, y_val, y_train, K_values)

        self.assertEqual(np.size(best_k), 1)
        self.assertEqual(best_k, best_k_expected)

    def test_model_selection_knn_errors(self):
        X_val = TEST_DATA['model_selection_KNN']['Xval']
        X_train = TEST_DATA['model_selection_KNN']['Xtrain']
        y_val = TEST_DATA['model_selection_KNN']['yval']
        y_train = TEST_DATA['model_selection_KNN']['ytrain']
        K_values = TEST_DATA['model_selection_KNN']['K_values']
        errors_expected = TEST_DATA['model_selection_KNN']['errors']

        _, _, errors = model_selection_knn(X_val, X_train, y_val, y_train, K_values)

        self.assertEqual(np.shape(errors), (5,))
        np.testing.assert_almost_equal(errors, errors_expected)


class TestEstimateAPrioriNB(TestCase):
    def test_estimate_a_priori_nb(self):
        y_train = TEST_DATA['estimate_a_priori_NB']['ytrain']
        p_y_expected = TEST_DATA['estimate_a_priori_NB']['p_y']

        p_y = estimate_a_priori_nb(y_train)

        self.assertEqual(np.shape(p_y), (4,))
        np.testing.assert_almost_equal(p_y, p_y_expected)


class TestEstimatePXYNB(TestCase):
    def test_estimate_p_x_y_nb(self):
        X_train = TEST_DATA['estimate_p_x_y_NB']['Xtrain']
        y_train = TEST_DATA['estimate_p_x_y_NB']['ytrain']
        a = TEST_DATA['estimate_p_x_y_NB']['a']
        b = TEST_DATA['estimate_p_x_y_NB']['b']
        p_x_y_expected = TEST_DATA['estimate_p_x_y_NB']['p_x_y']

        p_x_y = estimate_p_x_y_nb(X_train, y_train, a, b)

        self.assertEqual(np.shape(p_x_y), (4, 20))
        np.testing.assert_almost_equal(p_x_y, p_x_y_expected)


class TestPYXNB(TestCase):
    def test_p_y_x_nb(self):
        p_y = TEST_DATA['p_y_x_NB']['p_y']
        p_x_1_y = TEST_DATA['p_y_x_NB']['p_x_1_y']
        X = TEST_DATA['p_y_x_NB']['X']
        p_y_x_expected = TEST_DATA['p_y_x_NB']['p_y_x']

        p_y_x = p_y_x_nb(p_y, p_x_1_y, X)

        self.assertEqual(np.shape(p_y_x), (40, 4))
        np.testing.assert_almost_equal(p_y_x, p_y_x_expected)


class TestModelSelectionNB(TestCase):
    def test_model_selection_nb_best_error(self):
        X_train = TEST_DATA['model_selection_NB']['Xtrain']
        X_val = TEST_DATA['model_selection_NB']['Xval']
        y_train = TEST_DATA['model_selection_NB']['ytrain']
        y_val = TEST_DATA['model_selection_NB']['yval']
        a_values = TEST_DATA['model_selection_NB']['a_values']
        b_values = TEST_DATA['model_selection_NB']['b_values']
        error_best_expected = TEST_DATA['model_selection_NB']['error_best']

        error_best, _, _, _ = model_selection_nb(X_train, X_val, y_train, y_val, a_values, b_values)

        self.assertEqual(np.size(error_best), 1)
        self.assertAlmostEqual(error_best, error_best_expected)

    def test_model_selection_nb_best_a(self):
        X_train = TEST_DATA['model_selection_NB']['Xtrain']
        X_val = TEST_DATA['model_selection_NB']['Xval']
        y_train = TEST_DATA['model_selection_NB']['ytrain']
        y_val = TEST_DATA['model_selection_NB']['yval']
        a_values = TEST_DATA['model_selection_NB']['a_values']
        b_values = TEST_DATA['model_selection_NB']['b_values']
        best_a_expected = TEST_DATA['model_selection_NB']['best_a']

        _, best_a, _, _ = model_selection_nb(X_train, X_val, y_train, y_val, a_values, b_values)

        self.assertEqual(np.size(best_a), 1)
        self.assertEqual(best_a, best_a_expected)

    def test_model_selection_nb_best_b(self):
        X_train = TEST_DATA['model_selection_NB']['Xtrain']
        X_val = TEST_DATA['model_selection_NB']['Xval']
        y_train = TEST_DATA['model_selection_NB']['ytrain']
        y_val = TEST_DATA['model_selection_NB']['yval']
        a_values = TEST_DATA['model_selection_NB']['a_values']
        b_values = TEST_DATA['model_selection_NB']['b_values']
        best_b_expected = TEST_DATA['model_selection_NB']['best_b']

        _, _, best_b, _ = model_selection_nb(X_train, X_val, y_train, y_val, a_values, b_values)

        self.assertEqual(np.size(best_b), 1)
        self.assertEqual(best_b, best_b_expected)

    def test_model_selection_nb_errors(self):
        X_train = TEST_DATA['model_selection_NB']['Xtrain']
        X_val = TEST_DATA['model_selection_NB']['Xval']
        y_train = TEST_DATA['model_selection_NB']['ytrain']
        y_val = TEST_DATA['model_selection_NB']['yval']
        a_values = TEST_DATA['model_selection_NB']['a_values']
        b_values = TEST_DATA['model_selection_NB']['b_values']
        errors_expected = TEST_DATA['model_selection_NB']['errors']

        _, _, _, errors = model_selection_nb(X_train, X_val, y_train, y_val, a_values, b_values)

        self.assertEqual(np.shape(errors), (3, 3))
        np.testing.assert_almost_equal(errors, errors_expected)
