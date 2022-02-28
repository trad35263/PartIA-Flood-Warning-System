# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import matplotlib
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit

stations = build_station_list()

def run():

    update_water_levels(stations)
    stations_at_risk = stations_highest_rel_level(stations, 5)
    dt = 2

    for index, tuple in enumerate(stations_at_risk):

        dates_as_float = []
        station_at_risk = None

        for station in stations:
            if station.name == tuple[0]:
                station_at_risk = station
                break

        if not station_at_risk:
            print("Station \033[1m{}\033[0m could not be found".format(tuple[0]))
            return
        
        dates, levels = fetch_measure_levels(
        station_at_risk.measure_id, dt=datetime.timedelta(days=dt))

        for date in dates:
            dates_as_float.append(matplotlib.dates.date2num(date))

        if dates_as_float == []:
            print("\nWater level data for station \033[1m{}\033[0m could not be retrieved.".format(station_at_risk.name))
            continue
        else:
            print("\nWater level data for station \033[1m{}\033[0m succesfully retrieved.".format(station_at_risk.name))    

        plot_water_level_with_fit(station_at_risk, dates_as_float, levels, 4)


if __name__ == "__main__":
    print("\033[1mTask 2F\033[0m: CUED Part IA Flood Warning System")
    run()