import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics

import autosklearn.classification

import numpy as np


def main():
    #load and set data
    data = np.loadtxt("2003_NFL_TEAM_STATS.csv", delimiter=",")
    X = data[:,0:35] #identify columns as data sets
    y = data[:,36] #identfy last column as target
    X_train, X_test, y_train, y_test = \
        sklearn.model_selection.train_test_split(X, y, random_state=1)

    automl = autosklearn.classification.AutoSklearnClassifier(
        time_left_for_this_task=120, per_run_time_limit=30,
        tmp_folder='/tmp/autoslearn_cv_example_tmp',
        output_folder='/tmp/autosklearn_cv_example_out',
        delete_tmp_folder_after_terminate=False,
        resampling_strategy='cv',
        resampling_strategy_arguments={'folds': 10})

    automl.fit(X_train.copy(), y_train.copy(), dataset_name='digits')
    automl.refit(X_train.copy(), y_train.copy())

    print(automl.show_models())

    predictions = automl.predict(X_test)
    print("Accuracy score", sklearn.metrics.accuracy_score(y_test, predictions))


if __name__ == '__main__':
    main()
