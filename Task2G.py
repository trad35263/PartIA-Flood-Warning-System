import matplotlib.dates 
import datetime 
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import predict_future_level 
from floodsystem.datafetcher import fetch_measure_levels

stations = build_station_list()
update_water_levels(stations)
risk_levels = []

for station in stations:
    try:
        dates , levels = fetch_measure_levels(station.measureid, dt = datetime.timedelta(days = 10))
        level_tomorrow = predict_future_level(dates, levels)[1]
        relative_level_tomorrow = (level_tomorrow - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])

    except:
        print("something unexpected happened")
        relative_level_tomorrow = 1 

current_water_level = station.relative_water_level() or 1 

# if already flooded, eg water level more the double typical, rank severe
if current_water_level > 2:
        risk_levels.append([station, "Severe"])
# if extraperlated will flood within time X make severe
elif realtive_level_tommorow > 1.9:
        risk_levels.append([station, "Severe"])
# if extrapolated will flood within time Y make high
elif realtive_level_tommorow > 1.5:
        risk_levels.append([station, "High"])
elif current_water_level > 1.6:
        risk_levels.append([station, "High"])
elif current_water_level > 1.4:
        risk_levels.append([station, "Moderate"])
else: risk_levels.append([station, "Low"])

print(risk_levels)