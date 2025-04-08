import joblib
import numpy as np
import json


class Predictor:
    def __init__(self):
        model_local_path = "/var/task/model.pkl"
        try:
            self.model = joblib.load(model_local_path)
        except Exception as e:
            print(f"An error occurred loading the model: {e}")
            self.model = None

    def predict(self, inputs):
        try:
            input_array = np.array(inputs).reshape(1, -1)
            predictions = self.model.predict(input_array)
            predictions = predictions[0].tolist()
            return [round(elem, 3) for elem in predictions]
        except Exception as e:
            print(f"An error occurred: {e}")
            return []


def handler(event, context):
    # inputs = [41.27, 6.43, 3.55, 82.54, 11.6, 500, 120, 200, 0.1]
    my_string = event["body"].strip('"')
    data = json.loads(my_string)
    inputs = data["input"]
    prd = Predictor()
    predictions = list(prd.predict(inputs))
    print("predictions: ", predictions)
    return predictions
    # return {"statusCode": 200, "body": predictions}
