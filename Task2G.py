import matplotlib.dates 
import datetime 
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import predict_future_level 
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np

stations = build_station_list()
update_water_levels(stations)

stations_at_severe_risk = []
stations_at_high_risk = []
stations_at_moderate_risk = []
stations_at_low_risk = []

N = 100

def run():

    for station in stations:

        for i in np.linspace(10, N, 10).astype(int):
                if station == stations[i]:
                        print("{}%".format(i))
            
        if station == stations[N]:
            break

        if station.name == "Westmill" or station.name == "Saltford":
            continue

        dt = 2
        dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
        if dates == [] or levels == []:
            print("Water level data for station \033[1m{}\033[0m could not be retrieved.".format(station.name))
            continue
        dates_as_float = []
        for date in dates:
            dates_as_float.append(matplotlib.dates.date2num(date))
        level_tomorrow = predict_future_level(dates_as_float, levels)
        if station.typical_range == None:
            continue
        else:
            relative_level_tomorrow = (level_tomorrow - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])    

        current_water_level = station.relative_water_level()

        # if already flooded, eg water level more the double typical, rank severe
        if current_water_level > 2:
            stations_at_severe_risk.append(station.name)
        # if extrapolated will flood within time X make severe
        elif relative_level_tomorrow > 1.9:
            stations_at_severe_risk.append(station.name)
        # if extrapolated will flood within time Y make high
        elif current_water_level > 1.4:
            stations_at_high_risk.append(station.name)
        elif relative_level_tomorrow > 1.3:
            stations_at_high_risk.append(station.name)
        elif current_water_level > 0.7:
            stations_at_moderate_risk.append(station.name)
        else:
            stations_at_low_risk.append(station.name)

    print("\nStations at \033[1msevere\033[0m risk are as follows :\n\n{}".format(stations_at_severe_risk))
    print("\nStations at \033[1mhigh\033[0m risk are as follows :\n\n{}".format(stations_at_high_risk))
    print("\nStations at \033[1mmoderate\033[0m risk are as follows :\n\n{}".format(stations_at_moderate_risk))
    print("\nStations at \033[1mlow\033[0m risk are as follows :\n\n{}".format(stations_at_low_risk))

if __name__ == "__main__":
    print("\033[1mTask 2G\033[0m: CUED Part IA Flood Warning System")
    run()