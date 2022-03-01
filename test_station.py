# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

example_station_a = MonitoringStation("id_a", "id_a", "station_a", (10, 0), (-2.3, 3.4445), "river A", "town A")
example_station_b = MonitoringStation("id_b", "id_b", "station_b", (0, 5), (-2.3, -3.4445), "river B", "town B")
example_station_c = MonitoringStation("id_c", "id_c", "station_c", (10, 10), None, "river C", "town C")
stations = [example_station_a, example_station_b, example_station_c]

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    assert MonitoringStation.typical_range_consistent(example_station_a) == True
    assert MonitoringStation.typical_range_consistent(example_station_b) == False
    assert MonitoringStation.typical_range_consistent(example_station_c) == False

def test_inconsistent_typical_range_stations():
    expected_answer = ["station_b", "station_c"]
    assert inconsistent_typical_range_stations(stations) == expected_answer

# for milestone 2

def test_relative_water_level():
    assert MonitoringStation.relative_water_level(example_station_a) == None
    assert MonitoringStation.relative_water_level(example_station_b) == None
    assert MonitoringStation.relative_water_level(example_station_c) == None