
from typing import List
import datetime as dt
from datetime import datetime

from classes.TimeInterval import TimeInterval

class InitialDataRequirement():
    def __init__(self, 
                 name: str, 
                 ticker: str, 
                 selected_measurement_time: datetime, 
                 interval_to_measure_at: TimeInterval, 
                 measure_until: datetime = None) -> None:
        self.name = name
        self.ticker = ticker
        self.selected_measurement_time = selected_measurement_time
        self.interval_to_measure_at = interval_to_measure_at

        # optional
        self.measure_until = measure_until
    
    def to_dict(self) -> dict:
        initial_data_requirement = {
            "name": self.name,
            "ticker": self.ticker,
            "selected_measurement_time": int(self.selected_measurement_time.timestamp() * 1000),
            "interval_to_measure_at": self.interval_to_measure_at.value
        }
        if self.measure_until:
            initial_data_requirement["measure_until"] = int(self.measure_until.timestamp() * 1000)
        return initial_data_requirement

    def get_unique_identifier(self) -> str:
        # name should be unique
        return self.name

class ReoccuringDataRequirement():
    def __init__(self, 
                 ticker: str, 
                 interval_to_measure_at: TimeInterval, 
                 refresh_every_ms: int, 
                 num_required_measurements_needed_for_prediction: int) -> None:
        self.ticker = ticker
        self.interval_to_measure_at = interval_to_measure_at
        self.refresh_every_ms = refresh_every_ms
        self.num_required_measurements_needed_for_prediction = num_required_measurements_needed_for_prediction

    def to_dict(self) -> dict:
        return {
            "ticker": self.ticker,
            "interval_to_measure_at": self.interval_to_measure_at.value,
            "refresh_every_ms": self.refresh_every_ms,
            "num_required_measurements_needed_for_prediction": self.num_required_measurements_needed_for_prediction
        }
    
    def get_unique_identifier(self) -> str:
        # the concatonation of the ticker and interval will be unique
        return self.ticker + "_" + self.interval_to_measure_at

class ModelDataBlueprint():
    def __init__(self, 
                 initial_data_requirements: List[InitialDataRequirement], 
                 reoccuring_data_requirements: List[ReoccuringDataRequirement]) -> None:
        self.initial_data_requirements: List[InitialDataRequirement] = initial_data_requirements
        self.reoccuring_data_requirements: List[ReoccuringDataRequirement] = reoccuring_data_requirements

    def to_dict(self) -> dict:
        return {
            "initial": [initial_req.to_dict() for initial_req in self.initial_data_requirements],
            "on_new": [reoccur_req.to_dict() for reoccur_req in self.reoccuring_data_requirements]
        }