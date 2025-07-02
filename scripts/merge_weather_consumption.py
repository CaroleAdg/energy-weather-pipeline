import pandas as pd

def merge_meteo_et_conso():
    # Charger les fichiers CSV
    meteo = pd.read_csv("../data/weather_paris.csv", parse_dates=["date"])
    conso = pd.read_csv("../data/consommation_paris.csv", parse_dates=["date"])

    # Fusion sur la colonne "jour"
    df_merged = pd.merge(meteo, conso, on="date", how="inner")

    # Sauvegarde du fichier final
    df_merged.to_csv("../data/energy_weather_paris.csv", index=False)
    print("Fusion terminée. Fichier sauvegardé sous ../data/meteo_conso_paris.csv")
    print(df_merged.head())

if __name__ == "__main__":
    merge_meteo_et_conso()
