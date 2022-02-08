# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius 

stations = build_station_list()
city_centre_coords = (52.2053, 0.1218)

def run():
    print(stations_within_radius(stations, city_centre_coords, 10))

if __name__ == "__main__":
    print("\033[1mTask 1C\033[0m: CUED Part IA Flood Warning System")
    run()
