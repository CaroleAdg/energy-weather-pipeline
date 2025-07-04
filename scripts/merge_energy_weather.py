import pandas as pd

def merge_energy_weather():
    # Charger les fichiers CSV
    meteo = pd.read_csv("/opt/airflow/data/weather_paris.csv", parse_dates=["date"])
    conso = pd.read_csv("/opt/airflow/data/energy_paris.csv", parse_dates=["date"])

    # Fusion sur la colonne "date"
    df_merged = pd.merge(meteo, conso, on="date", how="inner")

    # Sauvegarde du fichier final
    df_merged.to_csv("/opt/airflow/data/energy_weather_paris.csv", index=False)
    print("Fusion terminée. Fichier sauvegardé sous /opt/airflow/data/energy_weather_paris")
    print(df_merged.head())
