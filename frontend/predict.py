# predict.py
import pandas as pd
import joblib
import os

def predict_conso(
    meteo_csv_path: str = None,
    model_path: str = None
) -> tuple:
    # Par défaut, chemins relatifs à ce fichier (robuste pour Streamlit Cloud)
    if meteo_csv_path is None:
        meteo_csv_path = os.path.join(os.path.dirname(__file__), "weather_paris.csv")
    if model_path is None:
        model_path = os.path.join(os.path.dirname(__file__), "..", "models", "random_forest_model.joblib")

    # Charger données météo
    df = pd.read_csv(meteo_csv_path, parse_dates=["date"])

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
