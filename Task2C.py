# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()

def run():
    update_water_levels(stations)
    msg = "\nThe \033[1m10 highest risk\033[0m stations are the following :\n\n{}"
    list = stations_highest_rel_level(stations, 10)
    print(msg.format(list))

if __name__ == "__main__":
    print("\033[1mTask 2C\033[0m: CUED Part IA Flood Warning System")
    run()