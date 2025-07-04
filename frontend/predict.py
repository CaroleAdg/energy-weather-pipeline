# predict.py

import pandas as pd
import joblib

def predict_conso(meteo_csv_path: str = "frontend/weather_paris.csv", model_path: str = "./models/random_forest_model.joblib") -> tuple:
    # Charger données météo
    df = pd.read_csv("frontend/weather_paris.csv", parse_dates=["date"])

    # Garder la dernière ligne (aujourd'hui)
    last_row = df.iloc[-1]

    # Colonnes utilisées pour l'entraînement du modèle
    features = [
        "temp_moyenne", "temp_min", "temp_max",
        "precipitations", "vitesse_vent",
        "rafales_vent", "pression", "ensoleillement"
    ]

    # Créer le vecteur de features
    X = pd.DataFrame([last_row[features].values], columns=features)

    # Charger le modèle
    model = joblib.load(model_path)

    # Faire la prédiction
    prediction = model.predict(X)[0]  # en kW

    return prediction, last_row