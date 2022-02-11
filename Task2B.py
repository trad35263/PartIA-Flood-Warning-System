# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels

stations = build_station_list()

def run():
    update_water_levels(stations)
    msg = "\nStations with \033[1mhigh water levels\033[0m are as follows :\n\n{}"
    list = stations_level_over_threshold(stations, 0.8)
    print(msg.format(list))


if __name__ == "__main__":
    print("\033[1mTask 2B\033[0m: CUED Part IA Flood Warning System")
    run()