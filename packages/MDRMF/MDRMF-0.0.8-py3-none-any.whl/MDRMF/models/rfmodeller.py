import logging
import pickle
import os
import sys
import random
from typing import Dict
import numpy as np
from numpy import newaxis, concatenate, std
from sklearn.ensemble import RandomForestRegressor
from MDRMF.models.modeller import Modeller
from MDRMF.dataset import Dataset

class RFModeller(Modeller):

    def __init__(
        self, 
        dataset,
        evaluator=None, 
        iterations=10, 
        initial_sample_size=10, 
        acquisition_size=10, 
        acquisition_method="greedy",
        retrain=True,
        seeds=[],
        add_noise=None,
        model_graphs=False,
        feature_importance_opt=None,
        use_pairwise=False,
        **kwargs) -> None:

        super().__init__(
            dataset, 
            evaluator,
            iterations, 
            initial_sample_size, 
            acquisition_size, 
            acquisition_method, 
            retrain,
            seeds,
            add_noise,
            model_graphs)

        self.kwargs = kwargs
        self.model = RandomForestRegressor(**self.kwargs)
        self.feature_importance_opt = feature_importance_opt
        self.use_pairwise = use_pairwise
        self.model_dataset = None

        if self.feature_importance_opt is not None:
            self.optimize_for_feature_importance(self.feature_importance_opt)
            self.dataset = self.eval_dataset.copy() # this is a hot-fix solution


    def fit(self, iterations_in=None):
        """
        Fits the RFModeller.
        """

        if iterations_in is not None:
            feat_opt = True
        else:
            feat_opt = False

        # Seed handling
        if self.seeds is None or len(self.seeds) == 0:
            initial_pts = self._initial_sampler(initial_sample_size=self.initial_sample_size)
        elif isinstance(self.seeds, (list, np.ndarray)) and all(np.issubdtype(type(i), np.integer) for i in self.seeds):
            self.seeds = list(self.seeds)  # Ensure seeds is a list
            if feat_opt == True:
                initial_pts = self.dataset.get_points(self.seeds)
            else:
                initial_pts = self.dataset.get_points(self.seeds, remove_points=True)
        else:
            logging.error("Invalid seeds. Must be a list or ndarray of integers, or None.")
            return

        # Add noise to the initial points if desired
        if self.add_noise is None:
            self.model_dataset = initial_pts
        else:
            noises = np.random.normal(0, self.add_noise, size=initial_pts.y.size)
            initial_pts.y = initial_pts.y + noises
            self.model_dataset = initial_pts

        if not feat_opt:
            print(f"y values of starting points {initial_pts.y}")
        
        # fits the model using a pairwise dataset or normal dataset
        if self.use_pairwise:
            initial_pts_pairwise = initial_pts.create_pairwise_dataset()

            self.model.fit(initial_pts_pairwise.X, initial_pts_pairwise.y)
        else:
            self.model.fit(self.model_dataset.X, self.model_dataset.y)

        # First evaluation, using only the initial points
        if self.evaluator is not None and feat_opt is False:
            self.call_evaluator(i=-1, model_dataset=initial_pts) # -1 because ´call_evaluator´ starts at 1, and this iteration should be 0.

        # implemented to allow the ´fit´ method to be used internally in the class to support ´feature_importance_opt´.
        if iterations_in is None:
            iterations = self.iterations
        else:
            iterations = iterations_in

        for i in range(iterations):

            # Acquire new points
            acquired_pts = self._acquisition(model=self.model, model_dataset=self.model_dataset, add_noise=self.add_noise)

            self.model_dataset = self.dataset.merge_datasets([self.model_dataset, acquired_pts])

            # Reset model before training if true
            if self.retrain:
                self.model = RandomForestRegressor(**self.kwargs)
            
            # fits the model using a pairwise dataset or normal dataset
            if self.use_pairwise:
                model_dataset_pairwise = self.model_dataset.create_pairwise_dataset()
                self.model.fit(model_dataset_pairwise.X, model_dataset_pairwise.y)
            else:
                self.model.fit(self.model_dataset.X, self.model_dataset.y)

            # Call evaluator if true
            if self.evaluator is not None and feat_opt is False:
                self.call_evaluator(i=i, model_dataset=self.model_dataset)

            if feat_opt:
                self._print_progress_bar(iteration=i, total=iterations)

        if feat_opt:
            print("\n")

        if self.model_graphs:
            self.graph_model()

        return self.model
    

    def _pairwise_predict_old(self, train_dataset: Dataset, predict_dataset: Dataset, model: RandomForestRegressor):
        """
        Predicts molecular properties in the prediction dataset using a RandomForestRegressor model and pairwise comparisons with the training dataset.

        Parameters:
        - train_dataset (Dataset): Dataset with known molecular properties for training.
        - predict_dataset (Dataset): Dataset of molecules to predict properties for.
        - model (RandomForestRegressor): Trained RandomForestRegressor model.

        Returns:
        - List[float]: Predicted properties for each molecule in the predict_dataset.
        """
        mols_predict = predict_dataset.X
        mols_train = train_dataset.X
        y_train = train_dataset.y

        predictions = []
        for pmol in mols_predict:
            X_test = []
            for tmol in mols_train:
                X = list(tmol) + list(pmol) + (list(tmol - pmol))
                X_test.append(X)      
            
            dy_preds = model.predict(np.array(X_test))
            y_preds = y_train + dy_preds
            y_pred = y_preds.mean()
            predictions.append(y_pred)

        predictions = np.array(predictions)
        return predictions

    
    def _pairwise_predict(self, train_dataset: Dataset, predict_dataset: Dataset, model: RandomForestRegressor):
        n1 = predict_dataset.X.shape[0]
        n2 = train_dataset.X.shape[0]

        X1X2 = self.PADRE_features(predict_dataset.X, train_dataset.X)
        y1_minus_y2_hat = model.predict(X1X2)
        y1_hat_distribution = y1_minus_y2_hat.reshape(n1, n2) + train_dataset.y[np.newaxis, :]
        mu = y1_hat_distribution.mean(axis=1)
        std = y1_hat_distribution.std(axis=1)
        return mu, std
    

    def predict(self, dataset: Dataset, dataset_train: Dataset = None, return_uncertainty = False):

        if isinstance(dataset, Dataset) is False:
            logging.error("Wrong object type. Must be of type `Dataset`")
            sys.exit()

        def pred_with_uncertainty(X, rfr):
            preds = np.zeros((len(dataset.y), len(rfr.estimators_)))
            for j, submodel in enumerate(rfr.estimators_):
                preds[:,j] = submodel.predict(X)
            return np.mean(preds, axis=1), np.var(preds, axis=1)        

        # If the user wants the uncertainty on the predictions this code is executed.
        if return_uncertainty:
            if isinstance(dataset, Dataset) and isinstance(dataset_train, Dataset) and self.use_pairwise:
                preds, uncertainty = self._pairwise_predict(dataset_train, dataset, self.model)
            elif isinstance(dataset, Dataset) is True:
                preds, uncertainty = pred_with_uncertainty(dataset.X, self.model)
            return preds, uncertainty
        else:
        # By default only the predictions are returned.
            if isinstance(dataset, Dataset) and isinstance(dataset_train, Dataset) and self.use_pairwise:
                preds, _ = self._pairwise_predict(dataset_train, dataset, self.model)
            elif isinstance(dataset, Dataset) is True:
                preds = self.model.predict(dataset.X)
            return preds


    def save(self, filename: str):
        """
        Save the RFModeller to a pickle file
        """
        # Check if filename is a string.
        if not isinstance(filename, str):
            raise ValueError("filename must be a string")
        
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except FileNotFoundError:
            logging.error(f"File not found: {filename}")
            raise
        except IOError as e:
            logging.error(f"IOError: {str(e)}")
            raise
        except pickle.PicklingError as e:
            logging.error(f"Failed to pickle model: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            raise
    
    # Can probably be deleted.
    # def _acquisition_pairwise(self):
        
    #     preds = self.predict(self.dataset, self.model_dataset)

    #     if self.acquisition_method == "greedy":

    #         # Find indices of the x-number of smallest values
    #         indices = np.argpartition(preds, self.acquisition_size)[:self.acquisition_size]

    #         # Get the best docked molecules from the dataset
    #         acq_dataset = self.dataset.get_points(indices, remove_points=True)

    #     if self.acquisition_method == "random":
            
    #         # Get random points and delete from dataset
    #         acq_dataset = self.dataset.get_samples(self.acquisition_size, remove_points=True)

    #     return acq_dataset


    @staticmethod
    def load(filename: str):
        
        # Check if filename is a string.
        if not isinstance(filename, str):
            raise ValueError("filename must be a string")
        
        # Check if file exists.
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"No such file or directory: '{filename}'")
        
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            logging.error(f"File not found: {filename}")
            raise
        except IOError as e:
            logging.error(f"IOError: {str(e)}")
            raise
        except pickle.UnpicklingError as e:
            logging.error(f"Failed to unpickle model: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            raise


    def optimize_for_feature_importance(self, opt_parameters: Dict):

        print('Computing feature importance...')

        iterations = opt_parameters['iterations']
        features_limit = opt_parameters['features_limit']
    
        model = self.fit(iterations_in=iterations)

        feature_importances = model.feature_importances_
        feature_importances_sorted = np.argsort(feature_importances)[:-1]
        important_features = feature_importances_sorted[-features_limit:]

        self.dataset.X = self.dataset.X[:, important_features]
        self.eval_dataset.X = self.eval_dataset.X[:, important_features]

        # important_feature_values = feature_importances[important_features]
        # print(f"values of most important features: {important_feature_values}")
        
        print(f"Indices of most important features: {important_features} \n")

        return important_features


    def _print_progress_bar(self, iteration, total, bar_length=50, prefix="Progress"):
        """
        Print the progress bar.

        Args:
            iteration (int): current iteration.
            total (int): total iterations.
            bar_length (int): length of the progress bar.
            prefix (str): Prefix to print before the progress bar. Default is "Progress".
        """
        iteration = iteration + 1
        progress = (iteration / total)
        arrow = '-' * int(round(progress * bar_length) - 1) + '>'
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write(f"\r{prefix}: [{arrow + spaces}] {int(progress * 100)}% ({iteration}/{total})")
        sys.stdout.flush()


    def PADRE_features(self, X1, X2):

        n1 = X1.shape[0]
        n2 = X2.shape[0]

        X1 = X1[:, newaxis, :].repeat(n2, axis=1)
        X2 = X2[newaxis, :, :].repeat(n1, axis=0)

        X1X2_combined = concatenate([X1, X2, X1 - X2], axis=2)
        return X1X2_combined.reshape(n1 * n2, -1)


    def PADRE_labels(self, y1, y2):
        return (y1[:, newaxis] - y2[newaxis, :]).flatten()


    def PADRE_train(self, model, train_X, train_y):
        X1X2 = self.PADRE_features(train_X, train_X)
        y1_minus_y2 = self.PADRE_labels(train_y, train_y)
        model.fit(X1X2, y1_minus_y2)
        return model


    def PADRE_predict(self, model, test_X, train_X, train_y):
        n1 = test_X.shape[0]
        n2 = train_X.shape[0]

        X1X2 = self.PADRE_features(test_X, train_X)
        y1_minus_y2_hat = model.predict(X1X2)
        y1_hat_distribution = y1_minus_y2_hat.reshape(n1, n2) + train_y[newaxis, :]
        mu = y1_hat_distribution.mean(axis=1)
        std = y1_hat_distribution.std(axis=1)
        return mu, std