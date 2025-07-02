from meteostat import Point, Daily
from datetime import datetime, timezone

# Coordonnées de Paris
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
df.to_csv("../data/weather_paris.csv", index=False)

print(df.head())
print(df.tail())