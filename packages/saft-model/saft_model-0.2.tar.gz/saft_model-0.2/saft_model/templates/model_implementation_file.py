
model_implementation_file_template = """
# ------------------------------------------------------------------------------------------
# SAFT MODEL PROJECT
#
# PROJECT NAME: {project_name}
# MODEL NAME: {model_name}
# ------------------------------------------------------------------------------------------


from saft_model.classes import SAFTModelClass
from saft_model.classes.InputData import InputData  
from saft_model.classes.PredictionResponse import PredictionResponse

class {model_name}(SAFTModelClass):
    def predict(self, data_input: InputData) -> PredictionResponse:
        return None

"""

def format_template_file(project_name: str, model_name: str):
    model_implementation_file_template.format(
        project_name=project_name,
        model_name=model_name
    )
    return model_implementation_file_template