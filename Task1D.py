# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations = build_station_list()
city_centre_coords = (52.2053, 0.1218)

def run():
    msg = "\nThere are \033[1m{} rivers\033[0m with an associated station. The first 10 alphabetically are as follows :\n\n{}"
    full_list = rivers_with_station(stations)
    print(msg.format(len(full_list), full_list[:10]))

    msg2 = "\nThe names of the stations located on the \033[1mRiver Aire\033[0m are as follows :\n\n{}\n\nThe names of the stations located on the \033[1mRiver Cam\033[0m are as follows :\n\n{}\n\nThe names of the stations located on the \033[1mRiver Thames\033[0m are as follows :\n\n{}"
    full_list2 = stations_by_river(stations)
    print(msg2.format(sorted(full_list2['River Aire']), sorted(full_list2["River Cam"]), sorted(full_list2["River Thames"])))

if __name__ == "__main__":
    print("\033[1mTask 1D\033[0m: CUED Part IA Flood Warning System")
    run()