from meteostat import Point, Daily
from datetime import datetime, timezone

def get_weather(start_date=None, end_date=None, save_path = "/opt/airflow/data/weather_paris.csv"):
    paris = Point(48.8566, 2.3522)
    start = datetime(2023, 1, 1)
    end = datetime.now()

    data = Daily(paris, start, end)
    df = data.fetch()
    df = df.reset_index()
    df = df.rename(columns={
        "time":"date",
        "tavg": "temp_moyenne",
        "tmin": "temp_min",
        "tmax": "temp_max",
        "prcp": "precipitations",
        "snow": "neige",
        "wdir": "direction_vent",
        "wspd": "vitesse_vent",
        "wpgt": "rafales_vent",
        "pres": "pression",
        "tsun": "ensoleillement"
    })
    df.to_csv(save_path, index=False)
    return df