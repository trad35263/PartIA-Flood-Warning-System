# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit

example_station_a = MonitoringStation("id_a", "id_a", "station_a", (10, 0), (-2.3, 3.4445), "river A", "town A")
example_station_b = MonitoringStation("id_b", "id_b", "station_b", (0, 5), (-2.3, -3.4445), "river B", "town B")
example_station_c = MonitoringStation("id_c", "id_c", "station_c", (10, 10), None, "river C", "town C")
stations = [example_station_a, example_station_b, example_station_c]

example_dates = [5, 4, 3, 2, 1, 0]
example_levels = [0, 1, 4, 9, 16, 25]


def test_polyfit():
    poly, d0 = polyfit(example_dates, example_levels, 2)
    assert round(poly(2)) == 9