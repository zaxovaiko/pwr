import numpy as np
import pickle
import scipy.io

def get_data():
    train_data = scipy.io.loadmat('/home/joanna/studia_doktoranckie/MSiD/zadanie2/data2.mat')
    test_data = scipy.io.loadmat('/home/joanna/studia_doktoranckie/MSiD/zadanie2/test.mat')

    return train_data, test_data['test']

def process_test_data(test_data):

    d = {'hamming_distance':
             {'X': test_data['hamming_distance'][0][0][0]['X'][0],
              'X_train': test_data['hamming_distance'][0][0][0]['Xtrain'][0],
              'Dist': test_data['hamming_distance'][0][0][0]['Dist'][0]
              },
         'sort_train_labels_KNN':
             {'y': test_data['sort_train_labels_KNN'][0][0][0]['y'][0][0],
              'y_sorted': test_data['sort_train_labels_KNN'][0][0][0]['y_sorted'][0],
              'Dist': test_data['sort_train_labels_KNN'][0][0][0]['Dist'][0]
              },
         'p_y_x_KNN':
             {'y': test_data['p_y_x_KNN'][0][0][0]['y'][0],
              'K': test_data['p_y_x_KNN'][0][0][0]['K'][0][0][0],
              'p_y_x': test_data['p_y_x_KNN'][0][0][0]['p_y_x'][0]
              },
         'error_fun':
             {'p_y_x': test_data['error_fun'][0][0][0]['p_y_x'][0],
              'y_true': test_data['error_fun'][0][0][0]['y_true'][0][0],
              'error_val': test_data['error_fun'][0][0][0]['error_val'][0][0][0]
              },
         'model_selection_KNN':
             {'Xtrain': test_data['model_selection_KNN'][0][0][0]['Xtrain'][0],
              'Xval': test_data['model_selection_KNN'][0][0][0]['Xval'][0],
              'ytrain': test_data['model_selection_KNN'][0][0][0]['ytrain'][0][0],
              'yval': test_data['model_selection_KNN'][0][0][0]['yval'][0][0],
              'K_values': test_data['model_selection_KNN'][0][0][0]['K_values'][0][0],
              'errors': test_data['model_selection_KNN'][0][0][0]['errors'][0][0],
              'error_best': test_data['model_selection_KNN'][0][0][0]['error_best'][0][0][0],
              'best_K': test_data['model_selection_KNN'][0][0][0]['best_K'][0][0][0]
              },
         'estimate_a_priori_NB':
             {'ytrain': test_data['estimate_a_priori_NB'][0][0][0]['ytrain'][0][0],
              'p_y': test_data['estimate_a_priori_NB'][0][0][0]['p_y'][0].reshape(4)
              },
         'estimate_p_x_y_NB':
             {'Xtrain': test_data['estimate_p_x_y_NB'][0][0][0]['Xtrain'][0],
              'ytrain': test_data['estimate_p_x_y_NB'][0][0][0]['ytrain'][0][0],
              'a': test_data['estimate_p_x_y_NB'][0][0][0]['a'][0][0],
              'b': test_data['estimate_p_x_y_NB'][0][0][0]['b'][0][0],
              'p_x_y': test_data['estimate_p_x_y_NB'][0][0][0]['p_x_y'][0],
              },
         'p_y_x_NB':
             {'p_x_1_y': test_data['p_y_x_NB'][0][0][0]['p_x_1_y'][0],
              'p_y': test_data['p_y_x_NB'][0][0][0]['p_y'][0].reshape(4),
              'X': test_data['p_y_x_NB'][0][0][0]['X'][0],
              'p_y_x': test_data['p_y_x_NB'][0][0][0]['p_y_x'][0]
              },
         'model_selection_NB':
             {'Xtrain': test_data['model_selection_NB'][0][0][0]['Xtrain'][0],
              'Xval': test_data['model_selection_NB'][0][0][0]['Xval'][0],
              'yval': test_data['model_selection_NB'][0][0][0]['yval'][0][0],
              'ytrain': test_data['model_selection_NB'][0][0][0]['ytrain'][0][0],
              'a': test_data['model_selection_NB'][0][0][0]['a'][0][0],
              'b': test_data['model_selection_NB'][0][0][0]['b'][0][0],
              'a_values': test_data['model_selection_NB'][0][0][0]['a_values'][0][0],
              'b_values': test_data['model_selection_NB'][0][0][0]['b_values'][0][0],
              'error_best': test_data['model_selection_NB'][0][0][0]['error_best'][0][0][0],
              'best_a': test_data['model_selection_NB'][0][0][0]['best_a'][0][0][0],
              'best_b': test_data['model_selection_NB'][0][0][0]['best_b'][0][0][0],
              'errors': test_data['model_selection_NB'][0][0][0]['errors'][0]
              }
         }

    with open('/home/joanna/studia_doktoranckie/MSiD/msid/zadanie2/test_data.pkl', 'wb') as f:
        pickle.dump(d, f)

def process_data(data):

    d = {'Xtest': data['Xtest'],
         'Xtrain': data['Xtrain'],
         'Xval': data['Xval'],
         'groupnames': np.array([x[0] for x in np.array(data['groupnames'][0])]),
         'wordlist': np.array([x[0] for x in np.array(data['wordlist'][0])]),
         'ytest': data['ytest'][0],
         'ytrain': data['ytrain'][0],
         'yval': data['yval'][0]
         }
    import pickle
    with open('/home/joanna/studia_doktoranckie/MSiD/msid/zadanie2/data.pkl', 'wb') as f:
        pickle.dump(d, f)

if __name__ == '__main__':
    train_data, test_data = get_data()
    process_test_data(test_data)
    process_data(train_data)