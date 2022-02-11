# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from .utils import sorted_by_key  # noqa

from .station import MonitoringStation

import math

def stations_level_over_threshold(stations, tol):
    stations_over_threshold = []
    levels_over_threshold = []
    for station in stations:
        if MonitoringStation.relative_water_level(station) == None:
            continue
        elif MonitoringStation.typical_range_consistent(station) == False:
            continue
        elif MonitoringStation.relative_water_level(station) > tol:
            stations_over_threshold.append(station.name)
            levels_over_threshold.append(MonitoringStation.relative_water_level(station))
    output = list(zip(stations_over_threshold, levels_over_threshold))
    return sorted_by_key(output, 1, True)