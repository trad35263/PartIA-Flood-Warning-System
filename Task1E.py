# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number 

stations = build_station_list()

def run():
    print(rivers_by_station_number(stations, 9))
    

if __name__ == "__main__":
    print("\033[1mTask 1E\033[0m: CUED Part IA Flood Warning System")
    run()
