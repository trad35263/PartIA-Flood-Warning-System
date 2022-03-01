# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.station import MonitoringStation

example_station_a = MonitoringStation("id_a", "id_a", "station_a", (10, 0), (-2.3, 3.4445), "river A", "town A")
example_station_b = MonitoringStation("id_b", "id_b", "station_b", (0, 5), (-2.3, -3.4445), "river B", "town B")
example_station_c = MonitoringStation("id_c", "id_c", "station_c", (10, 10), None, "river C", "town C")
stations = [example_station_a, example_station_b, example_station_c]

def test_stations_level_over_threshold():
    assert stations_level_over_threshold(stations, 1) == []

def test_stations_highest_rel_level():
    assert stations_highest_rel_level(stations, 3) == []