"""
End-to-End ML Pipeline
Titanic Survival Prediction
Author: Aditya Sawarkar
"""

import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def build_pipeline():

    try:
        print("Loading dataset...")

        # Load dataset
        df = pd.read_csv("../03_eda/titanic.csv")

        print(f"Dataset Shape: {df.shape}")

        # Drop unnecessary columns
        df = df.drop(columns=["Cabin", "Name", "Ticket", "PassengerId"])

        X = df.drop("Survived", axis=1)
        y = df["Survived"]

        # Feature categories
        numeric_features = ["Age", "Fare", "SibSp", "Parch"]
        categorical_features = ["Sex", "Embarked", "Pclass"]

        # Numeric pipeline
        numeric_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ])

        # Categorical pipeline
        categorical_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ])

        # Combine preprocessing
        preprocessor = ColumnTransformer([
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, categorical_features)
        ])

        # Full pipeline
        model_pipeline = Pipeline([
            ("preprocessing", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000))
        ])

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        print(f"Training samples: {len(X_train)}")
        print(f"Testing samples: {len(X_test)}")

        # Train
        model_pipeline.fit(X_train, y_train)

        # Evaluate
        y_pred = model_pipeline.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        print(f"Model Accuracy: {accuracy:.2f}")

        # Save model
        model_path = "model.pkl"
        joblib.dump(model_pipeline, model_path)

        print(f"Model successfully saved as {model_path}")

        return accuracy

    except Exception as e:
        print("Error occurred during pipeline execution:")
        print(e)


if __name__ == "__main__":
    build_pipeline()

