# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations = build_station_list()
city_centre_coords = (52.2053, 0.1218)

def run():
    msg = "\nThe \033[1mclosest\033[0m 10 stations from Cambridge city centre are as follows:\n\n{}\n\nThe \033[1mfurthest\033[0m 10 stations are as follows:\n\n{}"
    full_list = stations_by_distance(stations, city_centre_coords)
    print(msg.format(full_list[:10], full_list[-10:]))

if __name__ == "__main__":
    print("\033[1mTask 1B\033[0m: CUED Part IA Flood Warning System")
    run()
