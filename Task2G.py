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
