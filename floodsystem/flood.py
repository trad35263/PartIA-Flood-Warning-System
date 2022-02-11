# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation

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

def stations_highest_rel_level(stations, N):
    stations_by_rel_level = []
    rel_levels = []
    for station in stations:
        if MonitoringStation.relative_water_level(station) == None:
            continue
        else:
            stations_by_rel_level.append(station.name)
            rel_levels.append(MonitoringStation.relative_water_level(station))
    output = list(zip(stations_by_rel_level, rel_levels))
    return sorted_by_key(output, 1, True)[:N]
