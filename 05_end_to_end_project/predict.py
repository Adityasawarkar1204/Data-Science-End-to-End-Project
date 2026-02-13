"""
Prediction Script
"""

import pandas as pd
import joblib


def predict_survival(input_data: dict):

    model = joblib.load("model.pkl")

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    return prediction


if __name__ == "__main__":

    sample_passenger = {
        "Pclass": 3,
        "Sex": "male",
        "Age": 25,
        "SibSp": 0,
        "Parch": 0,
        "Fare": 7.25,
        "Embarked": "S"
    }

    result = predict_survival(sample_passenger)

    if result == 1:
        print("Passenger likely SURVIVED")
    else:
        print("Passenger likely DID NOT SURVIVE")
