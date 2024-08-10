"""ModelTemplateClass.py 

A template (interface-like) class for defining the expected methods of a model
NOTE: Every model will be a sub-class of this class
"""

from abc import ABC, abstractmethod

from classes.ModelDataBlueprint import ModelDataBlueprint
from classes.PredictionResponse import PredictionResponse
from saft_model.classes.InputData import PredictPostBody

class SAFTModelClass(ABC):
    @abstractmethod
    def predict(self, prediction_input: PredictPostBody) -> PredictionResponse:
        """
        Takes in dictionary of data points for prediction,
        returns a prediction response object
        """
        return None