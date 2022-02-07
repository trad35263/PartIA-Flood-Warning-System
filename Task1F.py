# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()

def run():
    msg = "\nStations with inconsistent typical ranges are as follows :\n\n{}"
    full_list = inconsistent_typical_range_stations(stations)
    print(msg.format(sorted(full_list)))

if __name__ == "__main__":
    print("\033[1mTask 1F\033[0m: CUED Part IA Flood Warning System")
    run()