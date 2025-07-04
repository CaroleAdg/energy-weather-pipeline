import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train_and_save_model():
    print("Chargement des données...")
    df = pd.read_csv("/opt/airflow/data/energy_weather_paris.csv", parse_dates=["date"])

    df_model = df.drop(columns=["date", "neige", "direction_vent"]) 
    df_model = df_model.dropna()

    print("Préparation des données...")
    X = df_model.drop(columns=["conso_kw"])
    y = df_model["conso_kw"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Entraînement du modèle...")
    rf = RandomForestRegressor(random_state=42)
    rf.fit(X_train, y_train)

    model_path = "/opt/airflow/models/random_forest_model.joblib"
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    print(f"Sauvegarde du modèle à {model_path}...")
    joblib.dump(rf, model_path)
    print("Modèle entraîné et sauvegardé avec succès.")
