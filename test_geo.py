# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the geo module"""

from floodsystem.geo import haversine, stations_within_radius
from floodsystem.geo import stations_by_distance
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation

example_station_a = MonitoringStation("id_a", "id_a", "station_a", (10, 0), (-2.3, 3.4445), "river A", "town A")
example_station_b = MonitoringStation("id_b", "id_b", "station_b", (0, 5), (-2.3, -3.4445), "river B", "town B")
example_station_c = MonitoringStation("id_c", "id_c", "station_c", (10, 10), None, "river C", "town C")
stations = [example_station_a, example_station_b, example_station_c]

def test_haversine():
    assert round(haversine((5, 50), (3, 58)), 2) == 899.01

def test_stations_by_distance():
    expected_answer = ["station_b", "station_a", "station_c"]
    assert stations_by_distance(stations, (0, 0))[0][0] == expected_answer[0]
    assert stations_by_distance(stations, (0, 0))[1][0] == expected_answer[1]
    assert stations_by_distance(stations, (0, 0))[2][0] == expected_answer[2]

def test_stations_within_radius():
    expected_answer = ["station_a", "station_b"]
    assert stations_within_radius(stations, (0, 0), 1112) == expected_answer

def test_rivers_with_station():
    expected_answer = ["river A", "river B", "river C"]
    assert rivers_with_station(stations) == expected_answer

def test_stations_by_river():
    expected_answer = {"river A": ["station_a"], "river B": ["station_b"], "river C": ["station_c"]}
    assert stations_by_river(stations) == expected_answer

def test_rivers_by_station_number():
    expected_answer = [("river A", 1), ("river B", 1), ("river C", 1)]
    assert rivers_by_station_number(stations, 3) == expected_answer