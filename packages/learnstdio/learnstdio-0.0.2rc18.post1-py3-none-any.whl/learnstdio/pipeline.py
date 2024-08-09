#   ---------------------------------------------------------------------------------
#   Copyright (c) Learnstdio. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is Pipeline module."""


from __future__ import annotations
import json
from sklearn.neighbors import KNeighborsClassifier


def load_pipeline(path: str) -> LoadableModel:
    """This is to load a pipeline from a file."""
    # Read file
    if not path:
        raise ValueError('Path not provided')
    if not path.endswith('.json'):
        raise ValueError('File format not supported')
    with open(path, 'r') as file:
        data = json.load(file)
    # Read model information
    model = data['model']
    if not model:
        raise ValueError('Model not found')
    # Read model parameters information
    parameters = model['parameters']
    if not parameters:
        raise ValueError('Model parameters not found')
    # Create a model object
    if 'knn' in model['name']:
        new_model = LoadableKNN(parameters)
    else:
        raise ValueError('Model not supported')
    #
    return new_model


class LoadableModel:
    """Loadable model from parameters."""

    def __init__(self):
        """Initialize the model."""
        self.model = None

    def predict(self, *args):
        """Predict the output from the model."""
        return self.model.predict([args])[0]


class LoadableKNN(LoadableModel):
    """Loadable KNN model from parameters."""

    def __init__(self, parameters):
        """Initialize the KNN model."""
        super().__init__()
        self.model = KNeighborsClassifier(
            n_neighbors=parameters['n_neighbors'],
        )
        self.model.fit(
            parameters['X'],
            parameters['y'],
        )
