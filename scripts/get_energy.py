import pandas as pd
from datetime import datetime, timezone

def get_energy(start_date = datetime(2023, 1, 1).date(),
    end_date = datetime.now(timezone.utc).date(), save_path = "/opt/airflow/data/energy_paris.csv"):
    url = "https://odre.opendatasoft.com/explore/dataset/eco2mix-metropoles-tr/download/?format=csv&refine.libelle_metropole=M%C3%A9tropole+du+Grand+Paris&timezone=Europe%2FParis"

    print("Téléchargement en cours...")
    df = pd.read_csv(url, sep=';')
    print("Téléchargement terminé.")

    # Convertir en datetime avec utc
    df["date_heure"] = pd.to_datetime(df["date_heure"], errors="coerce", utc=True)
    df = df.dropna(subset=["date_heure", "consommation"])  # filtre les NaT et NaN

    # Extraire la date
    df["date"] = df["date_heure"].dt.date
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    # Agrégation par jour
    df_journalier = df.groupby("date")["consommation"].sum().reset_index()
    df_journalier = df_journalier.rename(columns={
        "date": "date",
        "consommation": "conso_kw"
    })
    df_journalier.to_csv(save_path, index=False)
    return df_journalier